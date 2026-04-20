# backend/app/api/v1/documents.py
from fastapi import APIRouter, UploadFile, File
from app.services.rag_singleton import rag_pipeline
from pypdf import PdfReader

router = APIRouter()


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    return text

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()

    texts = extract_text_from_pdf(file.file)

    rag_pipeline.add_documents(texts)

    return {"message": "Document processed successfully"}
