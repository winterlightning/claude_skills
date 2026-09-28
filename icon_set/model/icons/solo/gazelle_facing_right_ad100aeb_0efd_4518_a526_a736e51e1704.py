"""Standing Gazelle Animal.

Plan: Slender right-facing gazelle with swept horn, upright neck, body and two straight legs; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Two legs shown as separated paired strokes; small eye and tail omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad100aeb-0efd-4518-a526-a736e51e1704'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/23-ad100aeb-0efd-4518-a526-a736e51e1704.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gazelle-facing-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('gazelle', 'facing', 'right')

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
        path('gazelle',(6,42),[('L',(6,28)),('A',(14,20),8,8,True),('L',(25,20)),('L',(29,12)),('L',(36,14)),('L',(42,21)),('L',(34,21)),('L',(31,31)),('L',(31,42))])
        poly('belly',(14,42),(14,31),(23,32),(23,42))
        line('back-leg-join',(14,31),(6,28));join('gazelle','back-leg-join');join('belly','back-leg-join')
        path('horn',(29,12),[('C',(20,6),(25,11),(20,9))]);join('gazelle','horn')
