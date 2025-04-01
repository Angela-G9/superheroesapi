from extensions import db  # Import db from extensions

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
            'hero': self.hero.to_dict(),
            'power': self.power.to_dict()
        }

    def validate_strength(self):
        if self.strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of 'Strong', 'Weak', or 'Average'.")
