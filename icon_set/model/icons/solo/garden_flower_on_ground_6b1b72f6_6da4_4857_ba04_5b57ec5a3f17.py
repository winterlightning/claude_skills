"""Small Growing Garden Flower.

Plan: Five-petal flower above paired leaves, stem and ground; bounds (8,4)-(40,44).
Construction: Lucide flower-2 and sprout: coherent petal lobes, paired leaves and attached stem.
Reduction: Small center omitted; leaf outlines and veins reduced to two broad blade strokes, keeping five petals and ground.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b1b72f6-6da4-4857-ba04-5b57ec5a3f17'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/18-6b1b72f6-6da4-4857-ba04-5b57ec5a3f17.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'garden-flower-on-ground'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('garden', 'flower', 'on', 'ground')

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
        path('bloom',(19,12),[('A',(29,12),5,8,True),('A',(33,21),6,6,True),('A',(24,25),5,5,True),('A',(15,21),5,5,True),('A',(19,12),6,6,True)],True)
        line('stem',(24,25),(24,44));join('bloom','stem')
        line('left-leaf',(24,36),(8,34));line('right-leaf',(24,36),(40,34));join('stem','left-leaf');join('stem','right-leaf');join('left-leaf','right-leaf')
        poly('ground',(8,44),(24,44),(40,44));join('stem','ground')
