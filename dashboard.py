import openai
import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd

# Configura la clau d'API d'OpenAI
openai.api_key = "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"  # Substitueix amb la teva clau d'API

# Flask i Dash
from flask import Flask
server = Flask(__name__)  # Aquí defines el servidor Flask
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Carrega les dades
file_path = "fully_expanded_funds_with_weights.csv"
data = pd.read_csv(file_path)

# Layout de l'aplicació
app.layout = html.Div([
    html.H1("Gestor Patrimonial IA", style={'textAlign': 'center'}),
    
    # Selecciona els fons
    html.Div([
        html.Label("Selecciona Fons:"),
        dcc.Checklist(
            id='fons-checklist',
            options=[{'label': row['Nom'], 'value': row['ISIN']} for _, row in data.iterrows()],
            value=[data['ISIN'][0]],  # Selecciona el primer fons per defecte
            inline=True
        )
    ], style={'width': '80%', 'margin': 'auto'}),
    
    # Gràfics
    dcc.Graph(id='sector-chart'),
    dcc.Graph(id='company-chart'),
    
    # Assistent IA
    html.Div([
        html.H2("Assistent Patrimonial", style={'textAlign': 'center'}),
        dcc.Textarea(
            id='user-input',
            placeholder="Escriu una pregunta sobre com gestionar el teu patrimoni...",
            style={'width': '100%', 'height': '100px'}
        ),
        html.Button('Enviar', id='submit-button', n_clicks=0),
        html.Div(id='assistant-response', style={'marginTop': '20px', 'border': '1px solid #ccc', 'padding': '10px'})
    ], style={'width': '80%', 'margin': 'auto', 'marginTop': '20px'})
])

# Callback per als gràfics
@app.callback(
    Output('sector-chart', 'figure'),
    Output('company-chart', 'figure'),
    Input('fons-checklist', 'value')
)
def update_charts(selected_funds):
    if len(selected_funds) == 0:
        return px.pie(title="No hi ha fons seleccionats"), px.bar(title="No hi ha fons seleccionats")
    
    selected_data = data[data['ISIN'].isin(selected_funds)]
    # Gràfic de sectors
    sectors = selected_data[[
        'Sector_Tecnologia', 'Sector_Salut',
        'Sector_Consum_Discrecional', 'Sector_Finances',
        'Sector_Comunicacio'
    ]].sum()
    sectors_df = pd.DataFrame({'Sector': sectors.index.str.replace('Sector_', ''), 'Presència': sectors.values})
    sector_chart = px.pie(sectors_df, names='Sector', values='Presència', title="Distribució de Sectors")
    
    # Gràfic d'empreses
    companies = selected_data.filter(like='Empresa_').sum()
    companies_df = pd.DataFrame({'Empresa': companies.index.str.replace('Empresa_', ''), 'Pes (%)': companies.values})
    company_chart = px.bar(companies_df, x='Empresa', y='Pes (%)', title="Pes de les Empreses")
    
    return sector_chart, company_chart

# Callback per a l'assistent
@app.callback(
    Output('assistant-response', 'children'),
    Input('submit-button', 'n_clicks'),
    State('user-input', 'value'),
    State('fons-checklist', 'value')
)
def assist_user(n_clicks, user_input, selected_funds):
    if n_clicks > 0 and user_input:
        # Processar dades seleccionades
        selected_data = data[data['ISIN'].isin(selected_funds)]
        sectors = selected_data[[
            'Sector_Tecnologia', 'Sector_Salut',
            'Sector_Consum_Discrecional', 'Sector_Finances',
            'Sector_Comunicacio'
        ]].sum().to_dict()
        companies = selected_data.filter(like='Empresa_').sum().to_dict()
        
        # Genera un prompt personalitzat per OpenAI
        prompt = f"""
        Ets un assessor patrimonial expert. Analitza el següent portafoli:
        Sectors: {sectors}
        Empreses: {companies}
        Pregunta de l'usuari: {user_input}
        Respon amb estratègies per balancejar, diversificar o millorar aquest patrimoni.
        """
        
        try:
            # Utilitza la nova API de `openai`
            response = openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Ets un expert en gestió patrimonial. Ajuda l'usuari a millorar el seu portafoli."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error al processar la consulta: {str(e)}"
    return "Espera una consulta de l'usuari."

# Executa l'aplicació
if __name__ == '__main__':
    app.run_server(debug=True)