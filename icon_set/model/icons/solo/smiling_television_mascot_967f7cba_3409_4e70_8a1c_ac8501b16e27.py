"""A smiling television mascot with aerials and feet.
Plan: SQUARE preserves a broad screen beneath the aerials.
Reduction: Prior inset screen border remains omitted; eyes are dots.
Construction: Lucide tv: rounded cabinet and steep aerial attachment; supplied reference owns expression and feet.
Layout: Mirrored aerials, eyes, feet, and cabinet; aerials attach at explicit top-edge nodes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '967f7cba-3409-4e70-8a1c-ac8501b16e27'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bilibili logo_967f7cba-3409-4e70-8a1c-ac8501b16e27.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'smiling-television-mascot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('television', 'tv', 'mascot', 'smile', 'screen', 'antenna', 'cartoon')

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
        path('tv',(10,10),[('L',(20,10)),('L',(28,10)),('L',(38,10)),('A',(42,14),4,4,True),('L',(42,34)),('A',(38,38),4,4,True),('L',(35,38)),('L',(13,38)),('L',(10,38)),('A',(6,34),4,4,True),('L',(6,14)),('A',(10,10),4,4,True)],True)
        for x,join in [(16,20),(32,28)]:
            self.add_line(f'aerial-{x}',(x,6),(join,10));self.relate('connect',f'aerial-{x}','tv')
        for x in (18,30):self.add_dot(f'eye-{x}',(x,19))
        path('smile',(20,28),[('C',(28,28),(22,30),(26,30))])
        for x in (13,35):self.add_line(f'foot-{x}',(x,38),(x,42));self.relate('connect',f'foot-{x}','tv')
