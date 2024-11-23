from TelcAPI import Backend, Runner
from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/api/getData")
def getData():
    response = Runner.getScenario("268bdbc6-1e37-4392-ab63-8b4b557bd0b5")
    return jsonify(response.json())


if __name__ == "__main__":
    sc = Backend.getScenario("268bdbc6-1e37-4392-ab63-8b4b557bd0b5")
    Runner.initScenario(sc)
    app.run(debug=True)
