"""Smiling Face with Sunglasses.

Plan: Rounded smiling face with sunglasses integrated into side rim; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Sunglasses temples integrated into face rim; smile retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b207644-924b-4415-9162-5bfe9adfd9bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/40-6b207644-924b-4415-9162-5bfe9adfd9bf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'smiling-face-wearing-sunglasses'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('smiling', 'face', 'wearing', 'sunglasses')

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
        path('face',(6,17),[('C',(24,6),(6,10),(16,6)),('C',(42,17),(32,6),(42,10)),('C',(24,42),(42,33),(34,42)),('C',(6,17),(14,42),(6,33))],True)
        poly('rim',(6,17),(22,17),(26,17),(42,17));join('face','rim')
        path('left-lens',(6,17),[('A',(22,17),8,8,False)]);path('right-lens',(26,17),[('A',(42,17),8,8,False)])
        join('rim','left-lens');join('rim','right-lens');join('face','left-lens');join('face','right-lens')
        path('smile',(21,32),[('C',(27,32),(23,34),(25,34))])
