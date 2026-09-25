"""Lobed Polyp Form
Plan: One soft five-lobed organic outline encloses one broad inverted-U fold. Asymmetric lower lobes retain organic character.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful exact Lucide match; coherent smooth closed silhouette.
Reduction: Dropped two short lower creases; retained lobed body and central fold.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6512139-3774-4e31-8783-0d31c1ae3da4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/polyp_a6512139-3774-4e31-8783-0d31c1ae3da4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lobed-polyp-form'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('polyp', 'biology', 'organism', 'lobes', 'folds', 'organic')

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
        path('polyp',(24,6),[('C',(34,13),(30,6),(29,12)),('C',(42,22),(40,13),(42,16)),('C',(38,32),(42,28),(38,28)),('C',(30,42),(40,40),(34,42)),('C',(22,39),(26,42),(26,39)),('C',(12,42),(18,39),(18,42)),('C',(8,30),(6,42),(6,35)),('C',(6,20),(8,26),(6,26)),('C',(14,12),(6,14),(10,12)),('C',(24,6),(20,12),(18,6))],True)
        path('fold',(18,28),[('C',(20,24),(20,31),(20,27)),('A',(28,24),4,4,True),('C',(30,28),(28,27),(28,31))])
