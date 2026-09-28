"""Standing Hook Beaked Vulture
Plan: Upright vulture with heavy hooked beak and long pointed folded wing.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Inner wing/tail notch simplified after spacing review; long wing silhouette and hooked head retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ca9c99f-67fa-4938-86d8-fb6ec5827812'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/buzzard_3ca9c99f-67fa-4938-86d8-fb6ec5827812.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-hook-beaked-vulture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('vulture', 'bird', 'beak', 'wing', 'scavenger', 'wildlife', 'standing')

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
        path('vulture',(8,38),[('C',(17,22),(9,31),(12,25)),('L',(18,14)),('C',(28,4),(15,7),(20,4)),('C',(40,14),(36,4),(39,8)),('L',(31,12)),('C',(32,28),(28,15),(36,22)),('L',(22,40)),('L',(14,40)),('L',(8,38))],True)
        self.add_polyline('leg',(27,34),(30,44),(37,44));self.relate('connect','leg','vulture')
