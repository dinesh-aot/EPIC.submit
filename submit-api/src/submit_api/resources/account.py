# Copyright © 2024 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""API endpoints for managing an account resource."""

from http import HTTPStatus

from flask_restx import Namespace, Resource
from submit_api.services.account_service import AccountService
from submit_api.utils.util import cors_preflight
from submit_api.schemas.account import AccountSchema, AccountCreateSchema
from .apihelper import Api as ApiHelper

API = Namespace("accounts", description="Endpoints for Account Management")
"""Custom exception messages
"""

account_create_model = ApiHelper.convert_ma_schema_to_restx_model(
    API, AccountCreateSchema(), "Account Create"
)
account_list_model = ApiHelper.convert_ma_schema_to_restx_model(
    API, AccountSchema(), "Account"
)


@cors_preflight("GET, OPTIONS, POST")
@API.route("", methods=["POST", "GET", "OPTIONS"])
class Accounts(Resource):
    """Resource for managing accounts."""

    @staticmethod
    @API.response(code=HTTPStatus.OK, description="Success", model=[account_list_model])
    @ApiHelper.swagger_decorators(API, endpoint_description="Fetch all accounts")
    def get():
        """Fetch all accounts."""
        accounts = AccountService.get_all_accounts()
        accounts_list_schema = AccountSchema(many=True)
        return accounts_list_schema.dump(accounts), HTTPStatus.OK

    @staticmethod
    @ApiHelper.swagger_decorators(API, endpoint_description="Create an account")
    @API.expect(account_create_model)
    @API.response(code=HTTPStatus.CREATED, model=account_list_model, description="Account Created")
    @API.response(HTTPStatus.BAD_REQUEST, "Bad Request")
    def post():
        """Create an account."""
        account_data = AccountCreateSchema().load(API.payload)
        created_account = AccountService.create_account(account_data)
        return AccountSchema().dump(created_account), HTTPStatus.CREATED
