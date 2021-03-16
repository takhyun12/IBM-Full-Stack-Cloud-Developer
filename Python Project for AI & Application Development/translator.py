from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class Translation:
    """ Main Class """
    def __init__(self):
        """ input(english) -> print(french) """
        authenticator = IAMAuthenticator('JDVKmKj3gLvbwQAVuHJWrvMD4n4YuCmjCLG28740j-dP')
        self.language_translator = LanguageTranslatorV3(
            version='2021-03-16',
            authenticator=authenticator
        )
        self.language_translator.set_service_url(
            'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/1b2ac512-fc0e-4960-bf35-ffe5380de3a1')

    def englishtofrench(self, english_input):
        """ input(english) -> return(french) """
        translation_result = self.language_translator.translate(
            text=english_input,
            model_id='en-fr').get_result()
        french_output = translation_result['translations'][0]['translation']
        return french_output

    def englishtogerman(self, english_input):
        """ input(english) -> return(german) """
        if english_input == "" or english_input is None:
            return ""
        translation_result = self.language_translator.translate(
            text=english_input,
            model_id='en-de').get_result()
        german_output = translation_result['translations'][0]['translation']
        return german_output

if __name__ == '__main__':
    """ This is Main function """
    ENGLISH = "Hello, My name is TackHyun Jung"
    german = Translation().englishtogerman(ENGLISH)
    print(german)
