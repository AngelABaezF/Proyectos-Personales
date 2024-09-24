let map = L.map('map').setView([0, 0], 1);
let userLatitude;
let userLongitude;

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("La geolocalización no es soportada por su navegador");
    }
}

function showPosition(position) {
    userLatitude = position.coords.latitude;
    userLongitude = position.coords.longitude;
    map.setView([userLatitude, userLongitude], 14);
    L.marker([userLatitude, userLongitude]).addTo(map)
        .bindPopup("Usted está aquí")
        .openPopup();
}

function locateNearestPharmacy() {
    var requiredMedicine = "Ibuprofeno"
    fetch('http://127.0.0.1:5000/nearest_pharmacy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            latitude: userLatitude,
            longitude: userLongitude,
            medicine: requiredMedicine
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                var pharmacyName = data.name;
                var distance = data.distance;
                var pharmacyLatitude = data.latitude;
                var pharmacyLongitude = data.longitude;

                L.marker([pharmacyLatitude, pharmacyLongitude]).addTo(map)
                    .bindPopup(`Farmacia más cercana: ${pharmacyName} (${distance.toFixed(2)} km)`)
                    .openPopup();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function locateCheapestPharmacy() {
    var requiredMedicine = 0;
    fetch('http://127.0.0.1:5000/cheapest_pharmacy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            latitude: userLatitude,
            longitude: userLongitude,
            medicine: requiredMedicine
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                var pharmacyName = data.name;
                var pharmacyLatitude = data.latitude;
                var pharmacyLongitude = data.longitude;

                L.marker([pharmacyLatitude, pharmacyLongitude]).addTo(map)
                    .bindPopup(`Farmacia más barata: ${pharmacyName}`)
                    .openPopup();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function locateBestOption() {
    var requiredMedicine;
    fetch('http://127.0.0.1:5000/best_option', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            latitude: userLatitude,
            longitude: userLongitude,
            medicine: requiredMedicine
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                var pharmacyName = data.name;
                var distance = data.distance;
                var pharmacyLatitude = data.latitude;
                var pharmacyLongitude = data.longitude;

                L.marker([pharmacyLatitude, pharmacyLongitude]).addTo(map)
                    .bindPopup(`La mejor opcion es: ${pharmacyName} (${distance.toFixed(2)} km)`)
                    .openPopup();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("El usuario ha denegado la solicitud de geolocalización.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("La información de la ubicación no está disponible.");
            break;
        case error.TIMEOUT:
            alert("La solicitud para obtener la ubicación ha caducado.");
            break;
        case error.UNKNOWN_ERROR:
            alert("Se ha producido un error desconocido.");
            break;
    }
}

getLocation()