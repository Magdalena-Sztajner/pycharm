from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange, NoneOf
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"

app.config["SECRET_KEY"] = "123"  #klucz do szyfrowania formularza?

db = SQLAlchemy(app)



class GamesDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    genre = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # price = db.Column(db.Integer, nullable=False)
    # price = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)

    date_added = db.Column(db.DateTime, default=datetime.utcnow)      # system doda datę automatycznie



class GameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), NoneOf("^", message="nie można użyć tego znaku")])
    genre = StringField("Genre", validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired(), NumberRange(min=1, max=100)])
    # price = IntegerField("Cena", validators=[DataRequired()])
    # price = StringField("Cena", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired(), NumberRange(min=0.1, message="wartość musi być większa od 0")])

    submit = SubmitField("Submit")



# db.create_all()



@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    name = None
    price = None
    form = GameForm()
    print("1")
    print(form.price.data)
    print(form.name.data)
    print(form.genre.data)

    if form.validate_on_submit():
        title = GamesDatabase.query.filter_by(name=form.name.data).first()
        if title is None:
            title = GamesDatabase(name=form.name.data.title(), genre=form.genre.data.upper(),
                                 rating=form.rating.data, price=form.price.data)
            db.session.add(title)
            db.session.commit()
            flash("Game added successfully")
            name = form.name.data
            # form.name.data = ""         # czyszczeni formularzy (potrzebne?)
            # form.genre.data = ""
            # form.rating.data = ""
            # form.price.data = ""
        else:

            flash("Error! The game with the given title already exists")

    list_of_games = GamesDatabase.query.order_by(GamesDatabase.date_added)

    return render_template("add_game.html", form=form, name=name, list_of_games=list_of_games)




@app.route("/")
def index():

    list_of_games = GamesDatabase.query.order_by(GamesDatabase.date_added)

    return render_template("index.html", list_of_games=list_of_games)


@app.route("/test")
def test():
    list_of_games = GamesDatabase.query
    # print(request.args)


    if "rating_min" in request.args:
        rating_min = request.args.get("rating_min", 1, int)
        list_of_games = list_of_games.filter(GamesDatabase.rating >= rating_min)

    if "rating_max" in request.args:
        rating_max = request.args.get("rating_max", 100, int)
        list_of_games = list_of_games.filter(GamesDatabase.rating <= rating_max)

    if "price_min" in request.args:
        price_min = request.args.get("price_min", 1, int)
        list_of_games = list_of_games.filter(GamesDatabase.price >= price_min)

    if "price_max" in request.args:
        price_max = request.args.get("price_max", 100, int)
        list_of_games = list_of_games.filter(GamesDatabase.price <= price_max)

    if "genre" in request.args:
        list_of_games = list_of_games.filter(GamesDatabase.genre == request.args["genre"].upper())

    list_of_games = list_of_games.order_by(GamesDatabase.date_added)


    k = 1

    c = list_of_games.count()

    list_of_games = list_of_games.order_by(GamesDatabase.date_added)[(k-1)*2:(k)*8]

    args = []
    if request.args:
        for arg, val in request.args.items():
            args.append({"name": arg, "value": val})

    print(args)
    return render_template("test.html", list_of_games=list_of_games, args=args)  #next_page=next_page





@app.route("/top10")
def top10():

    return render_template("top10.html")



@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
        return render_template("500.html"), 500






































