"""airplane-other: Airliner · top view; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH = 'pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'
AUTHOR = 'gpt-6'

class AirplaneOther(Solo48):
    icon_id = 'airplane-other'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'airplane-other')

    def build(self):
        # Plan: An upright aircraft constructed about one axis: broaden swept wing bands and the tailplane, with a rounded nose and exact mirrored nodes.

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
        right=[(28,10),(28,12),(42,20),(42,30),(28,22),(28,32),(36,42),(24,42)]
        mirror=lambda p:(48-p[0],p[1])
        commands=[('L',p) for p in right[1:]]+[('L',mirror(p)) for p in reversed(right[:-1])]+[('A',(28,10),4,4,True)]
        path('airframe',right[0],commands,True)
