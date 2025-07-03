from flask import Blueprint, jsonify, request
from services.DataImportService import get_entries_by_year, get_all_entries  # importing service functions

"""
    - Defines /entries endpoint (Blueprint)
    - Using Flask Blueprints - to help organize APIs, instead of defining all routes in app.py
"""

history_bp = Blueprint("entries", __name__)  # defining Blueprint

@history_bp.route("/entries", methods=["GET"])
def get_entries():

    """
    Returns Eurovision history data.
        - If 'year' query param is provided -> returns data for that year.
        - If no query param -> returns all data.
    """

    year = request.args.get("year")  # retrieving 'year' query parameter

    if year:
        results = get_entries_by_year(int(year))  # using get_entries_by_year service function
    else:
        results = get_all_entries()  # using get_all_entries service function to retrieve all entries in dataset

    return jsonify(results)
