import whisper
import os


def transcribe_movie(movie_path):

    print("[TRANSCRIBER] Loading Whisper model...")

    model = whisper.load_model("base")

    print(f"[TRANSCRIBER] Transcribing {movie_path}...")

    result = model.transcribe(movie_path)

    transcript = result["text"]

    movie_name = os.path.splitext(
        os.path.basename(movie_path)
    )[0]

    output_path = f"transcripts/{movie_name}.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"[TRANSCRIBER] Transcript saved to {output_path}")