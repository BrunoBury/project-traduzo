from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

language_controller = Blueprint("language_controller", __name__)


@language_controller.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )


@language_controller.route("/", methods=["POST"])
def post_index():
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]

    translator = GoogleTranslator(source=translate_from, target=translate_to)

    translated = translator.translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/reverse", methods=["POST"])
def post_reverse():
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]

    reversed_translate_from = translate_to
    reversed_translate_to = translate_from

    translator = GoogleTranslator(source=translate_from, target=translate_to)

    translated = translator.translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translated=text_to_translate,
        translate_from=reversed_translate_from,
        translate_to=reversed_translate_to,
    )
