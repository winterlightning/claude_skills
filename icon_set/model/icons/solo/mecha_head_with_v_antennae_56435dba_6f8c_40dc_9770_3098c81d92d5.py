'Futuristic Mecha Robot Head.\nSymbol plan: V antenna spans(6,6)-(42,18), joined by stem to rounded angular face at y24. Short side ear strokes and a single mouth dot at(24,33) retain robot cues; visor detail simplified.\nConstruction reference: Lucide bot: geometric face with ears and minimal facial marks; original V crest retained.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56435dba-6f8c-40dc-9770-3098c81d92d5'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-09/robot war crime gundam_56435dba-6f8c-40dc-9770-3098c81d92d5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'mecha-head-with-v-antennae'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('mecha', 'head', 'with', 'v', 'antennae')

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

        self.add_polyline('crest',(6,6),(24,18),(42,6))
        path('face',(10,24),[(18,24),(24,24),(30,24),(38,24),(38,30),(38,34),((30,42),8,8,True),(18,42),((10,34),8,8,True),(10,30),(10,24)],True)
        self.add_line('stem',(24,18),(24,24))
        self.relate('connect','crest','stem')
        self.relate('connect','face','stem')
        self.add_dot('mouth',(24,33))
        for j,(x,z) in enumerate(((6,10),(42,38))):
            self.add_line(f'ear-{j}',(x,30),(z,30))
            self.relate('connect',f'ear-{j}','face')
