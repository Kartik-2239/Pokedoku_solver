from PIL import Image
from google import genai
from google.genai import types
import time




def get_answers(arr,client):
    temp = []
    for i in arr:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[f"give me only the exact name of one pokemon that strictly satisfies both {i[0]} and {i[1]}"])
        s =  response.text
        temp.append(s)
        time.sleep(4)
    return temp