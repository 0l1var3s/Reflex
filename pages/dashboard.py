import reflex as rx
from activos_management.state.auth import AuthState

def dashboard_page():
    return rx.cond(
        AuthState.usuario_actual,  # Condición
        rx.vstack(
            rx.hstack(
                rx.heading(f"Bienvenido, {AuthState.usuario_actual.get('username', 'Usuario')}", size="2xl"),
                rx.spacer(),
                rx.button("Cerrar Sesión", on_click=AuthState.logout, color_scheme="red")
            ),
            rx.card(
                rx.vstack(
                    rx.heading("Resumen de Movimientos", size="lg"),
                    rx.cond(
                        len(AuthState.usuario_actual.get('movimientos', [])) > 0,
                        rx.vstack(
                            rx.foreach(
                                AuthState.usuario_actual.get('movimientos', []),
                                lambda movimiento: rx.card(
                                    rx.vstack(
                                        rx.text(f"Tipo: {movimiento['tipo_activo']}"),
                                        rx.text(f"Descripción: {movimiento['descripcion']}"),
                                        rx.text(f"Fecha: {movimiento['fecha']}")
                                    )
                                )
                            )
                        ),
                        rx.text("No hay movimientos registrados")
                    )
                )
            ),
            rx.link(
                rx.button("Registrar Movimiento", color_scheme="green"),
                href="/movimientos"
            ),
            width="full",
            spacing="4"
        ),
        rx.redirect("/login")  # Si no hay usuario autenticado
    )