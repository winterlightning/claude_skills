"""Simple Botanical Leaf.

Plan: Centerline6,6,42,42. Upper-right pointed leaf with rounded lower-left body; diagonal vein continues to stem.
Construction: Lucide leaf original and atomic-debug: pointed asymmetrical outline and central stem/vein.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c65dafc-c26f-4d60-b045-e9301d81fc96'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/16-0c65dafc-c26f-4d60-b045-e9301d81fc96.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'botanical-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('botanical', 'leaf')

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
        path('leaf',(14,34),[('C',(6,24),(8,34),(6,29)),('C',(42,6),(6,12),(26,6)),('C',(24,38),(42,23),(38,38)),('C',(14,34),(19,38),(16,36))],True)
        poly('vein',(6,42),(14,34),(28,20));join('leaf','vein')
