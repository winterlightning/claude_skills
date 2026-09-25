"""Upright Rocket with Round Window
Plan: Upright symmetric rocket, window, fins and blunt base.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide rocket: symmetric nose, round window and paired fins.
Reduction: Nose seam and inner fin seams omitted; nose, window and two external fins retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a92e946-47da-49a6-ad3c-041ba4080585'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/space ship_4a92e946-47da-49a6-ad3c-041ba4080585.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-rocket-with-round-window'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('rocket', 'spacecraft', 'window', 'fins', 'space', 'ship')

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
        path('rocket',(24,4),[('C',(36,28),(33,9),(36,19)),('L',(40,36)),('L',(40,44)),('L',(8,44)),('L',(8,36)),('L',(12,28)),('C',(24,4),(12,19),(15,9))],True)
        circle('window',24,29,3)
