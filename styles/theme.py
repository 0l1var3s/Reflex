import reflex as rx

# Definir un tema personalizado
def theme():
    return {
        "colors": {
            "primary": {
                "50": "#e6f1ff",
                "100": "#b3d7ff",
                "500": "#007bff",
                "900": "#004080"
            },
            "gray": {
                "50": "#f9fafb",
                "100": "#f3f4f6",
                "200": "#e5e7eb"
            }
        },
        "fonts": {
            "body": "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif"
        },
        "styles": {
            "global": {
                "body": {
                    "bg": "gray.50",
                    "color": "gray.900"
                }
            }
        }
    }

# Aplicar tema personalizado
def apply_theme(app):
    app.theme = theme()
    return app