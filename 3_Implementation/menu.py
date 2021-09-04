"""
Menu for the music player
"""
import pygame
import streamplayer


def userplaysong(objectval, userplaytrack):
    """
    Selecting track and opening audio player
    :param objectval:
    :param userplaytrack:
    :return: void
    """
    streamplayer.play(streamplayer.MusicPlayer.select_song(objectval, userplaytrack))
    print("\nPlaying----", userplaytrack)
    while True:
        print("Press 'p' to pause, 'r' to resume")
        print("Press 's' to stop the music")
        action = input("  ")
        if action == 'p':
            pygame.mixer.music.pause()
            print("\n----Music Paused---")
        elif action == 'r':
            pygame.mixer.music.unpause()
            print("\n----Music Resumed---")
        elif action == 's':
            pygame.mixer.music.stop()
            print("\n----Music Stopped---")
            break
        else:
            print("\n----Invalid operation---")


def __menu__():
    exitval = 1
    while exitval:
        print("\n**|Music Player|**")
        print("1.Search\n2.Browse \n3.Exit")
        choice = int(input("\n Choose 1/2/3: "))
        if choice == 1:
            keyword = input("Search Keyword: ")
            searchobj = streamplayer.SearchTracks(keyword)
            try:
                music, singer = searchobj.searchkeyword()
                listlength = len(music)
                for number in range(listlength):
                    print("\n{:>5} --------- {:5}".format(music[number], singer[number]))
                userplaytrack = input("\nEnter the song from the list: ")
                userplaysong(searchobj, userplaytrack)
            except TypeError:
                print("No results")
            except RuntimeError:
                print("The song requested doesn't exist")

        if choice == 2:
            browseobj = streamplayer.BrowseTracks()
            music, singer = browseobj.browse_list()
            listlength = len(music)
            for number in range(listlength):
                print(
                    "\n{:>5} ----------- {:5}".format(music[number], singer[number]))
            try:
                userplaytrack = input("\nEnter the song from the list: ")
                userplaysong(browseobj, userplaytrack)
            except RuntimeError:
                print("The song requested doesn't exist")

        if choice == 3:
            exitval = 0
