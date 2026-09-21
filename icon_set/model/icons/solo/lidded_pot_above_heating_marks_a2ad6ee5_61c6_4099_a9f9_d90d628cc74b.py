"""Lidded Pot above Heating Marks
Plan: Lidded pot over three heating marks and a stove baseline
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide cooking-pot.
Reduction: Knob reduced to stem; heating marks remain attached to stove."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2ad6ee5-61c6-4099-a9f9-d90d628cc74b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stove induction pot_a2ad6ee5-61c6-4099-a9f9-d90d628cc74b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lidded-pot-above-heating-marks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pot', 'lid', 'heat', 'induction', 'cooking', 'kitchen')

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
        path('pot',(8,12),[('L',(8,24)),('A',(12,28),4,4,False),('L',(36,28)),('A',(40,24),4,4,False),('L',(40,12))])
        self.add_line('lid',(8,12),(40,12));self.relate('connect','lid','pot');self.add_line('knob',(24,4),(24,12));self.relate('connect','knob','lid')
        self.add_line('stove',(8,44),(40,44))
        for x in (16,24,32):self.add_line(f'heat-{x}',(x,36),(x,44));self.relate('connect',f'heat-{x}','stove')
