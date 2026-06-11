import streamlit as st
import os

from utils.audio import extract_audio
from utils.speech import speech_to_text
from utils.analyzer import (
    count_fillers,
    generate_score,
    generate_feedback,
    calculate_confidence
)
from utils.eyecontact import analyze_eye_contact

st.set_page_config(
    page_title="AI Interview Analyzer",
    layout="wide"
)

st.title("AI Interview Analyzer")

uploaded_video = st.file_uploader(
    "Upload Interview Video",
    type=["mp4"]
)

if uploaded_video is not None:

    os.makedirs("uploads", exist_ok=True)

    video_path = os.path.join(
        "uploads",
        uploaded_video.name
    )

    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())

    st.success("Video Saved Successfully!")

    audio_path = extract_audio(video_path)

    st.success("Audio Extracted Successfully!")

    transcript = speech_to_text(audio_path)

    st.subheader("Interview Transcript")

    with st.expander("View Transcript"):
        st.write(transcript)

    filler_count = count_fillers(transcript)

    score = generate_score(filler_count)

    feedback = generate_feedback(filler_count)

    eye_contact_score = analyze_eye_contact(video_path)

    confidence_score = calculate_confidence(
        score,
        eye_contact_score
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Filler Words",
            filler_count
        )

    with col2:
        st.metric(
            "Interview Score",
            f"{score}/100"
        )

    with col3:
        st.metric(
            "Eye Contact Score",
            f"{eye_contact_score}%"
        )

    with col4:
        st.metric(
            "Overall Confidence",
            f"{confidence_score}/100"
        )

    st.subheader("Communication Feedback")

    st.info(feedback)

    st.subheader("Eye Contact Feedback")

    if eye_contact_score >= 80:

        st.success(
            "Strong eye contact maintained throughout the interview."
        )

    elif eye_contact_score >= 60:

        st.warning(
            "Moderate eye contact detected. Try maintaining more consistent eye contact."
        )

    else:

        st.error(
            "Low eye contact detected. Improving eye contact can increase confidence."
        )

    report = f"""
AI Interview Analysis Report

Transcript:
{transcript}

Filler Words: {filler_count}

Interview Score: {score}/100

Eye Contact Score: {eye_contact_score}%

Overall Confidence Score: {confidence_score}/100

Communication Feedback:
{feedback}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="interview_report.txt",
        mime="text/plain"
    )