import os
from googleapiclient.discovery import build
import re

api_key = os.environ['YOUTOBE']
youtube = build('youtube', 'v3', developerKey=api_key)
url = "https://www.youtube.com/watch?v=VIDEO_ID"

def extract_video_id(video_url):
    # 使用正则表达式从视频链接中提取视频ID
    video_id_match = re.search(r'[?&]v=([a-zA-Z0-9_-]+)', video_url)
    if video_id_match:
        return video_id_match.group(1)

    # 如果是短链接，使用 /shorts/ 后的部分作为视频ID
    shorts_match = re.search(r'/shorts/([a-zA-Z0-9_-]+)', video_url)
    if shorts_match:
        return shorts_match.group(1)

    return None
def get_video_info(video_url, is_commentl):
  try:
    video_id = extract_video_id(video_url)

    if not video_id:
      return {"code": 1, "errMsg": "video url error"}
    video_info = youtube.videos().list(part='snippet,statistics',
                                       id=video_id).execute()
    comments = []
    if is_commentl:
      comments_response = youtube.commentThreads().list(
          part='snippet,replies',
          videoId=video_id,
          textFormat='plainText',
          maxResults=50).execute()

      for comment_item in comments_response['items']:
        comment = comment_item['snippet']['topLevelComment']['snippet']
        comment_info = {
            'author_name': comment['authorDisplayName'],
            'comment_text': comment['textDisplay'],
            'comment_time': comment['publishedAt']
        }
        comments.append(comment_info)
    return {"code": 0, "errMsg": "", "data": video_info, "comments": comments}

  except Exception as e:
    print(f"An error occurred: {e}")
    return {"code": 2, "errMsg": '3'}
