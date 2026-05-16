import os

from yt_dlp import YoutubeDL

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

        url = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"

        with YoutubeDL(ydl_opts) as ydl:
            retcode = ydl.download([f"https://www.youtube.com/watch?v={vid}"])
            if retcode != 0:
                raise RuntimeError(f"Downloading failed with non-zero return code. ({vid})")


if __name__ == "__main__":
    main()
