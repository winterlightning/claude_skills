"""Female Demon with Wings and Horns.

Plan: Horned fairy-like demon figure with dress, bat wings and curved arrow tail. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Retain horns, bat wings, skirt and arrow tail; omit tiny feet and arm seams. Circular head detached by 4 ink units.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f764c646-54bb-44f8-8f0a-660266f16f3d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/04-f764c646-54bb-44f8-8f0a-660266f16f3d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'winged-female-demon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('winged', 'female', 'demon')

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
        circle('head',24,11,4)
        for x in (20,28):line(f'horn-{x}',(x,11),(x,6));join('head',f'horn-{x}')
        path('torso',(24,23),[('L',(24,27)),('L',(24,33))]);self.mark_human_figure('demon',head='head',torso='torso-0',torso_junction='start')
        poly('dress',(16,42),(24,33),(32,42),closed=True);join('torso','dress')
        for s in (-1,1):
         x=lambda v:24+s*v
         poly(f'wing-{s}',(x(0),27),(x(18),20),(x(15),31));join('torso',f'wing-{s}')
        join('wing--1','wing-1')
        path('tail',(32,42),[('A',(42,32),10,10,False)]);join('dress','tail')
        poly('tip',(37,32),(42,32),(42,37));join('tail','tip')
