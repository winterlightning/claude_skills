"""Gymnast doing a handstand.

Plan: Inverted stick gymnast with split legs and two supporting arms; exact head/torso centerline gap8; bounds (6,6)-(42,42).
Construction: Shared human full_body_ref.png: circular head and simple round-ended limbs; inverted torso axis aligns to head.
Reduction: Converted outlined body to shared stick-figure vocabulary while retaining split legs and two-arm balance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9c85943-9f04-45d6-8250-b8130ceafc94'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/45-f9c85943-9f04-45d6-8250-b8130ceafc94.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gymnast-in-split-leg-handstand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('gymnast', 'in', 'split', 'leg', 'handstand')

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
        circle('head',24,36,4)
        line('torso',(24,24),(24,16));self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
        poly('legs',(6,6),(24,16),(42,6));join('torso','legs')
        poly('arms',(8,42),(8,24),(24,24),(40,24),(40,42));join('torso','arms')
