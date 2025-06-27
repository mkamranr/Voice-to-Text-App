# Voice-to-Text App with Whisper + Speaker Diarization

This repository provides a pipeline to convert speech audio to text with speaker separation, using OpenAI Whisper for transcription and PyAnnote for speaker diarization.

---

## Features

- Speaker diarization to split audio by speaker segments.
- Transcription of each speaker segment with Whisper.
- Output shows who spoke what and when.

---

## Requirements

- Python 3.8+
- FFmpeg installed and added to system PATH (https://ffmpeg.org/download.html)
- Hugging Face account with access token for pyannote.audio pretrained models.

---

## Installation

1. Clone the repo:

    ```bash
    git clone <repo_url>
    cd voice-to-text-app
    ```

2. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set your Hugging Face token as an environment variable:

    ```bash
    export HF_TOKEN="your_hf_token_here"   # Linux/macOS
    set HF_TOKEN=your_hf_token_here        # Windows PowerShell
    ```

---

## Usage

### 1. Speaker Diarization Only

```bash
python diarize.py path/to/audio.wav
```

### 2. Transcription Only

```bash
python transcribe.py path/to/audio.wav
```

### 3. Full Pipeline (Diarization + Transcription)

```bash
python pipeline.py path/to/audio.wav
```

---

## Notes

- Input audio should be WAV or compatible format supported by pydub/ffmpeg.
- Speaker diarization accuracy depends on audio quality and number of speakers.
- Whisper model size can be changed in code (base, small, medium, large).

---

## Author

Muhammad Kamran Rafi  
[GitHub](https://github.com/mkamranr) • [LinkedIn](https://www.linkedin.com/in/kamranrafi/)
