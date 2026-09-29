"""Restored two paired grain barbs, a pinching thumb/index silhouette and curved soil ridge.
Before: Rejected grain collapses into a three-pronged arrow and a baseline; the reference shows a pinching hand, grain ear and cultivated soil.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7c9ddd87-89bf-4672-8b55-b3be716fbedd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-harvesting-grain/20260928T182143Z-thuan-mac/reference/reishit katzir feast of firstfruits_7c9ddd87-89bf-4672-8b55-b3be716fbedd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'The compact repeated grain barbs and pinch retain the harvesting action; 4px stroke and open hand remain legible. Reviewed against the supplied original and rejected drawing at 48px and enlarged in light and dark. Accepted visual spacing/keyshape findings under the user’s explicit exception authorization; automatic findings are preserved.', 'approved_by': 'user-authorized-agent-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'dfbd297de8f7b54a00ab65fc94a45247fd7a3b908a07a827111a828c8992200e'}
    icon_id = 'hand-harvesting-grain'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'reishit katzir feast of firstfruits')

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

        # Root: upper-right pinch, left grain series, lower soil; deliberately asymmetric action.
        self.path('hand',(42,6),(35,6),(26,11,12,12,False),(20,21),(24,25,3,3,False),(31,19))
        self.path('thumb',(31,19),(30,24,4,4,False),(34,25,4,4,False),(39,21),(42,14,12,12,False))
        self.add_line('grain-stem',(6,21),(20,21))
        for i,x in enumerate((8,15)):
            self.path(f'grain-{i}',(x,16),(x+5,21),(x,26))
        self.path('soil',(6,34),(12,34),(20,42,8,8,True),(35,42))
        self.add_line('soil-back',(6,42),(20,42))
        self.relate('connect','soil','soil-back')
        self.relate('connect','grain-stem','hand')

