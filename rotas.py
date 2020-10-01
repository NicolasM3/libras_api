from flask import Flask, jsonify

from scraping import scraping

scrap = scraping()

app = Flask("Libras Acedemy")

@app.route("/getDict/<latter>", methods=["GET"])
def getDictionary(latter):
    words = scrap.getDictionary(latter)
    return jsonify(words)

@app.route("/getGif/<word>", methods=["GET"])
def getGif(word):
    link = {"link": scrap.getGif(word)}
    return jsonify(link)

app.run()
