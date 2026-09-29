"""Widened the open jaw and restored a curved thumb mound, wrapping finger edge, and visible handle end.
Before: The rejected wrench has a tiny U slot and the hand is reduced to parallel bars with dots.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '69fd62d6-2807-4c9b-9e1a-35e009d9fd9f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-open-end-wrench/20260928T182143Z-thuan-mac/reference/self service wrench_69fd62d6-2807-4c9b-9e1a-35e009d9fd9f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The open jaw and wrapped finger divisions take priority over uniform spacing; negative spaces remain visible. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '53c382545e2825c890e6e477f1cd0bcc9636c90b79b5b6a7da14d83e6d25f6bc'}
    icon_id = 'hand-holding-open-end-wrench'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'self service wrench')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)

    def build(self):

        # Open wrench head and vertical shaft; transverse fist encloses shaft.
        self.path('wrench',(19,6),(19,14),(27,14,4,4,False),(27,6),(35,17,11,11,True),(27,26),(27,29))
        self.path('wrench-left',(19,6),(11,17,11,11,False),(19,26),(19,29))
        self.path('hand',(6,35),(12,33),(17,28),(19,28),(19,29),(35,29),(35,35,3,3,True),(30,35))
        self.path('fingers',(35,35),(35,41,3,3,True),(22,42),(15,42),(9,44))
        self.path('handle-end',(20,42),(27,42,4,3,False))

