"""Grand Piano Musical Instrument.

Plan: Grand piano with curved lid/body above full-width keyboard and two legs; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Dense key divisions reduced to three equally spaced divisions; both piano legs retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be85a6be-6f3c-4b29-80e7-c3cf2c4726e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/36-be85a6be-6f3c-4b29-80e7-c3cf2c4726e0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'grand-piano-with-keyboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('grand', 'piano', 'with', 'keyboard')

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
        path('body',(6,28),[('L',(6,16)),('A',(16,6),10,10,True),('C',(29,18),(25,6),(24,18)),('C',(42,28),(33,20),(42,20)),('L',(6,28))],True)
        poly('keyboard',(6,28),(6,36),(12,36),(34,36),(42,36),(42,28));join('body','keyboard')
        for j,x in enumerate((15,24,33)):
         line(f'key-{j}',(x,28),(x,36));join('body',f'key-{j}');join('keyboard',f'key-{j}')
        line('leg-left',(12,36),(12,42));line('leg-right',(34,36),(34,42));join('keyboard','leg-left');join('keyboard','leg-right')
