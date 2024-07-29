import warnings
import whisper
from subprocess import CalledProcessError

warnings.filterwarnings('ignore')

base_model = whisper.load_model('base')

def audiototext(filepath):
    """
    Args: Audio file path.
    Supports: wav, mp3, flac
    """
    try:
        result = base_model.transcribe(filepath)
        return result['text']
    except FileNotFoundError:
        return 'File not found error: The specified file does not exist.'
    except CalledProcessError:
        return 'CalledProcessError: An error occurred while processing the file with ffmpeg.'
    except Exception as e:
        return f'An unexpected error occurred: {str(e)}'