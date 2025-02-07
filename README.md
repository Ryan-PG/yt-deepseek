# YT DeepSeek Overview

## Overview
This project is for a YT video that you can find the link bellow. This repository contains a **PDF Summarizer** that extracts text from uploaded PDF files and generates a summarized translation in Persian. It provides two options for summarization:
- Using an **API-based model** (DeepSeek-R1-Distill-Qwen-32B via Hugging Face Inference API)
- Using a **local model** (DeepSeek-R1:8B via Ollama)

The application is built with **Streamlit** to provide a user-friendly interface for uploading PDFs and viewing summaries.

## Tutorial Video
A tutorial video demonstrating how to use this project is available. You can find it in the repository or watch it online:
[![Watch the tutorial](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)


## Features
- Extracts text from PDF files
- Summarizes extracted text
- Translates the summary into Persian
- Allows switching between a local model and an API-based model
- Uses **Streamlit** for an interactive UI

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip
- [Hugging Face Hub](https://huggingface.co/docs/huggingface_hub/index)
- [Ollama](https://ollama.com)
- Streamlit

### Setup
Clone the repository and navigate to the project directory:
```sh
git clone https://github.com/yourusername/pdf-summarizer.git
cd pdf-summarizer
```

Create a virtual environment and activate it:
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

### Run the Streamlit App
```sh
streamlit run main.py
```

### How to Use
1. Upload a PDF file.
2. Choose whether to use the local model or the API model.
3. Click the **GO** button to extract and summarize the text.
4. The summarized translation will be displayed.

## Configuration
To use the **Hugging Face API**, you need to provide an API key in `main.py`. Replace:
```python
api_key='YOUR API KEY'
```
with your own `Hugging Face API key`.

## Project Structure
```
📦 yt-deepseek
├── Files/              
    ├── DeepSeek_V3.pdf
    ├── DeepSeek_Slides.pdf
├── main.py             
├── DeepSeek_V3.pdf       
├── DeepSeek.Slides.pdf       
├── .gitignore          
└── README.md           
```

## Dependencies
This project uses the following Python libraries:
- `huggingface_hub`
- `pdfplumber`
- `langchain_community`
- `streamlit`

Install dependencies using:
```sh
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## Author
[Ryan Heida](https://github.com/Ryan-PG)

