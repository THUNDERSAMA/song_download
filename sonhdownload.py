import asyncio
import json
from youtubesearchpython.__future__ import VideosSearch
from pytube import YouTube
import os
from tqdm import tqdm


def download(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    destination = "G:/song_download/songs"
    out_file = audio.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded in .mp3 format.")


async def song():
    songname = input("Enter a song name:- \n")
    videosSearch = VideosSearch(songname, limit=1)
    videosResult = await videosSearch.next()
    link_text = videosResult["result"][0]["link"]

    # Use tqdm to create an interactive loader
    with tqdm(total=100, dynamic_ncols=True, unit="B", unit_scale=True) as pbar:
        async def download_with_progress():
            nonlocal pbar
            yt = YouTube(link_text)
            audio = yt.streams.filter(only_audio=True).first()
            out_file = audio.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            pbar.update(100)

        await asyncio.gather(download_with_progress())
    print(songname + " has been successfully downloaded in .mp3 format.")

if __name__ == '__main__':
    destination = "G:/song_download/songs"
    asyncio.run(song())
