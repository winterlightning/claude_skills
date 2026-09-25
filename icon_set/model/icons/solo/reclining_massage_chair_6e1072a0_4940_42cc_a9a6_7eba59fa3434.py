"""Reclining Massage Chair.

Plan: Centerline8,4,40,44. Seat arm and wide foot share nodes; back emerges above arm with no crowded lower sliver.
Construction: Lucide armchair: rounded upholstery contours; supplied side-view reclining pose retained.
Reduction: Occluded lower back omitted; broad side armrest and reclining upper back retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e1072a0-4940-42cc-a9a6-7eba59fa3434'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/01-6e1072a0-4940-42cc-a9a6-7eba59fa3434.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'reclining-massage-chair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('reclining', 'massage', 'chair')

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
        path('arm',(20,44),[('L',(20,32)),('L',(20,28)),('A',(26,22),6,6,True),('L',(30,22)),('L',(36,22)),('L',(36,44)),('L',(20,44))],True)
        path('foot',(20,32),[('A',(8,44),12,12,False),('L',(20,44))])
        path('back',(26,22),[('L',(30,8)),('A',(34,4),4,4,True),('L',(36,4)),('A',(40,8),4,4,True),('L',(36,22))])
        join('arm','foot');join('arm','back')
