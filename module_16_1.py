# uvicorn module_16_1.py:app --reload
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/user/admin")                     #маршрут к главной странице
async def read_root():
    return "Вы вошли как администратор"

@app.get("/users/{user_id}")               #маршрут к страницам пользователей, используя параметр в пути
async def get_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user')                          #маршрут к страницам пользователей, передавая данные в адресной строке
async def user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/")                              #маршрут к главной странице
async def read_root():
    return "Главная страница"


if __name__ == '__main__':
    uvicorn.run('module_16_1:app', host='127.0.0.1', port=8000, reload=True)
