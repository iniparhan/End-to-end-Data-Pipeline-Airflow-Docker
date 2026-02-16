import requests 
import json

from datetime import date

# import os
# from dotenv import load_dotenv
# load_dotenv(dotenv_path='./.env')
# API_KEY = os.getenv('API_KEY') 

from airflow.decorators import task
from airflow.models import Variable


API_KEY = Variable.get('API_KEY') 
CHANNEL_NAME = Variable.get('MrBeast')

max_result = 50

@task
def get_playlist_id():

    try:
        # https://developers.google.com/youtube/v3/docs/channels/list -> fill right section "APIs Explorer" based on step description page
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_NAME}&key={API_KEY}'

        response = requests.get(url)
        # print(response)           # for testing

        data = response.json()
        # print(json.dumps(data, indent=4))             # for testing

        channel_items = data["items"][0]
        channel_playlist_Id = channel_items["contentDetails"]["relatedPlaylists"]['uploads']
        # print(channel_playlist_Id)                # for testing

        return channel_playlist_Id

    except requests.exceptions.RequestException as e:
        raise e
    
    

@task
def get_video_id(playlist_id):
    '''
    This function still contain code for testing, list code or variabel that must to change:

    - Ganti `while` dengan `while True`
    - Un-Command baris kode `if not page_token`
    '''


    page_token = None
    video_id_list = []

    # for testing
    # Just set max page count to 2 
    max_page_count = 2
    page_count = 1

    try:
        while page_count <= max_page_count:
            url = 'https://youtube.googleapis.com/youtube/v3/playlistItems'
            params = {
                'part': 'contentDetails',
                'maxResults': max_result,
                'playlistId': playlist_id,
                'key': API_KEY,
                'pageToken': page_token
            }

            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            for item in data["items"]:
                video_id = item["contentDetails"]["videoId"]
                video_id_list.append(video_id)

            page_token = data.get("nextPageToken")

            # if not page_token:
            #     break

            page_count += 1             # for testing

        return video_id_list

    except requests.exceptions.RequestException as e:
        raise e
    

@task
def extract_video_data(video_id):

    extract_data = []

    def batch_list(video_id_list, batch_size):
        for video_id in range(0, len(video_id_list), batch_size):
            yield video_id_list[video_id : video_id + batch_size]

    try:

        for batch in batch_list(video_id, max_result):
            video_id_str = ",".join(batch)

            url = f'https://youtube.googleapis.com/youtube/v3/videos'
            params = {
                        'part': ['contentDetails', 'snippet', 'statistics'],
                        'id': video_id_str,
                        'key': API_KEY
                    }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
    
            for item in data.get('items', []):
                video_id = item['id']
                snippet = item['snippet']
                content_details = item['contentDetails']
                statistics = item['statistics']

                video_data = {
                    "video_id": video_id,
                    "title": snippet['title'],
                    "published_at": snippet['publishedAt'],
                    "duration": content_details['duration'],
                    "view_count": statistics.get('viewCount', None),
                    "like_count": statistics.get('likeCount', None),
                    "comment_count": statistics.get('commentCount', None)
                }

                extract_data.append(video_data)
                
        return extract_data

    except requests.exceptions.RequestException as e:
        raise e
    

@task
def save_to_json(extracted_data):
    file_path = f"./data/YT_data_{date.today()}.json"
    
    with open(file_path, "w", encoding="utf-8") as json_outfile:
        json.dump(extracted_data, json_outfile, indent=4, ensure_ascii=False)



def main():
    
    playlist_id = get_playlist_id()
    all_video_id = get_video_id(playlist_id)
    extract = extract_video_data(all_video_id)
    save_to_json(extract)
    
    print("Done!!")           # for testing  


if __name__ == "__main__":
    main()