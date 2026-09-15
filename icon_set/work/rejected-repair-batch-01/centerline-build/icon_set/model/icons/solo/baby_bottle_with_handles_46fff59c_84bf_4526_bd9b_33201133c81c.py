from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46fff59c-84bf-4526-bd9b-33201133c81c'
SOURCE_PATH = 'pictographic-primitives/babies/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg'
AUTHOR = 'gpt-6'

class BabyBottleWithHandles(Solo48):
    icon_id = 'baby-bottle-with-handles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby-care'
    aliases = ()
    keywords = ('bottle', 'handles', 'baby', 'milk', 'feeding', 'sippy', 'teat', 'infant')

    def build(self) -> None:
        # Diagonal feeding bottle with two physical handles. Each handle owns
        # its cardinal lobes; its endpoints share the bottle's diagonal seams.
        # SQUARE centerline extrema: (6,6)-(42,42).
        def contour(name, start, pieces, closed=False):
            members = []
            point = start
            for index, (end, radii) in enumerate(pieces):
                member = f'{name}-{index}'
                if radii:
                    rx, ry, sweep = radii
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                else:
                    self.add_line(member, point, end)
                members.append(member)
                point = end
            self.add_contour(name, *members, closed=closed)
        contour('bottle', (6, 28), [
            ((6, 34), None), ((14, 42), (8, 8, False)),
            ((24, 42), None), ((26, 40), None), ((40, 26), None),
            ((24, 10), None), ((10, 24), None),
            ((6, 28), None)], True)
        contour('teat', (24, 10), [
            ((34, 6), None), ((38, 6), None), ((42, 10), (4, 4, True)),
            ((42, 14), None), ((40, 26), None)])
        # Radius-10 circles use exact 6-8-10 attachment vectors.
        self.add_arc('handle-left', (10, 24), (24, 10), radius_x=10, large_arc=True)
        self.add_arc('handle-right', (40, 26), (26, 40), radius_x=10)
        for part in ('teat', 'handle-left', 'handle-right'):
            self.relate('connect', 'bottle', part)
