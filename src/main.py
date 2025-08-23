from mp3_downloader import *
from mp4_downloader import *
from info_obtainer import *

def main():
    video_url = input("Enter the video URL: ")
    
    video_url_cleaned = clean_url(video_url)
    if not video_url_cleaned:
        print("Invalid URL entered.", file=sys.stderr)
        return

    video_info = get_video_info(video_url_cleaned)
    if video_info:
        video_features = extract_features(video_info)
        display_video_features(video_features)
    else:
        print("Could not get video information.")

    choice = display_menu()

    match choice:
        case '1':
            settings = ask_user_options_mp3()
            download_audio(video_url_cleaned, settings)
        case '2':
            settings = ask_user_options_mp4()
            download_video(video_url_cleaned, settings)
        case _:
            print("Invalid choice. Please enter 1 or 2.")
            display_menu()


def display_menu():
    print("Choose download format:")
    print("1. MP3 (Audio only)")
    print("2. MP4 (Video and Audio)")
    choice = input("Enter 1 or 2: ")
    return choice

def display_video_features(video_features):
    print(f"\nVideo Title: {video_features['title']}")
    print(f"Duration: {video_features['duration']}")
    print(f"Available Audio Languages: {video_features['audio_languages']}")
    print(f"Available Video Qualities: {video_features['video_qualities']}")
     
def ask_user_options_mp3():
	"""
	Ask the user for download options: URL, start time, end time, audio language.
	"""
	start_time = input("Enter start time (hh:mm:ss or seconds, leave blank for start): ").strip()
	end_time = input("Enter end time (hh:mm:ss or seconds, leave blank for full audio): ").strip()
	language = input("Enter audio language code (leave blank for default): ").strip()
	settings = (start_time, end_time, language)
	return settings

def ask_user_options_mp4():
    """
    Ask the user for download options: URL, start time, end time, video quality.
    """
    start_time = input("Enter start time (hh:mm:ss or seconds, leave blank for start): ").strip()
    end_time = input("Enter end time (hh:mm:ss or seconds, leave blank for full video): ").strip()
    quality = input("Enter maximum video height (e.g., 720 for 720p, leave blank for best): ").strip()
    language = input("Enter audio language code (leave blank for default): ").strip()
    settings = (start_time, end_time, quality, language)
    return settings

if __name__ == "__main__":
    main()
