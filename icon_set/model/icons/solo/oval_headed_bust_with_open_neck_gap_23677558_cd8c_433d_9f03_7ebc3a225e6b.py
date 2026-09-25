"""Oval Headed Bust with Open Neck Gap
Plan: Centered circular head touches broad curved shoulders, with open bottom.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: human_ref/user.svg: rounded shoulders and round head; current avatar gap is zero.
Reduction: Closed torso base opened and head/body gap removed under current avatar rules; oval head regularized to circular."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23677558-cd8c-433d-9f03-7ebc3a225e6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/egghead_23677558-cd8c-433d-9f03-7ebc3a225e6b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oval-headed-bust-with-open-neck-gap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'profile', 'bust', 'head', 'shoulders', 'portrait', 'user')

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

        from ._base import HEAD_BODY_CENTERLINE_GAP
        cx,cy,r=24,13,9
        circle('head',cx,cy,r)
        top=cy+r+HEAD_BODY_CENTERLINE_GAP
        path('body',(8,44),[('L',(8,42)),('A',(24,top),16,16,True),('A',(40,42),16,16,True),('L',(40,44))])
        self.relate('connect','head','body')
