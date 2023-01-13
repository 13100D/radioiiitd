#!/usr/bin/env python

import nextcord
from pytube import YouTube
from pytube import Search
from nextcord.ext import commands
bot = commands.Bot()
from mpd import MPDClient
bot.client=MPDClient()
bot.client.connect("localhost", 6600)
bot.client.consume(1)
bot.playlist=[]
bot.nowplaying=0
bot.client.clear()
@bot.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=False)

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age_restricted', '_author', '_embed_html', '_fmt_streams', '_initial_data', '_js', '_js_url', '_metadata', '_player_config_args', '_publish_date', '_title', '_vid_info', '_watch_html', 'age_restricted', 'allow_oauth_cache', 'author', 'bypass_age_gate', 'caption_tracks', 'captions', 'channel_id', 'channel_url', 'check_availability', 'description', 'embed_html', 'embed_url', 'fmt_streams', 'from_id', 'initial_data', 'js', 'js_url', 'keywords', 'length', 'metadata', 'publish_date', 'rating', 'register_on_complete_callback', 'register_on_progress_callback', 'stream_monostate', 'streaming_data', 'streams', 'thumbnail_url', 'title', 'use_oauth', 'vid_info', 'video_id', 'views', 'watch_html', 'watch_url']
@bot.slash_command(description='search youtube to queue a video')
async def queue(interaction: nextcord.Interaction, query: str):
    await interaction.response.send_message(f"You searched for: {query}")
    s=Search(query).results
    bot.playlist.append('https://www.youtube.com/watch?v='+s[0].video_id)
    print(bot.playlist)
    await play()

async def play():
    yt=YouTube(bot.playlist[bot.nowplaying])
    bot.nowplaying+=1
    currentsong=(yt.streams.filter(only_audio=True))
    currentsong=currentsong[len(currentsong)-1]
    print(bot.client.playlistinfo())
    print(currentsong.url)
    bot.client.add(currentsong.url)
    bot.client.play()





bot.run("MTAyMzQ5NTY4MzU4OTgyMDQ0Ng.G4YjMZ.DEgoonRoYHkYjy8j9hNO4i_4mkfxK8pj2149TQ")
