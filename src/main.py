from mp3_downloader import *
from info_obtainer import *

def main():
    video_url = input("Enter the video URL: ")
    
    video_url_cleaned = clean_url(video_url)
    if not video_url_cleaned:
        print("Invalid URL entered.", file=sys.stderr)
        return

    video_info = get_video_info(video_url_cleaned)
    if video_info:
        display_summary(video_info)
    else:
        print("Could not get video information.")

    settings = ask_user_options_mp3()
    download_audio(video_url_cleaned, settings)

if __name__ == "__main__":
    main()