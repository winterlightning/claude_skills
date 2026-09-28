'Train rear: balanced carriage, clear doorway and evenly spaced running gear.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31f4c1fc-6f7b-4695-b8a0-184b74be65a0'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad train back_31f4c1fc-6f7b-4695-b8a0-184b74be65a0.svg'
AUTHOR = 'gpt-6'

class TrainRearView(Solo48):
    icon_id = 'train-rear-view'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('train', 'rear', 'carriage', 'railway', 'back', 'wagon', 'rail', 'coach')

    def build(self):
        # Train rear: balanced carriage, clear doorway and evenly spaced running gear.
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

        r('carriage',8,4,40,34,6)
        p('door',(20,34),(20,20),(28,20),(28,34))
        link('connect','door','carriage')
        l('track',(8,44),(40,44))
        for x in (16,32):
            l(f'wheel-{x}',(x,34),(x,44))
            link('connect',f'wheel-{x}','carriage')
            link('connect',f'wheel-{x}','track')
