"""Heart with a Curved Smile
Plan: Broad heart enclosing a single curved smile.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: Lucide heart: paired lobes and central notch.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c0883d6-7fdc-48dd-93d9-d18f75562941'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/badoo logo_2c0883d6-7fdc-48dd-93d9-d18f75562941.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heart-with-a-curved-smile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('heart', 'smile', 'happy', 'affection', 'face', 'emotion', 'love')

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
        path('heart',(24,40),[('C',(4,19),(12,34),(4,29)),('A',(14,8),10,11,True),('C',(24,13),(19,8),(21,10)),('C',(34,8),(27,10),(29,8)),('A',(44,19),10,11,True),('C',(24,40),(44,29),(36,34))],True)
        path('smile',(15,20),[('A',(24,29),9,9,False),('A',(33,20),9,9,False)])
