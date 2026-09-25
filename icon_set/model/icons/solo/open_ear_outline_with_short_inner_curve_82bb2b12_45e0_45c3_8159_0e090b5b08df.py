"""Open Ear Outline with Short Inner Curve
Plan: Open outer ear and separate inner fold; source right-side opening retained.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide ear: broad curves and reduced inner anatomy.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82bb2b12-45e0-45c3-8159-0e090b5b08df'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/e car location finding_82bb2b12-45e0-45c3-8159-0e090b5b08df.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-ear-outline-with-short-inner-curve'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('ear', 'hearing', 'curve', 'outline', 'fold', 'auditory', 'anatomy')

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
        path('ear',(40,10),[('C',(24,4),(36,6),(30,4)),('A',(8,20),16,16,False),('C',(23,44),(8,32),(18,38))])
        path('fold',(18,21),[('C',(34,18),(20,10),(29,11))])
