"""Speaker Horn with Three Sound Arcs
Plan: Right-facing speaker with 3 sound arcs; arc count is retained.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: Lucide volume-2: flared speaker and separate sound emanations.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86cb98f9-4d33-4e0a-b25e-f14ba903609e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emitter_86cb98f9-4d33-4e0a-b25e-f14ba903609e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'speaker-horn-with-three-sound-arcs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('speaker', 'sound', 'audio', 'horn', 'waves', 'volume', 'emitter')

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
        path('speaker',(4,20),[('L',(8,20)),('L',(16,8)),('L',(16,40)),('L',(8,28)),('L',(4,28)),('L',(4,20))],True)
        for i in range(3):
         x=26+i*9 if 3==3 else 31+i*13
         y=19-i*5 if 3==3 else 18-i*8
         path(f'wave-{i}',(x-2,y),[('C',(x,24),(x,y+2),(x,22)),('C',(x-2,48-y),(x,26),(x,46-y))])
