from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def tampil_data():
    # Baca file CSV pakai pandas
    data = pd.read_csv('data.csv')
    return render_template('tampil.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
