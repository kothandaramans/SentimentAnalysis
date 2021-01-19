from django.shortcuts import render
from django.contrib import messages
from sentimentAnalysis.models import UploadImage
from .Tviews import txt_sentiment_analyser
import pytesseract
from PIL import Image
from sentimentAnalysis.caption_generator import caption
from sentimentAnalysis.image_emotion import img_emotion, features

'''
		Sentiment Analysis from Image
'''

context = {'title':'Sentiment Analysis from Image'}

def img_index(request):
	context['contents'] = img_url()
	return render(request,'image_sentiment.html',context)

def img_upload(request):
	try:
		img = UploadImage()
		img.image = request.FILES['imgfile']
		img.save()
	except Exception as ex:
		messages.error(request, 'something went wrong... try again')
		print(ex)
	context['contents'] = img_url()
	messages.success(request, 'image uploaded successfully')
	return render(request,'image_sentiment.html',context)

def img_extractor(request):
	url = img_url()
	try:
		img = Image.open(url)
		pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
		result = pytesseract.image_to_string(img)
		# result += '\n\n' + caption(url)
	except Exception as ex:
		print(ex)
		messages.error(request, 'something went wrong... try again')
	if result != '':
		messages.info(request, 'text extracted from image')
	context['contents'],context['txt'] = url, result
	return render(request,'image_sentiment.html',context)

def img_analyser(request):
	if(request.POST):
		url = img_url()
		txts = request.POST['text']
		score = txt_sentiment_analyser(txts)
		img_score = img_emotion(url)
		fea_score = features(url)
		print(score,img_score, fea_score)
		if(score['positive'] == 0.0 and score['negative'] == 0.0 and score['neutral'] == 0.0):
			score = img_score
		else:
			for key in score:
				score[key] = (score[key] + img_score[key] + fea_score[key]) / 3
		#score[list(img_score.keys())[0]] = (score[list(img_score.keys())[0]] + img_score[list(img_score.keys())[0]]) / 2
		context['contents'],context['txt'],context['score'] = url,txts,score
	return render(request,'image_sentiment.html',context)

def img_url():
	try:
		img = UploadImage.objects.latest('id')
		url = img.image.url
		img.save()
	except Exception:
		url = r'media\images\sample.png'
	return url
