from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6932898-aa2f-4539-aa63-ecfb633b33be'
SOURCE_PATH = 'pictographic-primitives/transportation/segway person_f6932898-aa2f-4539-aa63-ecfb633b33be.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': 'f6932898-aa2f-4539-aa63-ecfb633b33be', 'source_path': 'pictographic-primitives/transportation/segway person_f6932898-aa2f-4539-aa63-ecfb633b33be.svg'}]

class PersonOnSegway(Solo48):
    icon_id = 'person-on-segway'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('segway', 'self-balancing', 'rider', 'personal transporter', 'scooter', 'speed', 'micromobility', 'person')

    def build(self):
        self.add_arc('head-a',(34,4),(34,10),radius_x=3)
        self.add_arc('head-b',(34,10),(34,4),radius_x=3)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('rider',(32,18),(28,30))
        self.add_line('arm',(32,18),(40,22))
        self.add_line('handle',(40,22),(35,37))
        pts=((28,30),(35,37),(28,44),(21,37),(28,30))
        for n,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'wheel-{n}',a,b,radius_x=7)
        self.add_contour('wheel',*(f'wheel-{n}' for n in range(4)),closed=True)
        for a,b in (('rider','arm'),('arm','handle'),('handle','wheel'),('rider','wheel')):self.relate('connect',a,b)
        self.add_line('speed-upper',(8,18),(20,18))
        self.add_line('speed-lower',(8,26),(16,26))
