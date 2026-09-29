"""Rebuilt a long-necked seal with a rounded muzzle, smoothly arched back, broad foreground flipper and tapered rear flipper.
The rejected silhouette has squared elephant-like feet and lacks the seal back and flippers. Restore the raised neck and tapered flipper anatomy.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7188aa8a-305f-404d-bfe3-07ee8f265206'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sea-lion/20260929T084651Z-thuan-mac/reference/seal body_7188aa8a-305f-404d-bfe3-07ee8f265206.svg'
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
    icon_id = 'sea-lion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('seal', 'body')

    def build(self):
        s=self
        # Plan: naturally asymmetric marine mammal, raised head left and sweeping body right.
        path(s,'outline',(10,10),('C',(23,14),(16,0),(23,6)),('L',(23,21)),('C',(43,35),(35,20),(43,25)),('C',(38,44),(45,40),(42,44)),('L',(32,44)),('L',(36,37)),('L',(32,32)),('C',(19,36),(28,35),(25,36)),('C',(8,18),(11,32),(8,25)),('C',(4,14),(3,18),(2,15)),('C',(10,10),(4,12),(7,12)),closed=True)
        path(s,'front-flipper',(19,32),('C',(24,44),(18,38),(20,42)),('C',(13,40),(18,44),(14,43)))
        path(s,'far-flipper',(11,32),('C',(5,39),(10,36),(7,38)),('C',(14,40),(8,41),(11,41)))
        s.add_dot('eye',(14,13))
