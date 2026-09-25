"""A left-facing minibus with a stepped bonnet, one window divider and equal wheels. HRECT_L ink (6,6)-(42,42). Lucide bus informed wheel/body connections and the sparse window structure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b93590e-9cce-4a0b-ac27-d1b07c3d8a29'
SOURCE_PATH = 'pictographic-primitives/transportation/bus 1_7b93590e-9cce-4a0b-ac27-d1b07c3d8a29.svg'
SOURCE_REFERENCES = (('7b93590e-9cce-4a0b-ac27-d1b07c3d8a29', 'pictographic-primitives/transportation/bus 1_7b93590e-9cce-4a0b-ac27-d1b07c3d8a29.svg'),)
AUTHOR = 'gpt-6'

class Minibus(Solo48):
    icon_id = 'minibus'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('minibus', 'bus', 'van', 'shuttle', 'vehicle', 'transport', 'public transport', 'side view')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('front-upper',(4, 34),*(((4, 30.6862915), (7.35786438, 28.0), (11.5, 28.0)), ((15.3137085, 28.0), (18.0, 30.6862915), (18, 34))))
        self.add_bezier('front-lower',(18, 34),*(((18.0, 37.3137085), (15.3137085, 40), (11.5, 40)), ((7.35786438, 40), (4, 37.3137085), (4, 34))))
        self.add_bezier('rear-upper',(30, 34),*(((30.0, 30.6862915), (32.6862915, 28.0), (36.5, 28.0)), ((40.64213562, 28.0), (44, 30.6862915), (44, 34))))
        self.add_bezier('rear-lower',(44, 34),*(((44, 37.3137085), (40.64213562, 40), (36.5, 40)), ((32.6862915, 40), (30.0, 37.3137085), (30, 34))))
        self.add_line('bonnet-1',(4, 34),(4, 34))
        self.add_line('bonnet-2',(4, 34),(4, 20))
        self.add_bezier('bonnet-corner',(4, 20),*(((4, 18.3837142), (4.72578466, 16.80131331), (6, 16)),))
        self.add_line('step-1',(6, 16),(9, 16))
        self.add_line('step-2',(9, 16),(9, 12))
        self.add_bezier('roof-front',(9, 12),*(((9.0, 9.790861), (11.23857625, 8), (14, 8)),))
        self.add_line('roof-1',(14, 8),(24, 8))
        self.add_line('roof-2',(24, 8),(42, 8))
        self.add_bezier('roof-rear',(42, 8),*(((43.27421534, 8.80131331), (44, 10.3837142), (44, 12)),))
        self.add_line('rear-1',(44, 12),(44, 34))
        self.add_line('rear-2',(44, 34),(44, 34))
        self.add_line('chassis',(18, 34),(30, 34))
        self.add_line('window',(24, 8),(24, 18))
        self.add_contour('front-wheel',*('front-upper', 'front-lower'),closed=True)
        self.add_contour('rear-wheel',*('rear-upper', 'rear-lower'),closed=True)
        self.add_contour('body',*('bonnet-1', 'bonnet-2', 'bonnet-corner', 'step-1', 'step-2', 'roof-front', 'roof-1', 'roof-2', 'roof-rear', 'rear-1', 'rear-2'),closed=False)
        self.relate('connect',*('window', 'body'))
        self.relate('connect',*('body', 'front-wheel'))
        self.relate('connect',*('chassis', 'front-wheel'))
        self.relate('connect',*('body', 'rear-wheel'))
        self.relate('connect',*('chassis', 'rear-wheel'))
