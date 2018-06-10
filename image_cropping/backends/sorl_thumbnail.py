from sorl.thumbnail.engines.convert_engine import EngineError
from sorl.thumbnail.images import ThumbnailError
from sorl.thumbnail.parsers import ThumbnailParseError
from sorl.thumbnail import get_thumbnail

from .base import ImageBackend


class SorlThumbnailBackend(ImageBackend):
    exceptions_to_catch = (EngineError, ThumbnailError, ThumbnailParseError, IOError, OSError)

    def get_thumbnail_url(self, image_path, thumbnail_options):
        geometry_string = '{}x{}'.format(thumbnail_options['size'][0], thumbnail_options['size'][1])

        thumb = get_thumbnail(
            image_path,
            geometry_string,
            cropbox=thumbnail_options['box'],
            upscale=thumbnail_options['upscale']
        )
        return thumb.url

    def get_size(self, image):
        return image.size
