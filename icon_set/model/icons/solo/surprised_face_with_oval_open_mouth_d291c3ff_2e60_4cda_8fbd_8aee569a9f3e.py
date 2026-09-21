"""Surprised Face with Oval Open Mouth
Plan: Round surprised face with two dot eyes and open oval mouth.
Keyshape: CIRCLE; exact inset SOLO48 envelope.
Construction: Lucide baby: simple facial marks inside round face.
Reduction: Fine eyebrows omitted; oval mouth normalized to a circular opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd291c3ff-2e60-4cda-8fbd-8aee569a9f3e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mad 1_d291c3ff-2e60-4cda-8fbd-8aee569a9f3e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'surprised-face-with-oval-open-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('face', 'surprised', 'emoji', 'mouth', 'brows', 'expression', 'round')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        circle('face',24,24,20)
        for x in (16,32):self.add_dot(f'eye-{x}',(x,17))
        circle('mouth',24,30,4)
