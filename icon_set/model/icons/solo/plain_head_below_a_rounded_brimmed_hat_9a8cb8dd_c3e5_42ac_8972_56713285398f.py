"""Plain Head Below a Rounded Brimmed Hat
Plan: Centered hemispherical hat above a circular open jaw.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: human_ref/user.svg: circular face construction.
Reduction: Face details absent in reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a8cb8dd-c3e5-42ac-8972-56713285398f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avatar tribal man_9a8cb8dd-c3e5-42ac-8972-56713285398f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-head-below-a-rounded-brimmed-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('head', 'hat', 'brim', 'portrait', 'face', 'headwear', 'person')

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
        path('cap',(10,20),[('A',(24,6),14,14,True),('A',(38,20),14,14,True)])
        self.add_line('brim',(6,20),(42,20));self.relate('connect','cap','brim')
        path('jaw',(11,29),[('A',(24,42),13,13,False),('A',(37,29),13,13,False)])
