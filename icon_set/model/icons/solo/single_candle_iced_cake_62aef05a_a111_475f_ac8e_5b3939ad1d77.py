"""Single Candle Iced Cake
Plan: Single centered candle above a wide rectangular cake. Icing crosses the cake as a shallow wave.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide cake: simple cake slab and single-stroke candles.
Reduction: Flame becomes a detached short stroke; icing remains one wave.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62aef05a-a111-475f-ac8e-5b3939ad1d77'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cake_62aef05a-a111-475f-ac8e-5b3939ad1d77.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-candle-iced-cake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('cake', 'candle', 'birthday', 'icing', 'flame', 'dessert', 'celebration')

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
        self.add_polyline('cake',(6,20),(24,20),(42,20),(42,31),(42,42),(6,42),(6,31),closed=True)
        self.add_line('candle',(24,20),(24,14));self.relate('connect','candle','cake-1');self.relate('connect','candle','cake-2')
        self.add_dot('flame',(24,6))
        path('icing',(6,31),[('C',(24,31),(12,28),(18,34)),('C',(42,31),(30,28),(36,34))])
        for a in ['cake-3','cake-4']:self.relate('connect','icing-1',a)
        for a in ['cake-6','cake-7']:self.relate('connect','icing-0',a)
