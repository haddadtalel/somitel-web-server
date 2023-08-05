from flask import Flask

app = Flask(__name__)

from .route import bp  # Import the blueprint

app.register_blueprint(bp)  # Register the blueprint
#load_dotenv()

#mogo_url = os.getenv("MONGO_URI")
#db = PyMongo(app)