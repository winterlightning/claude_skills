"""Stepped Crown Molding Cross Section
Plan: Stepped molding section with curved lower profile
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful Lucide match; source cross-section.
Reduction: Omit thin duplicate border."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6aa42ae8-a613-4fcf-ae93-eaac50c90b40'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/molding_6aa42ae8-a613-4fcf-ae93-eaac50c90b40.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stepped-crown-molding-cross-section'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('molding', 'cornice', 'profile', 'trim', 'architecture', 'section', 'corner')

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
        path('section',(6,42),[('L',(6,6)),('L',(42,6)),('L',(42,14)),('L',(34,14)),('L',(34,22)),('A',(22,34),12,12,True),('L',(14,34)),('L',(14,42)),('L',(6,42))],True)
