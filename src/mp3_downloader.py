import yt_dlp
import sys

def download_audio(url, settings):
	"""
	Download audio from the given URL, optionally trimming and selecting language.
	"""
	# Configure yt_dlp options based on user settings
	start_time, end_time, language = settings

	if language:
		format_str = f"bestaudio[language={language}]"
	else:
		format_str = "bestaudio/best"
	ydl_opts = {
		'format': format_str,
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'outtmpl': '%(title)s.%(ext)s',
	}

	post_args = []
	if start_time:
		post_args += ['-ss', start_time]
	if end_time:
		post_args += ['-to', end_time]
	if post_args:
		ydl_opts['postprocessor_args'] = post_args

	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
	except Exception as e:
		print(f"Error downloading audio: {e}", file=sys.stderr)
