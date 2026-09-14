"""A rear window with two upward airflow arrows. Broad keyshape preserves the curved glass. No exact Lucide match; elliptical roof and symmetric airflow reconstructed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '67cbb45c-42e3-535e-bf88-6fba87eb7fc3'
SOURCE_PATH = 'pictographic-primitives/transportation/car dashboard window rear_67cbb45c-42e3-535e-bf88-6fba87eb7fc3.svg'
SOURCE_REFERENCES = (('67cbb45c-42e3-535e-bf88-6fba87eb7fc3', 'pictographic-primitives/transportation/car dashboard window rear_67cbb45c-42e3-535e-bf88-6fba87eb7fc3.svg'),)
AUTHOR = 'gpt-6'

class RearWindowDefrost(Solo48):
    icon_id = 'rear-window-defrost'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('rear window', 'defrost', 'demist', 'windscreen', 'airflow', 'car', 'dashboard', 'heating')

    def build(self) -> None:
        self.add_arc('roof',(4,16),(44,16),radius_x=20,radius_y=8)
        self.add_line('right',(44,16),(44,28))
        self.add_arc('right-corner',(44,28),(36,36),radius_x=8)
        for i,(a,b) in enumerate(zip([(36,36),(33,33),(15,33)],[(33,33),(15,33),(12,36)])):
            self.add_arc(f'bottom-{i}',a,b,radius_x=15,sweep=False)
        self.add_arc('left-corner',(12,36),(4,28),radius_x=8)
        self.add_line('left',(4,28),(4,16))
        self.add_contour('glass','roof','right','right-corner','bottom-0','bottom-1','bottom-2','left-corner','left',closed=True)
        for x in (15,33):
            self.add_polyline(f'shaft-{x}',(x,40),(x,33),(x,18))
            self.add_polyline(f'head-{x}',(x-2,22),(x,18),(x+2,22))
            self.relate('connect',f'shaft-{x}','glass')
            self.relate('connect',f'head-{x}',f'shaft-{x}')
