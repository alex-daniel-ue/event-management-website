import flask
import models


# Change the static folder or template folder if frontend wants to reorder file structure.
app = flask.Flask(__name__,
                  static_folder="../frontend/assets",
                  template_folder='../frontend/')


@app.route("/", methods=["GET", "POST"])
def root():
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
    
    return flask.render_template("index.html", events=models.Event.read())


@app.route("/delete/<int:id>")
def delete(id: int):
    models.Event.delete(id)
    return flask.redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    match flask.request.method:
        case "POST":
            models.Event.update(id, **flask.request.form)
            return flask.redirect("/")
    
    current_event = models.Event.read("id = ?", id)[0]
    return flask.render_template("edit_event.html", event=current_event)


if __name__ == "__main__":
    app.run(debug=True)
