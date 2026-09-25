"""Sleeveless V Neck Vest with Hem Band
Plan: Symmetric V-neck vest with joined central opening and lower band.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide shirt: shaped armholes and a coherent garment boundary.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee26c52a-6832-4a0f-a7bd-307d086c560f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dickey_ee26c52a-6832-4a0f-a7bd-307d086c560f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sleeveless-v-neck-vest-with-hem-band'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('vest', 'sleeveless', 'clothing', 'garment', 'vneck', 'hem', 'waistcoat')

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
        path('vest',(6,29),[('C',(12,6),(14,25),(12,14)),('L',(20,6)),('L',(24,22)),('L',(28,6)),('L',(36,6)),('C',(42,29),(36,14),(34,25)),('L',(42,42)),('L',(6,42)),('L',(6,29))],True)
        self.add_line('opening',(24,22),(24,34));self.add_line('hem',(6,34),(42,34))
        self.relate('connect','vest','opening');self.relate('connect','vest','hem');self.relate('connect','opening','hem')
