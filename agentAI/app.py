import gradio as gr
from google import genai


GEMINI_API_KEY = "AIzaSyD42VVCll6N1HG8z-dP3svDnkICNFEUT8U"
model = "gemini-2.5-pro"

client = genai.Client(
    api_key=GEMINI_API_KEY,
)

def gemini_agent(question):
    if client is None:
        return "Verique a chave da api."
    
    question = question.strip()
    
    if not question:
        return "Por favor, digite novamente!"
    

    try:
        response = client.models.generate_content(
            model=model, contents=question
        )
        return response.text
    except Exception as err:
        return f"Houve um erro ao consultar o {model}.\n Erro: {err}"
    


interface = gr.Interface(
    fn=gemini_agent,
    title="Seja bem vindo! Acesse nossa IA Boladona 🦾.",
    description="Pergunte o que quiser.",
    inputs=gr.Textbox(lines=10, label="Faça sua pergunta!"),
    outputs=gr.Textbox(lines=10, label="Resposta da nossa IA Boladona"),

    flagging_mode="auto"
)

interface.launch(share=True)
