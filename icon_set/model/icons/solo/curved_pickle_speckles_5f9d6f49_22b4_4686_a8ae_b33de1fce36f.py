"""Curved Pickle with Speckles
Plan: Broad curved pickle with sparse speckles.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bean: curved continuous organic outline.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f9d6f49-22b4-4686-a8ae-b33de1fce36f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pickle_5f9d6f49-22b4-4686-a8ae-b33de1fce36f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-pickle-speckles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pickle', 'cucumber', 'vegetable', 'food', 'curved', 'speckles')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('pickle',(14,42),[('A',(6,34),8,8,True),('C',(18,21),(6,27),(13,26)),('C',(32,6),(23,17),(25,6)),('A',(42,16),10,10,True),('C',(14,42),(42,29),(29,42))],True)
        for i,p in enumerate([(18,32),(29,27),(33,15)]):self.add_dot(f'speckle-{i}',p)
