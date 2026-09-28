"""Low Crescent with Two Sparkles
Plan: Low crescent with two small sparkle crosses
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide moon; sparkles reduced to crossed rays.
Reduction: Four-point stars reduced to open cross rays for clearance."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__low-crescent-with-two-sparkles/20260927T164353Z-thuan-mac-1/reference/astrology stars_2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-crescent-with-two-sparkles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('moon', 'crescent', 'sparkles', 'stars', 'night', 'sky', 'celestial')

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
        # The original has a left facing crescent with both tips pointing right.
        path('moon',(22,6),[
            ('C',(6,30),(10,10),(6,19)),
            ('C',(24,42),(6,38),(14,42)),
            ('C',(28,36),(27,42),(29,39)),
            ('C',(15,25),(25,34),(18,31)),
            ('C',(22,6),(11,18),(14,10)),
        ],True)
        for name,x,y,rx,ry in (('upper-star',36,10,6,4),('lower-star',36,26,4,4)):
            self.add_line(name+'-vertical',(x,y-ry),(x,y+ry))
            self.add_line(name+'-horizontal',(x-rx,y),(x+rx,y))
            self.relate('connect',name+'-vertical',name+'-horizontal')
