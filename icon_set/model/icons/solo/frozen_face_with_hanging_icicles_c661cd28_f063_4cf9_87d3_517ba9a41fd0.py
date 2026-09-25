"""Freezing Cold Face.

Plan: Circular cold face upper region with three lower icicle strokes; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Eyes are round dots; simplified hanging strands to three icicles.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c661cd28-f063-4cf9-87d3-517ba9a41fd0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/08-c661cd28-f063-4cf9-87d3-517ba9a41fd0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'frozen-face-with-hanging-icicles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('frozen', 'face', 'with', 'hanging', 'icicles')

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
        path('face',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('C',(36,32),(40,25),(39,29)),('C',(24,36),(33,35),(29,36)),('C',(12,32),(19,36),(15,35)),('C',(8,20),(9,29),(8,25))],True)
        self.add_dot('eye-left',(18,17));self.add_dot('eye-right',(30,17));line('mouth',(20,26),(28,26))
        line('icicle-middle',(24,36),(24,44));join('face','icicle-middle')
        line('icicle-left',(12,32),(12,41));line('icicle-right',(36,32),(36,41));join('face','icicle-left');join('face','icicle-right')
