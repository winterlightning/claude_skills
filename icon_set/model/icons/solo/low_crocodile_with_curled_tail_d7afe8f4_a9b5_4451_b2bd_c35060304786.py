"""Low Crocodile with Curled Tail
Plan: Long right-facing snout, raised eye mound, bent leg and curled tail.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Tiny teeth and extra legs omitted for clear silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7afe8f4-a9b5-4451-b2bd-c35060304786'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crocodile_d7afe8f4-a9b5-4451-b2bd-c35060304786.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-crocodile-with-curled-tail'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crocodile', 'reptile', 'animal', 'snout', 'tail', 'wildlife', 'legs')

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
        path('crocodile',(4,29),[('C',(16,16),(4,21),(9,16)),('L',(29,16)),('A',(37,16),4,6,True),('L',(44,16)),('L',(41,29)),('L',(30,29)),('L',(32,38)),('L',(24,38)),('L',(21,29)),('L',(12,29)),('C',(12,38),(5,26),(6,34)),('C',(4,29),(6,38),(4,34))],True)
