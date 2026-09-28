"""A Cupid arrow pierces a heart diagonally; one fletching chevron replaces tiny feathers.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '32295af4-defa-5f3c-af21-d930830f3a88'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-pierced-by-arrow/20260927T061835Z-thuan-mac-1/reference/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg'
AUTHOR = 'gpt-6'

class HeartPiercedByArrow(Solo48):
    icon_id = 'heart-pierced-by-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('heart', 'arrow', 'cupid', 'love', 'romance', 'pierced')

    def build(self):
        # Plan: Move the complete heart away from the arrowhead; show the shaft entering and leaving its outline, with the middle naturally hidden behind the heart.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        # The heart takes the visual center; a straight diagonal arrow enters
        # at its lower-left edge and leaves near the upper-right shoulder.
        path('heart',(23,17), [
            ('C',(8,22),(18,7),(8,8)),
            ('C',(24,40),(8,29),(17,35)),
            ('C',(38,22),(31,35),(38,29)),
            ('C',(23,17),(38,8),(28,7)),
        ],True)
        line('arrow-front',(27,25),(42,6))
        poly('arrowhead',(36,6),(42,6),(42,12))
        join('arrow-front','heart');join('arrow-front','arrowhead')
        line('arrow-back',(6,42),(17,31))
        poly('fletching',(6,35),(6,42),(13,42))
        join('arrow-back','heart');join('arrow-back','fletching')
