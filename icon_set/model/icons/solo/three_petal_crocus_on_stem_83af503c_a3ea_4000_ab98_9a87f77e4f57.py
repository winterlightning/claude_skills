"""Three Petal Crocus on Stem
Plan: Three upright petals form one crown; central stem and paired leaves share x24.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide sprout: paired leaves attached to one stem.
Reduction: Omitted interior petal seams and used open leaves to keep the flower clear.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83af503c-a3ea-4000-ab98-9a87f77e4f57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crocus_83af503c-a3ea-4000-ab98-9a87f77e4f57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-petal-crocus-on-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('flower', 'crocus', 'petal', 'stem', 'leaf', 'plant', 'bloom')

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
        path('flower',(24,28),[('C',(10,10),(10,28),(10,18)),('L',(18,15)),('L',(24,4)),('L',(30,15)),('L',(38,10)),('C',(24,28),(38,18),(38,28))],True)
        self.add_line('stem',(24,28),(24,44));self.relate('connect','stem','flower-0');self.relate('connect','stem','flower-5')
        for name,x in [('left',8),('right',40)]:
            self.add_line(name,(24,44),(x,35));self.relate('connect',name,'stem')
        self.relate('connect','left','right')
