# Install necessary libraries
!pip install pytesseract pillow pyttsx3 googletrans==4.0.0-rc1

# Install Tesseract OCR
!apt-get install -y tesseract-ocr
!apt-get install -y libtesseract-dev
!apt-get install -y espeak-ng
!apt-get install -y espeak

# Import required libraries
import pytesseract
from pytesseract import Output
from PIL import Image
import pyttsx3
from googletrans import Translator
from google.colab import files

# Configure pytesseract for Colab
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# Initialize Text-to-Speech engine
tts_engine = pyttsx3.init()

# Translator for multi-language support
translator = Translator()

def extract_text(image_path):
    """
    Extracts text from an image using Tesseract OCR.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang="eng")
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {e}"

def translate_text(text, target_language="en"):
    """
    Translates text to the specified language (default: English).
    """
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error translating text: {e}"

def save_audio(text, filename="output.mp3"):
    """
    Saves the text as audio (MP3 format).
    """
    try:
        tts_engine.save_to_file(text, filename)
        tts_engine.runAndWait()
        print(f"Audio saved as {filename}")
    except Exception as e:
        print(f"Error with TTS: {e}")

def main():
    print("=== AI-Powered Accessibility Tool ===")
    
    # Upload image
    print("Please upload an image file...")
    uploaded = files.upload()
    if not uploaded:
        print("No file uploaded.")
        return
    
    # Extract uploaded file name
    image_path = list(uploaded.keys())[0]
    
    print("\nExtracting text from the image...")
    extracted_text = extract_text(image_path)
    if not extracted_text:
        print("No text detected in the image.")
        return
    
    print(f"\nExtracted Text:\n{extracted_text}")
    
    # User input for translation language
    target_language = input("\nEnter target language code (e.g., 'en' for English, 'es' for Spanish): ")
    translated_text = translate_text(extracted_text, target_language)
    print(f"\nTranslated Text:\n{translated_text}")
    
    # Save translated text as audio
    print("\nSaving the translated text as audio...")
    save_audio(translated_text)

if __name__ == "__main__":
    main()
