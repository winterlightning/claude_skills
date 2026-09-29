"""Replaced the hat-like geometry with parted shoulder-length hair, circular jaw and smooth jacket shoulders with lapels.
The rejected portrait has a rigid brim and hanging ends that read as a hat. The original shows parted hair, a rounded face and jacket lapels.
Keyshape VRECT_L; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1495fa08-4641-408e-af94-dd9ae47c139b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__scientist-woman-avatar/20260929T084651Z-thuan-mac/reference/scientist woman_1495fa08-4641-408e-af94-dd9ae47c139b.svg'
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
    icon_id = 'scientist-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('scientist', 'woman')

    def build(self):
        s=self
        # Plan: single domed hair mass, center part joined at crown; circular jaw and coat.
        path(s,'hair',(7,27),('C',(8,14),(10,22),(8,19)),('C',(24,4),(8,7),(16,4)),('C',(40,14),(32,4),(40,7)),('C',(41,27),(40,19),(38,22)))
        path(s,'part',(12,14),('C',(24,4),(18,14),(24,11)),('C',(36,14),(24,11),(30,14)))
        s.relate('connect','hair','part')
        s.add_arc('jaw',(36,14),(12,14),radius_x=12,sweep=True);s.relate('connect','part','jaw')
        path(s,'shoulders',(6,44),('L',(6,40)),('C',(24,30),(6,34),(16,30)),('C',(42,40),(32,30),(42,34)),('L',(42,44)))
        s.add_polyline('lapels',(17,32),(24,44),(31,32))
        s.human_construction='bust'
        s.relate('connect','jaw','shoulders')
