"""Seated Orangutan Front View
Plan: Frontal ape with blank muzzle and rounded paired knees.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Ear loops omitted; muzzle and paired knees regularized to round outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '014fc7d1-8818-495c-9f61-d1612dae4e23'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/orangutan_014fc7d1-8818-495c-9f61-d1612dae4e23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-orangutan-front-view'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('orangutan', 'primate', 'ape', 'seated', 'animal', 'mammal')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('body',(6,42),[('L',(6,31)),('C',(10,23),(6,27),(8,25)),('L',(10,20)),('A',(24,6),14,14,True),('A',(38,20),14,14,True),('L',(38,23)),('C',(42,31),(40,25),(42,27)),('L',(42,42)),('L',(6,42))],True)
        circle('muzzle',24,20,5)
        for x in (17,31):circle(f'knee-{x}',x,39,3);self.relate('connect',f'knee-{x}','body')
