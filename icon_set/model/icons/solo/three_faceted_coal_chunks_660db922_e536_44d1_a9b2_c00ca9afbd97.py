"""Three Faceted Coal Chunks
Plan: Three touching irregular coal chunks with angular face division.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '660db922-e536-44d1-a9b2-c00ca9afbd97'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/coal_660db922-e536-44d1-a9b2-c00ca9afbd97.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-faceted-coal-chunks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('coal', 'chunks', 'rocks', 'pile', 'facets', 'fuel', 'mineral')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        self.add_polyline('upper',(16,20),(18,6),(28,6),(36,18),(28,26),(16,20),closed=True)
        self.add_polyline('left',(6,32),(10,22),(16,20),(28,26),(24,42),(12,42),(6,32),closed=True)
        self.add_polyline('right',(28,26),(36,18),(42,26),(40,40),(24,42),closed=True)
        for a,b in [('upper','left'),('upper','right'),('left','right')]:self.relate('connect',a,b)
        self.add_polyline('facet',(6,32),(17,34),(24,42));self.relate('connect','facet','left')
