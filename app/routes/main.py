from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to my JobTracker!"}), 200


@main_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "jobtracker-api"}), 200
