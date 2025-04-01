from extensions import db  # Import db from extensions

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def validate_description(self):
        return self.description and len(self.description) >= 20
