from step_01_transcriber import transcribe_movie
from step_02_script_writer import create_recap_script
from step_03_voice_generator import generate_voiceover
from step_04_scene_detector import detect_scenes
from step_05_video_editor import create_video
from step_06_shorts_generator import generate_shorts
from step_07_metadata_generator import generate_metadata
from step_08_uploader import upload_content


def run_pipeline():

    print("\n====================================")
    print("      MOVIE FACTORY STARTED")
    print("====================================\n")

    movie_path = "input_movies/Saw.mp4"

    transcribe_movie(movie_path)

    create_recap_script()

    generate_voiceover()

    detect_scenes()

    create_video()

    generate_shorts()

    generate_metadata()

    upload_content()

    print("\n====================================")
    print("      MOVIE FACTORY COMPLETE")
    print("====================================\n")


if __name__ == "__main__":
    run_pipeline()