'rounded-rain-cloud-with-slanted-streaks. Plan: Closed rounded cloud with three slanted rain strokes. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide cloud-drizzle: detached rain series. Reduction: Keep three strokes and longer center streak.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79ac1e57-72f5-49a3-9839-d3ca493d1689'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/drizzle_79ac1e57-72f5-49a3-9839-d3ca493d1689.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-rain-cloud-with-slanted-streaks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cloud', 'rain', 'weather', 'drizzle', 'streaks', 'sky', 'precipitation')

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
        path('cloud',(12,24),[('C',(4,18),(7,24),(4,22)),('C',(14,12),(4,12),(8,10)),('C',(24,8),(16,8),(20,8)),('C',(34,14),(30,8),(34,10)),('C',(44,20),(40,12),(44,16)),('C',(38,24),(44,23),(42,24)),('L',(12,24))],True)
        for i,(x,end) in enumerate([(12,38),(24,40),(36,38)]):self.add_line(f'rain-{i}',(x,32),(x-2,end))
