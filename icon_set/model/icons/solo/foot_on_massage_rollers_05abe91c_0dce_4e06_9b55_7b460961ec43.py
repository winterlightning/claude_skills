"""Foot Massage Roller.

Plan: Foot above three round rollers and a base; shared roller radius4, pitch16; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Three circular rollers replace the outlined low humps; retained ankle, foot and base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05abe91c-0dce-4e06-9b55-7b460961ec43'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/05-05abe91c-0dce-4e06-9b55-7b460961ec43.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'foot-on-massage-rollers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('foot', 'on', 'massage', 'rollers')

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
        path('foot',(22,8),[('C',(10,16),(22,12),(15,14)),('C',(8,24),(4,17),(4,24)),('L',(34,24)),('A',(40,18),6,6,False),('C',(37,8),(40,13),(37,12))])
        for j,x in enumerate((8,24,40)):
         path(f'roller-{j}',(x,40),[('A',(x,32),4,4,True),('A',(x,40),4,4,True)],True)
        poly('base',(4,40),(8,40),(24,40),(40,40),(44,40))
        for j in range(3):join('base',f'roller-{j}')
