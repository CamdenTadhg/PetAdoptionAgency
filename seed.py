from models import Pet, db 
from app import app

db.drop_all()
db.create_all()

db.session.add_all([
Pet(name="Chaz", species="mouse", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI_hVJ_xxEQq5sW7nS4lcVNDn6oRx5kPPRaLnYMUyX6Q&s", age=1, notes="", available=True),
Pet(name="Ladybug", species="guinea pig", photo_url="https://as1.ftcdn.net/v2/jpg/00/60/75/46/1000_F_60754695_fBtK5Qe00xFNobcwzvCrKKROdWZBw3jR.jpg", age=3, notes="", available=True),
Pet(name="Cubby", species="guinea pig", photo_url="https://media.istockphoto.com/id/959889568/photo/guinea-pig-1-year-old-lying-against-white-background.jpg?s=612x612&w=0&k=20&c=FnM-RxNWHeq9DNC5Il0pJkPXyZItPNDL8AcvZzhKmik=", age=1, notes="", available=True),
Pet(name="Kipper", species="guinea pig", photo_url="https://media.istockphoto.com/id/466608706/photo/guinea-pig.jpg?s=612x612&w=0&k=20&c=0so4BPizNeaY9_eex2gobNpBLVYZl9seS9Xx3hSPcW0=", age=0, notes="in quarantine", available=False),
Pet(name="Sydney", species="rabbit", photo_url="https://t4.ftcdn.net/jpg/00/65/98/47/360_F_65984756_LgQt3q8Z1b6xA8y0ffL25MbqNdFg9uaK.jpg", age=4, notes="FRS", available=True),
Pet(name="Jess", species="iguana", photo_url="https://media.istockphoto.com/id/183825222/photo/iguana-isolated-on-white.jpg?s=612x612&w=0&k=20&c=_GgVBjvOdXdRYYEGp3gb20hFIgPfC1Vo-Y09b1YTxz0=", age=3, notes="", available=True),
Pet(name="Porky", species="pot-bellied pig", photo_url="https://media.istockphoto.com/id/482039492/photo/pink-with-black-spots-miniature-big.jpg?s=612x612&w=0&k=20&c=5WE5y5H3nB5FcJEyzcL9dNe7oQCBHOIcjnQU5pjESKc=", age=1, notes="", available=True),
Pet(name="Toffee", species="pot-bellied pig", photo_url="https://media.istockphoto.com/id/525805469/photo/pet-baby-pig.jpg?s=612x612&w=0&k=20&c=-TOTfBoyClL7uXhfqpghFiiHq114bHjIVCHnXT-VujA=", age=2, notes="adoption pending", available=False),
Pet(name="Capone", species="brown rat", photo_url="https://media.istockphoto.com/id/176430993/photo/rat.jpg?s=612x612&w=0&k=20&c=oX5uUrFGJzcf9aUOeUw2Z8NsDrzPtPYto7itsGVAi88=", age=0, notes="", available=True),
Pet(name="Moses", species="goldfish", photo_url="https://t4.ftcdn.net/jpg/02/74/09/49/360_F_274094985_PPtHIUCRnhlc8mwgyx43JwYGsyJLfJyu.jpg", age=0, notes="", available=False),
Pet(name="Bruiser", species="box turtle", photo_url="https://i.pinimg.com/originals/56/e4/0e/56e40e26a5ac3fe58f8e617a9970da0b.jpg", age=3, notes="", available=True)
])

db.session.commit()
