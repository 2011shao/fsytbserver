import os
from googleapiclient.discovery import build
# 设置API密钥
api_key = os.environ['YOUTOBE']
# 创建YouTube API服务
youtube = build('youtube', 'v3', developerKey=api_key)


def get_video_info(video_url):
  try:
    # 从视频链接中提取视频ID
    video_id = video_url.split('=')[1]
    # 你的 API 调用代码
    # 使用视频ID获取视频信息
    video_info = youtube.videos().list(part='snippet,statistics',
                                       id=video_id).execute()

    # 提取所需信息
    snippet = video_info['items'][0]['snippet']
    statistics = video_info['items'][0]['statistics']
    # 输出信息
    print(f"视频名称: {video_info}")
    print(f"视频名称: {snippet['title']}")
    print(f"播放量: {statistics['viewCount']}")
    print(f"评论数: {statistics['commentCount']}")
    print(f"点赞数: {statistics['likeCount']}")

  except Exception as e:
    print(f"An error occurred: {e}")
