"""Frustrated Persevering Face.

Plan: Circular frustrated face with tense inward brow-eye strokes and downward mouth; radius20 center24.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Eyebrows and flat eyes merged into two squeezed-eye strokes so the frustrated expression remains legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a2e9ebc-ac7b-4760-8c0d-cb5e1101e6de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/17-6a2e9ebc-ac7b-4760-8c0d-cb5e1101e6de.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'frustrated-face-with-angled-brows'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('frustrated', 'face', 'with', 'angled', 'brows')

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
        circle('face',24,24,20)
        poly('left-eye',(16,17),(20,20),(16,20));poly('right-eye',(32,17),(28,20),(32,20))
        path('frown',(17,33),[('C',(31,33),(21,26),(27,26))])
