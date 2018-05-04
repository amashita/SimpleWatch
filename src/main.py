import eel
from datetime import datetime

eel.init('web')

web_app_options = {
    "mode": "chrome-app",  # chromeのアプリケーションモードで起動
                           # "chrome" とすると、通常のchromeで起動
    "port": 8001,
    "chromeFlags": [
            #"--start-fullscreen",  # フルスクリーンで起動 他のChromeが起動していると機能しない？
            "--window-size=400,300",
            # "--window-position=0,0",
    ]
}

eel.start('main.html',size=(400,300), options=web_app_options, block=False)

while True:
    now = datetime.now()
    date_string = now.strftime("%Y/%m/%d %A")
    time_string = now.strftime("%H:%M:%S")
    eel.set_date_time(date_string, time_string)
    eel.sleep(0.2)
