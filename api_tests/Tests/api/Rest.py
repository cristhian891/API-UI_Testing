import requests
import json

class RestClient():

    #This method returns the response of a post request to the given endpoint
    def do_post_request(self, url, body):
        response = requests.post(url, data=json.dumps(body),
                                 headers={
                                     'Content-Type': 'application/json',
                                     'X-Requested-By': 'SDC',
                                     'X-SS-REST-CALL': 'true'
                                 })
        return response

    # This method returns the response of a GET request to the given endpoint
    def do_get_request(self, url):
        response = requests.get(url,
                                headers={
                                    'Content-Type': 'application/json',
                                    'X-Requested-By': 'SDC',
                                    'X-SS-REST-CALL': 'true'
                                })
        return response

    def get_status(self):
        r = requests.status_codes
        return r

