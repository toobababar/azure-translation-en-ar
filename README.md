# English-to-Arabic Translation Engine (Azure Text trnslation SDK)

A Python-based translation engine that converts English text into Arabic using the Azure Text Translation SDK. Designed for integration into business workflows, content localization pipelines, or multilingual communication systems, this engine provides fast, reliable, and scalable translation.

## Features

- Translates English text into Arabic using Azure Cognitive Services
- Supports `.env` configuration for secure API key handling
- Easy setup with `requirements.txt`
- Clean and minimal Python script

## Use Cases

- Automate multilingual support for web and mobile platforms.
- Streamline content localization for marketing or documentation.
- Enable customer support messaging in Arabic without manual translation.
- Serve as a backend translation module in larger AI/NLP pipelines.

## Requirements

- Python 3.7+
- Azure Translator resource (API Key + Region)
- Virtual environment (optional but recommended)

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/toobababar/azure-translation-en-ar.git
   cd azure-translation-en-ar

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows


3. **Install dependencies**

   ```bash
   pip install -r requirements.txt

4. **Add your Azure credentials**
   Create a .env file in the root folder with the following keys:

   ```bash
   AZURE_TRANSLATOR_KEY=your-key-here
   AZURE_TRANSLATOR_REGION=your-region-here

5. **Run the script**

   ```bash
   en-to-ar.py

## Example

### Input

    
    "Hello, how are you?"

### Output

    
                                                                                                                        "مرحبًا، كيف حالك؟"  

## Security

Your API keys are stored securely using a .env file. Be sure not to commit your real .env file to GitHub.

## License

This project is licensed under the Apache License 2.0.
See the LICENSE file for more information.
