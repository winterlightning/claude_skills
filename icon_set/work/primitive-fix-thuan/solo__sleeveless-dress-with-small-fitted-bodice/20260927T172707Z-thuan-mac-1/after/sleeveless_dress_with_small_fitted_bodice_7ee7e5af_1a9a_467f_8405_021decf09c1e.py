"""Sleeveless dress with a shaped neckline, fitted bodice, waist seam, and flared skirt. The source garment controls the proportion; no exact Lucide match was useful."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7ee7e5af-1a9a-467f-8405-021decf09c1e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sleeveless-dress-with-small-fitted-bodice/20260927T172707Z-thuan-mac-1/reference/mantua_7ee7e5af-1a9a-467f-8405-021decf09c1e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sleeveless-dress-with-small-fitted-bodice'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dress', 'sleeveless', 'bodice', 'skirt', 'waist', 'clothing', 'garment')

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
        path('dress',(18,4),[('A',(30,4),6,4,False),('L',(40,4)),('L',(34,21)),('L',(40,41)),('C',(24,44),(35,43),(30,44)),('C',(8,41),(18,44),(13,43)),('L',(14,21)),('L',(8,4)),('L',(18,4))],True)
        self.add_line('waist',(14,21),(34,21));self.relate('connect','dress','waist')
