import reflex as rx
import hashlib

class AuthState(rx.State):
    usuarios: dict = {}
    usuario_actual: dict = {}
    error_login: str = ""
    error_registro: str = ""

    def registrar_usuario(self, username: str, password: str, email: str):
        # Validaciones básicas
        if not username or not password or not email:
            self.error_registro = "Todos los campos son obligatorios"
            return

        if username in self.usuarios:
            self.error_registro = "El usuario ya existe"
            return

        # Hashear contraseña (de manera simple)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Guardar usuario
        self.usuarios[username] = {
            "username": username,
            "password": hashed_password,
            "email": email,
            "movimientos": []
        }
        
        # Limpiar error
        self.error_registro = ""
        
        # Redirigir a login
        return rx.redirect("/login")

    def login(self, username: str, password: str):
        # Hashear contraseña para comparación
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Verificar credenciales
        if (username in self.usuarios and 
            self.usuarios[username]["password"] == hashed_password):
            # Guardar usuario actual
            self.usuario_actual = self.usuarios[username]
            self.error_login = ""
            return rx.redirect("/dashboard")
        
        # Error de login
        self.error_login = "Credenciales inválidas"

    def logout(self):
        self.usuario_actual = {}
        return rx.redirect("/login")

    def registrar_movimiento(self, tipo_activo: str, descripcion: str):
        if not self.usuario_actual:
            return

        movimiento = {
            "tipo_activo": tipo_activo,
            "descripcion": descripcion,
            "fecha": rx.get_client_time()
        }

        self.usuarios[self.usuario_actual['username']]['movimientos'].append(movimiento)
        return rx.redirect("/dashboard")