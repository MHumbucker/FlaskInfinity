import flask
import requests
import schedule


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


PA_USERNAME = "USERNAME" #change it
PA_API_KEY = "API_KEY" #change it too

def restart_script():
    url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/"
    headers = {"Authorization": f"Token {PA_API_KEY}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        apps = response.json()
        if apps:
            app_name = apps[0]["domain_name"]
            restart_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{app_name}/reload/"
            requests.post(restart_url, headers=headers)
            print("✅ Succes")
        else:
            print("❌ Error: no web app founded")
    else:
        print(f"❌ Request error: {response.text}")

def scheduled_restart():
    now = datetime.datetime.utcnow().strftime('%H:%M:%S UTC')
    print(f"🔄 Auto restart in {now}.")
    restart_script()

schedule.every().day.at("21:00").do(scheduled_restart)  # 00:00 MOSCOW
schedule.every().day.at("03:00").do(scheduled_restart)  # 06:00 MOSCOW
schedule.every().day.at("09:00").do(scheduled_restart)  # 12:00 MOSCOW
schedule.every().day.at("15:00").do(scheduled_restart)  # 18:00 MOSCOW

def schedule_runner():
    while True:
        try:
            print("🕒 Schedule checking...")
            schedule.run_pending()
        except Exception as e:
            print(f"❌ Schedule error: {e}")
            print(f"❌ Auto restart error: {e}")
        time.sleep(60)

def run_flask():
    while True:
        try:
            app.run(host='0.0.0.0', port=8070) #U can change port, if its occupied
        except Exception as e:
            print(f"Flask error: {e}")

        print("No connection with flask, waiting...")
        time.sleep(5)

if __name__ == "__main__":
    Thread(target=run_flask, daemon=True).start()
    threading.Thread(target=schedule_runner, daemon=True).start()
