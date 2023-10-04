import sys, os
import time
import argparse
import constants
from pytube import YouTube
import whisper_timestamped
from metaphor_python import Metaphor
import pygame
from moviepy.editor import *

class SubtitleObject():
    def __init__(self, text, time, links):
        self.text = text
        self.time = time
        self.links = links

def main():
    parser = argparse.ArgumentParser(description="Argument Parser")
    parser.add_argument('-l', '--link', help='YouTube video url', required=True)
    parser.add_argument('-c', '--linkCount', help='Number of links to retrieve for each segment', default=1, required=False)
    args = vars(parser.parse_args())

    audioFilepath = getAudioFile(args['link'])

    subtitleObjects = processAudio(audioFilepath, int(args['linkCount']))

    playAudio(audioFilepath)

    displaySubtitles(subtitleObjects)

def getAudioFile(link):
    print("Getting audio file from link: " + link)

    audioFilepath = os.path.join(os.getcwd(), constants.tempFileName)

    if os.path.isfile(audioFilepath):
        os.remove(audioFilepath)

    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()
    downloadedAudioFilepath = audio.download(output_path=os.getcwd())

    mp4_without_frames = AudioFileClip(downloadedAudioFilepath)
    mp4_without_frames.write_audiofile(audioFilepath)
    mp4_without_frames.close()

    os.remove(downloadedAudioFilepath)

    return audioFilepath

def processAudio(path, linkCount):
    print("Processing audio file: " + path)
    audio = whisper_timestamped.load_audio(path)
    model = whisper_timestamped.load_model("base")
    result = whisper_timestamped.transcribe(model, audio, language="en")

    metaphor = Metaphor(constants.metaphorKey)
    subtitleObjects = []
    for segment in result["segments"]:
        text = segment["text"]
        time = segment["start"]
        response = metaphor.search(text, num_results=linkCount)
        links = []
        for result in response.results:
            links.append(result.url)
        subtitleObjects.append(SubtitleObject(text, time, links))
    return subtitleObjects

def playAudio(audioFilepath):
    print("Playing audio")
    pygame.mixer.init()
    pygame.mixer.music.load(audioFilepath)
    pygame.mixer.music.play()

def displaySubtitles(subtitleObjects):
    print("Displaying subtitles:")
    currentTime = 0
    for subtitleObject in subtitleObjects:
        time.sleep(subtitleObject.time - currentTime)
        currentTime = subtitleObject.time
        print(subtitleObject.text)
        for link in subtitleObject.links:
            print(f"\t{link}")

if __name__ == '__main__':
    main()