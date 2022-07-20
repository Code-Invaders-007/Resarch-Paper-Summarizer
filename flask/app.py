
#import Flask , render_template(to render html pages), and request
from ntpath import join
from flask import Flask, render_template, request
import re




app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

#defining function to retrive file from user
def index():
    if request.method=='POST':
        file = request.files['file']
    #   reading file without saving it
        txt = [] 
        txt=str(file.stream.readlines())
        txt=re.sub("['b]"," ",txt)
        # txt = txt.split("\\n")
        txt = str(txt)
        my_str=" "
        print(txt)
        for x in txt:
            my_str+=''+ x
        my_str=re.sub(r"\\n"," ",my_str)
        print(type(my_str))
        print(my_str)
        return render_template('index.html',txt = my_str)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


