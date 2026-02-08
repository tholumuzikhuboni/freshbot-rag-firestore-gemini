from vertexai.generative_models import GenerativeModel, HarmCategory, HarmBlockThreshold
from config import GENERATIVE_MODEL_NAME

gen_model = GenerativeModel(
    GENERATIVE_MODEL_NAME,
    generation_config={"temperature": 0}
)

def ask_gemini(question, context):
    # Safety settings required for food safety content (knives/heat)
    safety_settings = {
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH
    }

    prompt = f"""
    You are FreshBot, a food safety expert. Answer the question using ONLY the context provided. 
    If the answer is not in the context, say "I'm sorry, I don't have that information in the food safety manual."

    Context:
    {context}

    Question:
    {question}
    """

    response = gen_model.generate_content(prompt, safety_settings=safety_settings)
    return response.text
