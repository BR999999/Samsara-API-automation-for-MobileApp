import random
import unittest

from samsara_service import SamSaraService


class SamsaraApiTests(unittest.TestCase):

    def test_post_random_address(self):
        new_address = {
            "geofence": {
                "polygon": {
                    "vertices": [
                        {
                            "latitude": random.uniform(-90, 90),
                            "longitude": random.uniform(-90, 90),
                        },
                        {
                            "latitude": random.uniform(-90, 90),
                            "longitude": random.uniform(-90, 90),
                        },
                        {
                            "latitude": random.uniform(-90, 90),
                            "longitude": random.uniform(-90, 90),
                        }
                    ]
                }
            },
            "name": f"Random Name {random.randint(100, 1000)}",
            "formattedAddress": f"{random.randint(100, 1000)} Rhode Island St, San Francisco, CA"
        }

        # old count
        address_size = len(SamSaraService().get_all_address().json()['data'])

        # make call to Samsara to save
        SamSaraService().save_address(payload=new_address)

        # verify get address status code
        resp = SamSaraService().get_all_address()
        self.assertTrue('Verify call was 200', resp.status_code == 200)

        # verify increase in address size
        self.assertTrue('Verify address size got larger by 1',
                        lambda: True if len(resp.json()['data']) == address_size + 1 else False)

        # verify address object got saved correctly
        for address in resp.json()['data']:
            if address['name'] == new_address['name']:
                self.assertTrue('Verify same object', address == new_address)
                break
        else:
            self.fail('Did not find address object')

    def test_save_incomplete_data(self):
        new_address = {
            "geofence": {
                "polygon": {
                }
            },
            "name": f"Random Name {random.randint(100, 1000)}",
            "formattedAddress": f"{random.randint(100, 1000)} Rhode Island St, San Francisco, CA"
        }
        # make call to Samsara to save
        resp = SamSaraService().save_address(payload=new_address)

        # verify status code
        self.assertTrue('Verify 500', resp.status_code == 500) # should be 400 for bad request

        # verify error message
        self.assertTrue('Verify error message',
                        lambda: True if 'Internal Server Error' in resp.json['message'] else False)