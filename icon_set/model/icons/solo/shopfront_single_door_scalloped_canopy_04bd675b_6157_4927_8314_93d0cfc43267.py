"""Storefront with Scalloped Awning
Plan: Broad scalloped canopy and single central doorway in compact shop facade.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Three scallops instead of four, and a smaller doorway opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04bd675b-6157-4927-8314-93d0cfc43267'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/salon_04bd675b-6157-4927-8314-93d0cfc43267.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shopfront-single-door-scalloped-canopy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('storefront', 'salon', 'shop', 'awning', 'door', 'building')

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
        path('awning',(10,6),[('L',(38,6)),('L',(42,16)),('C',(38,22),(42,20),(40,22)),('C',(30,20),(35,22),(34,23)),('C',(18,20),(26,24),(22,24)),('C',(10,22),(14,23),(13,22)),('C',(6,16),(8,22),(6,20)),('L',(10,6))],True)
        path('walls',(10,22),[('L',(10,38)),('A',(14,42),4,4,False),('L',(20,42)),('L',(20,36)),('A',(28,36),4,4,True),('L',(28,42)),('L',(34,42)),('A',(38,38),4,4,False),('L',(38,22))]);join('walls','awning')
