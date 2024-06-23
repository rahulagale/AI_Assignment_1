# Audio Transcription, Summarization and Timestamps App using Whisper

The project offers a web-based application for transcribing and summarizing audio files using advanced machine learning models. Built using FastAPI for the backend and Streamlit for the frontend, it converts speech to text.

# Features
- Timestamps: Provides timestamps for each segment of the transcribed text.
- Automatic File Saving: Automatically saves the transcription and summary as text files on the user's local machine.
- User-Friendly Interface: Easy-to-use interface for uploading audio files and viewing results.
- Audio Transcription: Converts audio files into text using the Whisper model.
- Text Summarization: Generates a concise summary of the transcribed text using the BART model from the Hugging Face transformers library.

# Technologies Used
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- Streamlit: An open-source app framework for Machine Learning and Data Science projects.
- Whisper: A powerful speech recognition model.
- Hugging Face Transformers: A library of state-of-the-art pre-trained models for Natural Language Processing tasks.

# Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

# Running the Application

1. Start the FastAPI backend:
<pre>
python backend.py
</pre>

2. Start the Frontend:
<pre>
streamlit run app.py
</pre>

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Whisper by OpenAI for speech recognition.
Hugging Face for the BART summarization model.
The Streamlit and FastAPI communities for their excellent frameworks.
