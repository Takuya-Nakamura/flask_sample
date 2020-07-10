from flask import *  # 必要なライブラリのインポート
from sub import sub_module

app = Flask(__name__)  # アプリの設定
app.register_blueprint(sub_module)  # blueprint


@app.route("/")  # どのページで実行する関数か設定
def main():
    # return "Hello, World!"  # Hello, World! を出力
    # templatesフォルダは記載しなくてよい
    param = {'name': "takuya_para,", 'age': 100}
    return render_template("index.html", name="takuya", age=20, param=param)


@app.route("/<name>")
def hello_name(name):
    return "Hello, {}".format(name)


if __name__ == "__main__":  # 実行されたら
    # デバッグモード、localhost:8888 で スレッドオンで実行
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
