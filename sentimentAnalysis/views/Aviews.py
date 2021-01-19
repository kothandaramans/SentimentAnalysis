from django.shortcuts import render
from django.contrib import messages
from sentimentAnalysis.models import UploadAudio
from .Tviews import txt_sentiment_analyser
import speech_recognition as sr
from pydub import AudioSegment
'''
		Sentiment Analysis from Audio
'''
context = {'title':'Sentiment Analysis from Audio'}
def aud_index(request):
	context['contents'],context['some_flag'] = aud_url(), True
	return render(request,'audio_sentiment.html',context)
	
def aud_upload(request):
	try:
		aud = UploadAudio()
		aud.audio = request.FILES['audfile']
		aud.save()
	except Exception as ex:
		messages.error(request, 'something went wrong... try again')
		print(ex)
	messages.success(request, 'audio uploaded successfully')
	context['contents'] = aud_url()
	return render(request,'audio_sentiment.html',context)

def aud_extractor(request):
	trans = ''
	url = aud_url()
	print(url)
	try:
		trans = audio_to_text(url)
		if trans != '':
			messages.info(request, 'text extracted from audio')
		print(trans)
	except Exception as ex:
		messages.error(request, 'check internet connection')
		print(ex)
	context['contents'], context['txt'] = url, trans
	return render(request, 'audio_sentiment.html', context)

def audio_to_text(url):	
	if(url.endswith('.mp3')):
		sound = AudioSegment.from_mp3(url)
		AUDIO_FILE = "transcript.wav"
		sound.export(AUDIO_FILE, format="wav")  
	AUDIO_FILE = url
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)  # read the entire audio file   
		trans = r.recognize_google(audio)
	return trans

def aud_analyser(request):
	url = aud_url()
	if(request.POST):
		txts = request.POST['text']
		context['contents'], context['txt'], context['score'] = url, txts, txt_sentiment_analyser(txts)
	return render(request, 'audio_sentiment.html',context)

def aud_url():
	try:
		aud = UploadAudio.objects.latest('id')
		url = aud.audio.url
		aud.save()
	except Exception:
		url = r'media\audio\sample.wav'
	return url
	