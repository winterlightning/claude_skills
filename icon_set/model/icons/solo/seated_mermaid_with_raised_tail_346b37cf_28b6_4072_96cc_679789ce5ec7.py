"""Sitting Fantasy Mermaid.

Plan: Seated mermaid with supporting arm, fish tail and two forked fluke strokes; bounds (6,6)-(42,42).
Construction: Shared full_body_ref.png: circle head and stick torso, exact4 ink gap; fish tail identifies mermaid.
Reduction: Hair omitted and flukes reduced to two broad strokes; supporting arm and seated tail retained; forward arm omitted to keep the torso opening clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '346b37cf-28b6-4072-96cc-679789ce5ec7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/05-346b37cf-28b6-4072-96cc-679789ce5ec7.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'seated-mermaid-with-raised-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('seated', 'mermaid', 'with', 'raised', 'tail')

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
        circle('head',17,10,4);line('torso',(17,22),(17,32));self.mark_human_figure('mermaid',head='head',torso='torso',torso_junction='start')
        poly('support-arm',(17,22),(8,25),(6,42));join('torso','support-arm')
        path('tail',(17,32),[('C',(33,42),(20,40),(27,42)),('C',(40,32),(39,42),(40,38)),('L',(40,26)),('L',(32,26)),('C',(25,31),(32,29),(28,31)),('L',(17,32))],True);join('torso','tail')
        line('fluke-left',(32,26),(26,18));line('fluke-right',(40,26),(42,16));join('tail','fluke-left');join('tail','fluke-right')
