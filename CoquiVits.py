from TTS.api import TTS

# Initialize the VITS model for Brazilian Portuguese with voice cloning
model_name = "tts_models/pt/cv/vits"
tts = TTS(model_name=model_name)

# Load the speaker embedding using a sample .wav file of the target voice
speaker_wav = "reference2.mp3"
speaker_embedding = tts.speaker_manager.compute_embedding(speaker_wav)

# Define the text and output path
text = "Este é um teste de clonagem de voz para português brasileiro."
output_path = "CoquiVits.mp3"

# Run TTS with the cloned voice
tts.tts_to_file(text=text, speaker_embedding=speaker_embedding, file_path=output_path)
print(f"Audio saved to {output_path}")
