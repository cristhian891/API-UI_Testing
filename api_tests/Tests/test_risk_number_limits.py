from restClient.Rest_API import RestClient
import pytest


@pytest.fixture
def rest_client():
    return RestClient()

URL = "http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/"
endpoint1 = URL + "/peps"
endpoint2 = URL + "/peps"

def get_endpoint_by_id(ID):
    return URL + "/peps/{id}".format(id=ID)

@pytest.mark.api
def test_risk_number_inferior_limit(rest_client):
    """Test the endpoint that add the user"""
    r = rest_client
    body = {"country": "Scotland",
            "id": "54",
            "name": "Martin King",
            "position": "President",
            "risk": 0,
            "yob": "02/08/2018"
            }
    id = r.do_post_request(endpoint2, body)
    if id.status_code == 201:
        assert False, "The API should allow to create a user with risk > 5"
    else:
        assert True

@pytest.mark.api
def test_risk_number_superior_limit(rest_client):
    """Test the endpoint that add the user"""
    r = rest_client
    body = {"country": "Scotland",
            "id": "54",
            "name": "Martin King",
            "position": "President",
            "risk": 6,
            "yob": "02/08/2018"
            }
    id = r.do_post_request(endpoint2, body)
    if id.status_code == 201:
        assert False, "The API should allow to create a user with risk > 5"
    else:
        assert True


