import cv2
import os
import numpy as np
from keras.models import model_from_json, load_model
from keras.preprocessing import image

def img_emotion(img_path):
	
	face_haar_cascade = cv2.CascadeClassifier('media/models/haarcascade_frontalface_default.xml')

	test_img = cv2.imread(img_path)
	
	gray_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
	
	faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.12, 8)

	for(x,y,w,h) in faces_detected:
			model = model_from_json(open("media/models/fer.json", "r").read())
			model.load_weights('media/models/fer.h5')
			roi_gray=gray_img[y:y+w,x:x+h]
			roi_gray=cv2.resize(roi_gray,(48,48))
			img_pixels = image.img_to_array(roi_gray)
			img_pixels = np.expand_dims(img_pixels, axis = 0)
			img_pixels /= 255
			predictions = model.predict(img_pixels)

			max_index = np.argmax(predictions[0])

			emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
			predicted_emotion = emotions[max_index]
			print(predicted_emotion)

			res = {'positive':['happy','surprise'],'negative':['sad','fear','angry'],'neutral':['neutral','disgust']}
			if(predicted_emotion != None):
				if(predicted_emotion in res.get('positive')):
					return {'positive':66,'negative':17,'neutral':17}
				elif(predicted_emotion in res.get('negative')):
					return {'negative':66,'positive':17,'neutral':17}
				else:
					return {'neutral':66,'negative':17,'positive':17}
	return {'negative':33,'positive':33,'neutral':33}

def features(img_path):
	# new_model = load_model('media/models/imganlysis.h5')
	# classes = ['negative', 'neutral', 'positive']
	# im = cv2.imread(img_path)
	# im = cv2.resize(im, (100,100))
	# arg = new_model.predict(im.reshape((-1,100,100,3)))
	# if(classes[np.argmax(arg)] == 'negative'):
	# 	return {'negative':40,'positive':30,'neutral':30}
	# elif(classes[np.argmax(arg)] == 'neutral'):
	# 	return {'negative':30,'positive':30,'neutral':40}
	# else:
	# 	return {'negative':30,'positive':40,'neutral':30}
	return {'negative':33,'positive':33,'neutral':34}

