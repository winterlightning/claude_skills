"""Peacock Head with Broad Crest
Plan: Broad crest, small beak and tall peacock neck
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide bird contour principles.
Reduction: Remove eye; retain broad crest and narrow neck."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e818ba-d5c0-428b-965b-c68e132721e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/peacock head_d6e818ba-d5c0-428b-965b-c68e132721e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'peacock-head-broad-crest'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('peacock', 'bird', 'head', 'crest', 'beak', 'neck')

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
        path('head',(12,44),[('C',(18,22),(22,38),(18,30)),('L',(8,12)),('C',(24,4),(10,4),(18,4)),('L',(30,14)),('L',(40,20)),('L',(32,26)),('L',(30,44))])
