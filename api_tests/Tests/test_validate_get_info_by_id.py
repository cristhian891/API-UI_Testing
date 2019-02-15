from restClient.Rest_API import RestClient
import pytest
import json

@pytest.fixture
def rest_client():
    return RestClient()

URL = "http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/"
endpoint1 = URL + "/peps"
endpoint2 = URL + "/peps"

def get_enpoint_by_id(ID):
    return URL + "peps/{id}".format(id=ID)

@pytest.mark.api
def test_status_code_endpoint3(rest_client):
    """Test the validation of the empoint that bring the information of an user by ID  """
    r = rest_client
    id = r.do_get_request(get_enpoint_by_id("5c6185f017b9b5026a1c6021"))
    t = id.json()
    fullname = t["name"]
    print (fullname)
    assert fullname == "Cindy Alvarez", "The user doesn't match by ID"
