document.addEventListener('DOMContentLoaded', function() {
    // Obtener los datos del formulario del almacenamiento local
    const customGameData = localStorage.getItem('customGameData');

    if (customGameData) {
        // Convertir los datos JSON de nuevo a objeto JavaScript
        const formData = JSON.parse(customGameData);
        const numQuestions = formData.numQuestions;
        const numPlayers = formData.numPlayers;
        const playerNames = formData.playerNames;

        // Mostrar el número de preguntas
        const questionsInfo = document.getElementById('questionsInfo');
        questionsInfo.textContent = `Número de preguntas: ${numQuestions}`;

        // Mostrar el nombre del primer jugador
        let currentPlayerIndex = 0;
        displayCurrentPlayer(playerNames[currentPlayerIndex]);

        // Manejar el evento del botón para pasar al siguiente jugador
        const nextPlayerButton = document.getElementById('nextPlayerButton');
        nextPlayerButton.addEventListener('click', function() {
            currentPlayerIndex = (currentPlayerIndex + 1) % numPlayers;
            if (currentPlayerIndex === 0) {
                // Si se ha completado una ronda completa de turnos
                displayFinalMessage();
            } else {
                displayCurrentPlayer(playerNames[currentPlayerIndex]);
            }
        });
    } else {
        console.log('No se encontraron datos del formulario enviado.');
    }
});

function displayCurrentPlayer(playerName) {
    // Mostrar el nombre del jugador cuyo turno es actualmente
    const turnInfo = document.getElementById('turnInfo');
    turnInfo.textContent = `Turno de: ${playerName}`;
}

function displayFinalMessage() {
    // Mostrar "Finalizo" una vez que todos los jugadores hayan tenido su turno
    const turnInfo = document.getElementById('turnInfo');
    turnInfo.textContent = 'Finalizo';
    // Deshabilitar el botón de pasar turno
    const nextPlayerButton = document.getElementById('nextPlayerButton');
    nextPlayerButton.disabled = true;
}
