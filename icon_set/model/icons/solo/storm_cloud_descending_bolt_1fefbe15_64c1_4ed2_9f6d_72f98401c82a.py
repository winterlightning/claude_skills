'storm-cloud-descending-bolt. Plan: Cloud with a centered descending lightning stroke. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide cloud-lightning: open cloud and zigzag bolt. Reduction: Use an open three-segment bolt instead of doubled narrow outline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fefbe15-64c1-4ed2-9f6d-72f98401c82a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/poo storm_1fefbe15-64c1-4ed2-9f6d-72f98401c82a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'storm-cloud-descending-bolt'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('storm', 'cloud', 'lightning', 'weather', 'bolt', 'thunder')

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
        path('cloud',(12,26),[('C',(4,18),(7,26),(4,23)),('C',(14,12),(4,12),(8,10)),('C',(24,8),(16,8),(20,8)),('C',(34,14),(30,8),(34,10)),('C',(44,20),(40,12),(44,16)),('C',(38,26),(44,24),(42,26))])
        self.add_polyline('bolt',(24,24),(18,32),(30,32),(24,40))
