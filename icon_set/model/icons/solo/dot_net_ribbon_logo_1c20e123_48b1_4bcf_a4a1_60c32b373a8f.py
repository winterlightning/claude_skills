"""Dot Net Ribbon Logo
Plan: Continuous outlined wave ribbon with two rising ends; abstract logo, no literal text.
Keyshape: HRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c20e123-48b1-4bcf-a4a1-60c32b373a8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/microsoft net logo_1c20e123-48b1-4bcf-a4a1-60c32b373a8f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dot-net-ribbon-logo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('logo', 'ribbon', 'wave', 'dotnet', 'brand', 'symbol')

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
        path('ribbon',(4,38),[('C',(16,10),(9,27),(9,10)),('C',(28,22),(23,10),(24,22)),('C',(36,10),(31,22),(33,10)),('L',(44,10)),('C',(30,38),(39,23),(40,38)),('C',(18,26),(23,38),(22,26)),('C',(12,38),(16,26),(16,38)),('L',(4,38))],True)
