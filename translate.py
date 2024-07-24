import xml.etree.ElementTree as ET

from deep_translator import GoogleTranslator


def translate_strings(input_file, src_lang='en', dest_lang='vi'):
    translator = GoogleTranslator(source=src_lang, target=dest_lang)

    tree = ET.parse(input_file)
    root = tree.getroot()

    for string in root.findall('string'):
        original_text = string.text
        if original_text:
            if '@string/' in original_text:
                translated_text = original_text
                print(f"Keeping original text: '{original_text}'")
            else:
                translated_text = translator.translate(original_text)
                print(f"Translated '{original_text}' to '{translated_text}'")
            string.text = translated_text

    tree.write(f'translated_strings_{dest_lang}.xml', encoding='utf-8', xml_declaration=True)


file_input = 'strings.xml'
translate_strings(file_input)
