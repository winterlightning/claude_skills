"""Castle Tower.

Plan: Three equal 8-wide battlements with equal8-wide gaps and broad tower. Extremes4,8,44,40.
Construction: Lucide castle original/atomic-debug: repeated battlements and arched opening.
Reduction: Omit base seam and lower window edge; retain three battlements and a clear arched window mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c28de48-0a62-5ac5-8b45-54484a3e5ced'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/36-5c28de48-0a62-5ac5-8b45-54484a3e5ced.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'battlement-castle-tower'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('battlement', 'castle', 'tower')

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
        poly('tower',(4,8),(12,8),(12,16),(20,16),(20,8),(28,8),(28,16),(36,16),(36,8),(44,8),(44,24),(38,24),(38,40),(10,40),(10,24),(4,24),closed=True)
        path('window',(20,31),[('A',(28,31),4,4,True)])
