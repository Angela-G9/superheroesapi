from app import create_app, db
from models.hero import Hero
from models.power import Power
from models.hero_power import HeroPower

def seed_data():
    # Create some sample powers
    power1 = Power(name="Flight", description="Ability to fly through the skies at supersonic speed")
    power2 = Power(name="Super Strength", description="Incredible physical strength for lifting heavy objects")
    power3 = Power(name="Invisibility", description="Ability to become invisible to the naked eye")
    power4 = Power(name="Telepathy", description="Ability to read and communicate with other minds")

    # Add powers to the session
    db.session.add_all([power1, power2, power3, power4])
    db.session.commit()

    # Create some sample heroes
    hero1 = Hero(name="Clark Kent", super_name="Superman")
    hero2 = Hero(name="Bruce Wayne", super_name="Batman")
    hero3 = Hero(name="Diana Prince", super_name="Wonder Woman")

    # Add heroes to the session
    db.session.add_all([hero1, hero2, hero3])
    db.session.commit()

    # Link heroes and powers in the HeroPower table
    hero_power1 = HeroPower(strength="Strong", hero_id=hero1.id, power_id=power2.id)  # Superman has super strength
    hero_power2 = HeroPower(strength="Strong", hero_id=hero1.id, power_id=power1.id)  # Superman can fly
    hero_power3 = HeroPower(strength="Strong", hero_id=hero2.id, power_id=power2.id)  # Batman has super strength
    hero_power4 = HeroPower(strength="Average", hero_id=hero3.id, power_id=power3.id)  # Wonder Woman is invisible
    hero_power5 = HeroPower(strength="Strong", hero_id=hero3.id, power_id=power4.id)  # Wonder Woman has telepathy

    # Add hero powers to the session
    db.session.add_all([hero_power1, hero_power2, hero_power3, hero_power4, hero_power5])
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == "__main__":
    app = create_app()  # Create the app instance
    with app.app_context():
        db.create_all()  # Ensure tables are created before seeding
        seed_data()
