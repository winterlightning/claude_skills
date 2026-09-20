"""Building Entrance with Arch.

Plan: Lintel and roofcap over open arch facade x4..44 y8..40; door springs at baseline.
Construction: Lucide church: clear arched entrance.
Reduction: Merged base plinth into split baseline, omitted vertical door jambs to fit the arch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3eebd7ad-0dfa-4088-bed9-224b29b72881'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/16-3eebd7ad-0dfa-4088-bed9-224b29b72881.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'lobby-entrance'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('lobby', 'entrance')

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
        rect('lintel',4,16,40,8)
        poly('roof',(12,16),(12,8),(36,8),(36,16));join('roof','lintel')
        poly('walls',(8,24),(8,40),(16,40));join('walls','lintel')
        poly('wall-right',(32,40),(40,40),(40,24));join('wall-right','lintel')
        path('door',(16,40),[('A',(32,40),8,8,True)]);join('door','walls');join('door','wall-right')
