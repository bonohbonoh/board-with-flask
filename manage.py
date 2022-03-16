from apps import blueprint, blueprintIndex
from apps.src import app

app.register_blueprint(blueprint)
app.register_blueprint(blueprintIndex)
app.app_context().push()

if __name__ == "__main__":
    app.run()
