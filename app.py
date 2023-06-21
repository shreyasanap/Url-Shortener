from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.debug = True

# Rest of your Flask application code goes here
@app.route('/',method=["GET","POST"])
def index():
    if request.method=="POST":
        short_name=request.form.get('name')
        url=request.form.get('url')
        if 'http' not in url:
            url=f'http://{url}'
        if valid_url(url):
            if name_available(short_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
