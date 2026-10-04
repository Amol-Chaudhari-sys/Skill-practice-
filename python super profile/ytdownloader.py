import youtube_dl
import yt_dlp

url = input ("Enter the Url :")
ydl_opts = {
    "format": "bestvideo+bestaudio/best",
}
ydl_opts = {
    "format" :"bestaudio"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl :
    ydl.download ([url])