"""Potala palace: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b03a227-7fcd-4b0d-8f9b-301b2e6d6f80'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/potala palace tibet_5b03a227-7fcd-4b0d-8f9b-301b2e6d6f80.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'potala-palace'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('potala', 'palace', 'tibet', 'lhasa', 'fortress', 'monastery', 'landmark', 'heritage')

    def build(self):
        # Plan: Preserve the terraced hillside palace with broader tiers; simplify the cramped narrow annex wall and finial while retaining the stepped roofline.

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
        poly('outline',(4,30),(8,16),(14,16),(16,8),(28,8),(30,16),(34,16),(36,24),(44,24),(44,36))
        line('central-roof',(14,16),(30,16));join('central-roof','outline')
        poly('terraces',(4,30),(14,30),(16,36),(24,36),(24,40),(34,40));join('terraces','outline')
        line('central-wall',(36,24),(36,36));join('central-wall','outline')
