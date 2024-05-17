@echo off
if exist env\ (
CALL "env\Scripts\activate"
) else (
python -m venv env
CALL "env\Scripts\activate"
pip install -r requirements.txt
)
python main.py
