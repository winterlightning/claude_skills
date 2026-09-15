"""A windscreen with two rising airflow arrows; the small middle dash is omitted. HRECT_L ink (6,6)-(42,42). Lucide car-front informs the bilateral screen construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41f88605-cfdf-537e-9777-6da8f3a89587'
SOURCE_PATH = 'pictographic-primitives/transportation/air conditioner front_41f88605-cfdf-537e-9777-6da8f3a89587.svg'
AUTHOR = 'gpt-6'

class WindscreenAirflow(Solo48):
    icon_id = 'windscreen-airflow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('windscreen', 'windshield', 'defrost', 'demist', 'airflow', 'air conditioning', 'car', 'dashboard')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('screen-top',(4,16),((10,11),(17,8),(24,8)),((31,8),(38,11),(44,16)))
        self.add_line('screen-right',(44, 16),(43, 24))
        self.add_line('screen-left',(5, 24),(4, 16))
        self.add_line('air-0-1',(17, 40),(17, 23))
        self.add_line('head-0-1',(14, 28),(17, 23))
        self.add_line('head-0-2',(17, 23),(20, 28))
        self.add_line('air-1-1',(31, 40),(31, 23))
        self.add_line('head-1-1',(28, 28),(31, 23))
        self.add_line('head-1-2',(31, 23),(34, 28))
        self.add_contour('screen',*('screen-left', 'screen-top', 'screen-right'),closed=False)
        self.add_contour('air-0',*('air-0-1',),closed=False)
        self.add_contour('head-0',*('head-0-1', 'head-0-2'),closed=False)
        self.add_contour('air-1',*('air-1-1',),closed=False)
        self.add_contour('head-1',*('head-1-1', 'head-1-2'),closed=False)
        self.relate('connect',*('air-0', 'head-0'))
        self.relate('connect',*('air-1', 'head-1'))
