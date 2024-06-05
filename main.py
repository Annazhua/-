from flask import Flask, request, jsonify
import userData

app = Flask(__name__)

@app.route('/get_user', methods = ['GET'])
def funName2():

    id = int(request.args.get("id"))

    return jsonify(userData.data[id])

if __name__ == "__main__":
    app.run(debug=True)