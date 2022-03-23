from typing import Optional

from fastapi import FastAPI

app = FastAPI()

from pynput.keyboard import Key, Controller

keyboard = Controller()


@app.get("/")
def read_root():
    print("/")
    return {"Hello": "World"}

@app.get("/key/space")
def press_space():
    # Press and release space
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    return {}

@app.get("/key/{key_x}")
def press_x(key_x: str):
    # Press and release space
    keyboard.press(key_x)
    keyboard.release(key_x)
    return {}

@app.get("/key/shift/{key_x}")
def press_shift_x(key_x: str):
    with keyboard.pressed(Key.shift):
        keyboard.press(key_x)
        keyboard.release(key_x)
    return {}

@app.get("/key/alt/{key_x}")
def press_alt_x(key_x: str):
    with keyboard.pressed(Key.alt):
        keyboard.press(key_x)
        keyboard.release(key_x)
    return {}

@app.get("/key/ctrl/{key_x}")
def press_alt_x(key_x: str):
    with keyboard.pressed(Key.ctrl):
        keyboard.press(key_x)
        keyboard.release(key_x)
    return {}

@app.get("/word/{word_x}")
def enter_x(word_x: str):
    # Press and release space
    keyboard.type(word_x)
    return {}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
