class ImageReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        raise NotImplementedError


class GIFReader(ImageReader):
    def read(self):
        pass


class JPEGReader(ImageReader):
    def read(self):
        pass


class PNGReader(ImageReader):
    def read(self):
        pass


def get_image_reader(path):
    # [1, 2, 3]
    #  0  1  2
    # -3 -2 -1
    _, extension = path.rsplit('.', 1)
    # if extension == 'png':
    #     reader = PNGReader
    # elif extension == 'gif':
    #     reader = GIFReader
    # elif extension in ('jpeg', 'jpg'):
    #     reader = JPEGReader
    # else:
    #     raise ValueError('unsupported format')
    #
    # return reader(path)
    try:
        return {
            'png': PNGReader,
            'gif': GIFReader,
            'jpg': JPEGReader,
            'jpeg': JPEGReader,
        }[extension](path)
    except KeyError:
        raise ValueError('unsupported format')


if __name__ == '__main__':
    reader = get_image_reader('some.tiff')
    # assert isinstance(reader, JPEGReader)
    reader.read()
    