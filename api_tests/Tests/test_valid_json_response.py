from restClient.Rest_API import RestClient
import pytest
import json

@pytest.fixture
def rest_client():
    return RestClient()

URL = "http://ec2-34-251-162-89.eu-west-1.compute.amazonaws.com/"
endpoint1 = URL + "/peps"

def get_enpoint_by_id(ID):
    return URL + "/peps/{id}".format(id=ID)

@pytest.mark.api
def test_valid_json_response(rest_client):
    """Test if the json response is a valid json message"""
    r = rest_client
    id = r.do_get_request(endpoint1)
    t = id.json()
    print(json.dumps(t, indent=4, sort_keys=True))
    def is_json(j):
        try:
            json_object = json.loads(j)
        except Exception as err:
            return False
        return True
    assert is_json(t), "This is not a valid JSON format"
