from __future__ import absolute_import

from django.utils.functional import cached_property

from wangeditor import utils


class DummyBackend(object):
    def __init__(self, storage_engine, file_object):
        self.file_object = file_object
        self.storage_engine = storage_engine

    def save_as(self, filepath):
        return self.storage_engine.save(filepath, self.file_object)

    @cached_property
    def is_image(self):
        return utils.is_valid_image_extension(self.file_object.name)

    @cached_property
    def is_video(self):
        return utils.is_valid_video_extension(self.file_object.name)

