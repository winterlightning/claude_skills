"""Standing Coat Rack with Curved Hooks
Plan: Upright coat rack with two paired hook levels and curved foot.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Small top hook reduced to a straight pole tip; both paired hook levels and the curved foot retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfa1bba1-5b3f-4d10-8cf0-3b1b181af313'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/coat rack_cfa1bba1-5b3f-4d10-8cf0-3b1b181af313.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-coat-rack-with-curved-hooks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('coat-rack', 'hooks', 'stand', 'furniture', 'clothes', 'pole', 'storage')

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
        self.add_line('pole',(24,4),(24,41))
        path('foot',(8,44),[('C',(24,41),(8,41),(16,41)),('C',(40,44),(32,41),(40,41))]);self.relate('connect','foot','pole')
        for y,w in ((16,16),(32,10)):
         path(f'hooks-{y}',(24-w,y-7),[('C',(24,y),(24-w,y),(20,y)),('C',(24+w,y-7),(28,y),(24+w,y))]);self.relate('connect',f'hooks-{y}','pole')
