"""Balanced the smaller fish against a seated person, using a curved fishing rod, fine clear line and explicit stool.
The rejected fish is oversized and the body and fishing line merge into an ambiguous shape. Restore the seated angler, stool and suspended catch.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '773496ab-eaad-56ae-8665-60874f75a398'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-angler-with-catch/20260929T084651Z-thuan-mac/reference/fishing sit_773496ab-eaad-56ae-8665-60874f75a398.svg'
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
    icon_id = 'seated-angler-with-catch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('fishing', 'sit')

    def build(self):
        s=self
        # Plan: right-facing seated body on stool, left arcing rod, hanging fish at left.
        circle(s,'head',35,10,5)
        s.add_line('torso',(35,23),(35,33))
        s.add_polyline('leg',(35,33),(25,33),(24,44))
        s.add_polyline('arm',(35,23),(29,28),(22,23))
        for p in ('leg','arm'): s.relate('connect','torso',p)
        path(s,'rod',(22,23),('C',(7,5),(19,12),(13,5)))
        s.add_line('line',(7,5),(7,24));s.relate('connect','line','rod')
        path(s,'fish',(7,24),('C',(7,36),(0,28),(2,33)),('C',(7,24),(12,32),(13,28)),closed=True)
        s.relate('connect','line','fish')
        s.add_polyline('tail',(7,36),(3,41),(11,41),(7,36),closed=True);s.relate('connect','tail','fish')
        s.add_polyline('stool',(33,41),(43,41),(43,46))
        s.mark_human_figure('angler',head='head',torso='torso',torso_junction='start')
