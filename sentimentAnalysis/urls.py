from django.contrib import admin
from django.urls import path
from sentimentAnalysis.views import Tviews, Iviews, Aviews, Vviews

urlpatterns = [
	#main
	path('',Tviews.main, name='main'),

	#text path
	path('txt',Tviews.txt_index, name='index'),
	path('txt/upload',Tviews.txt_upload, name='txtupload'),
	path('txt/analyser',Tviews.txt_analyser, name='txtanalyser'),
	
	#image path
	path('img',Iviews.img_index, name='imgindex'),
	path('imgupload',Iviews.img_upload, name='imgupload'),
	path('imgextractor',Iviews.img_extractor, name='imgextractor'),
	path('imganalyser',Iviews.img_analyser, name='imganalyser'),

	#audio path
	path('audindex',Aviews.aud_index, name='audindex'),
	path('audupload',Aviews.aud_upload, name='audupload'),
	path('audextractor',Aviews.aud_extractor, name='audextractor'),
	path('audanalyser',Aviews.aud_analyser, name='audanalyser'),	

	#video path
	path('vidindex',Vviews.vid_index, name='vidindex'),
	path('vidupload',Vviews.vid_upload, name='vidupload'),
	path('vidextractor',Vviews.vid_to_audio, name='vidextractor'),
	path('vidanalyser',Vviews.vid_analyser, name='vidanalyser'),	

]
