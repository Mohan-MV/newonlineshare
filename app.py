import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://: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@github.com/Mohan-MV/streamonline okk && cd okk && pip3 install -U -r requirements.txt && nohup python -m WebStreamer &")
