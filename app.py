# app.py 2 200324
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
from dash import dash_table
#from dash.dash_table.Format import Group
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

server = app.server
# Crear el DataFrame para almacenar los datos
df = pd.DataFrame(columns=['Documento', 'Item', 'Razon Social', 'Descuento Orden', 'Descuento Solicitud' 'Descripción Item', 'Cantidad', 'U.M', 'Precio Unitario Local', 'Valor Bruto Local', 'Bodega', 'Comprador', 'Linea', 'Sublinea', 'Descripcion Pais', 'Tipo de Inventario', 'Lote', 'Tasa local', 'Estado'])

app.layout = html.Div(children=[ 
    html.H1("Formulario Proveedores y Escritura en Excel", style={'color': 'blue', 'textAlign': 'center'}),
    
    #html.Label("Documento:"),
    dcc.Input(id='input-documento', type='text', value='', placeholder='Ingrese Documento'),
    
    #html.Label("Item:"),
    dcc.Input(id='input-item', type='text', value='', placeholder='Ingrese Item'),
    
    #html.Label("Razón social proveedor:"),
    dcc.Input(id='input-razon', type='text', value='', placeholder='Ingrese Razón Social'),
    
    #tml.Label("Docto. orden:"),
    dcc.Input(id='input-documentoorden', type='text', value='', placeholder='Ingrese Docto Orden'),

    #html.Label("Docto. solicitud:"),
    dcc.Input(id='input-documentosolicitud', type='text', value='', placeholder='Ingrese Docto Solicitud'),
    
    #html.Label("Desc. item:"),
    dcc.Input(id='input-descripcionitem', type='text', value='', placeholder='Ingrese Descripción Item'),
    
    #html.Label("Cantidad:"),
    dcc.Input(id='input-cantidad', type='number', value='', placeholder='Ingrese Cantidad'),
    
    #html.Label("U.M:"),
    dcc.Input(id='input-um', type='text', value='', placeholder='Ingrese U.M'),
   
    #html.Label("Precio unit. local:"),
    dcc.Input(id='input-preciounitlocal', type='number', value='', placeholder='Ingrese Precio Unitario Local'), 
   
    #html.Label("Valor bruto local:"),
    dcc.Input(id='input-valorbrutolocal', type='number', value='', placeholder='Ingrese Valor Bruto Local'),
    
    #html.Label("Bodega:"),
    dcc.Input(id='input-bodega', type='text', value='', placeholder='Ingrese Bodega'),
    
    #html.Label("Comprador:"),
    dcc.Input(id='input-comprador', type='text', value='', placeholder='Ingrese Nombre Comprador'),
    
    #html.Label("Linea:"),
    dcc.Input(id='input-linea', type='text', value='', placeholder='Ingrese Línea'),
    
    #html.Label("Sublinea:"),
    dcc.Input(id='input-sublinea', type='text', value='', placeholder='Ingrese Sublínea'),
    
    #html.Label("Desc. País:"),
    dcc.Input(id='input-descpais', type='text', value='', placeholder='Ingrese Descripción País'),
    
    #html.Label("Tipo Inventario:"),
    dcc.Input(id='input-tipoinventario', type='text', value='', placeholder='Ingrese Tipo Inventario'),
    
    #html.Label("Lote:"),
    dcc.Input(id='input-lote', type='text', value='', placeholder='Ingrese Lote'),
    
    #Label("Tasa Local:"),
    dcc.Input(id='input-tasalocal', type='text', value='', placeholder='Ingrese Tasa Local'),
    
    #html.Label("Estado:"),
    dcc.Input(id='input-estado', type='text', value='', placeholder='Ingrese Estado'),
    
    
    html.Button('Enviar Datos', id='submit-button', n_clicks=0, style={'background-color': 'Blue', 'color': 'white','margin': '9px', 'padding': '10px'}),
    html.Button('Exportar a Excel', id='export_btn', n_clicks=0, style={'background-color': 'Green', 'color': 'white', 'margin': '9px', 'padding': '10px'}),
    #html.Button('Limpiar Formulario', id='clear_btn', n_clicks=0),
    
    dash_table.DataTable(
        id='data_table',
        columns=[
            {'name': 'Documento', 'id': 'Documento'},
            {'name': 'Item', 'id': 'Item'},
            {'name': 'Razon', 'id': 'Razon'},
            {'name': 'Documento Orden', 'id': 'Documento Orden'},
            {'name': 'Documento Solicitud', 'id': 'Documento Solicitud'},
            {'name': 'Descripcion Item', 'id': 'Descripcion Item'},
            {'name': 'Cantidad', 'id': 'Cantidad'},
            {'name': 'U.M', 'id': 'U.M'},
            {'name': 'Precio Unitario Local', 'id': 'Precio Unit Local'},
            {'name': 'Valor Bruto Local', 'id': 'Valor Bruto Local'},
            {'name': 'Bodega', 'id': 'Bodega'},
            {'name': 'Comprador', 'id': 'Comprador'},
            {'name': 'Linea', 'id': 'Linea'},
            {'name': 'Sublinea', 'id': 'Sublinea'},
            {'name': 'Descripcion Pais', 'id': 'Desc Pais'},
            {'name': 'Tipo Inventario', 'id': 'Tipo Inventario'},
            {'name': 'Lote', 'id': 'Lote'},
            {'name': 'Tasa Local', 'id': 'Tasa Local'},
            {'name': 'Estado', 'id': 'Estado'},
        ],
        data=df.to_dict('records')),
    
    html.Div(id='output-message')
    
   
])

@app.callback(
    Output('data_table', 'data'),
    [Input('submit-button', 'n_clicks')],
    [State('input-documento', 'value'),
     State('input-item', 'value'),
     State('input-razon', 'value'),
     State('input-documentoorden', 'value'),
     State('input-documentosolicitud', 'value'),
     State('input-descripcionitem', 'value'),
     State('input-cantidad', 'value'),
     State('input-um', 'value'),
     State('input-preciounitlocal', 'value'),
     State('input-valorbrutolocal', 'value'),
     State('input-bodega', 'value'),
     State('input-comprador', 'value'),
     State('input-linea', 'value'),
     State('input-sublinea', 'value'),
     State('input-descpais', 'value'),
     State('input-tipoinventario', 'value'),
     State('input-lote', 'value'),
     State('input-tasalocal', 'value'),
     State('input-estado', 'value')]
)

def update_table(n_clicks, documento, item, razon, documentoorden, documentosolicitud, descripcionitem, cantidad, um, preciounitlocal, valorbrutolocal, bodega, comprador, linea, sublinea, descpais, tipoinventario, lote, tasalocal, estado):
    if n_clicks > 0:
        global df
        #df = df.append({'Nombre': input_nombre, 'Edad': input_edad, 'Correo': input_correo}, ignore_index=True)
        df = df.append({'Documento': documento, 'Item': item, 'Razon': razon, 'Documento Orden': documentoorden, 'Documento Solicitud': documentosolicitud, 'Descripcion Item': descripcionitem, 'Cantidad': cantidad, 'U.M': um, 'Precio Unit Local': [preciounitlocal], 'Valor Bruto Local': valorbrutolocal, 'Bodega': bodega, 'Comprador': comprador, 'Linea': linea, 'Sublinea': sublinea, 'Desc Pais': descpais, 'Tipo Inventario': tipoinventario, 'Lote': lote,'Tasa Local': tasalocal,'Estado': estado}, ignore_index=True)
        return df.to_dict('records')
    else:
        raise PreventUpdate 
        

@app.callback(
    #Output('submit_btn', 'n_clicks'),
    Output('output-message', 'children'),
    [Input('export_btn', 'n_clicks')],
    [State('input-documento', 'value'),
     State('input-item', 'value'),
     State('input-razon', 'value'),
     State('input-documentoorden', 'value'),
     State('input-documentosolicitud', 'value'),
     State('input-descripcionitem', 'value'),
     State('input-cantidad', 'value'),
     State('input-um', 'value'),
     State('input-preciounitlocal', 'value'),
     State('input-valorbrutolocal', 'value'),
     State('input-bodega', 'value'),
     State('input-comprador', 'value'),
     State('input-linea', 'value'),
     State('input-sublinea', 'value'),
     State('input-descpais', 'value'),
     State('input-tipoinventario', 'value'),
     State('input-lote', 'value'),
     State('input-tasalocal', 'value'),
     State('input-estado', 'value')]
)
def update_output(n_clicks, documento, item, razon, documentoorden, documentosolicitud, descripcionitem, cantidad, um, preciounitlocal, valorbrutolocal, bodega, comprador, linea, sublinea, descpais, tipoinventario, lote, tasalocal, estado):
    if n_clicks > 0:
        # Crear un DataFrame con los datos ingresados
        df = pd.DataFrame({'Documento': [documento], 'Item': [item], 'Razon social proveedor': [razon], 'Documento orden': [documentoorden], 'Documento solicitud': [documentosolicitud], 'Desc. item': [descripcionitem], 'Cantidad': [cantidad], 'U.M': [um], 'Precio Unit Local': [preciounitlocal], 'Valor Bruto Local': [valorbrutolocal], 'Bodega': [bodega], 'Comprador': [comprador], 'Linea': [linea], 'Sublinea': [sublinea], 'Desc Pais': [descpais], 'Tipo Inventario': [tipoinventario], 'Lote': [lote],'Tasa Local': [tasalocal],'Estado': [estado] })
        
        # Leer el archivo Excel existente (o crear uno si no existe)
        try:
            excel_data = pd.read_excel('datos.xlsx')
        except FileNotFoundError:
            excel_data = pd.DataFrame()

        # Concatenar el nuevo DataFrame con los datos existentes
        excel_data = pd.concat([excel_data, df], ignore_index=True)

        # Escribir los datos en el archivo Excel
        excel_data.to_excel('datos.xlsx', index=False)
        
        return f'Datos enviados y escritos en el archivo Excel. ¡Gracias!'
    else:
        return ''
        
if __name__ == '__main__':
    app.run_server(debug=True)    
    #app.run_server()
