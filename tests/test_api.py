import requests

def test_get_user_details():
    # 1. API Endpoint
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    # 2. Send GET Request with User-Agent Header
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    # 3. Assert Status Code (200 OK రావాలో లేదో చెక్ చేయడం)
    assert response.status_code == 200
    
    # 4. JSON Response ని డిక్షనరీగా మార్చుకోవడం
    data = response.json()
    
    # 5. Assertions
    assert data["id"] == 1
    assert "email" in data
    print(f"\n[API SUCCESS] User Name: {data['name']} | Email: {data['email']}")
    import requests

def test_get_user_details():
    url = "https://jsonplaceholder.typicode.com/users/1"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data
    print(f"\n[API SUCCESS] User Name: {data['name']} | Email: {data['email']}")


# --- కొత్తగా యాడ్ చేస్తున్న POST Request టెస్ట్ కేస్ ---
def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    
    # 1. మనం పంపాల్సిన కొత్త యూజర్ డేటా (Payload)
    user_payload = {
        "name": "Sunny Gajula",
        "username": "sunny_qa",
        "email": "sunny@example.com"
    }
    
    # 2. Send POST Request (json=user_payload అని పంపాలి)
    response = requests.post(url, json=user_payload)
    
    # 3. Assert Status Code (201 Created రావాలో లేదో చెక్ చేయడం)
    assert response.status_code == 201
    
    # 4. Response చెక్ చేయడం
    response_data = response.json()
    assert response_data["name"] == "Sunny Gajula"
    assert "id" in response_data  # కొత్తగా ఐడీ జనరేట్ అయిందో లేదో చూస్తుంది
    
    print(f"\n[POST SUCCESS] Created User ID: {response_data['id']} for {response_data['name']}")