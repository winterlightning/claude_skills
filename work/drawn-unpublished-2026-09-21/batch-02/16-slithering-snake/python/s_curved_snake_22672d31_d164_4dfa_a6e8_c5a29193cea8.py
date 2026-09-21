"""S-Curved Snake
Plan: Continuous winding snake with raised rounded head and low tail.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Reconstructed thick ribbon after thin-stroke candidate lost the source silhouette; tight bends require review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22672d31-d164-4dfa-a6e8-c5a29193cea8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/anaconda_22672d31-d164-4dfa-a6e8-c5a29193cea8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 's-curved-snake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('snake', 'serpent', 'reptile', 'anaconda', 'curve', 'tail', 'wildlife')

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
        path('snake',(42,12),[('C',(30,6),(40,6),(34,6)),('C',(28,20),(22,6),(23,15)),('L',(33,25)),('C',(29,30),(39,31),(33,36)),('L',(18,19)),('C',(6,22),(13,14),(6,16)),('C',(12,34),(6,28),(8,30)),('C',(6,42),(20,42),(14,42)),('L',(17,42)),('C',(22,29),(30,39),(26,34)),('L',(15,23)),('C',(12,26),(10,19),(8,22)),('L',(24,37)),('C',(42,29),(33,42),(42,38)),('C',(35,17),(42,23),(40,21)),('C',(36,12),(30,12),(30,12)),('L',(42,12))],True)
