from flask import Flask, request, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def getOutput(data):
    ans = ""
    sz = len(data)

    if sz == 1:
        ans = data['input1']
    elif sz == 2:
        ans = ans + data['input2'][::-1]
        ans = ans + ', '
        ans = ans + data['input1'][::-1]
    else:
        if sz % 2 == 0:
            itr = sz
            while itr > 0:
                s = 'input' + str(itr)
                if (itr == (int(sz/2) + 1)) or (itr == int(sz/2)):
                    ans = ans + data[s]
                else:
                    ans = ans + data[s][::-1]
                itr = itr - 1
                ans = ans + ', '
        else:
            itr = sz
            while itr > 0:
                s = 'input' + str(itr)
                if itr == (int(sz/2) + 1):
                    ans = ans + data[s]
                else:
                    ans = ans + data[s][::-1]
                itr = itr - 1
                ans = ans + ', '

    return ans[:len(ans)-2]

@app.route('/', methods = ['POST'])
def getData():
    data = request.data
    data = json.loads(data)
    ans = getOutput(data)
    return ans

if __name__ == '__main__':
    app.run()