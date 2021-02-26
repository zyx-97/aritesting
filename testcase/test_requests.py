import json
import requests
import logging
import pytest

class TestRequest(object):
    root_logger = logging.getLogger()
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    #在logging.basicConfig前清理已有 handlers
    logging.basicConfig(level=logging.INFO)
    def test_get(self):
        r=requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))