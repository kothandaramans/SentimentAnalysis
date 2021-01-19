from django.shortcuts import render
from django.contrib import messages
from sentimentAnalysis.models import UploadTxt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
'''
		Sentiment Analysis from Text
'''

context = {'title':'Sentiment Analysis from Text'}
def main(request):
	context['score'] = txt_sentiment_analyser('')
	return render(request,'index.html')

def txt_index(request):
	context['contents'] = 'This is totally irritating and a waste of time.'
	return render(request,'text_sentiment.html',context)

def txt_upload(request):
	try:
		txt = UploadTxt()
		txt.text = request.FILES['txtfile']
		txt.save()
	except Exception as ex:
		messages.error(request, 'something went wrong... try again')
		print(ex)
	txt = UploadTxt.objects.latest('id')
	txt.save()
	messages.success(request, 'file uploaded successfully')
	context['contents'] = open(txt.text.url,'r').read()
	return render(request,'text_sentiment.html',context)

def txt_analyser(request):
	if(request.POST):
		txts = request.POST['text']
		context['contents'],context['score'] = txts,txt_sentiment_analyser(txts)
	return render(request,'text_sentiment.html',context)

def txt_sentiment_analyser(sentence):
	sentiment = {}
	score = SentimentIntensityAnalyzer().polarity_scores(sentence)
	sentiment['positive'] = score.get('pos') * 100 
	sentiment['negative'] = score.get('neg') * 100
	sentiment['neutral'] = score.get('neu') * 100
	#sentiment['compound'] = score.get('compound')

	return sentiment
	