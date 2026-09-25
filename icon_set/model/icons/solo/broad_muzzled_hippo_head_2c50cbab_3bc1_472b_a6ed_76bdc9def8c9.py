"""Broad Muzzled Hippo Head
Plan: Broad front-facing hippo muzzle, tall forehead and mirrored ears.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Lower lip merged into the broad muzzle; small round ears retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c50cbab-3bc1-472b-a6ed-76bdc9def8c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hippopotamus_2c50cbab-3bc1-472b-a6ed-76bdc9def8c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-muzzled-hippo-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hippo', 'hippopotamus', 'head', 'muzzle', 'animal', 'mammal')

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
        path('head',(12,23),[('L',(12,14)),('C',(6,10),(8,14),(6,13)),('C',(10,6),(6,7),(7,6)),('C',(17,10),(13,6),(16,7)),('C',(24,9),(19,9),(21,9)),('C',(31,10),(27,9),(29,9)),('C',(38,6),(32,7),(35,6)),('C',(42,10),(41,6),(42,7)),('C',(36,14),(42,13),(40,14)),('L',(36,23))])
        path('muzzle',(12,23),[('L',(36,23)),('A',(42,29),6,6,True),('L',(42,34)),('A',(34,42),8,8,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,29)),('A',(12,23),6,6,True)],True);join('head','muzzle')
