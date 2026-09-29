"""Rebuilt the skull and anatomical neck with a clearer nose, lower rounded jaw and a separate frown.
The rejected mouth merges with the chin into a heavy smiling-looking hook. Preserve the closed eye and separate a downturned mouth from the jaw.
Keyshape VRECT_L; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd69f2298-aacc-5680-816c-8c6ae6b44401'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sad-face-profile/20260929T084651Z-thuan-mac/reference/sadness emotions_d69f2298-aacc-5680-816c-8c6ae6b44401.svg'
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
    icon_id = 'sad-face-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('sadness', 'emotions')

    def build(self):
        s=self
        # Plan: continuous right-facing anatomical silhouette; detached eye and frown.
        path(s,'profile',(13,44),('L',(13,35)),('C',(8,22),(10,32),(8,28)),('L',(8,18)),('A',(36,18),14,14,True),('L',(40,24)),('L',(34,25)),('L',(34,31)),('A',(26,39),8,8,True),('L',(26,44)))
        s.add_line('closed-eye',(23,17),(27,17))
        path(s,'frown',(20,33),('C',(26,31),(22,31),(24,30)))
