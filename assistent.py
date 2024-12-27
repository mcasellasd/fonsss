import openai

# Configura la clau d'API d'OpenAI
openai.api_key = "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"  # Substitueix amb la teva clau real

# Funció per a cada assistent
def investigacio_isin(isin):
    messages = [
        {"role": "system", "content": "Ets un assistent que investiga informació de fons d'inversió basats en el seu ISIN."},
        {"role": "user", "content": f"ISIN: {isin}. Proporciona dades com: nom del fons, distribució sectorial, distribució geogràfica, rendiment històric, etc."}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=200
    )
    return response.choices[0].message["content"].strip()

def valoracio_fons(info_fons):
    messages = [
        {"role": "system", "content": "Ets un assistent que valora qualitativament i quantitativament un fons d'inversió."},
        {"role": "user", "content": f"Fons d'inversió a analitzar: {info_fons}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=200
    )
    return response.choices[0].message["content"].strip()

def resposta_preguntes(info_fons, pregunta):
    messages = [
        {"role": "system", "content": "Ets un assistent que respon preguntes sobre fons d'inversió basant-te en informació proporcionada."},
        {"role": "user", "content": f"Informació del fons: {info_fons}\nPregunta: {pregunta}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=150
    )
    return response.choices[0].message["content"].strip()

def integrar_informacio(info_fons, valoracio, resposta):
    messages = [
        {"role": "system", "content": "Ets un assistent que integra informació sobre fons d'inversió en un informe estructurat."},
        {"role": "user", "content": f"Informació del fons: {info_fons}\nValoració: {valoracio}\nResposta a les preguntes: {resposta}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=300
    )
    return response.choices[0].message["content"].strip()

# Flux de treball
isin = "LU0171307068"
info_fons = investigacio_isin(isin)
valoracio = valoracio_fons(info_fons)
pregunta = "És adequat per a inversors conservadors?"
resposta = resposta_preguntes(info_fons, pregunta)
informe_final = integrar_informacio(info_fons, valoracio, resposta)

# Mostra l'informe final
print("Informe Final:")
print(informe_final)