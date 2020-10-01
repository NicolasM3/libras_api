from flask import Flask, jsonify
import logging

from scraping import scraping


LOG_FORMAT = "%(levelname)s : %(filename)s : %(asctime)s : %(message)s"
logging.basicConfig(filename=".logs/ApiLogs",
                    level = logging.INFO,
                    format= LOG_FORMAT,
                    filemode= "w")
logger = logging.getLogger()

scrap = scraping()

app = Flask("Libras Acedemy")

@app.route("/getDict/<latter>", methods=["GET"])
def getDictionary(latter):
    logger.info(f"getDictionary of {latter}")

    words = scrap.getDictionary(latter)

    if(words == None):
        logger.info(f"Letra não encontrda")
        return jsonify({"None" : "Nenhuma palavra encontrada com essa letra"})

    return jsonify(words)

@app.route("/getGif/<word>", methods=["GET"])
def getGif(word):
    logger.info(f"getGif of {word}")

    link = {"link": scrap.getGif(word)}

    if link == None:
        logger.info(f"Palavra não encontrda")
        return jsonify({"None" : "Nenhnuma palavra encotrada"})
        
    return jsonify(link)

app.run()
