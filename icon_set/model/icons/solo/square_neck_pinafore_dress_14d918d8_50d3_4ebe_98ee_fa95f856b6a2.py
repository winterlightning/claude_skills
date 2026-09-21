"""Square-Neck Pinafore Dress
Plan: Square neckline, paired straps and broad flaring skirt.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide shirt: connected garment contour.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14d918d8-50d3-4ebe-98ee-fa95f856b6a2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pinafore_14d918d8-50d3-4ebe-98ee-fa95f856b6a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-neck-pinafore-dress'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pinafore', 'dress', 'clothing', 'straps', 'skirt', 'garment')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        self.add_polyline('bodice',(8,4),(20,4),(20,13),(28,13),(28,4),(40,4),(32,23),(16,23),closed=True)
        path('skirt',(16,23),[('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(32,23))]);self.relate('connect','bodice','skirt')
