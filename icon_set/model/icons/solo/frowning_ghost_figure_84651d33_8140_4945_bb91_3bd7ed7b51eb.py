"""Spooky Ghost Figure.

Plan: Rounded ghost robe, hollow eyes and frown; bounds (6,6)-(42,42).
Construction: Lucide ghost: single rounded outer silhouette and sparse eye marks.
Reduction: Arm seams omitted and shoulders consolidated into the robe; eye circles rendered as solid marks at this stroke weight; frown retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84651d33-8140-4945-bb91-3bd7ed7b51eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/06-84651d33-8140-4945-bb91-3bd7ed7b51eb.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'frowning-ghost-figure'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('frowning', 'ghost', 'figure')

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
        path('ghost',(6,42),[('L',(6,24)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('L',(42,42)),('L',(6,42))],True)
        circle('eye-left',18,22,2);circle('eye-right',30,22,2)
        path('frown',(20,33),[('C',(28,33),(21,31),(27,31))])
