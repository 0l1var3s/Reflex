import reflex as rx
from activos_management.state.auth import AuthState


def navbar():
    return rx.hstack(
        rx.link(
            rx.heading("Gestión de Activos", size="md"),
            href="/"
        ),
        rx.spacer(),
        rx.cond(
            AuthState.usuario_actual,
            rx.hstack(
                rx.text(f"Bienvenido, {AuthState.usuario_actual.get('username', '')}"),
                rx.button("Cerrar Sesión", on_click=AuthState.logout, size="sm", color_scheme="red")
            ),
            rx.hstack(
                rx.link("Iniciar Sesión", href="/login", padding="2"),
                rx.link("Registrarse", href="/registro", padding="2")
            )
        ),
        width="full",
        padding="4",
        bg="lightgray"
    )