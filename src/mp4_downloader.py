import yt_dlp
import sys

def download_video(url, settings):
    """
    Downloads a video from a URL, with options for trimming,
    selecting quality, and audio language.
    settings = (start_time, end_time, quality, language)
    """
    # Unpack the settings for clarity
    start_time, end_time, quality, language = settings

    # Base strings for video and audio
    video_format = "bestvideo"
    audio_format = "bestaudio"

    # Add quality filter to the video if specified
    if quality:
        # Remove the 'p' from '720p', '1080p', etc.
        quality_val = quality.replace('p', '')
        video_format += f"[height<={quality_val}]"

    # Add language filter to the audio if specified
    if language:
        audio_format += f"[language={language}]"

    # Combine everything into the final string for yt_dlp
    # Format: filtered_video + filtered_audio / general_fallback
    # The fallback ('best') is in case separate streams aren't found
    format_str = f"{video_format}+{audio_format}/best"
        
    ydl_opts = {
        'format': format_str,
        'outtmpl': '%(title)s - %(resolution)s.%(ext)s', # More descriptive filename
        'postprocessors': [], # Initialize an empty list of post-processors
    }

    post_args = []
    if start_time:
        post_args += ['-ss', start_time]
    if end_time:
        post_args += ['-to', end_time]
    
    # If there are trim arguments, we need a post-processor that will use them.
    if post_args:
        # FFmpegVideoConvertor ensures that ffmpeg processes the video,
        # allowing us to pass it the trim arguments.
        ydl_opts['postprocessors'].append({
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4', # Convert to a standard format like mp4
        })
        ydl_opts['postprocessor_args'] = {
            'ffmpeg': post_args,
        }

    try:
        print(f"Starting download with format: {format_str}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video download complete!")
    except Exception as e:
        print(f"Error downloading video: {e}", file=sys.stderr)