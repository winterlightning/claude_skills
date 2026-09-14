'PIN field: even entry spacing, smooth frame and an upright cursor.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b20c9046-7a9a-4d0f-a1fe-aec5c42fd4d8'
SOURCE_PATH = 'pictographic-primitives/symbol/keycode_b20c9046-7a9a-4d0f-a1fe-aec5c42fd4d8.svg'
AUTHOR = 'gpt-6'


class PinCodeField(Solo48):
    icon_id = 'pin-code-field'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('pin', 'code', 'password', 'input', 'field', 'keycode', 'passcode', 'security')

    def build(self):
        # PIN field: even entry spacing, smooth frame and an upright cursor.
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

        r('field',4,8,44,40,4)
        for x in (14,24):
            l(f'digit-{x}',(x,28),(x+1,28))
        l('cursor',(34,18),(34,30))
