"""Plain Bench with Backrest
Plan: Broad rounded backrest, thick seat and paired legs.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Perspective seat depth reduced to one rim."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aba85a97-ab73-46dc-a3d7-15768242bfaf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pew_aba85a97-ab73-46dc-a3d7-15768242bfaf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-bench-backrest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bench', 'seat', 'backrest', 'furniture', 'legs', 'seating')

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
        path('back',(8,24),[('L',(8,12)),('A',(12,8),4,4,True),('L',(36,8)),('A',(40,12),4,4,True),('L',(40,24))])
        rect('seat',4,24,40,8,2)
        for x in (10,38):
         self.add_line(f'leg-{x}',(x,32),(x,40));self.relate('connect','seat',f'leg-{x}')
        self.relate('connect','back','seat')
