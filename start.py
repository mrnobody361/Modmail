import threading
from server import app
from bot import run_bot   # your bot's start function

def start_web():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=start_web).start()
run_bot()
