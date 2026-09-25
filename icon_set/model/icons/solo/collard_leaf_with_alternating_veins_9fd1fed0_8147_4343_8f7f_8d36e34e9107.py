'collard-leaf-with-alternating-veins. Plan: Lobed leaf with central stem and alternating veins. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide leafy-green: rounded lobes and main vein. Reduction: Shortened the lower vein to preserve spacing inside the lobed leaf.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fd1fed0-8147-4343-8f7f-8d36e34e9107'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/collard_9fd1fed0-8147-4343-8f7f-8d36e34e9107.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'collard-leaf-with-alternating-veins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('collard', 'leaf', 'greens', 'vegetable', 'veins', 'plant', 'botanical')

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
        path('leaf',(24,4),[('C',(34,10),(30,4),(30,8)),('C',(40,20),(40,10),(40,16)),('C',(38,28),(40,24),(38,24)),('C',(24,38),(38,32),(28,38)),('C',(10,28),(20,38),(10,32)),('C',(8,20),(10,24),(8,24)),('C',(14,10),(8,16),(8,10)),('C',(24,4),(18,8),(18,4))],True)
        self.add_line('stem',(24,14),(24,44));self.relate('connect','leaf','stem')
        self.add_line('vein-left',(16,18),(24,26));self.relate('connect','stem','vein-left')
        self.add_line('vein-right',(24,28),(30,22));self.relate('connect','stem','vein-right')
