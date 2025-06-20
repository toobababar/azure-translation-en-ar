from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key and region from environment variables
apikey = os.getenv("AZURE_TEXT_TRANSLATION_APIKEY")
region = os.getenv("AZURE_TEXT_TRANSLATION_REGION")

if not apikey or not region:
    raise ValueError("API key or region is not set in environment variables.")

# Initialize Azure Text Translation client
credential = AzureKeyCredential(apikey)
text_translator = TextTranslationClient(credential=credential, region=region)

def translate_text(from_language, to_language, text):
    try:
        # Prepare input text for translation
        from_language = "en"
        to_language = ["ar"]  # Arabic language code
        input_text_elements = [InputTextItem(text=text)]
        # Perform translation
        response = text_translator.translate(
            body=input_text_elements, 
            to_language=to_language, 
            from_language=from_language
        )
        translation = response[0] if response else None
        # Process and display translation results
        if translation:
            for translated_text in translation.translations:
                print(f"Translated to: '{translated_text.to}'")
                print(f"Translation Result: '{translated_text.text}'")
        else:
            print("No translation response received.")
    
    except HttpResponseError as exception:
        print("An error occurred during translation.")
        if exception.error:
            print(f"Error Code: {exception.error.code}")
            print(f"Message: {exception.error.message}")
        else:
            print(str(exception))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
            # Prompt user for input text
    user_text = input("Enter the text you want to translate: ")
            # Call the translate_text function with user input
    translate_text(from_language="en", to_language="ar", text=user_text)













