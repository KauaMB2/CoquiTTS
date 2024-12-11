from TTS.api import TTS
tts = TTS("tts_models/en/multi-dataset/tortoise-v2")

# cloning `lj` voice from `TTS/tts/utils/assets/tortoise/voices/lj`
# with custom inference settings overriding defaults.
tts.tts_to_file(text="Olá, meu nome é Kauã Moreira Batista. E aí, o que achou?",
                file_path="output.wav",
                voice_dir=r"C:\Users\zkaua\Downloads\dataset2",
                speaker="clips",
                num_autoregressive_samples=1,
                diffusion_iterations=10)

# Using presets with the same voice
tts.tts_to_file(text="Olá, meu nome é Kauã Moreira Batista. E aí, o que achou?",
                file_path="output.wav",
                voice_dir=r"C:\Users\zkaua\Downloads\dataset2",
                speaker="clips",
                preset="ultra_fast")

# Random voice generation
tts.tts_to_file(text="Olá, meu nome é Kauã Moreira Batista. E aí, o que achou?",file_path="output.wav")