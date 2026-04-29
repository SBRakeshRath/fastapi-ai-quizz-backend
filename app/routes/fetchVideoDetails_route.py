from fastapi import APIRouter, HTTPException
from app.model.youtubeVideoDetails_input import VideoDetailsInput
from app.services.videoDetailExtractor_s import get_transcript


router = APIRouter()


@router.post("/fetch-video-details")
def fetch_video_details(video_details_input: VideoDetailsInput):
    video_url = video_details_input.video_url
    videoTranscript_result = get_transcript(video_url)
    print(videoTranscript_result)
    return {
        "video_url": video_url,
        "videoTranscript_result": videoTranscript_result
        
    }