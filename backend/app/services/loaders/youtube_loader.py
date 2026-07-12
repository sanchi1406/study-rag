from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled
)


def get_video_id(url: str) -> str:
    """
    Extract YouTube video ID.
    """

    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    if parsed.hostname in (
        "www.youtube.com",
        "youtube.com"
    ):
        return parse_qs(parsed.query)["v"][0]

    raise ValueError("Invalid YouTube URL")


def load_youtube(url: str) -> str:
    """
    Extract transcript from a YouTube video.
    """

    video_id = get_video_id(url)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id,
            languages=["en"]
        )

    except (NoTranscriptFound, TranscriptsDisabled):
        raise ValueError(
            "Transcript not available for this video."
        )

    text = " ".join(
        item["text"]
        for item in transcript
    )

    return text