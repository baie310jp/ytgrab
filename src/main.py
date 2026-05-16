import os

from yt_dlp import YoutubeDL

from videos import videos


def main(format="mp3"):
    for video in videos:
        vid = video["id"]
        title = video["title"]
        artist = video["artist"]

        if format == "mp3":
            output_vid = f"output/mp3/{vid}"
            file_path = output_vid + ".mp3"
        else:
            output_vid = f"output/mp4/{vid}"
            file_path = output_vid + ".mp4"

        if os.path.isfile(file_path):
            continue


if __name__ == "__main__":
    main()
