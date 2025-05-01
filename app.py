from flask import Flask, jsonify, render_template, request
from controllers.book_controller import book_bp
from db import close_db


def create_app():
    app = Flask(__name__)  # start a new flask app
    # we connect the blueprint to the flask app so /books will work
    app.register_blueprint(book_bp)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad request"}), 400

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def handle_server_error(error):
        return jsonify({"error": "Server error"}), 500

    app.teardown_appcontext(close_db)

    return app


if __name__ == "__main__":
    app = create_app()  # call the create_app function to create the flask app
    # start the app and if any error happened will show details(debug mode is on)
    app.run(debug=True)
