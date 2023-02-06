from flask import Flask,jsonify, request
from http import HTTPStatus
from datetime import datetime

itemsList = []

def create_app():
    app = Flask(__name__)


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

    return app
 