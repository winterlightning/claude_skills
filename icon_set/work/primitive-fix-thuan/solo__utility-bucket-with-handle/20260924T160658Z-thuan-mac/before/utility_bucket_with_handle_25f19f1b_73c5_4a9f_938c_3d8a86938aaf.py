"""Utility Bucket with Handle.

Plan: Centerline8,4,40,44. Broad elliptical opening, tapered curved base, and high arch handle.
Construction: No useful direct local Lucide bucket match; symmetric rim and high round bail handle.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25f19f1b-73c5-4a9f-938c-3d8a86938aaf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/11-25f19f1b-73c5-4a9f-938c-3d8a86938aaf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'utility-bucket-with-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('utility', 'bucket', 'with', 'handle')

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
        path('rim',(8,25),[('A',(40,25),16,5,True),('A',(8,25),16,5,True)],True)
        path('pail',(8,25),[('L',(12,39)),('C',(24,44),(12,44),(18,44)),('C',(36,39),(30,44),(36,44)),('L',(40,25))]);join('rim','pail')
        path('handle',(8,25),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,25))]);join('handle','rim')
