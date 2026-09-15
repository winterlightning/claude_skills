'Drone: paired rotors, a symmetric flowing body and open landing struts.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '673c2bb4-20d5-46ea-9272-e82a19207dfb'
SOURCE_PATH = 'pictographic-primitives/technology/drone 1_673c2bb4-20d5-46ea-9272-e82a19207dfb.svg'
AUTHOR = 'gpt-6'

class Drone1(Solo48):
    icon_id = 'drone-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('drone', 'technology')

    def build(self):
        # Drone: tangent capsule body, equal rotors and clean landing struts joined at exact endpoints.
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

        r('body',4,16,44,30,7)
        for x in (12,36):
            l(f'rotor-{x}',(x-8,8),(x+8,8))
            l(f'arm-{x}',(x,8),(x,16))
            link('connect',f'arm-{x}',f'rotor-{x}')
            link('connect',f'arm-{x}','body')
        p('landing-left',(14,30),(10,40),(14,40))
        p('landing-right',(34,30),(38,40),(34,40))
        link('connect','landing-left','body')
        link('connect','landing-right','body')
