from application.app import app, db
from datetime import date
from sqlalchemy import ARRAY
"""
- Table 3 : Users (No relationships in table 3)
  - Full Name : string
  - Login ID : string
  - Email ID : string
  - Password : password
  - Last Login : datetime
  - Number of attempts before successful login : int
"""


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    login_id = db.Column(db.String(80), unique=True, nullable=False)
    email_id = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))
    last_login = db.Column(db.Date)
    attempts_before_login = db.Column(db.Integer)
    """Need to use a hashing algorithm and change the data type later"""


# Sample for One-many and Many-Many relationship
# class WorkItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(120))

#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shared_with = db.relationship('User', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))

# shared_with = db.Table('shared_with',
#     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# Using the above sample write the DB models here
"""
- Table 1 : Cars (No relationships in table 1)
  - Car Name : string
  - Manufacturer : string
  - Launch Year : int
  - Type : string
  - Mileage : int
  - Variant : string
  - Price : float
"""


class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_name = db.Column(db.String(50), nullable=False)
    car_manufacturer = db.Column(db.String(50), nullable=False)
    car_launch_year = db.Column(db.Date, nullable=False)
    car_type = db.Column(db.String(10), nullable=False)
    car_mileage = db.Column(db.Float, nullable=False)
    car_variant = db.Column(db.String(50), nullable=False)
    car_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.Date, default=date.today())

"""
- Table 2 : Questions (No relationships in table 2)
  - QuestionID : int
  - Question : str
  - Options : list of str
    - Question1 : What is your driving condition? - City or Highway driving? : string
    - Question2 : Does all members of your family use the car? : string
    - Question3 : Does all members of your family know how to drive a manual car? : string
    - Question4 : How big is your family? : string
    - Question5 : Does Safety matter to you? : string
    - Question 6: Does Infotainment System in a car matter to you? : string
    - Question 7: Do you have any babies at home? : string
    - Question 8: Do you need a car with good mileage? : string
    - Question 9: Do you live in a state in India where there are restrictions on Diesel Cars? : string
    - Question 10: Do you live in a state where there are additional incentives for Electric Vehicles? : string
"""


class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(1200), nullable=False)
    options = db.Column(db.ARRAY(db.String), nullable=False)
    created_at = db.Column(db.Date, default=date.today())


"""
- Table 4: Quiz
  - QuizID : int auto-increment
  - UserName : str ref Users (Many quizzes can be taken by one user, so M21)
  - UserInputs : str ref Questions (Each question in a quiz can have only one answer, so 121)
  - Submitclicked : bool
  - CarRecommendation : string ref Cars (Each quiz can have only one car recommendation, so 121)
  - Datetime : datetime

Q1 U1
Q2 U1
Q3 U2

Ex: Separate Option table

Question1 [O1, O2, O3, O4] 
Q2        [O1, O2, O3]
"""
"""
Table User Options
- quiz_id
- question_id
- option


Quiz Question  UserAnswer

quiz = Quiz.query(id=2)
quiz.user_answer

# UserAnswer.query(quiz_id=2)

"""


class UserAnswer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quiz_id = db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.quiz_id'), nullable=False)
    question_id = db.Column('question_id', db.Integer, db.ForeignKey('question.question_id'), nullable=False)
    option = db.Column(db.String(64), nullable=False)


class Quiz(db.Model):
    # 1 quiz only be taken by 1 user
    quiz_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    # 1 quiz taken by 1 user can have multiple questions
    # the same question can be answered by a different user in a different quiz
    # Quiz1 - User1  - Q1,Q2,Q3...
    # Quiz2 - User2  - Q1,Q2,Q3...
    # Quiz3 - User1  - Q1,Q2,Q3...
    user_answer = db.relationship('Question', secondary=UserAnswer, lazy='subquery', backref=db.backref('Question', lazy=True))
    sub_click = db.Column('sub_click', db.Boolean, nullable=False)
    car_rec = db.Column('car_rec', db.Integer, db.ForeignKey('car.car_id'), nullable=False)
    quiz_time = db.Column(db.Date, default=date.today())

# create all tables and initialize app


db.create_all()
db.init_app(app)
