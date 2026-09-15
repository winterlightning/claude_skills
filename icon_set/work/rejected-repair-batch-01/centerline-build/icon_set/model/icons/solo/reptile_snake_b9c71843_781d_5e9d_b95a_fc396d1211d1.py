'Slithering snake: coherent rounded turns with a broad body and a clearly separated tail.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9c71843-781d-5e9d-b95a-fc396d1211d1'
SOURCE_PATH = 'pictographic-primitives/animals/reptile snake_b9c71843-781d-5e9d-b95a-fc396d1211d1.svg'
AUTHOR = 'gpt-6'


class SlitheringSnake(Solo48):
    icon_id = 'slithering-snake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('snake', 'slither', 'serpent', 'reptile', 'zigzag', 'coil', 'python', 'wild')

    def build(self):
        # Slithering snake: a single flowing S-shaped body and rounded head, replacing overlapping cramped coils.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        r('head',32,6,42,14,4)
        l('upper',(32,10),(15,10))
        a('left-turn',(15,10),(15,24),9,7,sweep=False)
        l('middle',(15,24),(33,24))
        a('right-turn',(33,24),(33,42),9)
        l('tail',(33,42),(15,42))
        self.add_contour('body','upper','left-turn','middle','right-turn','tail')
        link('connect','head','body')
