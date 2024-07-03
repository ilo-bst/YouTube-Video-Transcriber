import os
from pytube import YouTube
from moviepy.editor import AudioFileClip
import speech_recognition as sr
from pydub import AudioSegment

# Function to download YouTube video
def download_video(url, output_path):
    print(f"Downloading video from {url}")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=output_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    print(f"Video downloaded to {new_file}")
    return new_file

# Function to convert video to audio
def video_to_audio(video_file, output_audio_file):
    print(f"Converting video {video_file} to audio")
    audio_clip = AudioFileClip(video_file)
    audio_clip.write_audiofile(output_audio_file)
    audio_clip.close()
    print(f"Audio extracted to {output_audio_file}")

# Function to transcribe audio to text
def transcribe_audio(audio_file):
    print(f"Transcribing audio from {audio_file}")
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_file)

    # Split audio into chunks of 1 minute
    chunk_length_ms = 60000  # 1 minute
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    full_text = ""
    for i, chunk in enumerate(chunks):
        chunk.export("chunk.wav", format="wav")
        with sr.AudioFile("chunk.wav") as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                full_text += text + " "
                print(f"Chunk {i + 1}/{len(chunks)} transcribed.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

    os.remove("chunk.wav")
    print("Transcription complete")
    return full_text

# Main execution
if __name__ == "__main__":
    video_url = input("Please enter the YouTube video URL: ")
    text_output_file = input("Please enter the name for the output text file (with .txt extension): ")
    output_path = "downloads"
    audio_output_file = "audio.wav"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    print("Starting download process...")
    video_file = download_video(video_url, output_path)
    
    print("Starting audio extraction process...")
    video_to_audio(video_file, audio_output_file)
    
    print("Starting transcription process...")
    text = transcribe_audio(audio_output_file)
    
    with open(text_output_file, "w", encoding="utf-8") as file:
        file.write(text)
    
    print(f"Text has been extracted and saved to {text_output_file}")
