from google_play_scraper import app

def get_app_details(package_name):
    try:
        app_details = app(
            package_name,
            lang="es",
            country="cl"
        )

        app_data = {
            'Nombre App': app_details['title'],
            'Categoría de la App': app_details['genre'],
            'Rating de la App': app_details.get('score', 'N/A'),
            'Cantidad de Reviews de la App': app_details.get('ratings', 'N/A'),
            'Cantidad de instalaciones/descargas de la App': app_details.get('installs', 'N/A'),
            'Tipo de App al que pertenece': 'Paid' if app_details['free'] is False else 'Free',
            'Precio de la App': app_details.get('price', '0'),
            'Público al que está dirigido': app_details.get('contentRating', 'N/A'),
            'Género de la App': app_details.get('genre', 'N/A'),
            'Última actualización de la App': app_details.get('updated', 'N/A'),
            'Versión actual de la App': app_details.get('version', 'N/A'),
        }

        return app_data
    
    except Exception as e:
        print(f"Error al obtener los detalles de la app: {e}")
        return None

# Ejemplo de uso haciendo web scraping de la app Whatsapp
package_name = 'com.whatsapp'  # Reemplaza con el package name de la app que deseas analizar
app_info = get_app_details(package_name)

if app_info:
    for key, value in app_info.items():
        print(f'{key}: {value}')
