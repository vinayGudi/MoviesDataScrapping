from flask import Flask,request
app=Flask(__name__)



@app.route("/")
def index():
	return request.method



@app.route("/profile/<username>")

def tuna(username):
    return "<h2>Hello, %s</h2>" %username

@app.route("/check")
def check(method=["GET","POST"]):
    if request.method=="POST":
        return "UR USING POST"
    else:
        return "UR unLUCKY CR :("













if __name__=="__main__":
    app.run(debug=True)

