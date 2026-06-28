import os
import re


def clean_text(text):
    """
    Clean transcript text so it is easier to use inside the recap script.
    """
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def split_into_sentences(text):
    """
    Split transcript into sentences.
    """
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def create_recap_script():
    """
    Read transcript and generate a simple YouTube-style recap script.

    This is a local placeholder version.
    It does not use a paid AI API yet.
    """

    print("[SCRIPT WRITER] Reading transcript...")

    transcript_path = "transcripts/Saw.txt"

    if not os.path.exists(transcript_path):
        print(f"[SCRIPT WRITER] ERROR: Transcript not found at {transcript_path}")
        return

    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    transcript = clean_text(transcript)

    if not transcript:
        print("[SCRIPT WRITER] ERROR: Transcript is empty.")
        return

    print("[SCRIPT WRITER] Creating recap script...")

    os.makedirs("scripts", exist_ok=True)

    movie_name = os.path.splitext(os.path.basename(transcript_path))[0]

    sentences = split_into_sentences(transcript)

    intro_sentences = sentences[:3]
    middle_sentences = sentences[3:8]

    intro_text = " ".join(intro_sentences)
    recap_text = " ".join(middle_sentences)

    if not recap_text:
        recap_text = transcript

    recap_content = f"""
================================
        {movie_name.upper()}: THE RECAP
================================

[INTRO / HOOK]

Alright, welcome back to Movie Factory.

Today we are breaking down "{movie_name}" using an automatically generated transcript.
No human typing. No manual note-taking. Just Python, Whisper, and pure automation doing the heavy lifting.

Based on the transcript, this is what the video starts with:

"{intro_text}"

[RECAP SECTION]

Here is the simplified recap based on the transcript:

{recap_text}

Now obviously, this is still the early version of the script writer. It is not using a full AI writer yet.
But the important part is that Movie Factory can now take a video, understand the audio, and turn that transcript into a structured script file.

That means the pipeline is officially moving from:

Movie
to Transcript
to Recap Script

[OUTRO]

And that is the first real content-generation step for Movie Factory.

The system is still basic right now, but the foundation is working.
Next, this script can be passed into a voice generator, turned into narration, matched with clips, and eventually turned into full YouTube and TikTok content.

================================
        END OF RECAP
================================
"""

    output_path = f"scripts/{movie_name}_recap.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(recap_content)

    print(f"[SCRIPT WRITER] Script saved to {output_path}")