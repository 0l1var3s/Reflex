import reflex as rx
from components.forms import login_form

def login_page():
    return rx.center(
        rx.vstack(
            rx.heading("Iniciar Sesión", size="2xl"),
            login_form(),
            rx.link("¿No tienes cuenta? Regístrate", href="/registro"),
            spacing="4",
            width="100%",
            max_width="400px"
        ),
        height="calc(100vh - 100px)",
        width="full"
    )