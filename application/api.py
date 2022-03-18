from application.app import app, db
from flask import request
from application.models import User, Car, Question, UserAnswer, Quiz

# Import your models here
from application.models import User


@app.route("/")
def home():
    return {"Status": "Success"}, 200


# Write your API endpoints here

# Action          | Table Name | REST Method | Endpoint      | Response | Error | Request Parameters | Response Parameters |
# |-------------- |------------|-------------|---------------|----------|------ |--------------------|---------------------|
# |log in         | User       | POST        | /users        | 200      | 400   |                    |
# |sign up        | User       | POST        | /users        | 200      | 400   |                    |
# |update user    | User       | PUT         | /users        | 200      | 400   | user id            |
# |delete user    | User       | DELETE      | /users/id     | 200      | 400   | user id            |
# |get user       | User       | GET         | /users/id     | 200      | 400   | user id            |
# |add car        | Car        | POST        | /cars         | 200      | 400   | name,manu,launyear,type,milage,varient,price |
# |delete car     | Car        | DELETE      | /cars/id      | 200      | 400   | car id |
# |update car     | Car        | PUT         | /cars/id      | 200      | 400   | car id |
# |get car        | Car        | GET         | /cars/id      | 200      | 400   | car id |
# |add question   | Question   | POST        | /questions    | 200      | 400   | question,options |
# |update question| Question   | PUT         | /questions/id | 200      | 400   | question id |
# |delete question| Question   | DELETE      | /questions/id | 200      | 400   | question id |
# |get question   | Question   | GET         | /questions/id | 200      | 400   | question id |
# |start quiz     | Quiz       | POST        | /quiz         | 200      | 400   | user id |
# |end quiz       | Quiz       | POST        | /quiz/id      | 200      | 400   | quiz id | car recommen |


@app.route("/cars", methods=["POST"])
def add_car():
    params = request.json
    car = Car(car_name=params["name"], car_manufacturer=params["manufacturer"], car_launch_year=params["launch_year"],
              car_type=params["type"], car_mileage=params["mileage"], car_variant=params["variant"],
              car_price=params["price"])
    db.session.add(car)
    db.session.commit()
    return {"id": car.car_id, "name": car.car_name}


@app.route("/cars/<int:car_id>", methods=["GET"])
def get_car(car_id):
    car = Car.query.get("car_id")
    return {"name": car.car_name, "manufacturer": car.car_manufacturer, "launch_year": car.car_launch_year,
            "type": car.car_type, "mileage": car.car_mileage, "variant": car.car_variant, "price": car.car_price}


@app.route("/cars/<int:car_id>", methods=["PUT"])
def update_car(car_id):
    params = request.json
    car = Car.query.get("car_id")
    car.car_name = params["name"]
    car.car_manufacturer = params["manufacturer"]
    car.car_launch_year = params["launch_year"]
    car.car_type = params["type"]
    car.car_mileage = params["mileage"]
    car.car_variant = params["variant"]
    car.car_price = params["price"]
    db.session.add(car)
    db.session.commit()
    return {"Status": "Success", "message": "Car Updated"}


@app.route("/cars/<int:car_id>", methods=["DELETE"])
def delete_car(car_id):
    car = Car.query.get("car_id")
    db.session.delete(car)
    db.session.commit()
    return {"Status": "Success", "message": "Car Deleted"}


@app.route("/questions", methods=["POST"])
def add_question():
    params = request.json
    question = Question(question=params["question"], options=params["options"])
    db.session.add(question)
    db.session.commit()
    return {"id": question.question_id, "question": question.question, "options": question.options}


@app.route("/questions/<int:question_id>", methods=["PUT"])
def update_question(question_id):
    params = request.json
    question = Question.query.get("question_id")
    question.question = params["question"]
    question.options = params["options"]
    db.session.add(question)
    db.session.commit()
    return {"id": question.question_id, "question": question.question, "options": question.options}


@app.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question(question_id):
    question = Question.query.get("question_id")
    db.session.delete(question)
    db.session.commit()
    return {"Status": "Success", "message": "Question Deleted"}


@app.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = Question.query.get("question_id")
    return {"id": question.question_id, "question": question.question, "options": question.options}



def start_quiz():
    pass



def

