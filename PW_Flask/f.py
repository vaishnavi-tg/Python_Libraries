from flask import Flask

app=Flask(__name__)
@app.route("/")
def hw():
    return "hello world1 kishmish vaish prath"
@app.route("/hello1")
def hw1():
    return "hello world2 kishmish vaish prath"
@app.route("/hello2")
def hw2():
    return "hello world3 kishmish vaish prath"
@app.route("/test1")
def test():
    return "This is my first function in flask"
@app.route("/test2")
def test2(): 
    a=5+6
    return "The sum of the two numbers is{}".format(a)
@app.route("/clear")
def test3():
    return "Hello the world of bitm"



if __name__=="__main__":
    app.run(debug=True)