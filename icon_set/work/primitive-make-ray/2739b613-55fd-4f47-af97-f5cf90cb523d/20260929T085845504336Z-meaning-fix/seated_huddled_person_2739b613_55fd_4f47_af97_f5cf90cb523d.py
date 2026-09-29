"""Drew a bowed head close to a sloping shoulder, curved seated back, folded leg and embracing arm.
The rejected head floats above a horizontal bar and zigzag. Restore a bowed person embracing raised knees.
Keyshape VRECT_L; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2739b613-55fd-4f47-af97-f5cf90cb523d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-huddled-person/20260929T084651Z-thuan-mac/reference/poverty person_2739b613-55fd-4f47-af97-f5cf90cb523d.svg'
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
    icon_id = 'seated-huddled-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('poverty', 'person')

    def build(self):
        s=self
        # Plan: bowed head, shoulder to back curve, knees and embracing forearm.
        circle(s,'head',25,9,5)
        s.add_bezier('torso',(20,21),((15,33),(10,29),(10,35)))
        path(s,'hips',(10,35),('A',(21,41),7,7,False),('L',(29,30)),('L',(38,43)))
        s.relate('connect','torso','hips')
        s.add_polyline('embracing-arm',(20,21),(34,27),(23,29));s.relate('connect','torso','embracing-arm')
        s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
