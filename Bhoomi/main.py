import folium
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # Create a map centered on a specific location
    start_coords = [37.7749, -122.4194]  # Coordinates for San Francisco
    folium_map = folium.Map(location=start_coords, zoom_start=12)

    # Add a marker (example: a landmark in your community)
    folium.Marker(location=[37.7749, -122.4194], popup="Golden Gate Bridge").add_to(
        folium_map
    )

    # Save the map as an HTML file
    folium_map.save("templates/map.html")

    return render_template("index.html")


@app.route("/map")
def maps():
    return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
