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
                                                                                                      
                                                                                                      
                        ╔═════════════════════════════════════════════╗
                        [1] YOUTUBE DOWNLOADER
                        [2] INSTAGRAM DOWNLOADER
                        [3] QR CODE GENERATOR [COMING SOON]
                        [4] SPOTIFY DOWNLOADER [COMING SOON]
                        [5] EXIT
                        ╚═════════════════════════════════════════════╝
"""

print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner), 1))

print()
choice = Write.Input(">>> choice : ", Colors.yellow_to_red, interval=0.001)


if choice == "1":

    webbrowser.open("https://www.youtube.com/")
    print()
    print("We just open youtube, easier to have a link !")

    a = 0
    while a == 0:
        link = Write.Input("link: ", Colors.yellow_to_red, interval=0.001)
        yt = YouTube(link)

        video = yt.streams.get_highest_resolution()
        video.download()
        print("Done!")
        again =  Write.Input("wanna download another video [y/n] :", Colors.yellow_to_red, interval=0.001)
        if again == "y":
            a = 0
        if again == "n":
            a = 1


if choice == "2":

    webbrowser.open("https://www.instagram.com/")
    print()
    print("We just open instagram, easier to have a link !")

    a = 0
    while a == 0:
        ig = instaloader.Instaloader()
        dp = Write.Input("Enter Insta Username : ", Colors.yellow_to_red, interval=0.001)
        ig.download_profile(dp, profile_pic_only=True)
        print("Done!")
        again = Write.Input("wanna download another video [y/n] :", Colors.yellow_to_red, interval=0.001)
        if again == "y":
            a = 0
        if again == "n":
            a = 1


if choice == "3":
    Write.Input("[COMING SOON]", Colors.yellow_to_red, interval=0.001)

#link = input("link: ")
#img = qrcode.make(link)
#ing.show()
#song = input("enter the URL: ")
#os.system(f" spotdl {song}")
#os.remove(".spotdl-cache")

if choice == "4":
    Write.Input("[COMING SOON]", Colors.yellow_to_red, interval=0.001)

if choice == "5":
    os.system("PAUSE")
