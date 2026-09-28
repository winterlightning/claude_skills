"""Sauna House with Rising Steam.

Plan: Centerline4,8,44,40. Broad low sauna house with open centered doorway; three short steam curls sit above the roof.
Construction: Lucide house original/debug: peaked roof and broad structural doorway.
Reduction: Steam curves shortened while preserving all three marks; roof lowered to maintain spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e393f7a4-08ac-4a4f-b220-b7a7a78dde5d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-020/references/39-e393f7a4-08ac-4a4f-b220-b7a7a78dde5d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'sauna-house-rising-steam'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "spas"
    categories = ("primitives", "spas")
    aliases = ()
    keywords = ('sauna', 'house', 'rising', 'steam')

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
        poly('roof',(4,32),(8,30),(24,22),(40,30),(44,32))
        poly('walls',(8,30),(8,40),(20,40),(20,34),(28,34),(28,40),(40,40),(40,30));join('roof','walls')
        for x in (20,30,40):path(f'steam-{x}',(x,8),[('C',(x,14),(x-4,10),(x+4,12))])
