"""Flexed Arm with Right Elbow
Plan: Flexed arm silhouette: raised fist, forearm, bulging bicep and rounded elbow.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide biceps-flexed plus shared human full-body reference for simple anatomy.
Reduction: Fine thumb and muscle crease details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f54dafb-bff9-43fe-9ef5-197a6f0ab792'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/musculature_2f54dafb-bff9-43fe-9ef5-197a6f0ab792.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flexed-arm-right-elbow'
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
        path('arm',(42,37),[('C',(36,12),(42,27),(39,17)),('C',(26,6),(34,6),(30,6)),('C',(21,14),(21,6),(19,12)),('L',(28,16)),('L',(30,28)),('C',(18,24),(25,22),(23,23)),('C',(6,30),(11,20),(6,25)),('C',(13,42),(6,38),(9,42)),('L',(32,42)),('C',(42,37),(36,42),(42,41))],True)
