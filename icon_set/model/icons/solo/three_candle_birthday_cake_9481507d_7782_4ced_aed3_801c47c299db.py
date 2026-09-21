"""Three Candle Birthday Cake
Plan: Three repeated candles on the cake; axis-centered icing and plate.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide cake: repeated vertical candle strokes.
Reduction: Flames are detached dots; omitted serving line to reserve cake height.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9481507d-7782-4ced-aed3-801c47c299db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cake birthday_9481507d-7782-4ced-aed3-801c47c299db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-candle-birthday-cake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('cake', 'candles', 'birthday', 'icing', 'dessert', 'flames', 'celebration')

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
        path('cake',(6,24),[('L',(12,24)),('L',(24,24)),('L',(36,24)),('L',(42,24)),('L',(42,33)),('L',(42,42)),('L',(6,42)),('L',(6,33)),('L',(6,24))],True)
        for j,x in enumerate([12,24,36]):
            self.add_line(f'candle-{j}',(x,24),(x,14));self.add_dot(f'flame-{j}',(x,6))
            self.relate('connect',f'candle-{j}',f'cake-{j}');self.relate('connect',f'candle-{j}',f'cake-{j+1}')
        path('icing',(6,33),[('C',(24,33),(12,30),(18,36)),('C',(42,33),(30,30),(36,36))])
        for a in ['cake-4','cake-5']:self.relate('connect','icing-1',a)
        for a in ['cake-7','cake-8']:self.relate('connect','icing-0',a)
