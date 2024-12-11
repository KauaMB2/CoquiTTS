from TTS.api import TTS

# Initialize the multilingual TTS model that supports voice cloning and Portuguese
model_name = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name)

# Define the sample voice for cloning and the Portuguese text
speaker_wav = ["reference2.mp3"]  # Path to the reference .wav file for voice cloning
text = "Olá, tudo bem? Meu nome é Kauã Moreira Batista e este áudio é um teste do modelo Coqui para conversão de texto para áudio. E aí, o que você achou?"
output_path = "CoquiYourTTS.mp3"

# Generate the cloned voice in Portuguese
tts.tts_to_file(text=text, speaker_wav=speaker_wav, language="pt-br", file_path=output_path)

print(f"Áudio salvo em {output_path}")
