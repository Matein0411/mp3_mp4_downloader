import yt_dlp
import sys
import re 
from mp3_downloader import *

def clean_url(url):
    '''
    Cleans the URL by removing any unwanted parameters.
    '''
    # Remove common unwanted parameters like 'list', 'index', etc.
    cleaned_url = re.sub(r'([&?]list=[^&]+|[&?]index=\d+|[&?]t=\d+)', '', url)
    # Remove trailing '?' or '&' if they exist
    cleaned_url = cleaned_url.rstrip('&?')
    return cleaned_url


def get_video_info(video_url):
    '''
    Gets video information without downloading it.
    '''
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extract detailed video information
            info = ydl.extract_info(video_url, download=False)
            return info
        except yt_dlp.utils.DownloadError as e:
            print(f"Error getting information: {e}", file=sys.stderr)
            return None

def display_summary(info):
    '''
    Show a simple summary with the requested information.
    '''
    # 1. Video title
    title = info.get('title', 'Not available')

    # 2. Video duration (converted to MM:SS format)
    duration_seconds = info.get('duration', 0)
    if duration_seconds:
        minutes, seconds = divmod(duration_seconds, 60)
        duration_str = f"{minutes:02d}:{seconds:02d}"
    else:
        duration_str = "Not available"

    # 3. Audio languages available (without duplicates)
    audio_languages = set()
    for f in info.get('formats', []):
        # Check if the format is audio-only
        if f.get('language'):
            audio_languages.add(f.get('language'))
            
    if audio_languages:
        audio_languages_str = ", ".join(sorted(list(audio_languages)))
    else:
        audio_languages_str = "Not available "

    # 3. Video qualities available (without duplicates)

    available_qualities = set()
    for f in info.get('formats', []):
        # Ensure it's a video format with defined height
        if f.get('height'):
            available_qualities.add(f'{f["height"]}p')

    if available_qualities:
        # Sort qualities from highest to lowest
        qualities_str = ", ".join(sorted(list(available_qualities), key=lambda q: int(q[:-1]), reverse=True))
    else:
        qualities_str = "Not available"

    # 4. Subtitles languages available
    subtitles = info.get('subtitles', {})
    if subtitles:
        # Get language codes (e.g., 'en', 'es', 'fr')
        languages = ", ".join(subtitles.keys())
    else:
        languages = "Not available"

    # Display the summary
    print("\n--- Video Summary ---")
    print(f"Title: {title}")
    print(f"Duration: {duration_str}")
    print(f"Video Qualities: {qualities_str}")
    print(f"Subtitle Languages: {languages}")
    print(f"Audio Languages: {audio_languages_str}")


