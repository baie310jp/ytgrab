import argparse
import os
from urllib import request

from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from PIL import Image
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
                raise RuntimeError(f"Downloading failed. ({vid})") from e

            if format == "mp3":
                tags = EasyID3(file_path)
                tags["title"] = title
                tags["artist"] = artist
                tags.save()

                artwork_file_path = f"output/mp3/{vid}.jpg"

                with request.urlopen(f"https://img.youtube.com/vi/{vid}/0.jpg", timeout=10) as r:
                    data = r.read()
                    with open(artwork_file_path, mode="wb") as o:
                        o.write(data)

                with Image.open(artwork_file_path) as img:
                    width, height = img.size
                    crop_size = min(width, height)
                    left = (width - crop_size) // 2
                    top = (height - crop_size) // 2
                    cropped = img.crop((left, top, left + crop_size, top + crop_size))
                    resized = cropped.resize((300, 300))
                    resized.save(artwork_file_path)

                with open(artwork_file_path, mode="rb") as r:
                    data = r.read()
                    tags = ID3(file_path)
                    tags.delall("APIC")
                    tags.add(APIC(mime="image/jpeg", type=3, desc="Album cover", data=data))
                    tags.save(v2_version=3)

                os.remove(artwork_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("format", nargs="?", choices=["mp3", "mp4"], default="mp3")
    args = parser.parse_args()
    main(args.format)
