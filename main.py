import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
from tkinter import ttk
import urllib.parse


# Downloads the YouTube video specified by the URL entered by the user.
# It checks if the URL is valid and points to a YouTube video, if an output folder has been selected, and performs the download of the first available MP4 video.
# It displays a success or error alert based on the outcome of the download.
def download_video():
    url = url_entry.get()
    try:
        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.netloc not in ["www.youtube.com", "youtu.be"]:
            raise ValueError("The URL does not point to a YouTube video !")
    except:
        messagebox.showerror("Error", "The video URL is invalid !")
        return

    file_path = folder_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please choose an output folder !")
        return

    video = YouTube(url)
    mp4_streams = video.streams.filter(mime_type="video/mp4")

    window = tk.Tk()
    window.withdraw()
    file_path = folder_entry.get()

    stream = mp4_streams.first()
    stream.download(output_path=file_path)

    messagebox.showinfo("Success", "The video has been uploaded successfully!")

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, 'end')
    folder_entry.insert(0, folder_path)

# Function to download only the audio of the video
def download_audio():
    url = url_entry.get()
    try:
        parsed_url = urllib.parse.urlparse(url)

        if parsed_url.netloc not in ["www.youtube.com", "youtu.be"]:
            raise ValueError("The URL does not point to a YouTube video !")
    except:
        messagebox.showerror("Error", "The video URL is invalid !")
        return

    file_path = folder_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please choose an output folder !")
        return

    video = YouTube(url)

    window = tk.Tk()
    window.withdraw()
    file_path = folder_entry.get()

    audio_stream = video.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=file_path)

    messagebox.showinfo("Success", "The video has been uploaded successfully !")

# The main window
root = tk.Tk()
root.geometry("500x250")
root.title("Download It")

# Create a label to display text
text_label = tk.Label(root, text="This program is used to download a video or audio from a youtube video. Paste your video link, choose the output folder, and click on Download Video or Download Audio. Enjoy!", font=("Arial",10), wraplength=300)

# Pack the label in the main window
text_label.pack()

# Create a container for input fields and buttons
main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Create an input field for the video URL
url_label = ttk.Label(main_frame, text="Video URL:")
url_label.grid(row=0, column=0, sticky="W")

url_entry = ttk.Entry(main_frame, width=50)
url_entry.grid(row=0, column=1)

# Create an input field for the output folder
folder_label = ttk.Label(main_frame, text="Output folder:")
folder_label.grid(row=1, column=0, sticky="W")

folder_entry = ttk.Entry(main_frame, width=50)
folder_entry.grid(row=1, column=1)

browse_button = ttk.Button(main_frame, text="Browse", command=browse_folder)
browse_button.grid(row=1, column=2)

# Create a "Download" button to download the video
download_button = ttk.Button(main_frame, text="Download Video", command=download_video)
download_button.grid(row=2, column=1, pady=10)

# Create a "Download Audio" button to download only the audio from the video
download_audio_button = ttk.Button(main_frame, text="Download Audio", command=download_audio)
download_audio_button.grid(row=3, column=1, pady=10)

# Start the application's event loop
root.mainloop()
