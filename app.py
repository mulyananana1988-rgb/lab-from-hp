import flask from Flask

app = Flask('__name__')

@app.route('/')
def home():
  return "lab from HP"

if __name__=='__main__':
  app.run(host='0.0.0.0', port=50000)
