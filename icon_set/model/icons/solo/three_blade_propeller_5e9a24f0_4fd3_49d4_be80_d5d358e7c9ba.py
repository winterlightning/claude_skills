"""Three blade propeller; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e9a24f0-4fd3-49d4-be80-d5d358e7c9ba'
SOURCE_PATH = 'pictographic-primitives/transportation/propeller_5e9a24f0-4fd3-49d4-be80-d5d358e7c9ba.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '5e9a24f0-4fd3-49d4-be80-d5d358e7c9ba', 'SOURCE_PATH': 'pictographic-primitives/transportation/propeller_5e9a24f0-4fd3-49d4-be80-d5d358e7c9ba.svg', 'AUTHOR': 'gpt-6'}, {'SOURCE_ICON_ID': 'bd70fa47-b42c-42c2-ab20-6cff7b6e28c3', 'SOURCE_PATH': 'pictographic-primitives/transportation/propeller_bd70fa47-b42c-42c2-ab20-6cff7b6e28c3.svg', 'AUTHOR': 'gpt-6'}]

class ThreeBladePropeller(Solo48):
    icon_id = 'three-blade-propeller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('three', 'blade', 'propeller')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). A round hub joins three broad rounded blades.
        for name,a,b in [('upper',(16,24),(32,24)),('lower-right',(32,24),(24,32)),('lower-left',(24,32),(16,24))]:
            self.add_arc('hub-'+name,a,b,radius_x=8)
        self.add_contour('hub','hub-upper','hub-lower-right','hub-lower-left',closed=True)
        self.add_line('top-left',(16,24),(16,14))
        self.add_arc('top-tip',(16,14),(32,14),radius_x=8)
        self.add_line('top-right',(32,14),(32,24))
        self.add_contour('top-blade','top-left','top-tip','top-right')
        for name,side in [('left',-1),('right',1)]:
            self.add_line(name+'-leading',(24+side*8,24),(24+side*18,36))
            self.add_arc(name+'-tip',(24+side*18,36),(24+side*12,42),radius_x=6,sweep=side>0)
            self.add_line(name+'-trailing',(24+side*12,42),(24,32))
            self.add_contour(name+'-blade',name+'-leading',name+'-tip',name+'-trailing')
            self.relate('connect',name+'-blade','hub')
            self.relate('connect',name+'-blade','top-blade')
        self.relate('connect','hub','top-blade')
        self.relate('connect','left-blade','right-blade')
