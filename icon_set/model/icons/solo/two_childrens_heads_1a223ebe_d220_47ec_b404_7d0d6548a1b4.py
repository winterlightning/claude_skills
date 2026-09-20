"""Boy and Girl Child Avatars.

Plan: Two touching child heads r10 with tangent node22,24, each bisected by simple hairline; ponytail curls upper-right.
Construction: Human user.svg circular heads.
Reduction: Removed interior hair partitions and opened ponytail outline to prevent tight pockets; both circular heads and ponytail retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a223ebe-d220-47ec-b404-7d0d6548a1b4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/09-1a223ebe-d220-47ec-b404-7d0d6548a1b4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'two-childrens-heads'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('two', 'childrens', 'heads')

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
        path('left-head',(22,24),[('A',(6,16),10,10,True),('A',(16,6),10,10,True),('A',(26,16),10,10,True),('A',(22,24),10,10,True)],True)
        path('right-head',(22,24),[('A',(34,24),10,10,True),('A',(38,32),10,10,True),('A',(28,42),10,10,True),('A',(18,32),10,10,True),('A',(22,24),10,10,True)],True)
        join('left-head','right-head')
        path('ponytail',(34,24),[('C',(42,18),(34,15),(42,12))]);join('ponytail','right-head')
