from flask import Flask, send_file, make_response
import json
import cv2

app=Flask(__name__)

@app.route("/")
def yndex():
	sample="Hey Ashik !"
	ss={"name":"Ashik"}
	s=json.dumps(ss)
	s2=json.loads(s)
	print(s)
	print(s2)
	return s

@app.route("/image")
def index():
	image=cv2.imread("sample.png")
	return send_file("sample.png",mimetype='image/png')

@app.route("/o")
def new():
	image=cv2.imread("sample.png")
	print(type(image))
	image2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	print(type(image2))
	retval, buffer = cv2.imencode('.png', image2)
	response = make_response(buffer.tobytes())
	response.headers['Content-Type'] = 'image/png'
	return response

app.run()