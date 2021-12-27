from flask import Flask

app=Flask('ping')

@app.route('/ping',methods=['GET'])
def ping():
    return 'Adam Pong'

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0', port=9696)

#then can open it in browser:http://localhost:9696/ping
#or from terminal: curl http://0.0.0.0:9696/ping