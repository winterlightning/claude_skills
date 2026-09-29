"""Rebuilt the adult chair and seated posture with a smaller child placed above the adult thigh.
The rejected disconnected figures look like two unrelated seated adults. Restore a visibly smaller child seated on the adult lap and the chair.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5dbb97a5-f916-427b-894f-bc9f6c7b6886'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-adult-with-child/20260929T084651Z-thuan-mac/reference/seat child_5dbb97a5-f916-427b-894f-bc9f6c7b6886.svg'
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
    icon_id = 'seated-adult-with-child'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('seat', 'child')

    def build(self):
        s=self
        # Plan: adult and child share lap relationship, with distinct head radii and coherent limbs.
        circle(s,'adult-head',13,9,5)
        s.add_line('adult-torso',(13,22),(15,32))
        s.add_polyline('adult-leg',(15,32),(27,32),(31,44))
        s.relate('connect','adult-torso','adult-leg')
        path(s,'chair',(5,24),('L',(5,35)),('A',(11,41),6,6,False),('L',(20,41)))
        circle(s,'child-head',31,16,3)
        s.add_line('child-torso',(31,27),(32,32))
        s.add_polyline('child-leg',(32,32),(37,33),(41,40))
        s.relate('connect','child-torso','child-leg')
        s.add_line('holding-arm',(15,25),(24,28))
        s.mark_human_figure('adult',head='adult-head',torso='adult-torso',torso_junction='start')
        s.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
