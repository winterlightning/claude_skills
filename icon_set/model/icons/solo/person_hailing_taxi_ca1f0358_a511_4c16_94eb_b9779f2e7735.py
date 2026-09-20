'Person Hailing Taxi.\nPlan: Detached head above standing torso with one raised arm, beside small front taxi with roof sign. Head gap4; minor lamps omitted. Bounds6..42.\nReference: human_ref/full_body_ref.png: equal detached head spacing; Lucide car-front: roof/cabin/body stack.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca1f0358-a511-4c16-94eb-b9779f2e7735'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/taxi wave_ca1f0358-a511-4c16-94eb-b9779f2e7735.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-hailing-taxi'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('person', 'hailing', 'taxi')

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

        circle('head',10,10,4)
        self.add_line('torso',(10,22),(10,32));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('legs',(6,42),(10,32),(14,42));self.relate('connect','legs','torso')
        self.add_polyline('arms',(6,30),(10,22),(18,22),(24,8));self.relate('connect','arms','torso')
        self.add_polyline('car',(26,30),(31,22),(39,22),(42,30),(42,38),(40,38),(28,38),(26,38),closed=True)
        self.add_line('hood',(26,30),(42,30));self.relate('connect','hood','car')
        self.add_polyline('sign',(31,22),(31,14),(39,14),(39,22));self.relate('connect','sign','car')
        for x in (28,40):self.add_line(f'tire-{x}',(x,38),(x,42));self.relate('connect',f'tire-{x}','car')
