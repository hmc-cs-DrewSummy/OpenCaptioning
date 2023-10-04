Name: Drew Summy
Email: dtsummy@gmail.com
Status: graduated
Link to Project Github: 

Project Name: Open Captioning


## 1. Brief Explanation of Project:
Open Captioning is a proof-of-concept project that attempts to improve the viewer experience of live media events such as debates. Often, things can be said without being fact-checked because searching online for relevant websites to validate a statement can be too time consuming to do in real time. Like closed captioning, Open Captioning adds information in parallel to media in an easily accessible manner to viewers who want to learn more and fact checkers looking to set the record straight.

## 2. How you Built it:
After deciding on a project, I researched some NLP python libraries for translating speech into text and other utilities for downloading from YouTube, converting mp4s to mp3s, and playing audio. Then wrote the outline for how the code would run and implemented it.

## 3. Challenges/Feedback on the API: 
In it's current form, Open Captioning leverages OpenAI Whisper to divide speech into text segments and then queries Metaphor with those segments. However, not everything said require additional context; only declarative sentences where the user is making a factual claim should be investigated. Furthermore, some factual claims are made across multiple statements and speakers. A more complex NLP model would have to be used. Lastly, Open Captioning takes a youtube url as an input instead of a livestream of data and buffering system.

## 4. Why you’re interested in Metaphor:
Metaphor is a great opportunity to learn more about AI and gain responsibility. Also, it's a great product!

## Getting Started
Open constants.py and replace {YOUR-METAPHOR-KEY} with your metaphor key. Install the dependencies below, navigate to the directory with OpenCaptioning.py, and run "python OpenCaptioning.py --link https://www.youtube.com/watch?v=qX-lKrLPrEQ" to get started. For more information, use the "--help" flag.

## Dependencies
Python 3
Pip with these commands to get started
    pip install pytube
    pip install git+https://github.com/linto-ai/whisper-timestamped
    pip install metaphor_python
    pip install pygame
    pip install moviepy
This has been tested on a Windows PC with Python 3.11.0 and ffmpeg installed.
