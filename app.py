from flask import Flask,jsonify, request
from http import HTTPStatus
from datetime import datetime
app = Flask(__name__)

itemsList = []

@app.get("/items")
def retrieve():
    return jsonify(itemsList), HTTPStatus.OK

@app.post("/items")
def create():
    data = request.get_json()
    print(f"{data=}")
    req = request
    print(f"{req=}")

    data['created'] = datetime.now().strftime("%d/%m/%Y")
    
    if len(itemsList) == 0:
        data['id'] = 1
    else:
        data['id'] = itemsList[-1]['id'] + 1    

    itemsList.append(data)
    
    objReturn = {"message": "Item adicionado a lista", "item": data}
    
    return jsonify(objReturn), HTTPStatus.CREATED

if __name__ == "__main__":
   app.run(debug=True) 