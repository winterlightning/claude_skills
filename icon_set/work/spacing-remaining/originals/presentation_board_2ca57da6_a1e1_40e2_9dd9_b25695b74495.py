'Presentation board: even header band, rounded board and a symmetric tripod.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ca57da6-a1e1-40e2-9dd9-b25695b74495'
SOURCE_PATH = 'icons-json/office/presentation board_2ca57da6-a1e1-40e2-9dd9-b25695b74495.json'
AUTHOR = 'gpt-6'

class PresentationBoard(Solo48):
    icon_id = 'presentation-board-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'board', 'office')

    def build(self):
        # Presentation board: even header band, rounded board and a symmetric tripod.
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

        r('board',6,6,42,30,3)
        l('header',(6,14),(42,14))
        link('connect','header','board')
        l('stem',(24,30),(24,42))
        p('legs',(14,42),(24,30),(34,42))
        link('connect','stem','board')
        link('connect','legs','board')
        link('connect','legs','stem')
