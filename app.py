# -*- coding: utf-8 -*-
"""Formulario_Preprocesar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WOmV3pQSlK_MkNG0L06SJT7nyn1PS5Pd
"""

#pip install dash pandas openpyxl plotly dash-table scikit-learn xlrd gunicorn  dash-core-components dash-html-components dash-bootstrap-components

import dash
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
#import numpy as np
import joblib

# Crear la aplicación Dash
app = dash.Dash(__name__)

server = app.server

#from sklearn.preprocessing import LabelEncoder
#cargar datos con extesion csv o cualquier tipo como excel, json, MySQL, etc
#df = pd.read_excel("Archivo_comparativo28042024Todos.xlsx")
df = pd.read_excel("Archivo_comparativo30042024TodosCampos.xlsx")

# Opciones para el menú desplegable
documentos = df['RazonSocial'].unique()

# Layout con un menú desplegable, un botón, y una tabla para mostrar datos relacionados
app.layout = html.Div([
    html.H1('Formulario para predecir el Tipo de Proveedores Actuales', style={'text-align': 'center', 'color': '#007bff', 'font-family': 'Arial, sans-serif'}),
    dcc.Dropdown(
        id='document-dropdown',
        options=[{'label': doc, 'value': doc} for doc in documentos],
        placeholder='Selecciona una Razón Social y presiona Predecir.'
    ),
    html.Button("Predecir", id='predict-button', n_clicks=0),
    dash_table.DataTable(
        id='selected-data',
        columns=[{'name': col, 'id': col} for col in df.columns],  # Configuración de columnas
        data=[],  # Datos vacíos inicialmente
        style_table={'overflowX': 'auto'}
    ),
    html.Div(id='prediction-result')  # Para mostrar el resultado de la predicción
])

@app.callback(
    Output('selected-data', 'data'),  # Actualizar los datos de la tabla
    [Input('document-dropdown', 'value')]  # Escuchar la selección del menú desplegable
)
def mostrar_datos(documento_seleccionado):
    if documento_seleccionado:
        # Filtrar el DataFrame para obtener datos del documento seleccionado
        df_filtrado = df[df['RazonSocial'] == documento_seleccionado].copy()
        
        # Seleccionar las columnas que no empiezan con "Pre"
        #columnas_a_mostrar = [columna for columna in df_filtrado.columns if not columna.startswith('Pre')]
    
        # Obtener los datos correspondientes a las columnas seleccionadas y borrarlos
        #datos = df_filtrado[columnas_a_mostrar].to_dict('records')
        
        # Identificar las columnas que comienzan con "Pre"
        #columnas_a_eliminar = [col for col in df_filtrado.columns if col.startswith("Pre")]

        # Eliminar las columnas identificadas
        #df_filtrado.drop(columnas_a_eliminar, axis=1, inplace=True)
        
        # Eliminar la columna "Documento"
        #df_filtrado.drop('Documento', axis=1, inplace=True)  # Eliminar la columna
        
        # Eliminar las primeras 3 letras de cada nombre de columna
        #df.columns = df_filtrado.columns.str.slice(3)

        # Convertir a formato compatible con `dash_table.DataTable`
        #return datos
        return df_filtrado.to_dict('records')  # Devuelve como lista de diccionarios
    
    return []

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

def predecir_data(data):
    # Simular una predicción con el modelo cargado
    modelo = joblib.load('Modelo_KNN_Ordinal_Entrenado.pkl')  # Carga tu modelo entrenado
    resultado = modelo.predict(data)  # Predicción sobre datos preprocesados
    
    if resultado[0] == 1:
        return "El proveedor es Bueno."
    elif resultado[0] == 2:
        return "El proveedor es Malo."
    else:
        return f"Resultado desconocido: {resultado[0]}."

@app.callback(
    Output('prediction-result', 'children'),  # Para mostrar el resultado de la predicción
    [Input('predict-button', 'n_clicks')],
    [State('document-dropdown', 'value')]  # Para obtener el documento seleccionado
)
def predecir(n_clicks, documento_seleccionado):
    if n_clicks > 0 and documento_seleccionado:
        # Filtrar el DataFrame para obtener datos relacionados con el documento seleccionado
        df_filtrado = df[df['RazonSocial'] == documento_seleccionado].copy()  # Copiar para evitar cambios en el original
        
        # Eliminar las columnas originales que no se usan para predecir
        df_filtrado.drop('Documento', axis=1, inplace=True)  # Eliminar la columna
        df_filtrado.drop('Item', axis=1, inplace=True)
        df_filtrado.drop('RazonSocial', axis=1, inplace=True)
        df_filtrado.drop('DoctoOrden', axis=1, inplace=True)
        df_filtrado.drop('DoctoSolicitud', axis=1, inplace=True)
        df_filtrado.drop('DescItem', axis=1, inplace=True)
        df_filtrado.drop('Cantidad', axis=1, inplace=True)
        df_filtrado.drop('UM', axis=1, inplace=True)
        df_filtrado.drop('PrecioUnitLocal', axis=1, inplace=True)
        df_filtrado.drop('ValorBrutoLocal', axis=1, inplace=True)
        df_filtrado.drop('Fecha', axis=1, inplace=True)
        df_filtrado.drop('Bodega', axis=1, inplace=True)
        df_filtrado.drop('Comprador', axis=1, inplace=True)
        df_filtrado.drop('LINEA', axis=1, inplace=True)
        df_filtrado.drop('SUBLINEA', axis=1, inplace=True)
        df_filtrado.drop('DescPais', axis=1, inplace=True)
        df_filtrado.drop('TipoInventario', axis=1, inplace=True)
        df_filtrado.drop('Lote', axis=1, inplace=True)
        df_filtrado.drop('TasaLocal', axis=1, inplace=True)
        df_filtrado.drop('Estado', axis=1, inplace=True)
        
        # Llamar a la función de predicción
        resultado = predecir_data(df_filtrado)  # Pasar los datos sin las columnas originales anteriores
        
        return resultado
    
    return ""

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)