"""Oval Seed with Curved Seam
Plan: Upright almond-like seed with wavy central seam.
Keyshape: VRECT_M; exact inset SOLO48 envelope.
Construction: Lucide bean: simple organic enclosing contour.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '950810fc-7530-4b10-b9cb-37e8104497bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/seed_950810fc-7530-4b10-b9cb-37e8104497bc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oval-seed-with-curved-seam'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('seed', 'grain', 'plant', 'seam', 'oval', 'botanical')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('seed',(24,4),[('C',(38,28),(31,7),(38,19)),('C',(24,44),(38,38),(33,44)),('C',(10,28),(15,44),(10,38)),('C',(24,4),(10,19),(17,7))],True)
        path('seam',(24,4),[('C',(24,24),(32,12),(28,18)),('C',(24,44),(18,33),(20,39))]);self.relate('connect','seed','seam')
