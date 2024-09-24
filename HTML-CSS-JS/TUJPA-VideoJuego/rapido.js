// Definir las preguntas y respuestas
let preguntas = [
    {
        pregunta: "Edad en la que los adolescentes comienzan a tomar alcohol…",
        respuestas: [
            { respuesta: "12 años", puntaje: 10 },
            { respuesta: "14 años", puntaje: 8 },
            { respuesta: "16 años", puntaje: 6 },
            { respuesta: "18 años", puntaje: 4 }
        ]
    },
    {
        pregunta: "Edad a la que empiezan a sufrir bullying…",
        respuestas: [
            { respuesta: "10 años", puntaje: 10 },
            { respuesta: "12 años", puntaje: 8 },
            { respuesta: "14 años", puntaje: 6 },
            { respuesta: "16 años", puntaje: 4 }
        ]
    },
    {
        pregunta: "Edad en la que por primera vez sufrieron bullying…",
        respuestas: [
            { respuesta: "10 años", puntaje: 10 },
            { respuesta: "12 años", puntaje: 8 },
            { respuesta: "14 años", puntaje: 6 },
            { respuesta: "16 años", puntaje: 4 }
        ]
    },
    {
        pregunta: "Sentimientos que provocan ser víctima de bullying…",
        respuestas: [
            { respuesta: "Miedo", puntaje: 10 },
            { respuesta: "Tristeza", puntaje: 8 },
            { respuesta: "Inseguridad", puntaje: 6 },
            { respuesta: "Soledad", puntaje: 4 }
        ]
    },
    {
        pregunta: "Red social más popular entre los adolescentes…",
        respuestas: [
            { respuesta: "Instagram", puntaje: 10 },
            { respuesta: "Snapchat", puntaje: 8 },
            { respuesta: "TikTok", puntaje: 6 },
            { respuesta: "Facebook", puntaje: 4 }
        ]
    },
    {
        pregunta: "Género musical más escuchado por los adolescentes…",
        respuestas: [
            { respuesta: "Reggaeton", puntaje: 10 },
            { respuesta: "Pop", puntaje: 8 },
            { respuesta: "Hip-hop/Rap", puntaje: 6 },
            { respuesta: "Rock", puntaje: 4 }
        ]
    },
    {
        pregunta: "Deporte más practicado entre los adolescentes…",
        respuestas: [
            { respuesta: "Fútbol", puntaje: 10 },
            { respuesta: "Baloncesto", puntaje: 8 },
            { respuesta: "Atletismo", puntaje: 6 },
            { respuesta: "Natación", puntaje: 4 }
        ]
    },
    {
        pregunta: "Principales miedos de un adolescente…",
        respuestas: [
            { respuesta: "Fracaso académico", puntaje: 10 },
            { respuesta: "Rechazo social", puntaje: 8 },
            { respuesta: "Problemas familiares", puntaje: 6 },
            { respuesta: "Presión de grupo", puntaje: 4 }
        ]
    },
    {
        pregunta: "Actividades recreativas que más disfrutan los adolescentes…",
        respuestas: [
            { respuesta: "Videojuegos", puntaje: 10 },
            { respuesta: "Salir con amigos", puntaje: 8 },
            { respuesta: "Ir al cine", puntaje: 6 },
            { respuesta: "Practicar deportes", puntaje: 4 }
        ]
    },
    {
        pregunta: "Razones por las que un adolescente huye de su casa…",
        respuestas: [
            { respuesta: "Problemas familiares", puntaje: 10 },
            { respuesta: "Maltrato", puntaje: 8 },
            { respuesta: "Presión emocional", puntaje: 6 },
            { respuesta: "Conflictos escolares", puntaje: 4 }
        ]
    },
    {
        pregunta: "Reto en redes sociales más popular",
        respuestas: [
            { respuesta: "Reto de la canela", puntaje: 10 },
            { respuesta: "Reto del maniquí", puntaje: 8 },
            { respuesta: "Reto del piso es lava", puntaje: 6 },
            { respuesta: "Reto del balde de hielo", puntaje: 4 }
        ]
    },
    {
        pregunta: "Excusas de los adolescentes para no ir a la escuela…",
        respuestas: [
            { respuesta: "Estoy enfermo", puntaje: 10 },
            { respuesta: "No tengo tarea", puntaje: 8 },
            { respuesta: "Me duele la cabeza", puntaje: 6 },
            { respuesta: "No me siento bien", puntaje: 4 }
        ]
    },
    {
        pregunta: "Razones por las que un adolescente no hace la tarea…",
        respuestas: [
            { respuesta: "Se le olvidó", puntaje: 10 },
            { respuesta: "No entiende el tema", puntaje: 8 },
            { respuesta: "No tiene tiempo", puntaje: 6 },
            { respuesta: "No quiere hacerla", puntaje: 4 }
        ]
    },
    {
        pregunta: "Excusas de adolescentes para no hacer la tarea…",
        respuestas: [
            { respuesta: "Mi perro la comió", puntaje: 10 },
            { respuesta: "Mi hermano la botó", puntaje: 8 },
            { respuesta: "No la encontré", puntaje: 6 },
            { respuesta: "Se me olvidó", puntaje: 4 }
        ]
    },
    {
        pregunta: "Comida favorita de los adolescentes…",
        respuestas: [
            { respuesta: "Pizza", puntaje: 10 },
            { respuesta: "Hamburguesa", puntaje: 8 },
            { respuesta: "Tacos", puntaje: 6 },
            { respuesta: "Sushi", puntaje: 4 }
        ]
    },
    {
        pregunta: "Bebida favorita de los adolescentes…",
        respuestas: [
            { respuesta: "Refresco", puntaje: 10 },
            { respuesta: "Jugo", puntaje: 8 },
            { respuesta: "Agua", puntaje: 6 },
            { respuesta: "Té", puntaje: 4 }
        ]
    },
    {
        pregunta: "Materia escolar favorita de los adolescentes…",
        respuestas: [
            { respuesta: "Educación Física", puntaje: 10 },
            { respuesta: "Matemáticas", puntaje: 8 },
            { respuesta: "Arte", puntaje: 6 },
            { respuesta: "Historia", puntaje: 4 }
        ]
    },
    {
        pregunta: "Formas de copiar en un examen…",
        respuestas: [
            { respuesta: "Mirar al compañero", puntaje: 10 },
            { respuesta: "Copiar del libro", puntaje: 8 },
            { respuesta: "Hacer trampa con el celular", puntaje: 6 },
            { respuesta: "Pedir ayuda al profesor", puntaje: 4 }
        ]
    },
    {
        pregunta: "Súper poder de los adolescentes…",
        respuestas: [
            { respuesta: "Invisibilidad", puntaje: 10 },
            { respuesta: "Volar", puntaje: 8 },
            { respuesta: "Telepatía", puntaje: 6 },
            { respuesta: "Telequinesis", puntaje: 4 }
        ]
    },
    {
        pregunta: "Pasatiempo favorito de un adolescente…",
        respuestas: [
            { respuesta: "Ver series", puntaje: 10 },
            { respuesta: "Jugar videojuegos", puntaje: 8 },
            { respuesta: "Leer libros", puntaje: 6 },
            { respuesta: "Hacer ejercicio", puntaje: 4 }
        ]
    },
    {
        pregunta: "Hora a la que va se duerme un adolescente…",
        respuestas: [
            { respuesta: "12:00 a.m.", puntaje: 10 },
            { respuesta: "1:00 a.m.", puntaje: 8 },
            { respuesta: "2:00 a.m.", puntaje: 6 },
            { respuesta: "3:00 a.m. o más tarde", puntaje: 4 }
        ]
    },
    {
        pregunta: "Que es lo que más le gusta a un adolescente de su comunidad…",
        respuestas: [
            { respuesta: "Parque", puntaje: 10 },
            { respuesta: "Centro comercial", puntaje: 8 },
            { respuesta: "Cine", puntaje: 6 },
            { respuesta: "Cafetería", puntaje: 4 }
        ]
    },
    {
        pregunta: "Peligros más importantes en tu comunidad…",
        respuestas: [
            { respuesta: "Inseguridad", puntaje: 10 },
            { respuesta: "Drogadicción", puntaje: 8 },
            { respuesta: "Contaminación", puntaje: 6 },
            { respuesta: "Violencia", puntaje: 4 }
        ]
    },
    {
        pregunta: "Delitos que más se cometen en tu comunidad…",
        respuestas: [
            { respuesta: "Robo", puntaje: 10 },
            { respuesta: "Asalto", puntaje: 8 },
            { respuesta: "Vandalismo", puntaje: 6 },
            { respuesta: "Tráfico de drogas", puntaje: 4 }
        ]
    },
    {
        pregunta: "Edad en la que los adolescentes tienen su primera novia o novio…",
        respuestas: [
            { respuesta: "13 años", puntaje: 10 },
            { respuesta: "14 años", puntaje: 8 },
            { respuesta: "15 años", puntaje: 6 },
            { respuesta: "16 años o más tarde", puntaje: 4 }
        ]
    },
    {
        pregunta: "Edad más frecuente en la una mujer adolescentes se han embarazado…",
        respuestas: [
            { respuesta: "16 años", puntaje: 10 },
            { respuesta: "17 años", puntaje: 8 },
            { respuesta: "18 años", puntaje: 6 },
            { respuesta: "19 años o más tarde", puntaje: 4 }
        ]
    },
    {
        pregunta: "Método anticonceptivo que más conocen los adolescentes",
        respuestas: [
            { respuesta: "Condón", puntaje: 10 },
            { respuesta: "Pastillas anticonceptivas", puntaje: 8 },
            { respuesta: "Inyecciones", puntaje: 6 },
            { respuesta: "Implantes", puntaje: 4 }
        ]
    },
    {
        pregunta: "Droga más dañina para el ser humano…",
        respuestas: [
            { respuesta: "Heroína", puntaje: 10 },
            { respuesta: "Cocaína", puntaje: 8 },
            { respuesta: "Metanfetaminas", puntaje: 6 },
            { respuesta: "LSD", puntaje: 4 }
        ]
    },
    {
        pregunta: "Drogas con las que tienen contacto los adolescentes…",
        respuestas: [
            { respuesta: "Marihuana", puntaje: 10 },
            { respuesta: "Cocaína", puntaje: 8 },
            { respuesta: "Éxtasis", puntaje: 6 },
            { respuesta: "Anfetaminas", puntaje: 4 }
        ]
    },
    {
        pregunta: "Delito que los adolescentes cometen en su primera vez…",
        respuestas: [
            { respuesta: "Robo", puntaje: 10 },
            { respuesta: "Vandalismo", puntaje: 8 },
            { respuesta: "Consumo de drogas", puntaje: 6 },
            { respuesta: "Pelear", puntaje: 4 }
        ]
    },
    {
        pregunta: "Reglas que menos siguen los adolescentes en casa…",
        respuestas: [
            { respuesta: "Hacer la cama", puntaje: 10 },
            { respuesta: "Lavar los platos", puntaje: 8 },
            { respuesta: "Recoger su habitación", puntaje: 6 },
            { respuesta: "Ayudar en las tareas del hogar", puntaje: 4 }
        ]
    },
    {
        pregunta: "Reglas que menos siguen los adolescentes en la escuela…",
        respuestas: [
            { respuesta: "No usar celular en clase", puntaje: 10 },
            { respuesta: "Llegar a tiempo", puntaje: 8 },
            { respuesta: "Hacer la tarea", puntaje: 6 },
            { respuesta: "Respetar al profesor", puntaje: 4 }
        ]
    },
    {
        pregunta: "Es el mejor amigo de un adolescente…",
        respuestas: [
            { respuesta: "Su mascota", puntaje: 10 },
            { respuesta: "Su hermano(a)", puntaje: 8 },
            { respuesta: "Su mejor amigo(a)", puntaje: 6 },
            { respuesta: "Su novio(a)", puntaje: 4 }
        ]
    },
    {
        pregunta: "Derecho que más conocen los adolescentes…",
        respuestas: [
            { respuesta: "Derecho a la educación", puntaje: 10 },
            { respuesta: "Derecho a la salud", puntaje: 8 },
            { respuesta: "Derecho a la libertad de expresión", puntaje: 6 },
            { respuesta: "Derecho a la igualdad", puntaje: 4 }
        ]
    },
    {
        pregunta: "A quién le tienen más confianza los adolescentes…",
        respuestas: [
            { respuesta: "A sus amigos", puntaje: 10 },
            { respuesta: "A sus padres", puntaje: 8 },
            { respuesta: "A sus hermanos", puntaje: 6 },
            { respuesta: "A sus profesores", puntaje: 4 }
        ]
    },
    {
        pregunta: "Cuál es la meta más importante para un adolescente…",
        respuestas: [
            { respuesta: "Ser feliz", puntaje: 10 },
            { respuesta: "Tener éxito profesional", puntaje: 8 },
            { respuesta: "Viajar por el mundo", puntaje: 6 },
            { respuesta: "Formar una familia", puntaje: 4 }
        ]
    },
    {
        pregunta: "Cualidades de los adolescentes…",
        respuestas: [
            { respuesta: "Creatividad", puntaje: 10 },
            { respuesta: "Resiliencia", puntaje: 8 },
            { respuesta: "Empatía", puntaje: 6 },
            { respuesta: "Independencia", puntaje: 4 }
        ]
    },
    {
        pregunta: "Cuál es el cambio más importante de la etapa adolescente…",
        respuestas: [
            { respuesta: "Pubertad", puntaje: 10 },
            { respuesta: "Independencia", puntaje: 8 },
            { respuesta: "Identidad", puntaje: 6 },
            { respuesta: "Responsabilidad", puntaje: 4 }
        ]
    },
    {
        pregunta: "Mayor preocupación de los adolescentes…",
        respuestas: [
            { respuesta: "Futuro laboral", puntaje: 10 },
            { respuesta: "Relaciones sociales", puntaje: 8 },
            { respuesta: "Salud mental", puntaje: 6 },
            { respuesta: "Presión académica", puntaje: 4 }
        ]
    },
    {
        pregunta: "Para que sirve estudiar a un adolescente…",
        respuestas: [
            { respuesta: "Desarrollo personal", puntaje: 10 },
            { respuesta: "Mejorar el futuro", puntaje: 8 },
            { respuesta: "Adquirir conocimientos", puntaje: 6 },
            { respuesta: "Prepararse para la vida", puntaje: 4 }
        ]
    },
    {
        pregunta: "Actividad laboral que más le gustaría a un adolescente…",
        respuestas: [
            { respuesta: "Trabajar en tecnología", puntaje: 10 },
            { respuesta: "Trabajar en entretenimiento", puntaje: 8 },
            { respuesta: "Trabajar en arte", puntaje: 6 },
            { respuesta: "Trabajar en ciencia", puntaje: 4 }
        ]
    },
    {
        pregunta: "Libro preferido de los adolescentes…",
        respuestas: [
            { respuesta: "Harry Potter", puntaje: 10 },
            { respuesta: "Los Juegos del Hambre", puntaje: 8 },
            { respuesta: "Crepúsculo", puntaje: 6 },
            { respuesta: "El Señor de los Anillos", puntaje: 4 }
        ]
    },
    {
        pregunta: "Sanciones que pueden imponerse a los adolescentes que cometen delitos",
        respuestas: [
            { respuesta: "Reclusión", puntaje: 10 },
            { respuesta: "Servicio comunitario", puntaje: 8 },
            { respuesta: "Multas", puntaje: 6 },
            { respuesta: "Libertad condicional", puntaje: 4 }
        ]
    },
    {
        pregunta: "Autoridades que más conocen los adolescentes",
        respuestas: [
            { respuesta: "Policía", puntaje: 10 },
            { respuesta: "Juez", puntaje: 8 },
            { respuesta: "Presidente", puntaje: 6 },
            { respuesta: "Gobernador", puntaje: 4 }
        ]
    },
    {
        pregunta: "Autoridad en la que más pueden confiar los adolescentes",
        respuestas: [
            { respuesta: "Padres", puntaje: 10 },
            { respuesta: "Maestros", puntaje: 8 },
            { respuesta: "Amigos", puntaje: 6 },
            { respuesta: "Policía", puntaje: 4 }
        ]
    },
    {
        pregunta: "Actividad comunitaria en la que más participan los adolescentes",
        respuestas: [
            { respuesta: "Voluntariado", puntaje: 10 },
            { respuesta: "Eventos deportivos", puntaje: 8 },
            { respuesta: "Talleres culturales", puntaje: 6 },
            { respuesta: "Conciertos benéficos", puntaje: 4 }
        ]
    },
    {
        pregunta: "Temas de interés de los adolescentes",
        respuestas: [
            { respuesta: "Cambio climático", puntaje: 10 },
            { respuesta: "Derechos humanos", puntaje: 8 },
            { respuesta: "Igualdad de género", puntaje: 6 },
            { respuesta: "Salud mental", puntaje: 4 }
        ]
    },
    {
        pregunta: "Medidas preventivas que más conocen los adolescentes",
        respuestas: [
            { respuesta: "Vacunación", puntaje: 10 },
            { respuesta: "Lavado de manos", puntaje: 8 },
            { respuesta: "Uso de preservativo", puntaje: 6 },
            { respuesta: "Educación sexual", puntaje: 4 }
        ]
    },
    {
        pregunta: "Series que más han visto los adolescentes",
        respuestas: [
            { respuesta: "Stranger Things", puntaje: 10 },
            { respuesta: "13 Reasons Why", puntaje: 8 },
            { respuesta: "Riverdale", puntaje: 6 },
            { respuesta: "La Casa de Papel", puntaje: 4 }
        ]
    },
    {
        pregunta: "Sitios de Morelos que más visitan los adolescentes",
        respuestas: [
            { respuesta: "Tepoztlán", puntaje: 10 },
            { respuesta: "Cuernavaca", puntaje: 8 },
            { respuesta: "Tequesquitengo", puntaje: 6 },
            { respuesta: "Xochicalco", puntaje: 4 }
        ]
    }
];

// Función para mezclar el arreglo de preguntas
function mezclarPreguntas() {
    for (let i = preguntas.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [preguntas[i], preguntas[j]] = [preguntas[j], preguntas[i]];
    }
}

mezclarPreguntas(); // Mezclar las preguntas al inicio del juego

let preguntaActual = 0;
let puntajeTotal = 0;
let respuestasUsuario = []; // Almacenar respuestas del usuario
let numPreguntasJugadas = 0;
let numPreguntas = 5;
// Función para mostrar la pregunta actual
function mostrarPregunta() {
    const preguntaTexto = document.getElementById('pregunta-texto');
    preguntaTexto.textContent = preguntas[preguntaActual].pregunta;
}

// Función para enviar la respuesta
function enviarRespuesta() {
    const respuestaInput = document.getElementById('respuesta-input');
    const respuestaUsuario = respuestaInput.value.toLowerCase();
    const respuestasComunes = preguntas[preguntaActual].respuestas;
    let puntajeRespuesta = 0;

    respuestasUsuario.push({ pregunta: preguntas[preguntaActual].pregunta, respuesta: respuestaUsuario });

    for (let i = 0; i < respuestasComunes.length; i++) {
        if (respuestaUsuario === respuestasComunes[i].respuesta.toLowerCase()) {
            puntajeRespuesta = respuestasComunes[i].puntaje;
            break;
        }
    }

    puntajeTotal += puntajeRespuesta;

    preguntaActual++;
    numPreguntasJugadas++;

    if (numPreguntasJugadas < numPreguntas) {
        if (preguntaActual < preguntas.length) {
            mostrarPregunta();
            respuestaInput.value = '';
        } else {
            mostrarResultados();
        }
    } else {
        mostrarResultados();
    }
}

// Función para mostrar los resultados al finalizar el juego
function mostrarResultados() {
    const resultadosLista = document.getElementById('resultados-lista');
    let puntajeAcumulado = 0;
    resultadosLista.innerHTML = '';

    respuestasUsuario.forEach((respuestaUsuario, index) => {
        let puntajePregunta = 0;
        const respuestasComunes = preguntas[index].respuestas;

        resultadosLista.innerHTML += `<p>Pregunta: ${respuestaUsuario.pregunta}<br> Tu respuesta: ${respuestaUsuario.respuesta}</p>`;
        resultadosLista.innerHTML += '<ul>';

        for (let i = 0; i < respuestasComunes.length; i++) {
            const respuestaComun = respuestasComunes[i];
            const esRespuestaCorrecta = respuestaUsuario.respuesta.toLowerCase() === respuestaComun.respuesta.toLowerCase();

            resultadosLista.innerHTML += `${i+1}. Respuesta: ${respuestaComun.respuesta}, Puntaje: ${respuestaComun.puntaje}<br>`;
            if (esRespuestaCorrecta) {
                puntajePregunta = respuestaComun.puntaje;
            }
        }

        puntajeAcumulado += puntajePregunta;
        resultadosLista.innerHTML += `</ul><p>Puntaje de la pregunta: ${puntajePregunta}</p>`;
    });

    document.getElementById('puntaje-final').textContent = `Puntaje Total: ${puntajeAcumulado}`;
    document.getElementById('pregunta-container').style.display = 'none';
    document.getElementById('resultado-container').style.display = 'block';
}

// Función para reiniciar el juego
function reiniciarJuego() {
    preguntaActual = 0;
    puntajeTotal = 0;
    respuestasUsuario = [];
    numPreguntasJugadas = 0;
    mezclarPreguntas(); // Mezclar las preguntas al reiniciar
    mostrarPregunta();
    document.getElementById('pregunta-container').style.display = 'block';
    document.getElementById('resultado-container').style.display = 'none';
}

// Agregar evento al botón de reiniciar juego
document.getElementById('reiniciar-btn').addEventListener('click', reiniciarJuego);

// Inicializar el juego
mostrarPregunta();