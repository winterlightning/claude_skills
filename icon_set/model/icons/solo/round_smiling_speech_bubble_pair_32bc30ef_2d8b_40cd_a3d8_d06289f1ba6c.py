"""Round Smiling Speech Bubble Pair
Plan: Smiling round conversation bubble with smaller foreground reply bubble.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Eye strokes reduced to dots; face treated as intrinsic character."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/conversation smile type 1_32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-smiling-speech-bubble-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('chat', 'bubbles', 'smile', 'speech', 'conversation', 'message', 'round')

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
        path('back',(29,29),[('C',(14,32),(26,33),(19,34)),('L',(6,37)),('L',(9,27)),('A',(6,19),14,14,True),('A',(20,6),14,13,True),('A',(34,20),14,14,True)])
        path('front',(42,42),[('L',(34,38)),('A',(24,29),10,9,True),('A',(42,29),9,9,True),('L',(39,35)),('L',(42,42))],True)
        for x in (16,24):self.add_dot(f'eye-{x}',(x,16))
        path('smile',(16,24),[('C',(24,24),(18,27),(22,27))])
        self.relate('connect','back','front')
