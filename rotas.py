from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer
import logging

from scraping import scraping


LOG_FORMAT = "%(levelname)s : %(filename)s : %(asctime)s : %(message)s"
logging.basicConfig(filename=".logs/ApiLogs",
                    level = logging.INFO,
                    format= LOG_FORMAT,
                    filemode= "w")
logger = logging.getLogger()

scrap = scraping()

app = Flask(__name__)

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

@app.route("/getExamples/<word>", methods=["GET"])
def getExample(word):
    logger.info(f"get examples of {word}")

    example = scrap.getExample(word)

    if example == None:
        logger.info(f"Palavra não encontrda")
        return jsonify({"None" : "Nenhnuma palavra encotrada"})
        
    return jsonify(example)

@app.route("/getInfo/<word>", methods=["GET"])
def getWordInfo(word):
    logger.info(f"get info of {word}")

    info = scrap.getWordInfo(word)

    if info == None:
        logger.info(f"Palavra não encontrda")
        return jsonify({"None" : "Nenhnuma palavra encotrada"})
        
    return jsonify(info)

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    logger.info("Server running - localhost:5000")
    print("Server running - localhost:5000")
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()