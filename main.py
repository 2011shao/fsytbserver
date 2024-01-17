from flask import Flask, render_template, request, jsonify
from ytb import get_video_info
from flask_cors import CORS
app = Flask('app')
CORS(app)
@app.route('/')
def hello_world():
  video_url = request.args.get('video_url')
  is_comment = request.args.get('comment', 'false').lower() == 'true'
  video_dic = get_video_info(video_url, is_comment)
  return jsonify(video_dic)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
