"""Sous Vide Immersion Circulator.

Plan: Centerline10,4,38,44. Upright immersion circulator with elliptical top, waisted grip, lower cylinder and one dividing band.
Construction: No useful direct Lucide match; symmetric cylindrical appliance with clear waisted upper grip.
Reduction: Omitted second tightly spaced band; retained one short indicator mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa6d2811-979d-4fd9-a771-6060a570f207'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/33-fa6d2811-979d-4fd9-a771-6060a570f207.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'sous-vide-immersion-circulator'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('sous', 'vide', 'immersion', 'circulator')

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
        path('top',(10,9),[('A',(38,9),14,5,True),('A',(10,9),14,5,True)],True)
        path('body',(10,9),[('C',(10,29),(14,17),(14,21)),('L',(10,39)),('A',(38,39),14,5,False),('L',(38,29)),('C',(38,9),(34,21),(34,17))])
        path('seam',(10,29),[('A',(38,29),14,5,False)])
        join('top','body');join('body','seam')
        line('indicator',(24,23),(24,25))
