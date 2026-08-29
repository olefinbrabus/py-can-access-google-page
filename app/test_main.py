from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_have_access_google_page(
    mocked_internet_connection: MagicMock,
    mocked_google: MagicMock,
) -> None:
    if any((
            mocked_internet_connection.return_value is not True,
            mocked_google.return_value is not True
    )):
        assert False

    assert can_access_google_page("https://www.google.com") == "Accessible"
