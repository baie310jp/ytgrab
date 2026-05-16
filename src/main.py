import argparse
import os

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
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
            base_ydl_opts = ydl_opts_mp3
        else:
            output_vid = f"output/mp4/{vid}"
            file_path = output_vid + ".mp4"
            base_ydl_opts = ydl_opts_mp4

        ydl_opts = {**base_ydl_opts, "outtmpl": output_vid}

        if os.path.isfile(file_path):
            continue

        with YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([f"https://www.youtube.com/watch?v={vid}"])
            except Exception as e:
                print(e)
                raise RuntimeError(f"Downloading failed. ({vid})")

            if format == "mp3":
                tags = EasyID3(file_path)
                tags["title"] = title
                tags["artist"] = artist
                tags.save()

                tags = ID3(file_path)
                tags.save()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("format", nargs="?", choices=["mp3", "mp4"], default="mp3")
    args = parser.parse_args()
    main(args.format)
