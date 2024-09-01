import asyncio
import json
from youtubesearchpython.__future__ import VideosSearch
from pytube import YouTube
import os


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
    videosSearch = VideosSearch('Malang Sajna', limit=1)
    videosResult = await videosSearch.next()
    # print(videosResult)
    # data = json.loads(videosResult)
    link_text = videosResult["result"][0]["link"]
    print(link_text)
    download(link_text)

asyncio.run(song())
