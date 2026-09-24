"""Serpentine Fantasy Sea Dragon.

Plan: Sea dragon head with swept crest and a smooth S-shaped neck ending in upward tail. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduce double neck outline to one coherent S-curve; preserve pointed crest, jaw and upward tail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55d269d5-9f58-51d3-8d9e-a7901bc07acf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/43-55d269d5-9f58-51d3-8d9e-a7901bc07acf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'serpentine-sea-dragon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('serpentine', 'sea', 'dragon')

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
        path('dragon',(6,16),[('L',(20,10)),('L',(40,6)),('L',(32,16)),('C',(42,24),(39,18),(42,20)),('C',(20,29),(42,33),(20,21)),('C',(12,35),(15,29),(12,31)),('C',(27,42),(12,40),(19,42)),('C',(42,33),(35,42),(42,38)),('L',(40,28))])
        poly('jaw',(6,16),(9,24),(12,23));join('dragon','jaw')
