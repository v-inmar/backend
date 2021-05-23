from app.index import app
import os


# Run and expose the server
# NOTE: Not needed if using FLASK CLI but I kept it here for reference purposes
if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=os.getenv("PORT", 5000), debug=True)