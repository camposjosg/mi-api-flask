from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return ""

# Lista de carreras
carreras = [
    {"id": "01", "nombre": "Ing. en Sistemas Computacionales"},
    {"id": "02", "nombre": "Ing. Industrial"},
    {"id": "03", "nombre": "Ing. en Tecnologías de la Información y Comunicaciones"},
    {"id": "04", "nombre": "Ing. en Gestión Empresarial"},
    {"id": "05", "nombre": "Ing. Electrónica"},
    {"id": "06", "nombre": "Ing. Electromecánica"},
    {"id": "07", "nombre": "Ing. Mecatrónica"},
    {"id": "08", "nombre": "Ing. en Logística"}
]

# Lista de especialidades por carrera
especialidades = {
    "01": [
        {"id": "01", "nombre": "Cómputo Empresarial"},
        {"id": "02", "nombre": "Redes Convergentes de Alta Disponibilidad con Tecnologías Emergentes"},
        {"id": "03", "nombre": "Inteligencia Artificial"}
    ],
    "02": [
        {"id": "01", "nombre": "Ingeniería en Manufactura y Calidad"},
        {"id": "02", "nombre": "Manufactura en Artículos de Piel"}
    ]
}


# Lista de materias por carrera
materias = {
    "01": [
        "Cálculo Diferencial",
        "Matemáticas Discretas",
        "Fundamentos de Programación",
        "Taller de Administración",
        "Cálculo Integral",
        "Álgebra Lineal",
        "Programación Orientada a Objetos",
        "Contabilidad Financiera",
        "Cálculo Vectorial",
        "Investigación de Operaciones",
        "Estructura de Datos",
        "Cultura Empresarial",
        "Ecuaciones Diferenciales",
        "Fundamentos de Bases de Datos",
        "Tópicos Avanzados de Programación",
        "Simulación",
        "Fundamentos de Ingeniería de Software",
        "Taller de Bases de Datos",
        "Sistemas Operativos",
        "Graficación",
        "Fundamentos de Investigación",
        "Química",
        "Taller de Ética",
        "Probabilidad y Estadística",
        "Física General",
        "Desarrollo Sustentable",
        "Métodos Numéricos",
        "Principios Eléctricos y Aplicaciones Digitales",
        "Arquitectura de Computadoras",
        "Fundamentos de Telecomunicaciones",
        "Lenguajes de Interfaz",
        "Sistemas Programables",
        "Actividades Complementarias",
        "Servicio Social",
        "Residencia",
        "Inteligencia Artificial",
        "Taller de Sistemas Operativos",
        "Lenguajes y Autómatas 1",
        "Redes de Computadoras",
        "Lenguajes y Autómatas 2",
        "Taller de Investigación 1",
        "Conmutación y Enrutamiento de Redes de Datos",
        "Programación Lógica y Funcional",
        "Administración de Redes",
        "Taller de Investigación 2",
        "Inteligencia Artificial",
        "Gestión de Proyectos de Software",
        "Programación Web"
    ],
    "02": [
        "Química",
        "Taller de Ética",
        "Cálculo Diferencial",
        "Taller de Herramientas Intelectuales",
        "Fundamentos de Investigación",
        "Dibujo Industrial",
        "Actividades Complementarias",
        "Metrología y Normalización",
        "Electricidad y Electrónica Industrial",
        "Cálculo Integral",
        "Física",
        "Probabilidad y Estadística",
        "Análisis de la Realidad Nacional",
        "Taller de Liderazgo",
        "Propiedad de los Materiales",
        "Economía",
        "Cálculo Vectorial",
        "Álgebra Lineal",
        "Estadística Inferencial 1",
        "Estudio del Trabajo 1",
        "Administración de Proyectos",
        "Procesos de Fabricación",
        "Algoritmos y Lenguajes de Programación",
        "Administración de Operaciones 1",
        "Investigación de Operaciones 1",
        "Estadística Inferencial 2",
        "Estudio del Trabajo 2",
        "Higiene y Seguridad Industrial",
        "Gestión de Costos",
        "Mercadotecnia",
        "Administración de Operaciones 2",
        "Investigación de Operaciones 2",
        "Control Estadístico de la Calidad",
        "Ergonomía",
        "Desarrollo Sustentable",
        "Ing. Económica",
        "Taller de Investigación 1",
        "Ing. de Sistemas",
        "Simulación",
        "Administración del Mantenimiento",
        "Planeación Financiera",
        "Relaciones Industriales",
        "Planeación y Diseño de Instalaciones",
        "Sistemas de Manufactura",
        "Logística y Cadena de Suministro",
        "Gestión de los Sistemas de Calidad",
        "Formación y Evaluación de Proyectos",
        "Servicio Social",
        "Taller de Investigación 2",
        "Residencia Profesional"
    ],

    "03": [
        "Cálculo Diferencial",
        "Cálculo Integral",
        "Matemáticas Aplicadas a Comunicaciones",
        "Análisis de Señales y Sistemas de Comunicación",
        "Telecomunicaciones",
        "Redes Emergentes",
        "Administración y Seguridad de Redes",
        "Fundamentos de Programación",
        "Programación Orientada a Objetos",
        "Estructuras y Organización de Datos",
        "Programación II",
        "Administración de Proyectos",
        "Programación Web",
        "Desarrollo de Aplicaciones para Dispositivos Móviles",
        "Auditoría en Tecnologías de la Información",
        "Residencia Profesional",
        "Matemáticas Discretas I",
        "Matemáticas Discretas II",
        "Matemáticas para la Toma de Decisiones",
        "Fundamentos de Redes",
        "Redes de Computadoras",
        "Desarrollo de Emprendedores",
        "Taller de Investigación I",
        "Taller de Investigación II",
        "Introducción a las TIC's",
        "Álgebra Lineal",
        "Fundamentos de Base de Datos",
        "Taller de Base de Datos",
        "Base de Datos Distribuidas",
        "Sistemas Operativos I",
        "Sistemas Operativos II",
        "Ingeniería del Conocimiento",
        "Taller de Ética",
        "Probabilidad y Estadística",
        "Electricidad y Magnetismo",
        "Circuitos Eléctricos y Electrónicos",
        "Arquitectura de Computadoras",
        "Desarrollo Sustentable",
        "Negocios Electrónicos I",
        "Negocios Electrónicos II",
        "Fundamentos de Investigación",
        "Contabilidad y Costos",
        "Administración Gerencial",
        "Ingeniería de Software",
        "Taller de Ingeniería de Software",
        "Tecnologías Inalámbricas",
        "Interacción Humano Computadora",
        "Actividades Complementarias",
        "Servicio Social"
    ],

     "04": [
        "Administración General",
        "Cálculo Diferencial",
        "Contabilidad Financiera",
        "Taller de Ética",
        "Probabilidad y Estadística",
        "Matemáticas Financieras",
        "Cálculo Integral",
        "Álgebra Lineal",
        "Desarrollo Sustentable",
        "Economía",
        "Costos y Presupuestos",
        "Estadística Aplicada",
        "Planeación Estratégica",
        "Cálculo Vectorial",
        "Proyectos de Inversión",
        "Tecnologías de la Información y Comunicación",
        "Derecho Empresarial",
        "Diseño Organizacional",
        "Administración de la Producción",
        "Mercadotecnia",
        "Finanzas Corporativas",
        "Administración de la Calidad",
        "Investigación de Operaciones",
        "Administración de Recursos Humanos",
        "Gestión Empresarial",
        "Administración Estratégica de Costos",
        "Sistemas de Información Gerencial",
        "Desarrollo de Habilidades Directivas",
        "Desarrollo de Emprendedores",
        "Negocios Internacionales",
        "Administración Financiera",
        "Dirección Estratégica",
        "Empresas Familiares",
        "Planeación y Control de la Producción",
        "Dirección de Ventas",
        "Administración de la Cadena de Suministro",
        "Estrategias de Negocios",
        "Mercadotecnia Estratégica",
        "Gestión de Proyectos",
        "Administración de la Innovación y el Cambio",
        "Administración del Comercio Internacional",
        "Administración de Ventas",
        "Administración de la Logística",
        "Derecho Laboral y Fiscal",
        "Formulación y Evaluación de Proyectos",
        "Administración Estratégica de Recursos Humanos",
        "Liderazgo y Desarrollo Organizacional",
        "Simulación de Empresas",
        "Administración de la Mercadotecnia",
        "Auditoría Administrativa",
        "Administración de Proyectos de Tecnología",
        "Administración de la Calidad Total",
        "Administración de Operaciones",
        "Seminario de Investigación",
        "Administración de la Producción II",
        "Administración de la Calidad II",
        "Administración de Recursos Humanos II",
        "Administración de la Mercadotecnia II",
        "Administración Financiera II",
        "Desarrollo de Habilidades Directivas II",
        "Formación y Evaluación de Proyectos II",
        "Auditoría Administrativa II",
        "Seminario de Investigación II",
        "Empresas Familiares II",
        "Liderazgo y Desarrollo Organizacional II",
        "Simulación de Empresas II",
        "Taller de Investigación I",
        "Taller de Investigación II",
        "Taller de Ética y Valores",
        "Servicio Social",
        "Residencia Profesional"
    ],

     "05": [
        "Matemáticas I",
        "Química",
        "Introducción a la Ingeniería en Electrónica",
        "Fundamentos de Programación",
        "Cálculo Diferencial",
        "Física I",
        "Matemáticas II",
        "Álgebra Lineal",
        "Programación Avanzada",
        "Cálculo Integral",
        "Física II",
        "Matemáticas III",
        "Probabilidad y Estadística",
        "Ecuaciones Diferenciales",
        "Electrónica Básica",
        "Máquinas Eléctricas",
        "Física III",
        "Matemáticas IV",
        "Sistemas de Control",
        "Electrónica Analógica",
        "Electrónica Digital",
        "Comunicaciones I",
        "Microcontroladores",
        "Instrumentación Electrónica",
        "Electrónica de Potencia",
        "Sistemas Digitales",
        "Comunicaciones II",
        "Electrónica Industrial",
        "Sistemas Embebidos",
        "Procesamiento Digital de Señales",
        "Redes de Comunicaciones",
        "Robótica",
        "Diseño de Circuitos Integrados",
        "Proyectos de Electrónica",
        "Tópicos Selectos de Electrónica I",
        "Tópicos Selectos de Electrónica II",
        "Tópicos Selectos de Electrónica III",
        "Tópicos Selectos de Electrónica IV",
        "Taller de Ética",
        "Desarrollo Sustentable",
        "Formación Integral",
        "Seminario de Titulación",
        "Servicio Social",
        "Residencia Profesional"
            
    ],

     "06": [
        "Matemáticas I",
        "Química",
        "Introducción a la Ingeniería Electromecánica",
        "Fundamentos de Programación",
        "Cálculo Diferencial",
        "Física I",
        "Matemáticas II",
        "Álgebra Lineal",
        "Programación Avanzada",
        "Cálculo Integral",
        "Física II",
        "Matemáticas III",
        "Probabilidad y Estadística",
        "Ecuaciones Diferenciales",
        "Electrónica Básica",
        "Máquinas Eléctricas",
        "Física III",
        "Matemáticas IV",
        "Sistemas de Control",
        "Electrónica de Potencia",
        "Mecánica de Materiales",
        "Termodinámica",
        "Diseño de Elementos de Máquinas",
        "Métodos Numéricos",
        "Dinámica de Máquinas",
        "Diseño de Sistemas Mecánicos",
        "Procesos de Manufactura",
        "Mecanismos",
        "Máquinas Térmicas",
        "Diseño de Sistemas Hidráulicos y Neumáticos",
        "Máquinas y Equipos Eléctricos",
        "Automatización Industrial",
        "Control Automático",
        "Diseño de Plantas Industriales",
        "Sistemas de Potencia",
        "Proyectos de Ingeniería Electromecánica",
        "Tópicos Selectos de Ingeniería Electromecánica I",
        "Tópicos Selectos de Ingeniería Electromecánica II",
        "Tópicos Selectos de Ingeniería Electromecánica III",
        "Tópicos Selectos de Ingeniería Electromecánica IV",
        "Taller de Ética",
        "Desarrollo Sustentable",
        "Formación Integral",
        "Seminario de Titulación",
        "Servicio Social",
        "Residencia Profesional"
       
    ],

     "07": [
        "Matemáticas I",
        "Química",
        "Introducción a la Ingeniería Mecatrónica",
        "Fundamentos de Programación",
        "Cálculo Diferencial",
        "Física I",
        "Matemáticas II",
        "Álgebra Lineal",
        "Programación Avanzada",
        "Cálculo Integral",
        "Física II",
        "Matemáticas III",
        "Probabilidad y Estadística",
        "Ecuaciones Diferenciales",
        "Electrónica Básica",
        "Máquinas Eléctricas",
        "Física III",
        "Matemáticas IV",
        "Sistemas de Control",
        "Electrónica de Potencia",
        "Mecánica de Materiales",
        "Termodinámica",
        "Diseño de Elementos de Máquinas",
        "Métodos Numéricos",
        "Dinámica de Máquinas",
        "Diseño de Sistemas Mecánicos",
        "Procesos de Manufactura",
        "Mecanismos",
        "Máquinas Térmicas",
        "Diseño de Sistemas Hidráulicos y Neumáticos",
        "Máquinas y Equipos Eléctricos",
        "Automatización Industrial",
        "Control Automático",
        "Diseño de Plantas Industriales",
        "Sistemas de Potencia",
        "Mecatrónica",
        "Robótica",
        "Instrumentación",
        "Sistemas Hidráulicos y Neumáticos",
        "Controladores Lógicos Programables",
        "Sistemas Embebidos",
        "Sistemas Mecánicos",
        "Sistemas Eléctricos y Electrónicos",
        "Proyectos de Ingeniería Mecatrónica I",
        "Proyectos de Ingeniería Mecatrónica II",
        "Tópicos Selectos de Ingeniería Mecatrónica I",
        "Tópicos Selectos de Ingeniería Mecatrónica II",
        "Tópicos Selectos de Ingeniería Mecatrónica III",
        "Tópicos Selectos de Ingeniería Mecatrónica IV",
        "Taller de Ética",
        "Desarrollo Sustentable",
        "Formación Integral",
        "Seminario de Titulación",
        "Servicio Social",
        "Residencia Profesional"
       
    ],

     "08": [
        "Matemáticas I",
        "Química",
        "Introducción a la Ingeniería en Logística",
        "Fundamentos de Programación",
        "Cálculo Diferencial",
        "Física I",
        "Matemáticas II",
        "Álgebra Lineal",
        "Programación Avanzada",
        "Cálculo Integral",
        "Física II",
        "Matemáticas III",
        "Probabilidad y Estadística",
        "Ecuaciones Diferenciales",
        "Economía",
        "Física III",
        "Matemáticas IV",
        "Logística",
        "Modelos de Simulación",
        "Administración de la Cadena de Suministro",
        "Métodos Cuantitativos para la Toma de Decisiones",
        "Transporte y Distribución",
        "Sistemas de Almacenamiento y Manejo de Materiales",
        "Planeación y Control de la Producción",
        "Gestión de Inventarios",
        "Diseño de Redes Logísticas",
        "Logística Internacional",
        "Sistemas de Información en Logística",
        "Gestión de Proyectos Logísticos",
        "Optimización en Logística",
        "Logística Inversa",
        "Diseño de Almacenes y Centros de Distribución",
        "Logística de Distribución Física Internacional",
        "Tecnología de la Información Aplicada a la Logística",
        "Gestión de la Calidad en la Cadena de Suministro",
        "Gestión Ambiental en Logística",
        "Legislación y Normatividad en Logística",
        "Emprendimiento y Desarrollo de Negocios",
        "Planeación Estratégica en Logística",
        "Proyectos de Ingeniería en Logística I",
        "Proyectos de Ingeniería en Logística II",
        "Tópicos Selectos de Ingeniería en Logística I",
        "Tópicos Selectos de Ingeniería en Logística II",
        "Tópicos Selectos de Ingeniería en Logística III",
        "Tópicos Selectos de Ingeniería en Logística IV",
        "Taller de Ética",
        "Desarrollo Sustentable",
        "Formación Integral",
        "Seminario de Titulación",
        "Servicio Social",
        "Residencia Profesional"
        
    ]

     
}

# Lista de materias por especialidad
materias_especialidades = {
    "01": {
        "01": [
            "Bases de Datos Avanzadas",
            "Ciencia de Datos",
            "Cómputo y Servicios en la Nube",
            "Desarrollo de Aplicaciones Móviles",
            "Tópicos para el Despliegue de Aplicaciones"
        ],
        "02": [
            "Diseño de Redes",
            "Redes Inalámbricas",
            "Seguridad en Redes",
            "Infraestructura para Despliegue de Aplicaciones",
            "Fundamentos de IoT"
        ],
        "03": [
            "IA",
            "IA",
            "IA"
        ]
    },
    "02": {
        "01": [
            "Sistemas Neumáticos e Hidráulicos",
            "Diseño Asistido por Computadora",
            "Controladores Lógicos Programables",
            "Temas Selectos de Manufactura",
            "Core Tools",
            "Medición y Mejoramiento de la Productividad",
            "Robótica Industrial",
            "Manufactura Flexible"
        ],
        "02": [
            "Diseño y Modelado",
            "Diseño Asistido por Computadora",
            "Tecnología y Taller 1",
            "Temas Selectos de Manufactura",
            "Core Tools",
            "Tecnología y Taller 2",
            "Medición y Mejoramiento de la Productividad",
            "Administración de los Sistemas de Producción de Calzado"
        ]
    }
}

@app.route("/carreras/<carrera_id>")
def get_carrera(carrera_id):
    carrera = next((carrera for carrera in carreras if carrera["id"] == carrera_id), None)
    if carrera:
        query = request.args.get('query')
        if query:
            carrera["query"] = query
        return jsonify(carrera), 200
    else:
        return jsonify({"error": "Carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/especialidades")
def get_especialidades(carrera_id):
    if carrera_id in especialidades:
        return jsonify(especialidades[carrera_id]), 200
    else:
        return jsonify({"error": "No hay especialidades para esta carrera o carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/especialidades/<int:index>")
def get_especialidad(carrera_id, index):
    if carrera_id in especialidades:
        if 0 <= index < len(especialidades[carrera_id]):
            return jsonify(especialidades[carrera_id][index]), 200
        else:
            return jsonify({"error": "Índice de especialidad fuera de rango"}), 404
    else:
        return jsonify({"error": "Carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/materias")
def get_materias(carrera_id):
    if carrera_id in materias:
        return jsonify(materias[carrera_id]), 200
    else:
        return jsonify({"error": "No hay materias para esta carrera o carrera no encontrada"}), 404

@app.route("/carreras/<carrera_id>/especialidades/<especialidad_id>/materias")
def get_materias_especialidad(carrera_id, especialidad_id):
    if carrera_id in materias_especialidades and especialidad_id in materias_especialidades[carrera_id]:
        return jsonify(materias_especialidades[carrera_id][especialidad_id]), 200
    else:
        return jsonify({"error": "No hay materias para esta especialidad o especialidad no encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)