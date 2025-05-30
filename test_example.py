import time
import json

def test_passes():
    assert True

def test_with_sleep():
    time.sleep(5)

def test_fails():
    with open("test.txt", "w") as f:
        f.write(json.dumps({"test": "demo"}))

