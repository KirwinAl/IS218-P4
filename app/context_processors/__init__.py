from os import getenv
import datetime
from app.auth.forms import login_form


def utility_text_processors():
    message = "hello world"
    form = login_form()

    def current_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year

    def format_price(amount, currency="$"):
        return f"{currency}{amount:.2f}"

    return dict(
        form=form,
        mymessage=message,
        year=current_year(),
        format_price=format_price
    )
