from flask import Blueprint, jsonify, request
from extensions import db  # Import db from extensions
from models.hero import Hero
from models.power import Power
from models.hero_power import HeroPower

hero_routes = Blueprint('hero_routes', __name__)

def get_or_404(model, id):
    """Helper function to get a model instance or return a 404 error."""
    instance = model.query.get(id)
    if not instance:
        return jsonify({"error": f"{model.__name__} not found"}), 404
    return instance

@hero_routes.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@hero_routes.route('/heroes', methods=['POST'])
def create_hero():
    data = request.get_json()
    if not data.get('name') or not data.get('super_name'):
        return jsonify({"error": "Name and super_name are required"}), 400
    hero = Hero(name=data['name'], super_name=data['super_name'])
    db.session.add(hero)
    db.session.commit()
    return jsonify(hero.to_dict()), 201

@hero_routes.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = get_or_404(Hero, id)
    if isinstance(hero, tuple):  # If it's a 404 response
        return hero
    return jsonify(hero.to_dict())

@hero_routes.route('/heroes/<int:id>', methods=['PATCH'])
def update_hero(id):
    hero = get_or_404(Hero, id)
    if isinstance(hero, tuple):  # If it's a 404 response
        return hero

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    hero.name = data.get('name', hero.name)
    hero.super_name = data.get('super_name', hero.super_name)
    db.session.commit()
    return jsonify(hero.to_dict())

@hero_routes.route('/heroes/<int:id>', methods=['DELETE'])
def delete_hero(id):
    hero = get_or_404(Hero, id)
    if isinstance(hero, tuple):  # If it's a 404 response
        return hero

    db.session.delete(hero)
    db.session.commit()
    return jsonify({"message": "Hero deleted successfully"}), 200

@hero_routes.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@hero_routes.route('/powers', methods=['POST'])
def create_power():
    data = request.get_json()
    if not data.get('name') or not data.get('description'):
        return jsonify({"error": "Name and description are required"}), 400
    power = Power(name=data['name'], description=data['description'])
    db.session.add(power)
    db.session.commit()
    return jsonify(power.to_dict()), 201

@hero_routes.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = get_or_404(Power, id)
    if isinstance(power, tuple):  # If it's a 404 response
        return power
    return jsonify(power.to_dict())

@hero_routes.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = get_or_404(Power, id)
    if isinstance(power, tuple):  # If it's a 404 response
        return power

    data = request.get_json()
    if not data or not data.get('description') or len(data['description']) < 20:
        return jsonify({"errors": ["description must be at least 20 characters"]}), 400

    power.description = data['description']
    db.session.commit()
    return jsonify(power.to_dict())

@hero_routes.route('/powers/<int:id>', methods=['DELETE'])
def delete_power(id):
    power = get_or_404(Power, id)
    if isinstance(power, tuple):  # If it's a 404 response
        return power

    db.session.delete(power)
    db.session.commit()
    return jsonify({"message": "Power deleted successfully"}), 200

@hero_routes.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    if data.get('strength') not in ['Strong', 'Weak', 'Average']:
        return jsonify({"errors": ["Invalid strength value"]}), 400
    hero_power = HeroPower(
        hero_id=data['hero_id'],
        power_id=data['power_id'],
        strength=data['strength']
    )
    db.session.add(hero_power)
    db.session.commit()
    return jsonify(hero_power.to_dict()), 201