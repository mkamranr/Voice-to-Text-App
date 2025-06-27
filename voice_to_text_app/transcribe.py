# transcribe.py
import whisper

class WhisperTranscriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result["text"]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_path>")
        exit(1)
    audio_path = sys.argv[1]
    transcriber = WhisperTranscriber()
    print("Transcription:")
    print(transcriber.transcribe(audio_path))
