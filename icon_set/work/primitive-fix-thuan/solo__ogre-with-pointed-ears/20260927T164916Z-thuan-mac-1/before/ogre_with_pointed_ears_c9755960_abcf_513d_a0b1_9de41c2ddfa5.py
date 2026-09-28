"""Angry Ogre Monster.

Plan: Ogre circular head, long pointed ear strokes, slanted eyes and touching shoulders. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Retain slanted eyes and pointed ear strokes; omit arm seams. Circular face and touching shoulders follow the shared human reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9755960-abcf-513d-a0b1-9de41c2ddfa5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/31-c9755960-abcf-513d-a0b1-9de41c2ddfa5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'ogre-with-pointed-ears'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('ogre', 'with', 'pointed', 'ears')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = "shoulder-top" if name == "shoulders" and index == 1 else f"{name}-{index}"
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
        circle('face',24,20,14)
        path('shoulders',(6,42),[('A',(10,38),4,4,True),('L',(38,38)),('A',(42,42),4,4,True)]);join('face','shoulders')
        for s in (-1,1):
         x=lambda v:24+s*v
         line(f'ear-{s}',(x(14),20),(x(18),9));join('face',f'ear-{s}')
         line(f'eye-{s}',(x(5),18),(x(4),20))
