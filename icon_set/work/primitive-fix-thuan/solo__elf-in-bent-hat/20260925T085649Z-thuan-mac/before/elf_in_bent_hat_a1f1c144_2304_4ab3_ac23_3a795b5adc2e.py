"""Elf face with pointed hat.

Plan: Elf with circular jaw, tall bent hat and pointed ears. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Pointed ears become short single strokes; omit parted hair to preserve the bent hat and circular jaw.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1f1c144-2304-4ab3-ac23-3a795b5adc2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/49-a1f1c144-2304-4ab3-ac23-3a795b5adc2e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'elf-in-bent-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('elf', 'in', 'bent', 'hat')

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
        path('hat',(10,28),[('L',(10,22)),('A',(26,6),16,16,True),('L',(34,6)),('L',(42,14)),('L',(30,14)),('L',(38,28)),('L',(10,28))],True)
        path('jaw',(10,28),[('A',(38,28),14,14,False)]);join('hat','jaw')
        for s in (-1,1):
         x=lambda v:24+s*v
         poly(f'ear-{s}',(x(14),28),(x(18),20));join('hat',f'ear-{s}');join('jaw',f'ear-{s}')
