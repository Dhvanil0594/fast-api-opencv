from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from ..services import detect_services as _DS
from config.config import settings
from io import BytesIO
from PIL import Image

router = APIRouter(prefix="/fruit-detection")

@router.post("/detect_fruit_image")
async def detect_fruit_image(file: UploadFile = File(...)):
    try:
        # Read the uploaded image file
        img_bytes = await file.read()
        
        # Open the image using Pillow
        img = Image.open(BytesIO(img_bytes))
        
        # Make prediction
        predicted_class_label = _DS.predict_image(img)
        
        # Return the predicted label as a JSON response
        return JSONResponse(content={"predicted_class": predicted_class_label})
    
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})