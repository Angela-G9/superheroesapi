from extensions import db  # Import db from extensions
from .hero_power import HeroPower  # Adjusted import to avoid circular dependency

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

    powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'hero_powers': [
                {
                    'id': hero_power.id,
                    'hero_id': hero_power.hero_id,
                    'power_id': hero_power.power_id,
                    'strength': hero_power.strength,
                    'power': hero_power.power.to_dict()
                }
                for hero_power in self.powers
            ]
        }
