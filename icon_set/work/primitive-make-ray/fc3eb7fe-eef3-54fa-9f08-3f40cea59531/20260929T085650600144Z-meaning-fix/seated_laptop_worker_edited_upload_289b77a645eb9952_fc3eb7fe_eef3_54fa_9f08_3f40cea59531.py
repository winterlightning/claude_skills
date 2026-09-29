"""Rebuilt the torso and seated legs beside an open laptop and desk, with forearm reaching the keyboard.
No original is available; the displayed drawing has a floating head, no torso and a laptop that resembles a chair back. Restore an explicit person using a laptop at a desk.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fc3eb7fe-eef3-54fa-9f08-3f40cea59531'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-laptop-worker-edited-upload-289b77a645eb9952/20260929T084651Z-thuan-mac/reference/seated-laptop-worker-edited-upload-289b77a645eb9952_fc3eb7fe-eef3-54fa-9f08-3f40cea59531.svg'
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
    icon_id = 'seated-laptop-worker-edited-upload-289b77a645eb9952'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('seated-laptop-worker-edited-upload-289b77a645eb9952',)

    def build(self):
        s=self
        # Plan: laptop rests on desktop; reaching arm connects keyboard; seat joins body.
        circle(s,'head',35,9,5)
        s.add_line('torso',(35,22),(35,36))
        s.add_polyline('arm',(35,22),(30,28),(24,28));s.relate('connect','torso','arm')
        s.add_polyline('leg',(35,36),(25,36),(22,44));s.relate('connect','torso','leg')
        s.add_polyline('laptop',(7,14),(11,28),(24,28));s.relate('connect','arm','laptop')
        s.add_line('desk',(4,28),(11,28));s.relate('connect','laptop','desk')
        s.add_line('desk-leg',(8,28),(8,44));s.relate('connect','desk','desk-leg')
        s.add_polyline('chair',(35,36),(43,36),(43,44));s.relate('connect','chair','torso');s.relate('connect','chair','leg')
        s.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
