import yt_dlp
import sys

def ask_user_options_mp3():
	"""
	Ask the user for download options: URL, start time, end time, audio language.
	"""
	start_time = input("Enter start time (hh:mm:ss or seconds, leave blank for start): ").strip()
	end_time = input("Enter end time (hh:mm:ss or seconds, leave blank for full audio): ").strip()
	language = input("Enter audio language code (leave blank for default): ").strip()
	settings = (start_time, end_time, language)
	return settings

def download_audio(url, settings):
	"""
	Download audio from the given URL, optionally trimming and selecting language.
	"""
	ydl_opts = {
		'format': 'bestaudio',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'outtmpl': '%(title)s.%(ext)s',
	}

	post_args = []
	if settings[0]:
		post_args += ['-ss', settings[0]]
	if settings[1]:
		post_args += ['-to', settings[1]]
	if post_args:
		ydl_opts['postprocessor_args'] = post_args

	if settings[2]:
		ydl_opts['preferedlanguage'] = settings[2]

	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
	except Exception as e:
		print(f"Error downloading audio: {e}", file=sys.stderr)
