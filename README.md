# English to Arabic Translator using Azure Text Translation SDK

This is a simple Python application that uses the **Azure Text Translation SDK** to translate English text into Arabic. It leverages Azure's powerful AI translation capabilities and is ideal for experimenting with cloud-based NLP.

## Features

- Translates English text into Arabic using Azure Cognitive Services
- Supports `.env` configuration for secure API key handling
- Easy setup with `requirements.txt`
- Clean and minimal Python script

## Requirements

- Python 3.7+
- Azure Translator resource (API Key + Region)
- Virtual environment (optional but recommended)

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/toobababar/azure-translation-en-ar.git
   cd azure-english-arabic-translator

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

    ```bash
    "Hello, how are you?"

### Output

    ```bash
                                                                                                                        "مرحبًا، كيف حالك؟"  

## Security

Your API keys are stored securely using a .env file. Be sure not to commit your real .env file to GitHub.

## License

This project is licensed under the Apache License 2.0.
See the LICENSE file for more information.
