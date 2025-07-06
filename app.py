from flask import Flask, render_template,request, redirect, url_for,flash


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

products = [
    {"id": 1, "name": "iPhone 15 Pro", "price": "$999", "image": "https://via.placeholder.com/300x200"},
    {"id": 2, "name": "Apple Watch Series 9", "price": "$499", "image": "https://via.placeholder.com/300x200"},
    {"id": 3, "name": "Samsung Galaxy S24", "price": "$899", "image": "https://via.placeholder.com/300x200"},
    {"id": 4, "name": "Garmin Venu 3", "price": "$399", "image": "https://via.placeholder.com/300x200"}
]

@app.route('/')
def home():
    return render_template("index.html", products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    return render_template("product.html", product=product)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        comments = request.form['comments']

        # You can save this data to a database or file here

        flash('Thank you for your feedback!')
        return redirect(url_for('feedback'))
    return render_template('feedback.html')


if __name__ == "__main__":
    app.run(debug=True)