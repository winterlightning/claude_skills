"""Side-view pedestal toilet with a tall rounded tank, shared seat line, curved basin, and base. The source controls the proportion; no exact Lucide toilet match was needed."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cefe27aa-2dce-47c4-a0c4-096ec78be130'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__side-view-pedestal-toilet/20260927T172707Z-thuan-mac-1/reference/bidet_cefe27aa-2dce-47c4-a0c4-096ec78be130.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-pedestal-toilet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('toilet', 'bathroom', 'cistern', 'bowl', 'plumbing', 'pedestal', 'restroom')

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
        # Tall tank and wider rounded basin share the seat line.
        path('cistern',(6,26),[('L',(6,9)),('A',(9,6),3,3,True),('L',(17,6)),('A',(20,9),3,3,True),('L',(20,26))])
        path('bowl',(6,26),[('L',(42,26)),('C',(32,35),(42,32),(38,35)),('L',(32,42)),('L',(16,42)),('L',(16,35)),('C',(6,26),(10,35),(6,32))],True);self.relate('connect','bowl','cistern')
