"""Rebuilt five gently pointed oval seeds with distinct orientations and sizes while preserving the scattered layout.
The rejected five identical droplets read as water, not irregular scattered sesame. Restore seed-shaped ovals with varied orientation.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2226eb2f-4348-4488-af27-e4eedbfc8f8c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__scattered-sesame-seed/20260929T084651Z-thuan-mac/reference/sesame_2226eb2f-4348-4488-af27-e4eedbfc8f8c.svg'
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
    icon_id = 'scattered-sesame-seed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('sesame',)

    def build(self):
        s=self
        # Plan: five seed instances, each a smooth asymmetric tapered oval, not a flame.
        path(s,'seed-a',(14,6),('C',(7,20),(5,11),(3,18)),('C',(18,16),(14,24),(20,22)),('C',(14,6),(18,12),(15,10)),closed=True)
        path(s,'seed-b',(31,6),('C',(30,20),(28,11),(26,18)),('C',(42,17),(35,26),(44,22)),('C',(31,6),(43,12),(36,10)),closed=True)
        path(s,'seed-c',(25,23),('C',(19,32),(19,24),(16,29)),('C',(29,32),(21,38),(28,37)),('C',(25,23),(31,28),(27,25)),closed=True)
        path(s,'seed-d',(9,30),('C',(6,42),(6,33),(2,38)),('C',(17,39),(12,47),(19,44)),('C',(9,30),(17,34),(12,33)),closed=True)
        path(s,'seed-e',(40,31),('C',(31,39),(34,31),(31,34)),('C',(42,42),(35,45),(42,46)),('C',(40,31),(47,38),(45,32)),closed=True)
