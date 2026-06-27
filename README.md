# Movie Factory

Movie Factory is an AI-powered video transcription and content automation pipeline built in Python. The project is designed to turn a source video into a structured content workflow: transcription, recap script generation, narration, scene detection, edited video output, short-form clips, metadata, and eventual upload automation.

This repository is an early-stage build. The current working checkpoint focuses on the core pipeline structure and the first functional module: video transcription using OpenAI Whisper. The remaining modules are scaffolded as separate pipeline steps so they can be developed, tested, and improved independently.

## Project Goal

The goal of Movie Factory is to create a modular automation system that can process long-form video content and generate reusable outputs for content creation workflows.

Planned outputs include:

* Full video transcript
* Recap or narration script
* Voiceover audio
* Scene timestamps and clips
* Edited long-form recap video
* Short-form clips for social platforms
* Titles, descriptions, and tags
* Upload-ready content packages

## Current Status

The project currently includes:

* A main pipeline runner in `main.py`
* A functional Whisper-based transcription step in `step_01_transcriber.py`
* Modular placeholder files for later workflow steps
* Transcript output storage in the `transcripts/` folder
* Basic configuration and utility files

The current version is not a finished production system. It is a working project foundation that demonstrates pipeline design, modular architecture, and the first functional AI automation component.

## Pipeline Structure

```text
movie_factory/
├── main.py
├── config.py
├── step_01_transcriber.py
├── step_02_script_writer.py
├── step_03_voice_generator.py
├── step_04_scene_detector.py
├── step_05_video_editor.py
├── step_06_shorts_generator.py
├── step_07_metadata_generator.py
├── step_08_uploader.py
├── utils.py
└── transcripts/
```

## Workflow

The intended pipeline flow is:

1. Load an input video file
2. Transcribe the video using Whisper
3. Generate a recap script from the transcript
4. Generate narration or voiceover audio
5. Detect important scenes
6. Create a long-form edited video
7. Generate short-form clips
8. Generate metadata such as titles, descriptions, and tags
9. Prepare or upload the final content

The current implemented step is transcription. The later steps are intentionally separated into their own modules so the project can grow without turning into one large script.

## Tech Stack

* Python
* OpenAI Whisper
* FFmpeg planned for video/audio processing
* Modular pipeline architecture
* AI-assisted content automation

## Example Current Flow

`main.py` runs each project step in order:

```python
transcribe_movie(movie_path)
create_recap_script()
generate_voiceover()
detect_scenes()
create_video()
generate_shorts()
generate_metadata()
upload_content()
```

At the current checkpoint, the transcription step loads a Whisper model, transcribes the input video, and saves the transcript as a text file.

## Why This Project Matters

Movie Factory is meant to show practical AI workflow design rather than a single isolated script. The project demonstrates:

* Breaking a complex automation problem into smaller modules
* Building a repeatable AI pipeline
* Using speech-to-text to transform video into structured text
* Designing for future integration with LLMs, voice generation, video editing, and publishing tools
* Thinking about automation as a full system instead of a one-off task

## Roadmap

Planned improvements:

* Add input file validation
* Add a clean command-line interface
* Improve transcript formatting
* Add LLM-based recap script generation
* Add voiceover generation
* Add scene detection and clip selection
* Add FFmpeg-based video editing
* Add short-form clip generation
* Add metadata generation
* Add error handling and logging
* Add sample outputs and screenshots
* Add setup instructions and dependency management

## Disclaimer

This project is for learning, experimentation, and portfolio development. It is currently in progress and should not be treated as a finished production application.
