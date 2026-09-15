'Notepad: matched binder strokes, smooth paper corners and 8-unit top spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd23953b1-598e-4139-b842-25c8399f38c0'
SOURCE_PATH = 'pictographic-primitives/symbol/note_d23953b1-598e-4139-b842-25c8399f38c0.svg'
AUTHOR = 'gpt-6'

class Note(Solo48):
    icon_id = 'note'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('note', 'symbol')

    def build(self):
        # Notepad: matched binder strokes, smooth paper corners and 8-unit top spacing.
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

        r('paper',6,14,42,42,3)
        for x in (14,24,34):
            l(f'ring-{x}',(x,6),(x,18))
            link('connect',f'ring-{x}','paper')
