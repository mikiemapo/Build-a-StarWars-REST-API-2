from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    haircolor = db.Column(db.String(20), unique=True, nullable=False)
    eyecolor = db.Column(db.String(20), unique=True, nullable=False)


    def __repr__(self):
        return f'<Character {self.name}>'


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "haircolor": self.haircolor,
            "eyecolor": self.eyecolor
        }

    
class Planet(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(20), unique=True, nullable=False)
     climate = db.Column(db.String)
     gravity = db.Column(db.String)

     def __repr__(self):
        return f'<Planet {self.name}>'

     def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "gravity": self.gravity
        } 

  

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    manufacturer = db.Column(db.String(50), unique=True, nullable=False)
    length = db.Column(db.Numeric (4,2))
    passengers = db.Column(db.Integer)

    def __repr__(self):
        return f'<Vehicles {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "manufacturer": self.manufacturer,
            "length":self.length,
            "passengers":self.passengers
        } 

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    favorite_id = db.Column(db.Integer, unique=False, nullable=False)
    favorite_type = db.Column(db.String(256), unique=False, nullable=False)


    def __repr__(self):
        return f'<Favorite {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_if": self.user_id,
            "favorite_id":self.favorite_id,
            "favorite_type" : self.favorite_type
            # do not serialize the password, its a security breach
        }

    