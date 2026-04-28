from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

@app.route('/')
def index():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    data = {
        "content": f"New visitor IP: **{user_ip}**",
        "username": "Railway Logger"
    }

    print(f"DEBUG: Found IP {user_ip}") # This will show up in Railway Logs
requests.post(DISCORD_WEBHOOK_URL, json=data)

    return redirect("https://google.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
