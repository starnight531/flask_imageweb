from flask import Flask

app = Flask(__name__, 
            template_folder="../templates",
            static_folder="../assets",
            static_url_path="/assets")
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

# import 先将导入内容全部加载一遍,先有app,后执行xxxx_routes
from routes import user_routes