import flask
import models


app = flask.Flask(__name__,
                  static_folder="../frontend/assets",
                  template_folder='../frontend/')

@app.route("/", methods=["POST", "GET"])
def index():
    """
    When a <form> element in any .html file has the attribute action="/", it calls this function since @app.route("/") decorates it.
    When a <form> element also has the attribute method="POST", flask.request.method becomes "POST".
    By default, refreshing or opening the website counts as the "GET" method.
    """
    
    match flask.request.method:
        case "POST":
            models.Event.create(flask.request.form["name"])
            # Does redirect() makes flask.request.form = "GET", preventing duplicate entries?
            return flask.redirect("/")
    
    return flask.render_template("index.html", events=models.Event.select_all())

if __name__ == "__main__":
    app.run(debug=True)
