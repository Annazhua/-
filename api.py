from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/route_name', methods=['GET'])
def sayHelloWorld():
    data = {
        1: "Hello world"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)