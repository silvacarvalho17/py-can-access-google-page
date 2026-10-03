from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_accessible_when_url_is_valid_and_has_connection(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_url_is_invalid(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_no_connection(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_when_url_invalid_and_no_connection(
    mock_valid_google_url,
    mock_has_internet_connection,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
