from pydantic import BaseModel,HttpUrl

class VideoDetailsInput(BaseModel):
    video_url: HttpUrl


    