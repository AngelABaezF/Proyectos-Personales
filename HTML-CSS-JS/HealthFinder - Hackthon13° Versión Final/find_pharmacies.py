from flask import Flask, request, jsonify
from flask_cors import CORS
from math import radians, cos, sin, sqrt, atan2
import requests
import mysql.connector

app = Flask(__name__)
CORS(app)

def haversine(lon1, lat1, lon2, lat2):
    R = 6371  # Radio de la tierra en km
    dlon = radians(lon2 - lon1)
    dlat = radians(lat2 - lat1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def find_pharmacies(user_lat, user_lon, radius):
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="pharmacy"](around:{radius},{user_lat},{user_lon});
      way["amenity"="pharmacy"](around:{radius},{user_lat},{user_lon});
      relation["amenity"="pharmacy"](around:{radius},{user_lat},{user_lon});
    );
    out center;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    return data

def find_pharmacy(pharmacies, user_latitude, user_longitude, requiredMedicine):
    min_distance = float("inf")
    lowest_price = float("inf")
    lowest_cost = float("inf")
    nearest_pharmacy = None
    cheapest_pharmacy = None
    best_option = None

    for pharmacy in pharmacies["elements"]:
        if has_medicine(pharmacy, requiredMedicine):
            pharmacy_latitude = pharmacy["lat"]
            pharmacy_longitude = pharmacy["lon"]
            distance = haversine(user_longitude, user_latitude, pharmacy_longitude, pharmacy_latitude)
            price = 0
            cost = (distance * 1.76) + price

            if cost < lowest_cost:
                lowest_cost = cost
                best_option = pharmacy

            if price < lowest_price:
                lowest_price = price
                cheapest_pharmacy = pharmacy
            
            if distance < min_distance:
                min_distance = distance
                nearest_pharmacy = pharmacy
    
    return nearest_pharmacy, min_distance, cheapest_pharmacy, best_option

def has_medicine(pharmacy, medicine):
    # connection = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="1234",
    #     database="healthfinder"
    # )
    # cursor = connection.cursor(dictionary=True)

    # pharmacy_name = pharmacy["tags"]["name"]
    # query = """SELECT farmacia_id FROM farmacias WHERE Nombre=%s"""
    # cursor.execute(query, (pharmacy_name,))
    # pharmacy_id = cursor.fetchone()["farmacia_id"]

    # query = """SELECT medicamento_id FROM medicamentos WHERE Nombre=%s"""
    # cursor.execute(query, (medicine,))
    # medicine_id = cursor.fetchone()["medicamento_id"]

    # query = """SELECT cantidad_disponible FROM inventario WHERE farmacia_id=%s AND medicamento_id=%s"""
    # cursor.execute(query, (pharmacy_id,medicine_id,))
    # disponibility = cursor.fetchone()["cantidad_disponible"]

    # connection.close()
    # return disponibility
    return True

def get_medicine_price(pharmacy, medicine):
    # connection = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="1234",
    #     database="healthfinder"
    # )
    # cursor = connection(dictionary=True)

    # pharmacy_name = pharmacy["tags"]["name"]
    # query = """SELECT ID_Farmacia FROM farmacia WHERE Nombre=%s"""
    # cursor.execute(query, (pharmacy_name,))
    # pharmacy_id = cursor.fetchone()

    # query = """SELECT ID_Medicamento FROM medicamento WHERE Nombre=%s"""
    # cursor.execute(query, (medicine,))
    # medicine_id = cursor.fetchone

    # query = """SELECT Precio FROM inventario WHERE ID_Farmacia=%s AND ID_Farmacia=%s"""
    # cursor.execute(query, (pharmacy_id,medicine_id,))
    # price = cursor.fetchone

    # connection.close()

    # print("Price", price)
    # return price
    return 0

@app.route('/nearest_pharmacy', methods=['POST'])
def nearest_pharmacy():
    data = request.json
    user_lat = data['latitude']
    user_lon = data['longitude']
    medicine = data['medicine']
    radius = data.get('radius', 5000)
    pharmacies = find_pharmacies(user_lat, user_lon, radius)

    if pharmacies:
        closest_pharmacy, distance, _, _ = find_pharmacy(pharmacies, user_lat, user_lon, medicine)
        return jsonify({
            "name": closest_pharmacy["tags"].get("name", "Unknown"),
            "distance": distance,
            "latitude": closest_pharmacy["lat"],
            "longitude": closest_pharmacy["lon"]
        })
    else:
        return jsonify({"error": "No pharmacies found"}), 404

@app.route('/cheapest_pharmacy', methods=['POST'])
def cheapest_pharmacy():
    data = request.json
    user_lat = data['latitude']
    user_lon = data['longitude']
    medicine = data['medicine']
    radius = data.get('radius', 5000)
    pharmacies = find_pharmacies(user_lat, user_lon, radius)

    if pharmacies:
        _, _, cheapest_pharmacy, _ = find_pharmacy(pharmacies, user_lat, user_lon, medicine)
        return jsonify({
            "name": cheapest_pharmacy["tags"].get("name", "Unknown"),
            "latitude": cheapest_pharmacy["lat"],
            "longitude": cheapest_pharmacy["lon"]
        })
    else:
        return jsonify({"error": "No pharmacies found"}), 404

@app.route('/best_option', methods=['POST'])
def best_option():
    data = request.json
    user_lat = data['latitude']
    user_lon = data['longitude']
    medicine = data['medicine']
    radius = data.get('radius', 5000)
    pharmacies = find_pharmacies(user_lat, user_lon, radius)

    if pharmacies:
        _, _, _, best_option = find_pharmacy(pharmacies, user_lat, user_lon, medicine)
        return jsonify({
            "name": best_option["tags"].get("name", "Unknown"),
            "latitude": best_option["lat"],
            "longitude": best_option["lon"]
        })
    else:
        return jsonify({"error": "No pharmacies found"}), 4040

if __name__ == "__main__":
    app.run(debug=True)

    # connection = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="1234",
    #     database="healthfinder"
    # )
    # cursor = connection.cursor(dictionary=True)
    # cursor.execute("SELECT * FROM medicamentos")
    # registros = cursor.fetchone()
    # print(registros)

    # query = """INSERT INTO medicamentos (Nombre) VALUES ('Ibuprofeno')"""
    # cursor.execute(query)

    # query = """INSERT INTO inventario (farmacia_id, medicamento_id) VALUES (1, 3)"""
    # cursor.execute(query)

    # cursor.execute(f"SHOW COLUMNS FROM inventario")
    # columnas = cursor.fetchall()
    # print(columnas)
    # query = """SELECT medicamento_id FROM medicamentos WHERE Nombre=%s"""
    # cursor.execute(query, (medicine,))
    # medicine_id = cursor.fetchone()["medicamento_id"]
    # cursor.execute("SELECT * FROM medicamentos")
    # registros = cursor.fetchall()
    # print(registros)
    # connection.close()
