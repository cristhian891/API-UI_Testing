from restClient.Rest_API import RestClient
import pytest

@pytest.fixture
def rest_client():
    return RestClient()

URL = "http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/"
endpoint1 = URL + "/peps"
endpoint2 = URL + "/peps"

def get_enpoint_by_id(ID):
    return URL + "peps/{id}".format(id=ID)

@pytest.mark.api
def test_status_code_endpoint1(rest_client):
    """Test the status code of the response"""
    r = rest_client
    id = r.do_get_request(endpoint1)
    assert id.status_code == 200

@pytest.mark.api
def test_status_code_endpoint2( rest_client):
    """Test the status code of the response """
    r = rest_client
    body = {"country": "Australia",
            "id": "54",
            "name": "Cristhian Preciado",
            "position": "President",
            "risk": 5,
            "yob": "02/08/2018"
            }
    id = r.do_post_request(endpoint2, body)
    assert id.status_code == 201

@pytest.mark.api
def test_status_code_endpoint3(rest_client):
    """Test the status code of the response  """
    r = rest_client
    id = r.do_get_request(get_enpoint_by_id("5c6185f017b9b5026a1c6021"))
    assert id.status_code == 200

