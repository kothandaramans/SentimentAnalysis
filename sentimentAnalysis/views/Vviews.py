from django.shortcuts import render
from django.contrib import messages
from sentimentAnalysis.models import UploadVideo
from .Tviews import txt_sentiment_analyser
import moviepy.editor as editor
from .Aviews import audio_to_text
import os
import cv2
from sentimentAnalysis.caption_generator import caption

'''
		Sentiment Analysis from Video
'''
context = {'title':'Sentiment Analysis from Video'}
def vid_index(request):
	context['contents'] = vid_url()
	return render(request,'video_sentiment.html',context)

def vid_upload(request):
	try:
		vid = UploadVideo()
		vid.video = request.FILES['vidfile']
		vid.save()
	except Exception as ex:
		messages.error(request, 'something went wrong... try again')
		print(ex)
	context['contents'] = vid_url()
	messages.success(request, 'video uploaded successfully')
	return render(request,'video_sentiment.html',context)
    
def vid_analyser(request):
	url = vid_url()
	if(request.POST):
		txts = request.POST['text']
		context['contents'], context['txt'], context['score'] = url, txts, txt_sentiment_analyser(txts)
	return render(request, 'video_sentiment.html',context)

def vid_to_audio(request):
	url = vid_url()
	result = ''
	#messages.info(request, 'video analysing...')
	try:
		video = editor.VideoFileClip(url)
		audio = video.audio
		audio.write_audiofile('sample.wav')
		result = audio_to_text('sample.wav')
		result += '\n\n' + clip_caption(url)
		if result != '':
			messages.info(request, 'text extracted from video')
		#os.remove('sample.wav')
	except Exception as ex:
		print(ex)
		messages.error(request, 'something went wrong... try again')
	context['contents'],context['txt'] = url, result
	return render(request,'video_sentiment.html',context)

def clip_caption(url):
	cap = cv2.VideoCapture(url)
	framerate = cap.get(cv2.CAP_PROP_FPS)
	framecount = 0
	count = 0
	res = ''
	while(cap.isOpened()):
	    try:
	        ret, frame = cap.read()
	        framecount += 1
	        if(framecount == (round(framerate) * 4)):
	        	framecount = 0
	        	cv2.imwrite("media/frames/frame%d.jpg" % count, frame)
	        	res += ' ' + caption('media/frames/frame%d.jpg' % count)
	        	count += 1
	    except Exception as ex:
	        print(ex)
	        break
	cap.release()
	return res

def vid_url():
	try:
		vid = UploadVideo.objects.latest('id')
		url = vid.video.url
		vid.save()
	except Exception:
		url = r'media\video\sample.mp4'
	return url
