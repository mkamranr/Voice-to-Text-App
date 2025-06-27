# diarize.py
from pyannote.audio import Pipeline

class SpeakerDiarizer:
    def __init__(self, hf_token=None):
        # Use pretrained pyannote speaker diarization pipeline
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token=hf_token)

    def diarize(self, audio_path):
        diarization = self.pipeline(audio_path)
        # Return diarization result as list of segments with speaker label
        segments = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segments.append({"start": turn.start, "end": turn.end, "speaker": speaker})
        return segments

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python diarize.py <audio_path>")
        exit(1)
    audio_path = sys.argv[1]
    diarizer = SpeakerDiarizer()
    segments = diarizer.diarize(audio_path)
    for s in segments:
        print(f"Speaker {s['speaker']} from {s['start']:.2f}s to {s['end']:.2f}s")
