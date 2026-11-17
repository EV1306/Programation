from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__, template_folder="templates")

@app.get("/")
def index():
    return render_template(
        "Visualisation fichier CSV.html",
        csv_url=url_for("election_csv"),
        kml_url=url_for("states_kml"),
    )

@app.get("/data/election.csv")
def election_csv():
    return send_from_directory(
        app.template_folder,
        "Germany_Election_Master_Filled_2021.csv",
    )

@app.get("/data/states.kml")
def states_kml():
    return send_from_directory(
        app.template_folder,
        "states_level_1.kml",
    )

if __name__ == "__main__":
    app.run()