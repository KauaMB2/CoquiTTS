from TTS.api import TTS
import torch

# Load the model without specifying GPU initially
tts = TTS("tts_models/multilingual/multi-dataset/bark") 

# Check if CUDA is available and set the device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"
tts.to(device)

# Cloning a new speaker
tts.tts_to_file(
    text="Hello, my name is Manmay, how are you?",
    file_path="output.wav",
    voice_dir=r"C:\Users\zkaua\Downloads\dataset2",
    speaker="clips"
)

# Reuse the stored values to generate the voice
tts.tts_to_file(
    text="Hello, my name is Manmay, how are you?",
    file_path="output.wav",
    voice_dir=r"C:\Users\zkaua\Downloads\dataset2",
    speaker="clips"
)

# Random speaker (no need for GPU)
tts = TTS("tts_models/multilingual/multi-dataset/bark")
tts.to("cpu")  # Explicitly set to CPU
tts.tts_to_file("hello world", file_path="out.wav")
