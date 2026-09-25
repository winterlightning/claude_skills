"""Circular Frame Spectacles
Plan: Paired matching rims and curved bridge.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: Lucide glasses: paired rims and bridge.
Reduction: None; circular lenses preserved; diagonal arrangement fits while retaining circular lenses."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24408388-63fe-4b98-892d-b1ef4d414cc9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bifocals_24408388-63fe-4b98-892d-b1ef4d414cc9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-frame-spectacles'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('spectacles', 'glasses', 'round', 'lens', 'eyewear', 'vision', 'frames')

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
        # Two circular lenses on a diagonal, with a curved connecting bridge.
        circle('left-lens',12,16,8)
        circle('right-lens',36,32,8)
        path('bridge',(12,24),[('L',(20,24)),('A',(28,32),8,8,True)])
        self.relate('connect','bridge','left-lens')
        self.relate('connect','bridge','right-lens')
