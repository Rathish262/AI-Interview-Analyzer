# AI Interview Analyzer

An AI-powered interview assessment system that evaluates communication skills and non-verbal behavior from interview videos using Natural Language Processing (NLP) and Computer Vision techniques.

## Features

* Upload interview videos for automated analysis
* Extract audio from video recordings
* Convert speech to text using Speech Recognition
* Detect filler words (e.g., "um", "uh", "like")
* Generate interview performance scores
* Analyze eye contact using MediaPipe and OpenCV
* Calculate overall confidence score
* Provide personalized feedback for improvement
* Download interview analysis reports

## Tech Stack

* Python
* Streamlit
* SpeechRecognition
* MoviePy
* OpenCV
* MediaPipe
* Natural Language Processing (NLP)
* Computer Vision

## Project Workflow

1. User uploads an interview video.
2. Audio is extracted from the video.
3. Speech-to-text conversion generates the transcript.
4. NLP techniques analyze filler word usage.
5. Computer Vision evaluates eye contact consistency.
6. Interview and confidence scores are generated.
7. Personalized feedback and downloadable reports are provided.

## Installation

```bash
git clone https://github.com/Rathish262/AI-Interview-Analyzer.git
cd AI-Interview-Analyzer
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```
AI-Interview-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── uploads/
└── utils/
    ├── analyzer.py
    ├── audio.py
    ├── speech.py
    └── eyecontact.py
```

## Future Enhancements

* Integration with OpenAI Whisper for improved transcription accuracy
* Real-time interview analysis using webcam input
* Facial emotion recognition
* AI-generated interview improvement suggestions
* Support for multilingual interviews

## Author

**Rathish**

It's harder to read code than to write it.

