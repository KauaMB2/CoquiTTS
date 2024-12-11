from TTS.api import TTS

# Initialize TTS with the Brazilian Portuguese model
model_name = "tts_models/pt/cv/vits"  # Portuguese model for TTS
tts = TTS(model_name, progress_bar=False)

# Set the Portuguese text to synthesize
text = "Olá, tudo bem? Meu nome é Kauã Moreira Batista e este áudio é um teste do modelo Coqui para conversão de texto para áudio. E aí, o que você achou?"
output_path = "CoquiTacotron2.mp3"

# Generate and save the audio file
tts.tts_to_file(text=text, file_path=output_path)
print(f"Áudio salvo em {output_path}")