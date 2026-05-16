import os

from yt_dlp import YoutubeDL
import requests

from config import ydl_opts_mp3, ydl_opts_mp4
from videos import videos


def main(format="mp3"):
    for video in videos:
        vid = video["id"]
        title = video["title"]
        artist = video["artist"]

        if format == "mp3":
            output_vid = f"output/mp3/{vid}"
            file_path = output_vid + ".mp3"
            ydl_opts = ydl_opts_mp3
            ydl_opts["outtmpl"] = output_vid
        else:
            output_vid = f"output/mp4/{vid}"
            file_path = output_vid + ".mp4"
            ydl_opts = ydl_opts_mp4
            ydl_opts["outtmpl"] = output_vid

        if os.path.isfile(file_path):
            continue

        resp = requests.head(f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg")
        if resp.status_code != 200:
            raise RuntimeError(f"Video not found or unavailable. ({vid})")

        with YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([f"https://www.youtube.com/watch?v={vid}"])
            except Exception as e:
                print(e)
                raise RuntimeError(f"Downloading failed. ({vid})")

            print(title, artist)


if __name__ == "__main__":
    main()
