from pages.project_api import ProjectAPI

x_api_key = "06ABXMP-7CC4Q6M-PGZMA9G-62PFSKX"

api_key = {
    "X-API-KEY": f"{x_api_key}"
}

kinopoisk = ProjectAPI("https://api.kinopoisk.dev/v1.4/")


def test_get_movies(filtres={"rating.kp": "9.1-10"}, auth_token=api_key):
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
