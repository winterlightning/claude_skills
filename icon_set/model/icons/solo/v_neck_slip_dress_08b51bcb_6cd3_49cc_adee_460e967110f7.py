"""V-Neck Slip Dress
Plan: Slip dress with thin straps, pointed neckline and flared skirt.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide shirt: shared neckline and body joints.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08b51bcb-6cd3-49cc-adee-460e967110f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/negligee_08b51bcb-6cd3-49cc-adee-460e967110f7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'v-neck-slip-dress'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dress', 'slip', 'nightwear', 'straps', 'clothing', 'garment')

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
        path('dress',(15,4),[('L',(15,13)),('L',(24,20)),('L',(33,13)),('L',(33,4))])
        path('body',(15,13),[('C',(16,25),(10,18),(17,20)),('L',(8,44)),('L',(40,44)),('L',(32,25)),('C',(33,13),(31,20),(38,18))]);self.relate('connect','dress','body')
