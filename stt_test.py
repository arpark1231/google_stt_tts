from google.cloud import speech
import os
import io

#setting Google credential
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'speechtotext-378508-7f523e888801.json'
# create client instance 
client = speech.SpeechClient()

#the path of your audio file
file_name = "dialog1.wav"
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    enable_automatic_punctuation=True,
    audio_channel_count=2,
    language_code="ko-KR",
)

# Sends the request to google to transcribe the audio
response = client.recognize(request={"config": config, "audio": audio})
# Reads the response
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))