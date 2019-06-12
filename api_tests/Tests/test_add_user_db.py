from .api.Rest import RestClient
import pytest
import json


@pytest.fixture
def rest_client():
    return RestClient()

URL = "http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/"
endpoint1 = URL + "/peps"
endpoint2 = URL + "/peps"

def get_endpoint_by_id(ID):
    return URL + "/peps/{id}".format(id=ID)

@pytest.mark.api
def test_adding_a_politician(rest_client):
    """Test the endpoint that add the user"""
    r = rest_client
    body = {"country": "Scotland",
            "id": "54",
            "name": "Martin King",
            "position": "President",
            "risk": 5,
            "yob": "02/08/2018"
            }
    id = r.do_post_request(endpoint2, body)
    assert id.status_code == 201
