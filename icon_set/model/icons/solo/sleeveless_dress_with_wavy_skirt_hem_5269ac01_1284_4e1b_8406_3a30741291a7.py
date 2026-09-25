"""Sleeveless Dress with Wavy Skirt Hem
Plan: Rounded sleeveless bodice, waist seam and flared wavy skirt.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide shirt: single coherent garment silhouette.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5269ac01-1284-4e1b-8406-3a30741291a7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dirndl_5269ac01-1284-4e1b-8406-3a30741291a7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sleeveless-dress-with-wavy-skirt-hem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dress', 'sleeveless', 'skirt', 'bodice', 'clothing', 'garment', 'hem')

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
        path('bodice',(10,4),[('L',(18,4)),('A',(30,4),6,6,False),('L',(38,4)),('C',(31,23),(38,13),(33,18)),('L',(17,23)),('C',(10,4),(15,18),(10,13))],True)
        path('skirt',(17,23),[('C',(8,40),(12,30),(8,36)),('C',(13,44),(8,44),(10,44)),('C',(24,40),(18,44),(19,40)),('C',(35,44),(29,40),(30,44)),('C',(40,40),(38,44),(40,44)),('C',(31,23),(40,36),(36,30))]);self.relate('connect','bodice','skirt')
