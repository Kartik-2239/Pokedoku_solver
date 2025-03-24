from google import genai
from PIL import Image
import io
import base64
import time

def get_text(cropped_image,client):
    
    # Converting PIL Image to base64
    buffer = io.BytesIO()
    cropped_image.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()
    base64_image = base64.b64encode(image_bytes).decode('utf-8')
    
    # Using inline_data approach which is most reliable
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            "get only text from the image continuously if they are at a particular location together and seperate them by ','",
            {"inline_data": {"mime_type": "image/jpeg", "data": base64_image}}
        ]
    )
    
    return response.text

def get_questions(s):

    print("Raw text from OCR:", s)
    
    s = s.split(',')
    l1 = []
    l2 = []
    for i in range(3):
        l1.append(s[i])
        l2.append(s[i+3])
    main_list = []
    for i in l1:
        for j in l2:
            main_list.append((i,j))
    return main_list