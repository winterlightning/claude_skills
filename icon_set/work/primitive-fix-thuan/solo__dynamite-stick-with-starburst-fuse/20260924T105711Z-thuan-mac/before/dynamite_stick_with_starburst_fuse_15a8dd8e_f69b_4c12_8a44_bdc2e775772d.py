"""Dynamite Stick with Starburst Fuse
Plan: Diagonal dynamite capsule, attached fuse and pointed spark.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Filled outlined starburst reduced to four connected spark strokes; short fuse retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15a8dd8e-f69b-4c12-8a44-bdc2e775772d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dynamite_15a8dd8e-f69b-4c12-8a44-bdc2e775772d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dynamite-stick-with-starburst-fuse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('dynamite', 'fuse', 'spark', 'explosive', 'stick', 'starburst', 'blast')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('stick',(6,34),[('L',(19,21)),('C',(25,21),(21,19),(23,19)),('L',(27,23)),('L',(29,25)),('C',(29,31),(31,27),(31,29)),('L',(18,42)),('L',(6,34))],True)
        line('fuse',(27,23),(34,16));join('fuse','stick')
        poly('spark',(29,11),(34,16),(39,21));poly('spark-cross',(29,21),(34,16),(42,8));poly('spark-up',(34,6),(34,16));join('spark','spark-cross');join('spark','spark-up');join('fuse','spark')
