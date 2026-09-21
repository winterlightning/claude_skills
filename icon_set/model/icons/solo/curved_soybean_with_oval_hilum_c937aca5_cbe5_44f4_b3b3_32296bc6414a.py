"""Curved Soybean with Oval Hilum
Plan: Curved diagonal bean with oval hilum.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bean: kidney contour and single interior feature.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c937aca5-cbe5-44f4-b3b3-32296bc6414a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/soybean_c937aca5-cbe5-44f4-b3b3-32296bc6414a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-soybean-with-oval-hilum'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('soybean', 'bean', 'seed', 'food', 'legume', 'hilum')

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
        path('bean',(14,42),[('C',(6,30),(8,42),(6,36)),('C',(15,17),(6,23),(13,25)),('C',(30,6),(16,9),(23,6)),('C',(42,20),(38,6),(42,12)),('C',(14,42),(42,33),(27,42))],True)
        path('hilum',(21,25),[('A',(27,25),3,4,True),('A',(21,25),3,4,True)],True)
