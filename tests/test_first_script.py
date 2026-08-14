def test_google_title(setup):
    driver = setup
    driver.get("https://www.google.com")
    
    # ❌ Intentionally failing to test screenshot capture
    assert "Yahoo" in driver.title