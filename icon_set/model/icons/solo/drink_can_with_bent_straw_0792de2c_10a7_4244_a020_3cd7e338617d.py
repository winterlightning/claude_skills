"""Drink Can with Bent Straw
Plan: Plain drink can with narrowed rim and bent straw.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0792de2c-10a7-4244-a020-3cd7e338617d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/softdrink_0792de2c-10a7-4244-a020-3cd7e338617d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'drink-can-with-bent-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('can', 'drink', 'straw', 'soda', 'beverage', 'container')

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
        path('can',(12,16),[('L',(36,16)),('C',(40,23),(36,20),(40,20)),('L',(40,39)),('A',(35,44),5,5,True),('L',(13,44)),('A',(8,39),5,5,True),('L',(8,23)),('C',(12,16),(8,20),(12,20))],True)
        self.add_line('rim',(8,24),(40,24));self.relate('connect','rim','can')
        self.add_polyline('straw',(28,16),(31,7),(40,4));self.relate('connect','straw','can')
