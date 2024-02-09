from flask import Blueprint, render_template
from models.language_model import LanguageModel

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
