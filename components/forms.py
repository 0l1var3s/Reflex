import reflex as rx
from activos_management.state.auth import AuthState

def login_form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Nombre de usuario",
                id="username_login",
                required=True
            ),
            rx.input(
                placeholder="Contraseña", 
                type="password",
                id="password_login",
                required=True
            ),
            rx.button(
                "Iniciar Sesión", 
                type="submit",
                width="full"
            ),
            rx.text(AuthState.error_login, color="red")
        ),
        on_submit=lambda form_data: AuthState.login(
            form_data['username_login'], 
            form_data['password_login']
        )
    )

def registro_form():
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Nombre de usuario",
                id="username_registro",
                required=True
            ),
            rx.input(
                placeholder="Correo electrónico", 
                type="email",
                id="email_registro",
                required=True
            ),
            rx.input(
                placeholder="Contraseña", 
                type="password",
                id="password_registro",
                required=True
            ),
            rx.button(
                "Registrarse", 
                type="submit",
                width="full"
            ),
            rx.text(AuthState.error_registro, color="red")
        ),
        on_submit=lambda form_data: AuthState.registrar_usuario(
            form_data['username_registro'], 
            form_data['password_registro'],
            form_data['email_registro']
        )
    )