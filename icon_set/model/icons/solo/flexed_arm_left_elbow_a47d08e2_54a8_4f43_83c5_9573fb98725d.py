"""Flexed Arm with Left Elbow
Plan: Flexed arm silhouette: raised fist, forearm, bulging bicep and rounded elbow.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide biceps-flexed plus shared human full-body reference for simple anatomy.
Reduction: Fine thumb and muscle crease details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a47d08e2-54a8-4f43-83c5-9573fb98725d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/muscle_a47d08e2-54a8-4f43-83c5-9573fb98725d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flexed-arm-left-elbow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arm', 'bicep', 'muscle', 'flex', 'anatomy', 'strength')

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
        path('arm',(6,37),[('C',(12,12),(6,27),(9,17)),('C',(22,6),(14,6),(18,6)),('C',(27,14),(27,6),(29,12)),('L',(20,16)),('L',(18,28)),('C',(30,24),(23,22),(25,23)),('C',(42,30),(37,20),(42,25)),('C',(35,42),(42,38),(39,42)),('L',(16,42)),('C',(6,37),(12,42),(6,41))],True)
