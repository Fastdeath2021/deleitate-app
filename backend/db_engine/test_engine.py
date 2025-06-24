from engine import DBEngine
from bson.objectid import ObjectId

# Instancia la base de datos
db = DBEngine()

# Nombre de la colección temporal para pruebas
COLLECTION = "test_products"

# 🔹 1. Insertar un documento
print("🟢 Insertando documento...")
nuevo = {"nombre": "Torta de limón", "precio": 8500}
insert_result = db.insert_one(COLLECTION, nuevo)
print("ID insertado:", insert_result.inserted_id)

# 🔹 2. Buscar por ID
print("\n🔵 Buscando por ID...")
doc_id = str(insert_result.inserted_id)
encontrado = db.find_by_id(COLLECTION, doc_id)
print("Documento encontrado:", encontrado)

# 🔹 3. Actualizar documento
print("\n🟡 Actualizando documento...")
update_result = db.update_by_id(COLLECTION, doc_id, {"precio": 8900})
print("Modificados:", update_result.modified_count)

# 🔹 4. Buscar todos los documentos
print("\n🟣 Buscando todos...")
todos = db.find_all(COLLECTION)
for doc in todos:
    print(doc)

# 🔹 5. Eliminar por ID
print("\n🔴 Eliminando por ID...")
delete_result = db.delete_by_id(COLLECTION, doc_id)
print("Eliminados:", delete_result.deleted_count)

# 🔹 6. Contar documentos restantes
print("\n⚪ Conteo final:")
print("Total documentos:", db.count_documents(COLLECTION))
