"""Bonfire Beside a Bare Grain Stalk
Plan: Flame at left above crossed sticks, grain-like branch at right. This is a physical festival scene.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: No useful exact Lucide match.
Reduction: Reduced branch count to two opposing pairs; retained flame and crossed wood.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56bd7c99-2b79-4137-b30e-f3e5fd7f8442'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bhogi fire_56bd7c99-2b79-4137-b30e-f3e5fd7f8442.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bonfire-beside-a-bare-grain-stalk'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bonfire', 'flame', 'sticks', 'grain', 'stalk', 'harvest', 'festival')

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
        path('flame',(14,8),[('C',(20,22),(19,14),(20,18)),('A',(4,22),8,6,True),('C',(8,14),(4,18),(5,17)),('L',(11,19)),('C',(14,8),(15,15),(14,12))],True)
        self.add_polyline('log-one',(4,38),(12,39),(20,40));self.add_polyline('log-two',(4,40),(12,39),(20,38))
        for a in ['log-one-1','log-one-2']:
            for b in ['log-two-1','log-two-2']:self.relate('connect',a,b)
        self.add_polyline('stem',(36,8),(36,22),(36,38),(36,40))
        for j,y in enumerate([22,38]):
            for side,x in [('left',28),('right',44)]:
                name=f'branch-{side}-{j}';self.add_line(name,(36,y),(x,y-12))
                self.relate('connect',name,f'stem-{j+1}');self.relate('connect',name,f'stem-{j+2}')
            self.relate('connect',f'branch-left-{j}',f'branch-right-{j}')
