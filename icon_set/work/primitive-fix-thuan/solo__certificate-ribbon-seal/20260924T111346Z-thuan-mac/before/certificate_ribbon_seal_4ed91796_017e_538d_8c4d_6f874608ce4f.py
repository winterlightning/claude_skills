"""Certificate With Ribbon Seal.

Plan: Centerline4,8,44,40. Certificate corner is physically replaced by a ribbon-seal silhouette, with one short internal text rule.
Construction: Lucide scroll-text original/debug: document with a spaced text rule; seal and ribbon integrated into a single uncluttered silhouette.
Reduction: Second text rule omitted; seal and ribbon share one outline, retaining the round medallion and notched ribbon.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed91796-017e-538d-8c4d-6f874608ce4f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/27-4ed91796-017e-538d-8c4d-6f874608ce4f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'certificate-ribbon-seal'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('certificate', 'ribbon', 'seal')

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
        poly('document',(25,30),(4,30),(4,8),(44,8),(44,21),(36,21))
        path('seal',(25,30),[('A',(36,21),10,10,True),('A',(43,30),9,9,True),('A',(38,37),9,9,True),('L',(38,40)),('L',(34,37)),('L',(30,40)),('L',(30,37)),('A',(25,30),9,9,True)],True)
        line('text',(13,17),(20,17));join('document','seal')
