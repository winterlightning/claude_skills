"""Striped Winged Insect
Plan: Mirrored insect with head, antennae, paired wings and tapered striped abdomen.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No direct match; repeated mirrored curves.
Reduction: Legs and one abdominal stripe omitted; head and body share one continuous outline with paired wings and antennae."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90fc40b4-507f-4dc2-be3c-14fdfadec7e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gnat_90fc40b4-507f-4dc2-be3c-14fdfadec7e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'striped-winged-insect'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('insect', 'bee', 'wings', 'antennae', 'striped', 'bug')

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
        path('body',(20,14),[('C',(18,10),(18,13),(18,12)),('C',(24,6),(18,6),(21,6)),('C',(30,10),(27,6),(30,6)),('C',(28,14),(30,12),(30,13)),('L',(30,22)),('L',(30,30)),('C',(24,42),(30,36),(27,40)),('C',(18,30),(21,40),(18,36)),('L',(18,22)),('L',(20,14))],True)
        line('band',(18,30),(30,30));join('band','body')
        line('antenna-left',(18,10),(15,6));line('antenna-right',(30,10),(33,6));join('antenna-left','body');join('antenna-right','body')
        path('left-wing',(18,22),[('C',(6,22),(12,20),(6,18)),('C',(18,30),(6,28),(10,34))]);join('left-wing','body')
        path('right-wing',(30,22),[('C',(42,22),(36,20),(42,18)),('C',(30,30),(42,28),(38,34))]);join('right-wing','body')
