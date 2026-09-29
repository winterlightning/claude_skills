"""Added a curved wind-filled sail, diagonal mast and boom, shallow board hull and smooth water.
The rejected straight triangle and disconnected bars lose the leaning mast, curved sail and board-like hull. Restore that sailing silhouette.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6e5eb979-36c1-4127-b9b4-93312561e604'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sailboard-on-waves/20260929T084651Z-thuan-mac/reference/nautic sports sailing_6e5eb979-36c1-4127-b9b4-93312561e604.svg'
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
    icon_id = 'sailboard-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('nautic', 'sports', 'sailing')

    def build(self):
        s=self
        # Plan: curved sail on a leaning mast; shallow hull and regular wave rhythm.
        path(s,'sail',(19,4),('C',(7,29),(9,10),(7,18)),('L',(26,24)),('L',(19,4)),closed=True)
        s.add_line('mast',(26,24),(29,33));s.relate('connect','mast','sail')
        s.add_line('boom',(8,22),(29,16));s.relate('connect','boom','sail')
        path(s,'board',(8,35),('L',(42,29)),('C',(29,38),(41,36),(35,38)))
        path(s,'water',(4,42),('C',(14,39),(8,42),(11,42)),('C',(24,42),(17,42),(20,42)),('C',(34,39),(28,42),(31,42)),('C',(44,42),(37,42),(40,42)))
