
#import Flask , render_template(to render html pages), and request
from flask import Flask, render_template, request




app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

#defining function to retrive file from user
def index():
    if request.method=='POST':
        file = request.files['file']
    #   reading file without saving it 
        txt=file.stream.read()
        print("ehel",txt)
        return render_template('index.html',txt = txt)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


