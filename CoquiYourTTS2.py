import os
from TTS.api import TTS

# Initialize the multilingual TTS model that supports voice cloning and Portuguese
model_name = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name)

# Define the folder containing the dataset audio files
dataset_folder = r"C:\Users\zkaua\Downloads\dataset2\clips"
# Get a sorted list of all .mp3 files in the dataset folder
speaker_wav_files = sorted([f for f in os.listdir(dataset_folder) if f.endswith('.mp3')])

# Debugging: Print the number of .mp3 files found
print(f"Found {len(speaker_wav_files)} .mp3 files in the dataset folder.")

# # Limit to the first 100000 files
# if len(speaker_wav_files) > 100000:
#     speaker_wav_files = speaker_wav_files[:100000]

# Check if we have any files to process
if not speaker_wav_files:
    print("No .mp3 files found in the specified directory.")
else:
    # Choose one reference file for voice cloning (for example, the first one)
    reference_file = os.path.join(dataset_folder, speaker_wav_files[0])

    # Define the text for speech generation
    text = "Olá, tudo bem? Meu nome é Kauã Moreira Batista e este áudio é um teste do modelo Coqui para conversão de texto para áudio. E aí, o que você achou?"

    # Define the output path for the generated audio
    output_path = "YourTTSWithLargeDataset.mp3"  # Single output file

    try:
        # Generate the cloned voice in Portuguese using the reference file
        tts.tts_to_file(text=text, speaker_wav=reference_file, language="pt-br", file_path=output_path)
        print(f"Áudio salvo em {output_path}")
    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")
