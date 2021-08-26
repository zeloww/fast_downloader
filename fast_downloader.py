import os

try:
    import youtube_dl
except:
    os.system("pip install youtube_dl")
    import youtube_dl

os.system("color d")
os.system("cls")
zelow = """
███████╗ █████╗ ███████╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
█████╗  ███████║███████╗   ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██╔══╝  ██╔══██║╚════██║   ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║  ██║███████║   ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                  by Zelow#9999
"""

def main():
    print(zelow)

    while True:
        videos_url = []
        while True:
            video_url = input("Enter the video URL or enter 'stop' >>> ")
            if video_url == "stop":
                break
            videos_url.append(video_url)

        video_type = input("What format do you want >>> ")
        video_quality = input("What quality do you want (don't add the denominator [P, kbps...] ) >>> ")

        ydl_opts = {
            'format': f'bestvideo[height<={video_quality}]+bestaudio/best[height<={video_quality}]',
            'outtmpl': 'fast_downloader/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': video_type.lower()
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(videos_url)
            print("Check the folder of the tool!")
        
        restart = input("Do you want restart? [y/n]")
        if restart.lower() not in ["y", "yes"]:
            break

    print("bye :D")


main()
