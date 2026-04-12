import os
import yt_dlp 

# Define the output directory based on your desired path
output_directory = 'D:\\Ye Hai Mohabatein\\8\\90'

# Create the directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Set the options for yt-dlp, including the output directory and video range
ydl_opts = {
    'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),  # Save in the specified output directory
    'playliststart': 996+3 ,  # Start downloading from video number 415 (1-based index)
    'playlistend': 1005+3 ,    # Stop downloading at video number 423 (1-based index)
}

# Initialize yt-dlp with options
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        # Provide the playlist URL here
        playlist_url = 'https://www.youtube.com/playlist?list=PLAM7IOZnvD2FGWdj3ytcZCMnQdw6FBaHg'
        
        # Download the specified range of videos from the playlist
        ydl.download([playlist_url])
        
        print("Download successful!")
    except Exception as e:
        print(f"An error occurred: {e}")
