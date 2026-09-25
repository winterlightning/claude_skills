'A front-facing seated frog with raised eye bumps, haunches and forelegs.\nPlan: SQUARE balances the broad head and paired haunches.\nReduction: Merged the body/haunch exterior to remove grazing duplicate belly curves; retained short forelegs.\nConstruction: No useful exact Lucide match; supplied frog reference governs the silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b274b037-6061-4c72-b6f8-f750487d883c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amphibian frog body_b274b037-6061-4c72-b6f8-f750487d883c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-seated-frog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('frog', 'amphibian', 'seated', 'legs', 'animal', 'pond', 'wildlife')

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
        # Plan: eye bumps and haunches share one exterior contour, avoiding
        # grazing duplicate belly edges. Two short forelegs join the baseline.
        path('frog',(12,20),[
            ('C',(12,11),(9,17),(10,13)),('A',(24,11),6,5,True),
            ('A',(36,11),6,5,True),('C',(36,20),(38,13),(39,17)),
            ('L',(34,26)),('C',(42,30),(42,20),(42,25)),
            ('L',(42,38)),('A',(38,42),4,4,True),
            ('L',(32,42)),('L',(16,42)),('L',(10,42)),
            ('A',(6,38),4,4,True),('L',(6,30)),
            ('C',(14,26),(6,25),(6,20)),('L',(12,20))],True)
        for side,x in [('left',16),('right',32)]:
            self.add_line(side+'-foreleg',(x,32),(x,42))
            self.relate('connect','frog',side+'-foreleg')
