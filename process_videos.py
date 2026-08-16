import os
import subprocess
os.makedirs("audios_mp3", exist_ok=True)
files = os.listdir("videos")
# print(files)
for file in files:
    tutorial_num = file.split("-")[0]
    tutorial_name = file.split("-")[1]
    tutorial_name= tutorial_name.split("#")[0]
    # print(tutorial_num)
    # print(tutorial_name)
    input_path = os.path.join("videos", file)
    output_path = os.path.join("audios_mp3", f"{tutorial_num}_{tutorial_name}.mp3")
    subprocess.run([
        "ffmpeg",
        "-i", input_path,
        "-vn",                   # Extract audio only
        "-acodec", "libmp3lame", # MP3 encoder
        "-q:a", "2",             # High audio quality
        "-y",                    # Overwrite if file exists
        output_path
    ], check=True)
