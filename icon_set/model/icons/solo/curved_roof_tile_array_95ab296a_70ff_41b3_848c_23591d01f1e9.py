"""Curved Roof Tile Array
Plan: Three columns of arched roof tiles with shared seams; perspective is intentional.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Perspective flattened to a rectangular tile array; three columns and three arch rows retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95ab296a-70ff-41b3-848c-23591d01f1e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/material tile roof_95ab296a-70ff-41b3-848c-23591d01f1e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-roof-tile-array'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('roof', 'tiles', 'roofing', 'architecture', 'building', 'clay')

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
        self.add_polyline('roof',(6,42),(6,6),(42,6),(42,42))
        for x in (18,30):self.add_line(f'seam-{x}',(x,6),(x,42));self.relate('connect',f'seam-{x}','roof')
        for y in (18,30,42):
         path(f'tiles-{y}',(6,y),[('C',(18,y),(10,y-4),(15,y-4)),('C',(30,y),(21,y-4),(27,y-4)),('C',(42,y),(33,y-4),(38,y-4))])
         for s in ('roof','seam-18','seam-30'):self.relate('connect',f'tiles-{y}',s)
