from TelcAPI import Backend, Runner
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/api/getData")
def getData():
    scenarioId = request.args.get("scenarioId")
    response = Runner.getScenario(scenarioId)
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)
