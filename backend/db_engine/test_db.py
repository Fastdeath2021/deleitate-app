from backend.db_engine.engine import DBEngine

db = DBEngine()
db.create_collection("usuarios")
result = db.insert_one("usuarios", {"nombre": "Marcelo", "rol": "admin"})
print("Insertado con ID:", result.inserted_id)
