"""Redrew a single bowed sail, a shallow curved boat hull and two broad waves, removing the invented crossbar.
The rejected straight triangular sail and extra crossbar replace the reference curved sail. Restore the distinctive bowed sail above the hull.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b61a055f-e1d4-4f45-b688-2b287b42a5a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sailboat-on-waves/20260929T084651Z-thuan-mac/reference/boat_b61a055f-e1d4-4f45-b688-2b287b42a5a9.svg'
AUTHOR = 'gpt-6'

def path(s, name, start, *steps, closed=False):
    members=[]; here=start
    for i, step in enumerate(steps):
        kind, end, *p = step
        ident=f'{name}-{i}'
        if kind == 'L': s.add_line(ident, here, end)
        elif kind == 'A': s.add_arc(ident, here, end, radius_x=p[0], radius_y=p[1], sweep=p[2])
        elif kind == 'C': s.add_bezier(ident, here, (p[0], p[1], end))
        members.append(ident); here=end
    s.add_contour(name, *members, closed=closed)

def circle(s, name, x, y, r):
    path(s,name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

class Drawing(Solo48):
    icon_id = 'sailboat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('boat',)

    def build(self):
        s=self
        # Plan: single bowed sail, shallow hull, visibly detached wave band.
        path(s,'sail',(17,4),('C',(37,23),(28,5),(36,13)),('L',(22,25)),('L',(17,4)),closed=True)
        path(s,'hull',(4,33),('L',(44,33)),('C',(39,38),(43,35),(41,37)))
        path(s,'hull-left',(4,33),('C',(9,38),(5,35),(7,37)));s.relate('connect','hull','hull-left')
        path(s,'water',(5,44),('C',(15,42),(9,45),(12,44)),('C',(25,44),(18,44),(21,45)),('C',(35,42),(29,45),(32,44)),('C',(43,44),(38,44),(41,45)))
