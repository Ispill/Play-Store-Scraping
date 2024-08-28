# Playstore Web Scraping
En este repositorio se mostrará el análisis de datos que se le realizó a un dataset sobre aplicaciones de la Playstore de Google. Principalmente se enfatizará la visualización de dichos datos para poder realizar correlaciones y llegar a conclusiones acerca de cada categoria de dichas aplicaciones.

![Headers](/assets/Headers.png "Headers del dataset")

## Limpieza de los datos
En la limpieza se llevó a cabo simplemente aplicando la función
~~~
data_frame.dropna()
~~~
con la finalidad de borrar todos los valores *`Null`* o *`NaN`* que se pudieran encontrar dentro de el dataset.

La cantidad de datos antes de realizar la limpieza fueron un total de 10,841 filas. Posterior a la limpieza nos quedamos con un total de 9,360 datos ya limpios y listos para utilizarse.

### Datos antes y después de la limpieza
<table>
    <tr>
        <th>Datos sin limpiar</th>
        <th>Datos limpios</th>
    </tr>
    <tr>
        <td><img src="/assets/B_clean.png"></td>
        <td><img src="/assets/A_clean.png"></td>
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
        <td><img src="/assets/Not_Normalized_rating.png"></td>
        <td><img src="/assets/Normalized_rating.png"></td>
    </tr>
</table>

Trabajo ejecutado y testeado sobre *`Python 3.12.4`*.
