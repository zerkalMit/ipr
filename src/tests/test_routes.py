import json

import numpy as np
import pytest
import requests


@pytest.fixture
def generate_data_for_tests():
    path = "api/users/2"
    schema_extra = {
            "example": {
                "p_res": 250,
                "wct": 50,
                "pi": 1,
                "pb": 150,
            }
    }
    response = requests.get(url='http://127.0.0.1:8002/ipr/calc',json=schema_extra)
    responseJson = json.loads(response.text)
    assert response.status_code == 405
    pass


def test_calc_model_success(api_client, generate_data_for_tests):

    pass
