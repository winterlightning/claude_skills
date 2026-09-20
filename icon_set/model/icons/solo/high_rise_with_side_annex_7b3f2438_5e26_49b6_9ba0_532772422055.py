'Modern City Skyscraper.\nPlan: Tall stepped tower, two floor seams and shorter right annex. Ground shared; minor floor repetitions omitted. Bounds8,4..40,44.\nReference: Lucide building-2: stepped building mass and sparse repeated floors.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b3f2438-5e26-49b6-9ba0-532772422055'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/high rise_7b3f2438-5e26-49b6-9ba0-532772422055.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'high-rise-with-side-annex'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('high', 'rise', 'with', 'side', 'annex')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('tower',(10,44),(10,32),(10,22),(10,12),(16,12),(24,12),(28,12),(28,22),(28,30),(28,32),(28,44))
        self.add_polyline('roof-block',(16,12),(16,4),(24,4),(24,12));self.relate('connect','roof-block','tower')
        self.add_polyline('annex',(28,30),(38,30),(38,44));self.relate('connect','annex','tower')
        self.add_polyline('ground',(8,44),(10,44),(28,44),(38,44),(40,44));self.relate('connect','ground','tower');self.relate('connect','ground','annex')
        for y in (22,32):self.add_line(f'floor-{y}',(10,y),(28,y));self.relate('connect',f'floor-{y}','tower')
