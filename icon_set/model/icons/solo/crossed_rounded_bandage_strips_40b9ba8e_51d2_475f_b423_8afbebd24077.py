"""Crossed Rounded Bandage Strips
Plan: Two broad bandage strips crossing at right angles
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful Lucide match; rounded diagonal strips.
Reduction: Omit central pad seam to keep overlap clean."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40b9ba8e-51d2-475f-b423-8afbebd24077'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/chafe_40b9ba8e-51d2-475f-b423-8afbebd24077.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-rounded-bandage-strips'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bandage', 'strips', 'crossed', 'first-aid', 'medical', 'adhesive', 'care')

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
        path('front',(6,12),[('C',(12,6),(6,8),(8,6)),('C',(16,8),(14,6),(14,6)),('L',(40,32)),('C',(42,36),(42,34),(42,34)),('C',(36,42),(42,40),(40,42)),('C',(32,40),(34,42),(34,42)),('L',(8,16)),('C',(6,12),(6,14),(6,14))],True)
        path('back-top',(24,16),[('L',(32,8)),('C',(36,6),(34,6),(34,6)),('C',(42,12),(40,6),(42,8)),('C',(40,16),(42,14),(42,14)),('L',(32,24))]);self.relate('connect','front','back-top')
        path('back-bottom',(24,32),[('L',(16,40)),('C',(12,42),(14,42),(14,42)),('C',(6,36),(8,42),(6,40)),('C',(8,32),(6,34),(6,34)),('L',(16,24))]);self.relate('connect','front','back-bottom')
