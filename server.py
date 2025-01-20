from flask import Flask, render_template, request


app =Flask("Emotion Detector")


@app.route("/emotionDetector")
def 