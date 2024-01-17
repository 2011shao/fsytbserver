import os
from googleapiclient.discovery import build
api_key = 'AIzaSyDki3M1XufmBDy8Vq-87VCNpo6OUCKk91M'
youtube = build('youtube', 'v3', developerKey=api_key)
url = "https://www.youtube.com/watch?v=VIDEO_ID"
def get_video_info(video_url, is_commentl):
  try:
    if video_url is None or ('youtube.com' not in video_url):
      return {"code": 1, "errMsg": "video url error"}
    video_id = video_url.split('=')[1]
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
