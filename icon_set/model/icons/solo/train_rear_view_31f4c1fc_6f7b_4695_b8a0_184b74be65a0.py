"""Train rear view; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31f4c1fc-6f7b-4695-b8a0-184b74be65a0'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad train back_31f4c1fc-6f7b-4695-b8a0-184b74be65a0.svg'
AUTHOR = 'gpt-6'

class TrainRearView(Solo48):
    icon_id = 'train-rear-view'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('train', 'rear', 'carriage', 'railway', 'back', 'wagon', 'rail', 'coach')

    def build(self) -> None:
        # VRECT_L (8,6)-(40,42); arched carriage roof and centered open doorway.
        self.add_arc('roof',(10,10),(38,10),radius_x=14,radius_y=6)
        self.add_line('right-wall',(38,10),(38,36))
        self.add_line('base-1', (38, 36), (32, 36))
        self.add_line('base-2', (32, 36), (28, 36))
        self.add_line('base-3', (28, 36), (20, 36))
        self.add_line('base-4', (20, 36), (16, 36))
        self.add_line('base-5', (16, 36), (10, 36))
        self.add_line('left-wall',(10,36),(10,10))
        self.add_contour('body','roof','right-wall','base-1','base-2','base-3','base-4','base-5','left-wall',closed=True)
        self.add_line('door-left',(20,36),(20,22))
        self.add_arc('door-upper-left',(20,22),(22,20),radius_x=2)
        self.add_line('door-top',(22,20),(26,20))
        self.add_arc('door-upper-right',(26,20),(28,22),radius_x=2)
        self.add_line('door-right',(28,22),(28,36))
        self.add_contour('door','door-left','door-upper-left','door-top','door-upper-right','door-right')
        self.relate('connect','door','body')
        self.add_polyline('rail',(8,42),(16,42),(32,42),(40,42))
        for name,x in [('left',16),('right',32)]:
            self.add_line(name+'-bogie',(x,36),(x,44))
            self.relate('connect',name+'-bogie','body')
            self.relate('connect',name+'-bogie','rail')

