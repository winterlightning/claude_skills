"""Boxer in Fighting Stance.

Plan: Boxing torso with two coherent bent arms and paired circular gloves; exact detached head gap8 at torso26.
Construction: Human full_body_ref.png: aligned circular head and open action limbs.
Reduction: Smaller left glove guards chest; outlined torso omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7de26cb7-7475-4fc2-9562-2738e9bd49cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/08-7de26cb7-7475-4fc2-9562-2738e9bd49cd.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'boxer-with-raised-gloves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('boxer', 'with', 'raised', 'gloves')

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
        circle('head',20,12,6)
        line('torso',(20,26),(20,42));self.mark_human_figure('boxer',head='head',torso='torso',torso_junction='start')
        poly('left-arm',(20,36),(6,36),(8,26));join('left-arm','torso')
        circle('left-glove',8,24,2);join('left-glove','left-arm')
        poly('right-arm',(20,26),(30,28),(38,24));join('right-arm','torso')
        circle('right-glove',38,20,4);join('right-glove','right-arm')
