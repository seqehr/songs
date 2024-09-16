import pygame
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame for music handling
pygame.init()

# Dictionary to map numeric keys to music files
music_map = {
    '1': "./1.mp3",
    '2': "./2.mp3",
    '3': "./3.mp3",
    '4': "./4.mp3",
    '5': "./5.mp3",
    '6': "./6.mp3",
    '7': "./7.mp3",
    '8': "./8.mp3",

}

# Function to play the song based on key press
def play_song(song):
    print(f"Playing {song}")
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

# Function to handle key press events
def handle_key_press(event):
    # Log key event details for debugging
    print(f"Key pressed: {event.keysym}, Keycode: {event.keycode}")
    
    # Check which key is pressed
    key = event.keysym

    # Log detected key
    print(f"Detected key: {key}")

    # Play the corresponding song if key is in music_map
    if key in music_map:
        play_song(music_map[key])
    else:
        print("No action for this key")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to display available shortcuts
def show_shortcuts():
    shortcuts = "\n".join([f"{key}: {value}" for key, value in music_map.items()])
    messagebox.showinfo("Keyboard Shortcuts", shortcuts)

# Function to add a new song to the shortcuts
def add_song(key, song_path):
    if key in music_map:
        print(f"Key {key} already in use. Updating song.")
    music_map[key] = song_path
    print(f"Added/Updated song: {key} -> {song_path}")

# Function to remove a song from the shortcuts
def remove_song(key):
    if key in music_map:
        del music_map[key]
        print(f"Removed song associated with key: {key}")
    else:
        print(f"No song associated with key: {key}")

# Initialize Tkinter for the UI
root = tk.Tk()
root.title("Music Shortcut Player")
root.geometry("400x300")

# Bind keyboard events to Tkinter window
root.bind('<KeyPress>', handle_key_press)

# Create UI elements
title_label = tk.Label(root, text="Music Shortcut Player", font=("Arial", 16))
title_label.pack(pady=20)

shortcuts_button = tk.Button(root, text="Show Shortcuts", command=show_shortcuts)
shortcuts_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Music", command=stop_music)
stop_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Example usage
# Add a new song shortcut
# add_song('4', "song4.mp3")

# Remove an existing song shortcut
# remove_song('2')

# Start the Tkinter event loop
root.mainloop()

# Quit pygame when done
pygame.quit()
