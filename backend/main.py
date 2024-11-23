from TelcAPI import Backend, Runner
from flask import Flask, jsonify, request
from flask_cors import CORS
from eventloop import eventLoop
from multiprocessing import Process
import json

app = Flask(__name__)
CORS(app)


@app.route("/api/getData")
def getData():
    scenarioId = request.args.get("scenarioId")
    response = Runner.getScenario(scenarioId)
    return jsonify(response.json())


@app.route("/api/startScenario")
def startScenario():
    scenarioId = request.args.get("scenarioId")
    Runner.initScenarioById(scenarioId)
    Runner.launchScenario(scenarioId, 0.001)
    response = Runner.getScenario(scenarioId)
    process = Process(target=eventLoop, args=(scenarioId,))
    process.start()
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
