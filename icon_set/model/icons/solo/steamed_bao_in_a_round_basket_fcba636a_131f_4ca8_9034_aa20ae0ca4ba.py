"""Steamed Bao in a Round Basket
Plan: Scalloped bun in shallow round steamer, paired steam trails.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide coffee: separate repeated steam.
Reduction: Fine bun pleats and basket band omitted; two mirrored steam wisps retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcba636a-131f-4ca8-9034-aa20ae0ca4ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/asian food bao steam bun dimsum tray_fcba636a-131f-4ca8-9034-aa20ae0ca4ba.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steamed-bao-in-a-round-basket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bao', 'bun', 'steamer', 'steam', 'dumpling', 'food', 'basket')

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
        path('basket',(6,30),[('L',(6,38)),('C',(24,42),(6,42),(18,42)),('C',(42,38),(30,42),(42,42)),('L',(42,30))]);poly('rim',(6,30),(10,30),(38,30),(42,30));join('rim','basket')
        path('bun',(10,30),[('C',(16,24),(10,26),(11,24)),('C',(24,22),(18,19),(22,19)),('C',(32,24),(26,19),(30,19)),('C',(38,30),(37,24),(38,26))]);join('bun','rim')
        for x,s in ((18,1),(30,-1)):path(f'steam-{x}',(x,6),[('C',(x,11),(x+2*s,7),(x-2*s,10))])
