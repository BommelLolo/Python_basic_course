class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def fits(self, peg):
        return self.radius >= peg.radius


class RoundPeg:
    def __init__(self, radius):
        self.radius = radius


class SquarePeg:
    def __init__(self, side):
        self.side = side


class SquareToRoundPegAdapter(RoundPeg):
    def __init__(self, peg):
        self.peg = peg

    @property
    def radius(self):
        return self.peg.side


if __name__ == '__main__':
    round_peg = RoundPeg(3)
    round_hole = RoundHole(4)

    assert round_hole.fits(round_peg)

    square_peg = SquarePeg(7)
    assert not round_hole.fits(SquareToRoundPegAdapter(square_peg))
    assert round_hole.fits(SquareToRoundPegAdapter(SquarePeg(3)))
