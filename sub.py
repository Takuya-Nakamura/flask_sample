from flask import Flask, Blueprint

sub_module = Blueprint("sub_module", __name__)


@sub_module.route("/sub/")
def main_sub():
    return "Hello, World!"


@sub_module.route("/sub/<name>")
def hello_name_sub(name):
    return "Hello, {}".format(name)
