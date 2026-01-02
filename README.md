# 📄 AI-Powered Resume Parser & Entity Extractor (88% Accuracy)

A high-performance NLP-based system that automates extraction of key information from unstructured resumes (PDF/DOCX/TXT). Built using custom NER with Transformer architecture, this model achieves **88% success rate** across diverse resume formats.

Developed & maintained by **Trashu**.

---

## 🎯 Key Features

Extracts **11 critical entities** with high precision:

| Category       | Entities                          |
|----------------|-----------------------------------|
| Personal       | Name, Email, Phone, Location      |
| Professional   | Organization, Experience, Skills, CTC |
| Academic       | Degree, College, Certifications   |

- Supports multiple input formats: **PDF, DOCX, TXT**
- Fast inference with optimized Transformer-based NER
- Easy to integrate into HR pipelines

---

## 🚀 Performance

- **Overall Success Rate**: 88% (tested on 500+ real-world resumes)
- Model: Fine-tuned Transformer NER
- Lightweight & production-ready

---

## 📥 Important: Model Download

GitHub limits file size to 100MB. The trained model (~485MB) is hosted externally.

👉 [**Download Trained Model from Google Drive**](https://drive.google.com/drive/folders/1iUGFAbzPf94bvskv625uAGbJUA6z9ImT?usp=sharing)

**Instructions**:
1. Download the model folder
2. Place it in the root directory of this project

---

## 🛠️ Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/Trashu/resume-parser-spacy-advance.git
cd resume-parser-spacy-advance

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the parser
python main.py
Upload a resume when prompted, and get structured JSON output!

👤 Author
Trashu
AI/ML Developer | NLP Enthusiast
If you find this project helpful, please give it a ⭐ – it means a lot!

📝 Future Improvements (Planned)

Add support for image-based resumes (via OCR)
Web UI with Streamlit/Gradio
Multi-language resume support

Contributions welcome! 🚀
