from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse as urlparse
from urllib.parse import parse_qs


def extract_video_id(video_url):
    video_url = str(video_url)
    if "youtu.be" in video_url:
        return video_url.split("/")[-1]
    elif "youtube.com" in video_url:
        parsed_url = urlparse.urlparse(video_url)
        return parse_qs(parsed_url.query).get("v")[0]
    return None

def get_transcript(video_url):
    try:
        video_id = extract_video_id(video_url)
        if not video_id:
            return {
                "error": "Could not extract video ID from the provided URL.",
                "transcript": None,
                "status": "error"
            }
        transcript_list = YouTubeTranscriptApi().list(video_id)
        available_languages = [t.language_code for t in transcript_list]
        transcriptObj = None
        
        if ("en" in available_languages):
            transcriptObj = transcript_list.find_transcript(['en'])
        else:
            transcriptObj = next(iter(transcript_list))
        
        
        
        transcript = transcriptObj.fetch()
        
        

        return {
            "full_text": " ".join([entry['text'] for entry in transcript.to_raw_data()]),
            "transcript": transcript.to_raw_data(),
            "transcript_language": transcript.language_code,
            "status": "success",
            
        }
    except Exception as e:
        return {
            "error": str(e),
            "transcript": None,
            "status": "error"
        }