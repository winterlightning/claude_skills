"""Handmade bag (hobbies), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6623581c-aaba-513b-8ed5-306d094d6b6b'
SOURCE_PATH = 'pictographic-primitives/hobbies/handmade bag_6623581c-aaba-513b-8ed5-306d094d6b6b.svg'
AUTHOR = 'gpt-6'

class HandmadeBag(Solo48):
    icon_id = 'handmade-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('handmade', 'bag', 'hobbies')

    def build(self):
        # Plan: Lucide shopping-bag: rounded body and symmetric dome handle joined at the rim; remove cramped dangling handle ends.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('body',(12,16), [('L',(14,16)),('L',(34,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,20)),('A',(12,16),4,4,True)],True)
        path('handle',(14,16), [('L',(14,14)),('A',(34,14),10,10,True),('L',(34,16))])
        join('body','handle')
