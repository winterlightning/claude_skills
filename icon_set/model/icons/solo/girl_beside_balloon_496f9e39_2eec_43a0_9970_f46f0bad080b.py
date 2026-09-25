'Girl with Balloon.\nPlan: Detached round head above a simple dress and two feet, with round balloon and short string. Bounds6..42.\nReference: human_ref/full_body_ref.png: circular head, exactly4 ink clearance; Lucide balloon: simple rounded balloon and string.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '496f9e39-2eec-43a0-9970-f46f0bad080b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/girl ballon_496f9e39-2eec-43a0-9970-f46f0bad080b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'girl-beside-balloon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('girl', 'beside', 'balloon')

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

        circle('head',14,14,4)
        self.add_line('torso',(14,26),(14,28));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('dress',(14,28),(6,38),(10,38),(18,38),(22,38),(14,28));self.relate('connect','dress','torso')
        for x in (10,18):self.add_line(f'foot-{x}',(x,38),(x,42));self.relate('connect',f'foot-{x}','dress')
        circle('balloon',35,13,7)
        self.add_line('string',(35,20),(35,28));self.relate('connect','balloon','string')
