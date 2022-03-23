# Keyboard-Companion2
FastAPI Pynput Mapping

# Convert the Application to EXE
```
auto-py-to-exe
```

Windows
```
pyinstaller --noconfirm --onefile --console --add-data "C:/Project/Keyboard_FastAPI/main.py;." --hidden-import "fastapi" --hidden-import "pynput"  "C:/Project/Keyboard_FastAPI/application.py"
```

 
Linux
```
pyinstaller --noconfirm --onefile --console --add-data "C:/Project/Keyboard_FastAPI/main.py;." --hidden-import "fastapi" --hidden-import "pynput.keyboard._xorg" --hidden-import "pynput.mouse._xorg" "C:/Project/Keyboard_FastAPI/application.py"
```