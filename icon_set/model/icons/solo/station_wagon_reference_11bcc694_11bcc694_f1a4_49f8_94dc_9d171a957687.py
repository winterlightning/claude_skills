"""Station Wagon
Plan: Long station wagon, two wheels and raised glazed cabin.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: Lucide package/truck construction principles; windows share body seams.
Reduction: Three window sections reduced to two."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11bcc694-f1a4-49f8-94dc-9d171a957687'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/station wagon_11bcc694-f1a4-49f8-94dc-9d171a957687.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'station-wagon-reference-11bcc694'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('car', 'wagon', 'station', 'vehicle', 'transport', 'wheel', 'window', 'automobile')

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
        path('body',(6,32),[('L',(4,32)),('L',(4,22)),('L',(12,10)),('L',(28,10)),('L',(36,22)),('L',(40,22)),('A',(44,26),4,4,True),('L',(44,32)),('L',(42,32))])
        for x in (12,36):circle(f'wheel-{x}',x,32,6);self.relate('connect',f'wheel-{x}','body')
        self.add_line('chassis',(18,32),(30,32))
        for x in (12,36):self.relate('connect','chassis',f'wheel-{x}')
        self.add_line('windows',(4,22),(36,22));self.relate('connect','windows','body')
        self.add_line('pillar',(22,10),(22,22));self.relate('connect','pillar','body');self.relate('connect','pillar','windows')
