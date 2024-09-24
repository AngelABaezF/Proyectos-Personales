function updateServiceName() {
    const serviceInput = document.getElementById('serviceInput');
    const button = document.querySelector('button');

    if (serviceName) {
        serviceInput.removeAttribute('disabled');
        if (serviceName.value === 'Análisis') {
            serviceInput.innerHTML = `
                <select>
                    <option value="rayosX">Rayos X</option>
                    <option value="sanguineos">Sanguíneos</option>
                    <option value="orina">Orina</option>
                    <option value="resonancia">Resonancia Magnética</option>
                    <option value="ecografia">Ecografía</option>
                </select>`;
        } else {
            serviceInput.innerHTML = `<input type="text" placeholder="Introduce el nombre del servicio">`;
        }
        button.removeAttribute('disabled');
    } else {
        serviceInput.innerHTML = `<input type="text" placeholder="Introduce el nombre del servicio" disabled>`;
        button.setAttribute('disabled', true);
    }
}

