import moviepy as mp
import os 

path = input ("Enter video path fro video :")

videoclip = mp.VideoFileClip (path)
audioclip = videoclip.audio
audioclip.write_autofile("audio.mp3")

