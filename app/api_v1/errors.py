# Copyright 2016 Allan Rank
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import jsonify
from . import api


@api.app_errorhandler(400)
def bad_request(e):
    response = jsonify({"error": "bad request"})
    response.status_code = 400
    return response


@api.app_errorhandler(403)
def forbidden(e):
    response = jsonify({"error": "forbidden"})
    response.status_code = 403
    return response


@api.app_errorhandler(404)
def page_not_found(e):
    response = jsonify({"error": "not found"})
    response.status_code = 404
    return response


@api.app_errorhandler(405)
def page_not_found(e):
    response = jsonify({"error": "method not allowed"})
    response.status_code = 405
    return response


@api.app_errorhandler(500)
def internal_server_error(e):
    response = jsonify({"error": "internal server error"})
    response.status_code = 500
    return response
