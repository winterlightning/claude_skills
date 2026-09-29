"""Separated the frown from the chin and reshaped the skull, nose and neck; retained the reference slanted eye.
The rejected face has a compressed jaw and a heavy mouth joined to the chin. Restore the sorrowful slanted eye and delicate downturned mouth.
Keyshape VRECT_L; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '96c50c3f-13ad-5908-ba78-3a34437c067f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sad-head-profile/20260929T084651Z-thuan-mac/reference/depression disorder symptoms_96c50c3f-13ad-5908-ba78-3a34437c067f.svg'
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
    icon_id = 'sad-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('depression', 'disorder', 'symptoms')

    def build(self):
        s=self
        # Plan: continuous right-facing anatomical silhouette, slanted eyelid and frown.
        path(s,'profile',(13,44),('L',(13,35)),('C',(8,22),(10,32),(8,28)),('L',(8,18)),('A',(36,18),14,14,True),('L',(40,24)),('L',(34,25)),('L',(34,31)),('A',(26,39),8,8,True),('L',(26,44)))
        s.add_line('closed-eye',(22,19),(27,16))
        path(s,'frown',(21,32),('C',(26,30),(23,30),(24,29)))
