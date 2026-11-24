"""
Main file for video-to-MP3 converter
------------------------------------
Author: Ace Carpenter

"""
import tkinter as tk
from tkinter import filedialog


"""
Prompts the user for both a CSV and MP3 file path and calls coresponding modules

>If user has URL, will call modules MP3_Downloader.py

>If user has CSV, will call modules CSV_Reader.py, Video_Finder.py, and MP3_Downloader.py
"""

def main():
    
    user_choice = input(f"Hello! Welcome to the Video-to-MP3 Converter.\n"
                        + '~'*40
                        +"\nDo you have a YouTube playlist URL (1) or a CSV (2)\nChoose: (1, 2) ")
    
    while user_choice != "1" and user_choice != "2":
        print("Try again buddy.")
        user_choice = input(f"Do you have a YouTube playlist URL (1) or a CSV (2)\nChoose: (1, 2) ")

    if user_choice == "1":
        URL_input = input("Paste URL here: ")
        #Setting up path the converted MP3('s) will go
        print("Select where you want you MP3 Files to be stored")
        MP3_file_path = filedialog.askdirectory(title = "Select where you want you MP3 Files to be stored")
        
    else:
        #Setting up path where CSV is stored
        print("Select CSV File")
        CSV_file_path = filedialog.askopenfilename(title = "Select CSV File", filetypes=[("CSV Files," "*.csv")])

if __name__ == "__main__":
    main()