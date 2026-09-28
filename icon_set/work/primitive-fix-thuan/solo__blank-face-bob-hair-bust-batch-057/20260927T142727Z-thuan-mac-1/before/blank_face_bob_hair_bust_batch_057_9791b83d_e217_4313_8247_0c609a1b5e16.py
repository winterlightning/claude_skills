'Blank circular jaw with parted short hair silhouette; broad circular shoulders. Shared human user.svg informs proportions. Touching head/body ink: jaw bottom24, shoulders top28. No facial details.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9791b83d-e217-4313-8247-0c609a1b5e16'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grandmother_9791b83d-e217-4313-8247-0c609a1b5e16.svg'
AUTHOR = 'gpt-6'

class Result(Solo48):
    icon_id = 'blank-face-bob-hair-bust-batch-057'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('woman', 'bust', 'portrait', 'bob', 'hair', 'avatar')
    human_construction = "bust"

    def build(self):
        # Parted bob shares its crown node; paired radii preserve balance.
        cx = 24
        for side in (-1, 1):
            point = lambda x,y: (cx+side*x,y)
            self.add_arc(f'hair-{side}',(cx,4),point(16,16),radius_x=16,radius_y=12,sweep=side>0)
            self.add_line(f'tip-{side}',point(16,16),point(16,22))
            self.add_contour(f'outer-{side}',f'hair-{side}',f'tip-{side}')
            self.add_arc(f'fringe-{side}',(cx,4),point(8,16),radius_x=8,radius_y=12,sweep=side<0)
            self.relate('connect',f'outer-{side}',f'fringe-{side}')
        self.relate('connect','outer--1','outer-1')
        self.relate('connect','fringe--1','fringe-1')
        self.add_arc('jaw',(32,16),(16,16),radius_x=8)
        self.relate('connect','jaw','fringe--1')
        self.relate('connect','jaw','fringe-1')
        self.add_arc('shoulder',(8,44),(40,44),radius_x=16)
        self.relate('connect','jaw','shoulder')
