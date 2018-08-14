from app import create_app
from flask import jsonify


app = create_app()

@app.errorhandler(404)
def page_not_found(e):
	return jsonify({
		"status": "ERROR",
		"message": "Routes is not available",
		"data": None
		}), 404


@app.errorhandler(405)
def request_method_not_allowed(e):
	return jsonify({
		"status": "ERROR", 
		"message": "Method not allowed"
		}), 405


if __name__ == '__main__':
	app.run()