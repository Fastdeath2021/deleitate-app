db = db.getSiblingDB("admin");

db.createUser({
  user: "admin_user",
  pwd: "admin_pass",
  roles: [{ role: "clusterAdmin", db: "admin" }]
});

// 2. Configurar un replica set
const config = {
  _id: "rs0", // ID del replica set
  members: [
    {
      _id: 0,
      host: "0.0.0.0:27017"
    }
  ]
};

// 3. Inicializar el replica set
rs.initiate(config);

// 4. Crear la base de datos "deleitate_dev"
db = db.getSiblingDB("deleitate_dev");
db.createCollection("test_init"); // solo para asegurarnos que se crea