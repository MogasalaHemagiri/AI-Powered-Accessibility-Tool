## AI-Powered Accessibility Tool

## Overview

The **AI-Powered Accessibility Tool** is designed to enhance accessibility by converting images with text into audio files. This tool leverages advanced AI techniques such as Optical Character Recognition (OCR) for text extraction, machine translation for multilingual support, and text-to-speech (TTS) for auditory output. It is especially useful for individuals with visual impairments or those looking for multi-language accessibility in images.

## Features

- **Image to Text Conversion**: Utilizes Tesseract OCR to extract text from images.
- **Multi-Language Translation**: Supports multiple languages using Google Translate API.
- **Text-to-Speech (TTS)**: Converts the extracted text or translated text into an audio file using pyttsx3.

## Demo

![AI-Powered Accessibility Tool Demo](assets/demo_image.png)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Snippets](#code-snippets)
- [Environment Setup](#environment-setup)
- [License](#license)

## Installation

### Prerequisites

To run the AI-Powered Accessibility Tool, make sure you have the following installed:

- **Python 3.x**
- **pip** (Python package installer)
  
### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-powered-accessibility-tool.git
   cd ai-powered-accessibility-tool
   ```

2. **Install Required Libraries**:
   Run the following command to install all necessary dependencies:
   ```bash
   pip install pytesseract pillow pyttsx3 googletrans==4.0.0-rc1
   ```

3. **Install Tesseract OCR**:
   Depending on your environment, install Tesseract as described below:

   - **Linux**:
     ```bash
     sudo apt-get install -y tesseract-ocr
     sudo apt-get install -y libtesseract-dev
     sudo apt-get install -y espeak-ng
     sudo apt-get install -y espeak
     ```

   - **Windows**:
     Download and install Tesseract from [this link](https://github.com/UB-Mannheim/tesseract/wiki) and add it to your system PATH.

4. **Google Colab Setup** (Optional):
   If you're using Google Colab, the necessary dependencies (like Tesseract) are already available. Ensure to run the Colab code snippets as shown in the main code section.

## Usage

### Running the Tool

1. **Upload an Image**: Upon running the program, you will be prompted to upload an image file containing text.
2. **Text Extraction**: The tool uses Tesseract OCR to extract text from the image.
3. **Translation**: After text extraction, you will be prompted to enter a target language code (e.g., 'en' for English, 'es' for Spanish).
4. **Text-to-Speech**: The translated text is converted into an audio file (MP3 format) and saved.

### Example Flow

```bash
=== AI-Powered Accessibility Tool ===
Please upload an image file...
Image uploaded: 'image_example.png'
Extracting text from the image...
Extracted Text: "This is a sample text."

Enter target language code (e.g., 'en' for English, 'es' for Spanish): es
Translated Text: "Este es un texto de muestra."

Saving the translated text as audio...
Audio saved as output.mp3
```

### Code Snippets

#### Text Extraction from Image

```python
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
```

#### Translation Function

```python
def translate_text(text, target_language="en"):
    """
    Translates text to the specified language (default: English).
    """
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error translating text: {e}"
```

#### Save Text as Audio

```python
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
```

## Environment Setup

This tool can be executed in different environments:

### 1. **Google Colab**
   - Open the notebook in Google Colab, and run each code cell in order. The required libraries and dependencies are pre-installed on Colab, except Tesseract which can be installed using the command `!apt-get install`.

### 2. **Local Environment (Linux/Mac/Windows)**
   - Make sure Python 3.x and pip are installed.
   - Follow the **Installation** steps to set up the environment.
   - Install Tesseract OCR and configure the path for your operating system.

### 3. **Virtual Environment (Recommended)**
   To avoid dependency conflicts, it is highly recommended to use a virtual environment. Run the following commands to set up a virtual environment:

   ```bash
   python3 -m venv accessibility-env
   source accessibility-env/bin/activate  # On Windows, use `accessibility-env\Scripts\activate`
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! If you'd like to improve the project or add features, please feel free to submit a pull request. Here's how:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

--`
