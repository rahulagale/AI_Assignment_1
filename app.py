import streamlit as st
import requests
import os
from sumy.parsers.plaintext import PlaintextParser # type: ignore
from sumy.nlp.tokenizers import Tokenizer # type: ignore
from sumy.summarizers.lex_rank import LexRankSummarizer # type: ignore

# Streamlit app title
st.title("Audio Transcription, Summarization and Timestamps App")

# File uploader for the user to upload an audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a", "flac"])

if uploaded_file is not None:
    # Display a loading spinner while the file is being processed
    with st.spinner('Transcribing...'):
        # Make a request to the FastAPI backend to transcribe the audio file
        try:
            files = {'file': uploaded_file.getvalue()}
            response = requests.post("http://localhost:8000/transcribe/", files=files)
            
            if response.status_code == 200:
                # Get the transcribed text and segments with timestamps
                data = response.json()
                transcription = data.get("transcription")
                segments = data.get("segments")

                # Display the transcribed text
                st.subheader("Transcription")
                st.write(transcription)

                # Save transcription to a local file
                transcription_file = "transcription.txt"
                with open(transcription_file, "w", encoding="utf-8") as file:
                    file.write(transcription)

                st.success(f"Transcription saved as {transcription_file}")

                # Summarize the transcribed text using sumy
                parser = PlaintextParser.from_string(transcription, Tokenizer("english"))
                summarizer = LexRankSummarizer()
                summary = summarizer(parser.document, sentences_count=3)  # Adjust sentences_count as needed
                
                # Join summarized sentences into a single string
                summarized_text = ' '.join([str(sentence) for sentence in summary])
                
                # Display the summary
                st.subheader("Summary")
                st.write(summarized_text)
                
                # Save summary to a local file
                summary_file = "summary.txt"
                with open(summary_file, "w", encoding="utf-8") as file:
                    file.write(summarized_text)
                
                st.success(f"Summary saved as {summary_file}")
                
                # Display the transcribed text with timestamps
                st.subheader("Timestamps")
                for segment in segments:
                    start = segment['start']
                    end = segment['end']
                    text = segment['text']
                    st.write(f"[{start:.2f}s - {end:.2f}s]: {text}")
                
                # Save transcription to a local file
                transcription_file = "timestamps.txt"
                with open(transcription_file, "w", encoding="utf-8") as file:
                    for segment in segments:
                        start = segment['start']
                        end = segment['end']
                        text = segment['text']
                        file.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")
                
                st.success(f"Timestamps saved as {transcription_file}")             
                
            else:
                error_message = response.json().get("error", "Unknown error occurred")
                st.error(f"Error in transcription: {error_message}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

else:
    st.write("Please upload an audio file.")
