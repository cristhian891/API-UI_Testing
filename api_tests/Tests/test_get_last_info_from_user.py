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
def test_get_info_politician(rest_client):
    """Test the json fields generated"""
    r = rest_client
    body = {"country": "England",
            "id": "54",
            "name": "Sarah Barcroft",
            "position": "President",
            "risk": 4,
            "yob": "02/08/2018"
            }
    r.do_post_request(endpoint2, body)

    j = r.do_get_request(endpoint1)
    t = j.json()
    #print(json.dumps(t, indent=4, sort_keys=True))
    id = t[0]["id"]

    j2 = r.do_get_request(get_endpoint_by_id(id))
    t2 = j2.json()
    #print(json.dumps(t2, indent=4, sort_keys=True))
    fullname = t2["name"]
    #print(fullname)
    assert fullname == "Sarah Barcroft" , "The politician wasn't added to the DB"
