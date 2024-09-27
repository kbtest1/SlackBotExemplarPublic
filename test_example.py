
import time

def test_passes():
    assert True

def test_with_sleep():
    time.sleep(5)

def test_fails():
    with open("test.txt", "w") as f:
        f.write({"test": "demo"})

# test 2
# test 3
