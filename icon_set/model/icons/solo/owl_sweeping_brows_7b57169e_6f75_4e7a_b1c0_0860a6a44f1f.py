"""Owl with Sweeping Brows
Plan: Owl face with swept brows, circular eyes and centered beak.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Large eye-area enclosure seams omitted; leaf-shaped beak reduced to a point; round eyes and sweeping brows retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b57169e-6f75-4e7a-b1c0-0860a6a44f1f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/owl_7b57169e-6f75-4e7a-b1c0-0860a6a44f1f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'owl-sweeping-brows'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('owl', 'face', 'bird', 'eyes', 'beak', 'brows')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('head',(4,8),[('C',(24,13),(6,17),(18,6)),('C',(44,8),(30,6),(42,17)),('L',(44,28)),('C',(24,40),(44,37),(32,40)),('C',(4,28),(16,40),(4,37)),('L',(4,8))],True)
        for x in (16,32):circle(f'eye-{x}',x,22,3)
        self.add_dot('beak',(24,31))
