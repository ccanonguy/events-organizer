from flask import Flask
import testCalendar as cal

app = Flask(__name__)

@app.route('/test')
def test():
   return cal.main()

if __name__ == '__main__':
   app.run(debug = True)