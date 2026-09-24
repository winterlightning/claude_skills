"""Fairy with Butterfly Wings.

Plan: Fairy round head, detached torso/skirt and open butterfly-wing contours. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Open lobed wing contours preserve butterfly form; omit tiny feet. Circular head has exactly 4 ink units to torso.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f2464f7-258f-5a66-a48b-a08297ea0c92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/01-9f2464f7-258f-5a66-a48b-a08297ea0c92.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fairy-with-butterfly-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fairy', 'with', 'butterfly', 'wings')

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
        circle('head',24,10,4)
        path('torso',(24,22),[('L',(24,26)),('L',(24,32))]);self.mark_human_figure('fairy',head='head',torso='torso-0',torso_junction='start')
        poly('skirt',(16,42),(24,32),(32,42),closed=True);join('torso','skirt')
        for s in (-1,1):
         x=lambda v:24+s*v
         path(f'wing-{s}',(24,26),[('C',(x(18),18),(x(8),19),(x(18),12)),('C',(x(14),25),(x(18),22),(x(18),24)),('C',(x(18),32),(x(18),27),(x(18),30))]);join('torso',f'wing-{s}')
        join('wing--1','wing-1')
