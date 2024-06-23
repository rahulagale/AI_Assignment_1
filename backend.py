# backend.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import whisper # type: ignore
import os

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    try:
        audio_file = file.file.read()

        # Save the uploaded audio file temporarily
        with open("temp_audio_file.mp3", "wb") as f:
            f.write(audio_file)

        # Transcribe the audio file with timestamps
        result = model.transcribe("temp_audio_file.mp3", language="en", verbose=True)

        # Remove the temporary audio file
        os.remove("temp_audio_file.mp3")

        # Return the transcription and timestamps
        return JSONResponse(content={"transcription": result["text"], "segments": result["segments"]})

    except Exception as e:
        # Log the error and return an appropriate message
        return JSONResponse(content={"error": str(e)}, status_code=500)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
