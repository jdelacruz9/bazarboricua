from flask import Flask, render_template, jsonify, request, url_for
import requests
import json
import urllib

app = Flask(__name__)

@app.route("/")
def render_index():

	results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/9mk69doc?apikey=HgwBvprFyRc0bv4DSiR3gXgM8fOS541L"))
	m_list = results
	
	return render_template("test.html", m_list = m_list)


if __name__=="__main__":
	app.run(debug=True)