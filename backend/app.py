from flask import Flask
from v1.users import users_bp
from v1.products import products_bp
from v1.orders import orders_bp
from v1.raw_materials import raw_materials_bp

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(orders_bp, url_prefix="/orders")
app.register_blueprint(raw_materials_bp, url_prefix="/raw-materials")

@app.route("/")
def home():
    return {"message": "Bienvenido a Deleítate APP"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
