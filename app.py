from flask import Flask, send_from_directory
from routes.auth import auth_bp
from routes.characters import characters_bp
from routes.events import events_bp
#  导入新增的蓝图 
from routes.relationships import relationships_bp
from routes.statistics import statistics_bp

app = Flask(__name__, static_folder='static', static_url_path='')

# 1. 注册所有路由（蓝图）
app.register_blueprint(auth_bp)
app.register_blueprint(characters_bp)
app.register_blueprint(events_bp)
#  注册新增的蓝图 
app.register_blueprint(relationships_bp)
app.register_blueprint(statistics_bp)

# 2. 配置页面路由
@app.route('/')
def root():
    return send_from_directory('static', 'login.html')

@app.route('/<path:path>')
def static_files(path):
    # 确保所有html文件都能被正确访问
    if path.endswith('.html'):
        return send_from_directory('static', path)
    return send_from_directory('static', path)

if __name__ == '__main__':
    print("系统启动中... 请访问 http://127.0.0.1:5000")
    app.run(debug=True, port=5000)