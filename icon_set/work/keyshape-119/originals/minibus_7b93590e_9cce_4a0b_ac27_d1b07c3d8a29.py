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
    category = 'objects/transportation'
    aliases = ()
    keywords = ('minibus', 'bus', 'van', 'shuttle', 'vehicle', 'transport', 'public transport', 'side view')

    def build(self) -> None:
        for side,x in [('front',12),('rear',36)]:
            self.add_arc(side+'-upper',(x-6,34),(x+6,34),radius_x=6)
            self.add_arc(side+'-lower',(x+6,34),(x-6,34),radius_x=6)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('bonnet-1',(6, 34),(6, 34))
        self.add_line('bonnet-2',(6, 34),(6, 20))
        self.add_arc('bonnet-corner',(6,20),(8,16),radius_x=4)
        self.add_line('step-1',(8, 16),(10, 16))
        self.add_line('step-2',(10, 16),(10, 12))
        self.add_arc('roof-front',(10,12),(14,8),radius_x=4)
        self.add_line('roof-1',(14, 8),(24, 8))
        self.add_line('roof-2',(24, 8),(40, 8))
        self.add_arc('roof-rear',(40,8),(42,12),radius_x=4)
        self.add_line('rear-1',(42, 12),(42, 34))
        self.add_line('rear-2',(42, 34),(42, 34))
        self.add_contour('body','bonnet-1','bonnet-2','bonnet-corner','step-1','step-2','roof-front','roof-1','roof-2','roof-rear','rear-1','rear-2')
        self.add_line('chassis',(18,34),(30,34))
        self.add_line('window',(24,8),(24,18))
        self.relate('connect','window','body')
        for wheel in ['front-wheel','rear-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)
