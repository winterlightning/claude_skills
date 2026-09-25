"""Flying Bird Carrying Taped Parcel
Plan: An uplifted wing and rightward bird silhouette connect to a parcel below. Intentional directional asymmetry.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide bird: unified head, wing and tail silhouette.
Reduction: Omitted parcel tape and bird eye to preserve open regions; retained delivery parcel.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a59b9a96-1dec-40f6-8f00-593c3fe69eb2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dropshipper bird box_a59b9a96-1dec-40f6-8f00-593c3fe69eb2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flying-bird-carrying-taped-parcel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('bird', 'parcel', 'delivery', 'box', 'wing', 'flight', 'package')

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
        path('bird',(6,6),[('C',(24,16),(20,6),(24,8)),('A',(36,12),7,7,True),('L',(42,16)),('L',(36,20)),('C',(20,28),(35,29),(29,29)),('L',(6,28)),('L',(12,20)),('C',(6,6),(8,18),(6,12))],True)
        path('parcel',(20,28),[('L',(34,28)),('L',(34,42)),('L',(20,42)),('L',(20,28))],True)
        self.relate('connect','bird-4','parcel-0');self.relate('connect','bird-4','parcel-3')
        self.relate('connect','bird-5','parcel-0');self.relate('connect','bird-5','parcel-3')
