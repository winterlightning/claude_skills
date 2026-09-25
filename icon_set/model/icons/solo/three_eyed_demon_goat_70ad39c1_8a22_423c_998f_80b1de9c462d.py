"""Demon Goat Head with Third Eye.

Plan: Goat with down-curving horns, broad forehead, tapered muzzle and three eyes. Extremes4,8,44,40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Use three spaced eye dots and open horn strokes; retain the long muzzle and downward horn turns.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70ad39c1-8a22-423c-998f-80b1de9c462d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/45-70ad39c1-8a22-423c-998f-80b1de9c462d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-eyed-demon-goat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('three', 'eyed', 'demon', 'goat')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('head',(16,12),[('C',(24,8),(18,8),(21,8)),('C',(32,12),(27,8),(30,8)),('C',(37,20),(36,14),(37,17)),('L',(37,29)),('C',(32,35),(37,32),(32,32)),('A',(16,35),8,5,True),('C',(11,29),(16,32),(11,32)),('L',(11,20)),('C',(16,12),(11,17),(12,14))],True)
        for s in (-1,1):
         x=lambda v:24+s*v
         path(f'horn-{s}',(x(8),12),[('C',(x(20),14),(x(15),6),(x(20),8))]);join('head',f'horn-{s}')
        self.add_dot('third-eye',(24,17))
        for s in (-1,1):self.add_dot(f'eye-{s}',(24+s*4,26))
