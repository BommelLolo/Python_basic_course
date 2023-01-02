import json


class JsonParser:
    """Context manager is parsing json object to python object."""
    def __init__(self, data: str):
        self.data = data

    def __enter__(self):
        return json.loads(self.data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Point:
    """Creates a point on 2D-surface."""
    def __init__(self, x_coord, y_coord):
        self._coord = (x_coord, y_coord)

    def __getitem__(self, index):
        return self._coord[index]


class Rectangle:
    """Creates a rectangular on 2D-surface. Its sides are parallel to the axes."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, point):
        """Checks location of the point inside rectangular"""
        if self.start[0] <= point[0] <= self.end[0] and self.start[1] <= point[1] <= self.end[1]:
            print(f"Point ({point[0]}, {point[1]}) is INside rect")
            return True
        print(f"Point ({point[0]}, {point[1]}) is OUTside rect")
        return False


if __name__ == '__main__':

    with JsonParser('"hello"') as res:
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res == {"hello": "world", "key": [1, 2, 3]}

    with JsonParser('""') as res:
        assert res == ""

    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)

    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
    assert rect.contains(Point(5, 3))
    assert rect.contains(Point(7, 0))
    assert rect.contains(Point(5, 1.5))
    assert rect.contains(end_point)
    assert rect.contains(Point(1, 3))
