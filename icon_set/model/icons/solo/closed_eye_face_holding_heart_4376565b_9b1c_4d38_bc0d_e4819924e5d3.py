"""Closed Eye Face Holding Heart
Plan: Round face with closed eyes holding a heart between two hands.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide heart: paired lobes and pointed lower tip.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4376565b-9b1c-4d38-bc0d-e4819924e5d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emoji care hug heart face_4376565b-9b1c-4d38-bc0d-e4819924e5d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-eye-face-holding-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('emoji', 'heart', 'hug', 'face', 'hands', 'care', 'affection')

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
        path('face',(10,38),[('A',(6,24),18,18,True),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('A',(38,38),18,18,True)])
        path('heart',(24,38),[('L',(13,27)),('A',(24,22),6,6,True),('A',(35,27),6,6,True),('L',(24,38))],True)
        for x in (13,35):circle(f'hand-{x}',x,37,5);self.relate('connect',f'hand-{x}','heart')
        for x in (19,29):path(f'eye-{x}',(x-2,17),[('C',(x+2,17),(x-1,13),(x+1,13))])
