"""A rock-concert horns gesture with three energy marks.
Symbol plan and construction: hand-metal: paired raised outer fingers and curled inner fingers; human_ref/user.svg and full_body_ref.png checked for human vocabulary.
Keyshape: SQUARE accommodates the broad hand below three energy marks.
Omissions: Interior thumb/palm creases; small lightning zigzags simplified to three rays.
Review: Rounded finger caps, an open palm interior and three separate rays read cleanly at native size. Hand-only subject: no detached head/body measurement applies."""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '3a11e17f-1153-59b2-b135-910a41a584c7'
SOURCE_PATH = 'pictographic-primitives/entertainment/concert rock_3a11e17f-1153-59b2-b135-910a41a584c7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'concert-rock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('concert', 'rock')



    def build(self):
        # Human-reference vocabulary: rounded continuous hand silhouette; no detached head.
        # Paired raised outer fingers, two curled middle knuckles, thumb and three energy bolts.
        self.add_arc('index-cap',(8,22),(16,22),radius_x=4)
        self.add_line('index-inner',(16,22),(16,30))
        self.add_arc('middle-knuckle',(16,30),(24,30),radius_x=4)
        self.add_arc('ring-knuckle',(24,30),(32,30),radius_x=4)
        self.add_line('little-inner',(32,30),(32,22))
        self.add_arc('little-cap',(32,22),(40,22),radius_x=4)
        self.add_line('right-palm',(40,22),(40,30))
        self.add_arc('palm-right',(40,30),(28,42),radius_x=12)
        self.add_line('palm-bottom',(28,42),(20,42))
        self.add_arc('palm-left',(20,42),(8,30),radius_x=12)
        self.add_line('left-palm',(8,30),(8,22))
        self.add_contour('hand','index-cap','index-inner','middle-knuckle','ring-knuckle','little-inner','little-cap','right-palm','palm-right','palm-bottom','palm-left','left-palm',closed=True)
        # Omit cramped palm creases; raised outer fingers and curled middle pair remain.
        for name,points in [('left-bolt',[(6,6),(10,10)]),('top-bolt',[(26,6),(22,12)]),('right-bolt',[(42,6),(38,10)])]:
            self.add_polyline(name,*points)
