from app import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('Hello.html')

if __name__ == '__main__':
   app.run()