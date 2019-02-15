from restClient.Rest_API import RestClient
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
def test_get_info_politician(rest_client):
    """Test the json fields generated"""
    r = rest_client
    resp = r.do_get_request(get_endpoint_by_id("5c6185f017b9b5026a1c6021"))
    t = resp.json()

    country = t["country"]
    id = t["id"]
    name = t["name"]
    position = t["position"]
    risk = t["risk"]
    yob = t["yob"]

    if (isinstance(country, str) & isinstance(id,str) & isinstance(name, str) & isinstance(position, str) & isinstance(risk, int)
        & isinstance(yob, str)):
        assert True
    else:
        assert False, "The Json data dont have the correct data types"
