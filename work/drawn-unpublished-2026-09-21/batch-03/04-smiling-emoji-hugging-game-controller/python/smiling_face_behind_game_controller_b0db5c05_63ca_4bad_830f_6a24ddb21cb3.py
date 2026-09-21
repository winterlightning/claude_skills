"""Smiling Face Behind Game Controller
Plan: Smiling face above a broad two-grip controller.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide gamepad-2: two grips and broad upper control deck.
Reduction: Tiny controls and mouth omitted in first fit; review identity before release."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0db5c05-63ca-4bad-830f-6a24ddb21cb3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emoji gaming lover hug 1_b0db5c05-63ca-4bad-830f-6a24ddb21cb3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-face-behind-game-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('emoji', 'game', 'controller', 'face', 'smile', 'gaming', 'controls')

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
        path('face',(10,31),[('A',(6,24),18,18,True),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('A',(38,31),18,18,True)])
        path('controller',(13,28),[('L',(35,28)),('C',(39,33),(38,28),(39,30)),('L',(42,40)),('C',(36,42),(42,42),(38,42)),('L',(30,36)),('L',(18,36)),('L',(12,42)),('C',(6,40),(10,42),(6,42)),('L',(9,33)),('C',(13,28),(9,30),(10,28))],True)
        for x in (19,29):path(f'eye-{x}',(x-2,17),[('C',(x+2,17),(x-1,14),(x+1,14))])
        self.relate('connect','face','controller')
