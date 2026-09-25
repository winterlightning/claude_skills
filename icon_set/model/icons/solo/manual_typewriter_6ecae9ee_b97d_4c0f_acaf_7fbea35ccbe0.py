"""Classic Manual Typewriter.

Plan: Sheet behind carriage with central indentation and broad tapered base;6..42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Removed tiny carriage end strokes; retained central curved cutout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ecae9ee-b97d-4c0f-acaf-7fbea35ccbe0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/45-6ecae9ee-b97d-4c0f-acaf-7fbea35ccbe0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'manual-typewriter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('manual', 'typewriter')

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
        path('sheet',(14,18),[('L',(14,10)),('A',(18,6),4,4,True),('L',(30,6)),('A',(34,10),4,4,True),('L',(34,18))])
        path('carriage',(6,18),[('L',(42,18)),('L',(42,28)),('L',(32,28)),('C',(16,28),(29,36),(19,36)),('L',(6,28)),('L',(6,18))],True);join('sheet','carriage')
        path('base',(8,28),[('L',(6,38)),('A',(10,42),4,4,False),('L',(38,42)),('A',(42,38),4,4,False),('L',(40,28))]);join('base','carriage')
