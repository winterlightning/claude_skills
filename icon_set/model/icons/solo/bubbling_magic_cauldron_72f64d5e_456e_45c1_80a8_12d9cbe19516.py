"""Bubbling Magic Potion Cauldron.

Plan: Round cauldron, integrated rim and two feet; bubble and magic cross rise above. Extremes 6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Rim reduced to one thick stroke; bubble and sparkle retained as magical emissions, not an applied status badge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72f64d5e-456e-45c1-80a8-12d9cbe19516'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/35-72f64d5e-456e-45c1-80a8-12d9cbe19516.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bubbling-magic-cauldron'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('bubbling', 'magic', 'cauldron')

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
        poly('rim',(6,20),(10,20),(38,20),(42,20))
        path('bowl',(10,20),[('L',(10,26)),('C',(15,36),(10,30),(12,33)),('C',(24,40),(18,39),(20,40)),('C',(33,36),(28,40),(30,39)),('C',(38,26),(36,33),(38,30)),('L',(38,20))]);join('rim','bowl')
        for s in (-1,1):line(f'foot-{s}',(24+s*9,36),(24+s*13,42));join('bowl',f'foot-{s}')
        circle('bubble',14,8,2)
        poly('magic-h',(30,8),(34,8),(38,8));poly('magic-v',(34,6),(34,8),(34,12));join('magic-h','magic-v')
