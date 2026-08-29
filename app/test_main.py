import pytest
from unittest.mock import patch, MagicMock


from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "connection,google,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_have_access_google_page(
        mocked_internet_connection: MagicMock,
        mocked_google: MagicMock,
        connection: bool,
        google: bool,
        result: str
) -> None:
    mocked_internet_connection.return_value = connection
    mocked_google.return_value = google

    assert can_access_google_page("https://www.google.com") == result
