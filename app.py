from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/temperature", methods=["POST"])
def temperature():
    """An endpoint accepting a temperature reading"""

    data = request.json  # temperature reading
    
    print(data)

#    response = return.post(url, json=temp)
    return jsonify(data)
    # if temperature exceeds a certain treshold (e.g. 20 °C),
    # reply with a warning so the client can set the red LED

    # else just reply all is well and maybe signal that
    # the red LED should be switched off


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)