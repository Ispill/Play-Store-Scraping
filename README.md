<p align="center">
    <img src="./assets/google_play_logo.png" alt="Playstore Logo" title="Playstore" width=500>
</p>

<h1 align="center">Google Play Store Web Scraping</h1>

<hr>

Este repositorio presenta el análisis de datos realizado sobre un dataset de aplicaciones de la Google Play Store. El enfoque principal es la visualización de estos datos para permitir la identificación de correlaciones y la derivación de conclusiones sobre las diferentes categorías de aplicaciones.

![Headers](./assets/Headers.png "Headers del dataset")

## Limpieza de los datos

En la limpieza se llevó a cabo simplemente aplicando la función
~~~
data_frame.dropna()
~~~
con la finalidad de borrar todos los valores *`Null`* o *`NaN`* que se pudieran encontrar dentro del dataset.

La cantidad de datos antes de realizar la limpieza fueron un total de 10,841 filas. Posterior a la limpieza nos quedamos con un total de 9,360 datos ya limpios y listos para utilizarse.

### Datos antes y después de la limpieza
<table>
    <tr>
        <th>Datos sin limpiar</th>
        <th>Datos limpios</th>
    </tr>
    <tr>
        <td><img src="./assets/B_clean.png"></td>
        <td><img src="./assets/A_clean.png"></td>
    </tr>
</table>

## Transformación de los datos
Para la transformación de los datos, para graficar ciertos datos como lo son los datos de la columna *`Rating`*, se normalizaron los datos para que los valores fueran modulos de entre 0.5 y 1 estrella entera.

### Datos antes y después de la normalización de la columna *Rating*
<table>
    <tr>
        <th>Datos sin normalizar</th>
        <th>Datos normalizados</th>
    </tr>
    <tr>
        <td><img src="./assets/Not_Normalized_rating.png"></td>
        <td><img src="./assets/Normalized_rating.png"></td>
    </tr>
</table>

Trabajo ejecutado y testeado sobre *`Python 3.12.4`*.
