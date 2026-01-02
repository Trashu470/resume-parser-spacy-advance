import spacy
import pdfplumber
from docx import Document
import os
import json
import sys


try:
    nlp = spacy.load("./resume_parser_trf_2025_final")ो
    print(" Custom NER Model loaded successfully!\n")
except Exception as e:
    print(f" Error loading model: {e}")
    print("Make sure the model folder is in the root directory.")
    sys.exit(1)

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    
    if ext == ".pdf":
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print(f"PDF reading error: {e}")
            return ""
            
    elif ext in [".docx", ".doc"]:
        try:
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
        except Exception as e:
            print(f"DOCX reading error: {e}")
            return ""
            
    elif ext == ".txt":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"TXT reading error: {e}")
            return ""
    
    else:
        print(" Unsupported file format. Use PDF, DOCX, or TXT.")
        return ""
    
    return text

def parse_resume(file_path):
    print(f" Processing: {os.path.basename(file_path)}")
    text = extract_text(file_path)
    
    if not text.strip():
        print("  No text extracted from the resume.")
        return {}
    
    doc = nlp(text)
    
    labels = ["Person", "Degree", "College", "Experience", "Skills", "Ctc", "Org", "Location", "Certification", "Email", "Phone"]
    result = {label: [] for label in labels}
    
    for ent in doc.ents:
        if ent.label_ in result:
            result[ent.label_].append(ent.text.strip())
    
    for key in result:
        result[key] = list(set([item for item in result[key] if item]))
    
    return result

if __name__ == "__main__":
    print(" AI-Powered Resume Parser (88% Accuracy)\n")
    
    path = input("Enter resume file path (PDF/DOCX/TXT): ").strip().strip('"\'')
    
    if not os.path.exists(path):
        print(" File not found! Please check the path.")
    else:
        data = parse_resume(path)
        if data:
            print("\n Extraction Complete!\n")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
            
            output_file = "parsed_output.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\n Results saved to {output_file}")
        else:
            print("\n  No data extracted. Try another resume.")
