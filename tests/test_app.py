

def test_homepage(client):
    response = client.get("/")
    assert b"Kate Drew" in response.data
    assert b"Believe you can and you're halfway there." in response.data
    assert b"Theodore Roosevelt" in response.data

def test_colour_picker_route(client):
    response = client.get("/colour-picker")
    assert b"Colour Picker" in response.data
    

def test_non_existent_route(client):
    response = client.get('/non-existent')
    assert response.status_code == 404
