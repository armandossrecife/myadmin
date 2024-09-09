from fastapi import FastAPI
from admin import create_admin #we will create this file in a while
import example_database
import models

app = FastAPI(title="AppName")
admin = create_admin(app)  # we will write this function in a while

db_session = example_database.session()

username = "armando"
user = db_session.query(models.User).filter(models.User.username == username).first()

if not user: 
    db_user = models.User(id=1, email="armando@ufpi.edu.br", username="armando", password="armando", firstname="Armando", lastname="Sousa", is_admin=True)
    db_session.add(db_user)
    db_session.commit()
    print(f"Usuário: {db_user.username} criado com sucesso!")

# list your APIs here
@app.get("/")
async def hello_world():
    return {"message":"Hello World"}