"""Personal Watercraft. Left-facing riderless craft retains handlebar, stepped seat and bow; omit decorative waves.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide caravan: coherent side silhouette and tangent quarter-circle stern. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a399a9e-7cbc-42d5-93cf-c819c7a3329e'
SOURCE_PATH = 'pictographic-primitives/recreation/jet ski_0a399a9e-7cbc-42d5-93cf-c819c7a3329e.svg'
AUTHOR = 'gpt-6'


class PersonalWatercraft(Solo48):
    icon_id = 'personal-watercraft'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('personal', 'watercraft')

    def build(self):
        # Plan: A broad deck band, smooth stern and exact seat/post attachment replace the pinched diagonal deck; preserve the raised handle and open hull ends.

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
        poly('post',(4,36),(12,20),(18,8),(24,8))
        path('shell',(12,20), [('L',(20,20)),('L',(26,26)),('L',(36,26)),('A',(44,34),8,8,True),('L',(44,36)),('C',(42,40),(44,38),(43,39))]);join('post','shell')
        line('deck',(4,36),(44,36));line('hull',(4,36),(12,40));join('deck','post');join('deck','shell');join('hull','post');join('hull','deck')
