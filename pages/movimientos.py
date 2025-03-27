import reflex as rx
from activos_management.state.auth import AuthState

def movimientos_page():
    return rx.cond(
        AuthState.usuario_actual,  # Condición
        rx.vstack(
            rx.heading("Registro de Movimiento de Activos", size="2xl"),
            rx.card(
                rx.vstack(
                    rx.select(
                        ["Equipo de Computo", "Mobiliario", "Vehículo", "Maquinaria"],
                        placeholder="Seleccione Tipo de Activo",
                        id="tipo_activo"
                    ),
                    rx.text_area(
                        placeholder="Descripción del Movimiento",
                        id="descripcion_movimiento"
                    ),
                    rx.button(
                        "Registrar Movimiento", 
                        on_click=lambda: AuthState.registrar_movimiento(
                            rx.get_client_value('tipo_activo'),
                            rx.get_client_value('descripcion_movimiento')
                        ),
                        width="full"
                    )
                ),
                width="md"
            ),
            spacing="4"
        ),
        rx.redirect("/login")  # Si no hay usuario autenticado
    )