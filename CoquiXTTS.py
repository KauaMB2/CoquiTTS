from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="Olá, tudo bem? Meu nome é Kauã Moreira Batista e este áudio é um teste do modelo Coqui para conversão de texto para áudio. E aí, o que você achou?",
                file_path="CoquiXTTS.mp3",
                speaker_wav=["reference.mp3"],
                language="pt",
                split_sentences=True
                )