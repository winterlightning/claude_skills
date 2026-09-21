"""Large Ear Terrier Head
Plan: Large rounded upright ears lead into a short square muzzle. Mirrored contours retain terrier proportions.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide dog: wide facial space and minimal marks.
Reduction: Removed interior ear seams and cheek splits; retained oversized ears and short muzzle.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30852f42-8904-49f5-8f30-405d2200041b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boston terrier_30852f42-8904-49f5-8f30-405d2200041b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'large-ear-terrier-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('dog', 'terrier', 'head', 'ears', 'canine', 'pet', 'muzzle')

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
        path('head',(8,17),[('C',(12,4),(8,8),(9,4)),('C',(19,16),(16,4),(18,10)),('L',(29,16)),('C',(36,4),(30,10),(32,4)),('C',(40,17),(39,4),(40,8)),('C',(36,31),(40,25),(36,27)),('L',(36,38)),('A',(30,44),6,6,True),('L',(18,44)),('A',(12,38),6,6,True),('L',(12,31)),('C',(8,17),(12,27),(8,25))],True)
        self.add_dot('eye-left',(20,26));self.add_dot('eye-right',(28,26));self.add_dot('nose',(24,35))
