"""Added rounded shoulders with inward-curving hands and a low crossing-leg silhouette, preserving the upright meditating head.
The rejected torso forms an angular tent over a large X; the hands and curved arms disappear. Restore relaxed inward-curving arms and lotus legs.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ded0b984-4a7d-5b44-8214-e8c48cf563e0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-meditation-curved-arms/20260929T084651Z-thuan-mac/reference/yoga meditate_ded0b984-4a7d-5b44-8214-e8c48cf563e0.svg'
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
    icon_id = 'seated-meditation-curved-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('yoga', 'meditate')

    def build(self):
        s=self
        # Plan: mirrored shoulders/curved forearms, separate hands, crossed seated legs.
        circle(s,'head',24,9,5)
        s.add_line('torso',(24,22),(24,32))
        for side,sgn in [('left',-1),('right',1)]:
            p=lambda x,y:(24+sgn*x,y)
            path(s,'arm-'+side,(24,22),('C',p(15,30),p(10,22),p(15,23)),('C',p(7,33),p(15,35),p(10,33)))
            s.relate('connect','torso','arm-'+side)
        s.relate('connect','arm-left','arm-right')
        path(s,'leg-front',(8,36),('L',(37,44)),('C',(41,37),(43,45),(44,40)),('L',(35,35)))
        path(s,'leg-back',(8,36),('C',(7,44),(2,36),(3,43)),('L',(20,40)))
        s.relate('connect','leg-front','leg-back')
        s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
