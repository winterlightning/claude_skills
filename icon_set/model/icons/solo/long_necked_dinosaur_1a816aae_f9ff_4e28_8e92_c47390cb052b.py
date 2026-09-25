"""Long Neck Brachiosaurus Dinosaur.

Plan: Right-facing long-neck dinosaur with two thick legs and extended tail. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit tiny eye and distant legs; retain rounded small head, tall neck and long low tail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a816aae-f9ff-4e28-8e92-c47390cb052b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/19-1a816aae-f9ff-4e28-8e92-c47390cb052b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'long-necked-dinosaur'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('long', 'necked', 'dinosaur')

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
        path('dino',(6,34),[('C',(20,24),(12,34),(13,24)),('C',(28,16),(28,24),(28,22)),('L',(28,12)),('A',(34,6),6,6,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,15)),('L',(36,15)),('L',(36,32)),('L',(38,42)),('L',(29,42)),('L',(28,33)),('L',(19,33)),('L',(19,42)),('L',(10,42)),('L',(6,42)),('L',(6,34))],True)
