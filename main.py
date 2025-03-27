import reflex as rx
from pages.login import login_page
from pages.registro import registro_page
from pages.dashboard import dashboard_page
from pages.movimientos import movimientos_page
from state.auth import AuthState
from components.navbar import navbar
from components.forms import login_form
from styles.theme import apply_theme


def index():
    return rx.redirect("/login")

app = rx.App()
apply_theme(app)

def layout():
    return rx.vstack(
        navbar(),
        rx.box(rx.outlet()),
        width="full"
    )

app.layout = layout


app.add_page(index, route="/")
app.add_page(login_page, route="/login")
app.add_page(registro_page, route="/registro")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(movimientos_page, route="/movimientos")
