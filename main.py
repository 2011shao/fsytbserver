from flask import Flask, render_template, request, jsonify
from ytb import get_video_info

app = Flask('app')


@app.route('/')
def hello_world():
  print('你好')
  video_url = request.args.get('video_url')
  video_dic = get_video_info(video_url)
  print(video_url)
  return jsonify(video_dic)
  # render_template(
  #     'index.html',
  #     user_id=request.headers['X-Replit-User-Id'],
  #     user_name=request.headers['X-Replit-User-Name'],
  #     user_roles=request.headers['X-Replit-User-Roles'],
  #     user_bio=request.headers['X-Replit-User-Bio'],
  #     user_profile_image=request.headers['X-Replit-User-Profile-Image'],
  #     user_teams=request.headers['X-Replit-User-Teams'],
  #     user_url=request.headers['X-Replit-User-Url'])


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
