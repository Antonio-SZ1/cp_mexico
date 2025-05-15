# API de Códigos Postales de México 🇲🇽

## 📋 Descripción  
Esta aplicación expone una API REST que permite consultar asentamientos y zonas (urbano/rural) por código postal en México, respaldada por una base de datos PostgreSQL normalizada y un frontend mínimo en HTML + TailwindCSS. Está contenerizada con Docker y lista para desplegarse.

---

## 🚀 Tecnologías  
- **Python** 3.11  
- **FastAPI** (API y servidor)  
- **SQLAlchemy** (ORM)  
- **PostgreSQL** (BD)  
- **Docker & Docker Compose** (contenedores)  
- **TailwindCSS** (frontend mínimo)  
- **uvicorn** (ASGI server)

---

## 📂 Estructura del proyecto  

├── app/
│ ├── init.py
│ ├── main.py # Punto de entrada de FastAPI
│ ├── database.py # Configuración de SQLAlchemy
│ ├── models.py # Definición de entidades (Estado, Municipio, Asentamiento)
│ ├── crud.py # Funciones de creación y consulta
│ ├── seed.py # Script para inicializar y poblar la BD
│ └── routers/ # Routers de la API
│ ├── codigos.py # GET /api/codigo
│ ├── estados.py # GET /api/estados, /api/municipios
│ └── resumen.py # GET /api/resumen-zona
├── static/
│ └── index.html # Frontend responsivo en TailwindCSS
├── data/
│ └── codigos_postales.csv # Datos originales (delimitados por |)
├── Dockerfile # Imagen de la aplicación
├── docker-compose.yml # Servicios: app + PostgreSQL
├── requirements.txt # Dependencias Python
├── .gitignore
└── README.md # Este archivo
