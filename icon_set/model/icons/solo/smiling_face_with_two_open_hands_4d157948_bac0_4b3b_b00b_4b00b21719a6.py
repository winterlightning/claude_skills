"""Smiling Face with Two Open Hands
Plan: Smiling face above two open inward-angled hands.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: human_ref/user.svg: rounded face; source open hands retained.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d157948-bac0-4b3b-b00b-4b00b21719a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emoji smiling face open hands_4d157948-bac0-4b3b-b00b-4b00b21719a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-face-with-two-open-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('emoji', 'smile', 'face', 'hands', 'hug', 'gesture', 'palms')

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
        path('head',(10,22),[('A',(24,6),14,16,True),('A',(38,22),14,16,True)])
        path('left-hand',(6,31),[('L',(10,25)),('L',(18,31)),('L',(19,27)),('C',(22,39),(25,23),(24,37)),('C',(6,31),(16,48),(9,37))])
        path('right-hand',(42,31),[('L',(38,25)),('L',(30,31)),('L',(29,27)),('C',(26,39),(23,23),(24,37)),('C',(42,31),(32,48),(39,37))])
        path('smile',(19,20),[('C',(29,20),(22,25),(26,25))])
