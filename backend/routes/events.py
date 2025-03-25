import flask
import models

blueprint = flask.Blueprint("events", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def root():
    """
    When a <form> element in any .html file has the attribute action="/", it calls this function since @blueprint.route("/") decorates it.
    When a <form> element also has the attribute method="POST", flask.request.method becomes "POST".
    By default, refreshing or opening the website counts as the "GET" method.
    """
    
    # TODO: Move this to a separate route! Maybe /create.
    match flask.request.method:
        case "POST":
            models.Event.create(flask.request.form["name"])
            return flask.redirect("/")
    
    return flask.render_template("index.html", events=models.Event.read())


@blueprint.route("/update/<int:id>", methods=["GET", "POST"])
def update(id: int):
    match flask.request.method:
        case "POST":
            models.Event.update(id, **flask.request.form)
            return flask.redirect("/")
    
    current_event = models.Event.read("id = ?", id, limit=(1,))[0]
    return flask.render_template("update_event.html", event=current_event)


@blueprint.route("/delete/<int:id>")
def delete(id: int):
    models.Event.delete(id)
    return flask.redirect("/")