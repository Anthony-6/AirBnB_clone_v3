#!/usr/bin/python3
"""Create a new view for review objects that
handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import request, abort, jsonify
from models.review import Review
from models import storage


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'])
def reviewsWithId(review_id=None):
    """Methods that retrieves all methods for reviews with id"""
    reviewId = storage.get(Review, review_id)
    if reviewId is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(reviewId.to_dict())

    if request.method == 'DELETE':
        reviewId.delete()
        del reviewId
        return jsonify({}), 200

    if request.method == 'PUT':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        reviewId.save()
        return jsonify(reviewId.to_dict())


@app_views.route('/reviews/', methods=['POST', 'GET'])
def reviewsNoId():
    """Methods that retrieves all methods for reviews without id"""
    if request.method == 'POST':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        if request.get_json().get('name') is None:
            abort(400, 'Missing name')
        newReview = Review(**request.get_json())
        newReview.save()
        return jsonify(newReview.to_dict()), 200

    if request.method == 'GET':
        allreview = storage.all(Review)
        allreview = [allObject.to_dict() for allObject in allreview.values()]
        return jsonify(allreview)
