"""Fast train nose; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd432bbc7-119a-4e1b-8b69-405e46b997eb'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad fast train_d432bbc7-119a-4e1b-8b69-405e46b997eb.svg'
AUTHOR = 'gpt-6'

class FastTrainNose(Solo48):
    icon_id = 'fast-train-nose'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('fast train', 'high speed rail', 'bullet train', 'train', 'railway', 'rail', 'express', 'transport')

    def build(self) -> None:
        def wheel(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)
        # HRECT_L (6,8)-(42,40). Two tangent arcs and a diagonal form the streamlined nose.
        self.add_line('roof',(4,8),(20,8))
        self.add_arc('roof-shoulder',(20,8),(26,10),radius_x=10)
        self.add_line('nose-slope-1', (26, 10), (34, 16))
        self.add_line('nose-slope-2', (34, 16), (38, 19))
        self.add_arc('nose-upper',(38,19),(40,23),radius_x=5)
        self.add_arc('nose-middle',(40,23),(39,26),radius_x=5)
        self.add_arc('nose-lower',(39,26),(35,28),radius_x=5)
        self.add_line('floor-1', (35, 28), (12, 28))
        self.add_line('floor-2', (12, 28), (4, 28))
        self.add_contour('body','roof','roof-shoulder','nose-slope-1','nose-slope-2','nose-upper','nose-middle','nose-lower','floor-1','floor-2')
        self.add_polyline('windscreen',(34,16),(16,16),(24,24),(39,26))
        self.relate('connect','windscreen','body')
        wheel('wheel',12,34,6)
        self.relate('connect','wheel','body')
        self.add_polyline('rail',(4,40),(12,40),(44,40))
        self.relate('connect','wheel','rail')

