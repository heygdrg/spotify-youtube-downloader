import os

from pystyle import *
from pytube import YouTube
import webbrowser
from instaloader import *
banner = """

    $$$$$$$\   $$$$$$\  $$\      $$\ $$\   $$\ $$\       $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$$\  
    $$  __$$\ $$  __$$\ $$ | $\  $$ |$$$\  $$ |$$ |     $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
    $$ |  $$ |$$ /  $$ |$$ |$$$\ $$ |$$$$\ $$ |$$ |     $$ /  $$ |$$ /  $$ |$$ |  $$ |$$ |      $$ |  $$ |
    $$ |  $$ |$$ |  $$ |$$ $$ $$\$$ |$$ $$\$$ |$$ |     $$ |  $$ |$$$$$$$$ |$$ |  $$ |$$$$$\    $$$$$$$  |
    $$ |  $$ |$$ |  $$ |$$$$  _$$$$ |$$ \$$$$ |$$ |     $$ |  $$ |$$  __$$ |$$ |  $$ |$$  __|   $$  __$$< 
    $$ |  $$ |$$ |  $$ |$$$  / \$$$ |$$ |\$$$ |$$ |     $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
    $$$$$$$  | $$$$$$  |$$  /   \$$ |$$ | \$$ |$$$$$$$$\ $$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$$$\ $$ |  $$ |
    \_______/  \______/ \__/     \__|\__|  \__|\________|\______/ \__|  \__|\_______/ \________|\__|  \__|
                                        
                                            >BKS#1958<                                                                     
                                >>> https://discord.gg/6eAAKVuw <<<                                                         
                       
                            ╔═════════════════════════════════════════════╗
                            [1] YOUTUBE DOWNLOADER
                            [2] INSTAGRAM DOWNLOADER
                            [3] SPOTIFY DOWNLOADER [coming soon]
                            [4] EXIT
                            ╚═════════════════════════════════════════════╝
"""

print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner), 1))

print()
choice = input(">>> choice : ")

if choice == "1":

    webbrowser.open("https://www.youtube.com/")
    print()
    print("We just open youtube, easier to have a link !")

    a = 0
    while a == 0:
        link = input("enter the link: ")
        yt = YouTube(link)

        video = yt.streams.get_highest_resolution()
        video.download()
        print("Done!")
        again = input("wanna download another video [y/n] :")
        if again == "y":
            a = 0
        if again == "n":
            a = 1


if choice == "2":
    a = 0
    while a == 0:
        ig = instaloader.Instaloader()
        dp = input("Enter Insta Username : ")
        ig.download_profile(dp, profile_pic_only=True)
        print("Done!")
        again = input("wanna download another video [y/n] :")
        if again == "y":
            a = 0
        if again == "n":
            a = 1

if choice == "3":

    print("coming soon")
    #song = input("enter the URL: ")
    #os.system(f" spotdl {song}")
    #os.remove(".spotdl-cache")

if choice == "4":
    os.system("PAUSE")
