"""Storefront with Scalloped Awning
Plan: Scalloped awning above a two-panel storefront.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide store: sloped awning and scalloped valance.
Reduction: Five scallops reduced to three broad panels."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72ab6b94-557a-4169-8926-09bd70b7c34f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/book store_72ab6b94-557a-4169-8926-09bd70b7c34f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'storefront-with-scalloped-awning'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('store', 'shop', 'storefront', 'awning', 'retail', 'building', 'commerce')

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
        path('awning',(6,18),[('L',(10,6)),('L',(38,6)),('L',(42,18)),('A',(36,24),6,6,True),('A',(30,18),6,6,True),('A',(24,24),6,6,True),('A',(18,18),6,6,True),('A',(12,24),6,6,True),('A',(6,18),6,6,True)],True)
        # Scalloped silhouette retained without a parallel inner fold.
        self.add_polyline('shop',(12,24),(12,42),(36,42),(36,24));self.relate('connect','shop','awning')
        self.add_line('middle',(24,24),(24,42));self.relate('connect','middle','shop');self.relate('connect','middle','awning')
