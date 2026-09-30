"""Two Connected Sensors Before a Tablet
Plan: Two small sensor heads with stems beside larger tablet
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide network device hierarchy.
Reduction: Omit controls; keep attached stem connections."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04aef027-7699-4c4d-a6e2-afbaea113fbc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/aws iot services farm ipad_04aef027-7699-4c4d-a6e2-afbaea113fbc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-connected-sensors-before-a-tablet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sensors', 'tablet', 'devices', 'network', 'buttons', 'connected', 'electronics')

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
        rect('tablet',28,8,16,32,2)
        rect('sensor-a',4,8,12,8,2)
        rect('sensor-b',4,32,12,8,2)
        self.add_line('stem-a',(10,16),(10,24));self.add_line('stem-b',(10,24),(10,32));self.add_line('link',(10,24),(28,24))
        for a,b in [('stem-a','sensor-a'),('stem-b','sensor-b'),('stem-a','stem-b'),('link','stem-a'),('link','stem-b'),('link','tablet')]:self.relate('connect',a,b)
