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
