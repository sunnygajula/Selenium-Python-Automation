import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_list():
    # 1. API కి GET రిక్వెస్ట్ పంపుతున్నాం
    response = requests.get(f"{BASE_URL}/posts/1")
    
    # 2. Status Code 200 (Success) అని చెక్ చేస్తున్నాం
    assert response.status_code == 200
    
    # 3. Response JSON డేటాని చెక్ చేస్తున్నాం
    json_data = response.json()
    assert json_data["id"] == 1
    assert "title" in json_data

def test_create_post():
    # 1. కొత్త పోస్ట్‌ని క్రియేట్ చేయడానికి డేటా (Payload)
    payload = {
        "title": "Automation Test",
        "body": "API Testing with Python Requests",
        "userId": 1
    }
    
    # 2. POST రిక్వెస్ట్ పంపుతున్నాం
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    # 3. Status Code 201 (Created) అని చెక్ చేస్తున్నాం
    assert response.status_code == 201
    
    # 4. రెస్పాన్స్‌లో మన డేటా ఉందో లేదో చెక్ చేస్తున్నాం
    json_data = response.json()
    assert json_data["title"] == "Automation Test"
    assert json_data["userId"] == 1