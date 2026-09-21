"""Laced Hand Drum
Plan: One tapered drum body below an oval top, with one central lacing V.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide drum: elliptical top and simplified drum shell.
Reduction: Dropped stacked narrow rim bands; kept oval head, tapered shell and lacing.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a331962-eda4-4ed1-bc0b-89186524adb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bongo_0a331962-eda4-4ed1-bc0b-89186524adb9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laced-hand-drum'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/music'
    aliases = ()
    keywords = ('drum', 'bongo', 'percussion', 'music', 'instrument', 'lacing', 'rhythm')

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
        path('drum-top',(8,12),[('A',(40,12),16,8,True),('A',(8,12),16,8,True)],True)
        path('shell',(8,12),[('L',(10,26)),('L',(12,40)),('A',(36,40),12,4,False),('L',(38,26)),('L',(40,12))])
        self.relate('connect','shell-0','drum-top-0');self.relate('connect','shell-0','drum-top-1')
        self.relate('connect','shell-4','drum-top-0');self.relate('connect','shell-4','drum-top-1')
        self.relate('connect','lacing-1','shell-0');self.relate('connect','lacing-1','shell-1')
        self.relate('connect','lacing-2','shell-3');self.relate('connect','lacing-2','shell-4')
        self.add_polyline('lacing',(10,26),(24,40),(38,26))
