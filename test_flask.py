from unittest import TestCase
from app import app
from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petagency_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING']=True
app.config['WTF_CSRF_ENABLED']=False

db.drop_all()
db.create_all()

class PetAgencyTestCase(TestCase):
    """Tests for view functions for Pet Agency site"""

    def setUp(self):
        """Add sample pet"""

    db.session.query(Pet).delete()
    db.session.commit()

    pet = Pet(name="Test", species="rabbit", age=8, available=True)
    db.session.add(pet)
    db.session.commit()

    def tearDown(self):
        """Clean up any fouled transactions."""

        db.session.rollback()

    def test_show_home_page(self):
        with app.test_client() as client:
            resp=client.get('/')
            html=resp.get_data(as_text=True)
        
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Test', html)

    def test_show_add_form(self):
        with app.test_client() as client:
            resp=client.get('/add')
            html=resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('New Pet', html)
    
    def test_add_pet(self):
        with app.test_client() as client:
            data = {'name': 'Tester', 'species': 'rabbit', 'age':0}
            resp=client.post('/add', data=data)
            test_pet = db.session.execute(db.select(Pet).where(Pet.name == 'Tester')).scalar()

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, '/')
        self.assertEqual(str(Pet.query.get(test_pet.id)), f'<Pet {test_pet.id} {test_pet.name} {test_pet.species}>')
            
    def test_add_pet_redirect(self):
        with app.test_client() as client:
            data = {'name': 'Tester', 'species': 'rabbit', 'age': 0}
            resp=client.post('/add', data=data, follow_redirects=True)
            html=resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('Tester</a> is <b>AVAILABLE</b>', html)
    
    def test_show_pet(self):
        with app.test_client() as client:
            test_pet=db.session.execute(db.select(Pet).where(Pet.name == "Test")).scalar()
            resp=client.get(f'/{test_pet.id}')
            html=resp.get_data(as_text=True)
        
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Test', html)
        self.assertIn('Available: Yes', html)

    def test_show_edit_pet_form(self):
        with app.test_client() as client:
            test_pet=db.session.execute(db.select(Pet).where(Pet.name == "Test")).scalar()
            resp=client.get(f'/{test_pet.id}/edit')
            html=resp.get_data(as_text=True)
        
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Save', html)

    def test_edit_pet(self):
        with app.test_client() as client:
            test_pet=db.session.execute(db.select(Pet).where(Pet.name == "Test")).scalar()
            data = {'age': 0, 'available': False}
            resp=client.post(f'/{test_pet.id}/edit', data=data)
            
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, f'/{test_pet.id}')    

    def test_edit_pet_redirect(self):
        with app.test_client() as client:
            test_pet=db.session.execute(db.select(Pet).where(Pet.name == "Test")).scalar()
            data = {'age': 0, 'available': False}
            resp=client.post(f'/{test_pet.id}/edit', data=data, follow_redirects=True)
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Pet Test updated!', html)
            self.assertIn('Available: No', html)
