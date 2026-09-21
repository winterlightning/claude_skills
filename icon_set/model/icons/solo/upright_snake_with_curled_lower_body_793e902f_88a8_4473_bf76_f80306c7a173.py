"""Upright Snake with Curled Lower Body
Plan: Raised snake head, S-curved neck and curled lower body.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Reconstructed thick snake ribbon with broad head and inward tail; crowded bend remains subject to release review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '793e902f-88a8-4473-bf76-f80306c7a173'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/snake_793e902f-88a8-4473-bf76-f80306c7a173.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-snake-with-curled-lower-body'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('snake', 'reptile', 'coil', 'tail', 'animal', 'serpent')

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
        path('snake',(6,12),[('C',(18,6),(7,7),(13,6)),('C',(27,14),(24,6),(27,8)),('C',(18,29),(27,20),(18,24)),('C',(22,34),(15,35),(18,38)),('C',(35,24),(28,26),(29,24)),('C',(42,34),(42,24),(42,29)),('C',(34,42),(42,39),(39,42)),('L',(28,42)),('C',(34,34),(30,38),(36,39)),('C',(29,33),(34,29),(32,29)),('C',(15,41),(24,40),(21,42)),('C',(9,29),(6,40),(6,34)),('L',(18,16)),('C',(15,13),(22,10),(19,10)),('L',(6,13)),('L',(6,12))],True)
