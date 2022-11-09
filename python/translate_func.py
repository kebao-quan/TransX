# _*_ coding: utf-8 _*_
"""
Time:     11 Oct 2022
Author:   Yiding Wang
File:     translate_func.py
"""


import deepl
import six
from google.cloud import translate_v2 as translate
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/kyoma/transx-364516-6f75b84dc8b5.json"


def deepl_translate(target, content):
    # https://pypi.org/project/deepl

    auth_key = "b9eb9e4b-f53a-a5ab-09c0-f02e15950f0a:fx"
    translator = deepl.Translator(auth_key)

    result = translator.translate_text(content, target_lang=target)
    # support target: https://www.deepl.com/docs-api/translate-text/?utm_source=github&utm_medium=github-python-readme

    return result.text


def google_translate(target, content):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    support target: https://cloud.google.com/translate/docs/languages
    """

    translate_client = translate.Client()

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(content, target_language=target)

    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result["translatedText"]


