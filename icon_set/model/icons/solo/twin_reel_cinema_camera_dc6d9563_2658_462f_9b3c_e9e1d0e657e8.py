'twin-reel-cinema-camera. Plan: Two equal reel circles above rounded camera body and right flared lens. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide video: body/lens attachment. Reduction: Reduced reels to two small detached circles; kept camera body and flared lens.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc6d9563-2658-462f-9b3c-e9e1d0e657e8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cinema_dc6d9563-2658-462f-9b3c-e9e1d0e657e8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twin-reel-cinema-camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('camera', 'cinema', 'reels', 'film', 'movie', 'lens', 'video')

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
        rect('body',4,24,26,16,4)
        for x in (8,24):
         circle(f'reel-{x}',x,12,4)
        path('lens',(30,28),[('L',(44,22)),('L',(44,40)),('L',(30,36))]);self.relate('connect','body','lens')
