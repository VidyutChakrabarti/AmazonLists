import pytest
import asyncio
from pathlib import Path
import os
from unittest.mock import Mock, patch
from video_processor import VideoProcessor, TokenBucket

@pytest.fixture
def google_api_key():
    return os.getenv('GOOGLE_API_KEY', 'test_key')

@pytest.fixture
async def processor(google_api_key):
    with patch('os.path.exists', return_value=True):
        return VideoProcessor(google_api_key)

@pytest.fixture
def sample_video_path():
    return Path("test_data/sample.mp4")

@pytest.mark.asyncio
async def test_token_bucket():
    bucket = TokenBucket(tokens_per_second=1, max_tokens=2)
    assert await bucket.acquire()
    assert await bucket.acquire()
    assert not await bucket.acquire()

@pytest.mark.asyncio
async def test_video_download(processor):
    with patch('video_processor.VideoProcessor._download_with_ytdl', return_value=True):
        result = await processor.download_video("https://example.com/video")
        assert result is not None
        assert isinstance(result, Path)

@pytest.mark.asyncio
async def test_audio_extraction(processor, sample_video_path):
    with patch('librosa.load', return_value=(Mock(), 16000)):
        waveform, sr = await processor._extract_audio(sample_video_path)
        assert waveform is not None
        assert sr == 16000

@pytest.mark.asyncio
async def test_frame_extraction(processor, sample_video_path):
    mock_frame = Mock()
    with patch('cv2.VideoCapture') as mock_cap:
        mock_cap.return_value.read.return_value = (True, mock_frame)
        mock_cap.return_value.get.return_value = 100
        
        frames = await processor._extract_frames(sample_video_path, num_frames=3)
        assert len(frames) == 3

@pytest.mark.asyncio
async def test_frame_analysis(processor):
    mock_frame = Mock()
    with patch('google.generativeai.GenerativeModel.generate_content') as mock_generate:
        mock_generate.return_value.text = "Test description"
        description = await processor._analyze_frame(mock_frame)
        assert description == "Test description"

@pytest.mark.asyncio
async def test_process_video(processor):
    with patch.multiple(processor,
        download_video=Mock(return_value=Path("test.mp4")),
        _extract_audio=Mock(return_value=(Mock(), 16000)),
        _transcribe_audio=Mock(return_value="Test transcription"),
        _extract_frames=Mock(return_value=[Mock()]),
        _analyze_frames=Mock(return_value=["Frame description"]),
        _generate_description=Mock(return_value="Final description")):
        
        result = await processor.process_video("https://example.com/video")
        assert result['status'] == 'success'
        assert 'final_description' in result

@pytest.mark.asyncio
async def test_error_handling(processor):
    with patch('video_processor.VideoProcessor.download_video', side_effect=Exception("Test error")):
        result = await processor.process_video("https://example.com/video")
        assert result['status'] == 'error'
        assert 'message' in result

def test_initialization_error():
    with patch('os.path.exists', return_value=False):
        with pytest.raises(RuntimeError):
            VideoProcessor("test_key")
