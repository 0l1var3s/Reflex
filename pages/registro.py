import reflex as rx
from components.forms import registro_form

def registro_page():
    return rx.center(
        rx.vstack(
            rx.heading("Registro de Usuario", size="2xl"),
            registro_form(),
            rx.link("¿Ya tienes cuenta? Inicia Sesión", href="/login"),
            spacing="4",
            width="100%",
            max_width="400px"
        ),
        height="calc(100vh - 100px)",
        width="full"
    )