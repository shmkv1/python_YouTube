import requests


def test_status():
    resp = requests.get("https://api.hh.ru/vacancies?test=['qa','python']")
    assert resp.status_code == 200, f"Статус код не корректныйб \nres{resp.status_code}"
    print("Api работает!")