"""Long Bodied Cockroach
Plan: Paired antennae and three pairs of jointed legs around long split shell.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bug: six paired limbs and central shell seam.
Reduction: Compact shared shell/head boundary; paired antennae and six legs retained. Antennae meet exact circular head nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed1d04e4-8a81-4353-8d4c-321c16995cfd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/cockroach_ed1d04e4-8a81-4353-8d4c-321c16995cfd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-bodied-cockroach'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cockroach', 'insect', 'bug', 'antennae', 'legs', 'body', 'animal')

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
        path('shell',(18,20),[('L',(19,20)),('L',(24,20)),('L',(29,20)),('L',(30,20)),('A',(34,24),4,4,True),('L',(34,32)),('A',(30,40),10,10,True),('A',(24,42),10,10,True),('A',(18,40),10,10,True),('A',(14,32),10,10,True),('L',(14,24)),('A',(18,20),4,4,True)],True)
        path('head',(19,20),[('L',(19,15)),('A',(20,12),5,5,True),('A',(24,10),5,5,True),('A',(28,12),5,5,True),('A',(29,15),5,5,True),('L',(29,20))]);self.relate('connect','head','shell')
        self.add_line('seam',(24,20),(24,42));self.relate('connect','seam','shell')
        for s in (-1,1):
         for i,(y,end_y) in enumerate([(24,16),(32,32),(40,42)]):
          name=f'leg-{s}-{i}';self.add_polyline(name,(24+s*(6 if i==2 else 10),y),(24+s*16,y),(24+s*18,end_y));self.relate('connect',name,'shell')
         name=f'antenna-{s}';self.add_line(name,(24+s*4,12),(24+s*9,6));self.relate('connect',name,'head')
