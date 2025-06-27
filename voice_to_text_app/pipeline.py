# pipeline.py
import os
import tempfile
from pydub import AudioSegment
from transcribe import WhisperTranscriber
from diarize import SpeakerDiarizer

class VoiceToTextPipeline:
    def __init__(self, whisper_model="base", hf_token=None):
        self.diarizer = SpeakerDiarizer(hf_token)
        self.transcriber = WhisperTranscriber(whisper_model)

    def run(self, audio_path):
        print("Running speaker diarization...")
        segments = self.diarizer.diarize(audio_path)

        audio = AudioSegment.from_file(audio_path)
        transcripts = []

        print("Transcribing each speaker segment...")
        for seg in segments:
            start_ms = int(seg["start"] * 1000)
            end_ms = int(seg["end"] * 1000)
            segment_audio = audio[start_ms:end_ms]

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmpfile:
                segment_audio.export(tmpfile.name, format="wav")
                text = self.transcriber.transcribe(tmpfile.name)

            transcripts.append({"speaker": seg["speaker"], "start": seg["start"], "end": seg["end"], "text": text})

        return transcripts

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python pipeline.py <audio_path>")
        exit(1)

    audio_path = sys.argv[1]
    hf_token = None  # Add your HuggingFace token if needed

    pipeline = VoiceToTextPipeline(hf_token=hf_token)
    results = pipeline.run(audio_path)

    for res in results:
        print(f"[{res['speaker']}][{res['start']:.2f}-{res['end']:.2f}]: {res['text']}")
