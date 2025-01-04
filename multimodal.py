from transformers import BlipProcessor, BlipForConditionalGeneration
import whisper
from gtts import gTTS
from PIL import Image
import nltk
import os

nltk.download('punkt')

# Load Whisper model for audio transcription
DEVICE = "cpu"
try:
    whisper_model = whisper.load_model("base", device=DEVICE)
    print("Whisper model loaded successfully.")
except Exception as e:
    whisper_model = None
    print(f"Error loading Whisper model: {e}")

# Load BLIP for image-to-text
try:
    blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    print("BLIP model loaded successfully.")
except Exception as e:
    blip_processor = None
    blip_model = None
    print(f"Error loading BLIP model: {e}")

def img2txt(input_image):
    if not blip_model or not blip_processor:
        return "Image-to-text model is not available. Please ensure BLIP is loaded correctly."
    try:
        image = Image.open(input_image).convert("RGB")
        inputs = blip_processor(image, return_tensors="pt")
        outputs = blip_model.generate(**inputs)
        caption = blip_processor.decode(outputs[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error processing image: {e}"

def transcribe(audio_file):
    try:
        temp_audio_path = "temp_audio.wav"
        if hasattr(audio_file, "save"):
            audio_file.save(temp_audio_path)
        else:
            temp_audio_path = audio_file

        audio = whisper.load_audio(temp_audio_path)
        mel = whisper.log_mel_spectrogram(audio).to(whisper_model.device)

        options = whisper.DecodingOptions(fp16=False)
        result = whisper.decode(whisper_model, mel, options)

        if os.path.exists("temp_audio.wav"):
            os.remove("temp_audio.wav")

        return result.text.strip()
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return "Sorry, I could not understand your audio input."

def text_to_speech(text, filename):
    try:
        audio_dir = os.path.join(os.getcwd(), "static", "audio")
        file_path = os.path.join(audio_dir, filename)
        os.makedirs(audio_dir, exist_ok=True)

        tts = gTTS(text=text, lang="en", slow=False)
        tts.save(file_path)
        return file_path
    except Exception as e:
        print(f"Error generating text-to-speech audio: {e}")
        return None
