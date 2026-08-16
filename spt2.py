import os

# Fix potential PyTorch weights_only security block
os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"

import json
import subprocess
import whisper

os.makedirs("all_json", exist_ok=True)
files = os.listdir("audios_mp3")

# Load medium model (~3 GB VRAM footprint)
model = whisper.load_model("medium", device="cuda")

for file in files:
    tutorial_name = os.path.splitext(file)[0]
    input_path = os.path.join("audios_mp3", file)
    output_path = os.path.join("all_json", f"{tutorial_name}.json")
    tutorial_num = file.split("_")[0]

    result = model.transcribe(
        audio=input_path,
        language="hi",
        task="translate",
        verbose=True,
        word_timestamps=False,
    )

    chunk = []
    for segment in result["segments"]:
        chunk.append(
            {
                "number": tutorial_num,
                "title": tutorial_name,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"],
            }
        )

    # Wrap the full transcript text + individual chunk segments
    data_to_dump = {"text": result["text"], "chunks": chunk}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data_to_dump, f, ensure_ascii=False, indent=4)