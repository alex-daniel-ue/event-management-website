import flask
import routes.events

# Change the static folder or template folder if frontend wants to reorder file structure.
app = flask.Flask(__name__,
                  static_folder="../frontend/assets",
                  template_folder='../frontend/')

app.register_blueprint(routes.events.blueprint)

if __name__ == "__main__":
    app.run(debug=True)
