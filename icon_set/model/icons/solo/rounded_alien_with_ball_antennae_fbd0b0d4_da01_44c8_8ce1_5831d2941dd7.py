"""Rounded Alien with Ball Antennae
Plan: Rounded blank alien body with two feet and ball-tipped antennae.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbd0b0d4-da01-44c8-8ce1-5831d2941dd7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/creature_fbd0b0d4-da01-44c8-8ce1-5831d2941dd7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-alien-with-ball-antennae'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('alien', 'creature', 'antennae', 'space', 'monster', 'body', 'feet')

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
        path('alien',(8,28),[('C',(16,18),(8,23),(12,20)),('C',(24,16),(20,16),(21,16)),('C',(32,18),(27,16),(28,16)),('C',(40,28),(36,20),(40,23)),('L',(40,35)),('C',(36,40),(40,37),(38,39)),('L',(36,44)),('L',(28,44)),('L',(28,38)),('L',(20,38)),('L',(20,44)),('L',(12,44)),('L',(12,40)),('C',(8,35),(10,39),(8,37)),('L',(8,28))],True)
        for x in (12,36):circle(f'ball-{x}',x,7,3)
        for s in (-1,1):self.add_line(f'antenna-{s}',(24+s*8,18),(24+s*12,10));self.relate('connect',f'antenna-{s}','alien');self.relate('connect',f'antenna-{s}',f'ball-{24+s*12}')
