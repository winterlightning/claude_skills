"""A left-facing SUV with an angular one-window cabin. Broad envelope retains the long bonnet and squared rear. Lucide car informed body/wheel joins; hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5be4a7d-6716-51a7-a80f-948144c7011e'
SOURCE_PATH = 'pictographic-primitives/transportation/car_e5be4a7d-6716-51a7-a80f-948144c7011e.svg'
SOURCE_REFERENCES = (('e5be4a7d-6716-51a7-a80f-948144c7011e', 'pictographic-primitives/transportation/car_e5be4a7d-6716-51a7-a80f-948144c7011e.svg'),)
AUTHOR = 'gpt-6'

class AngularSuv(Solo48):
    icon_id = 'angular-suv'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('suv', 'car', 'crossover', 'vehicle', 'side view', 'automobile', '4x4', 'driving')

    def build(self) -> None:
        self.add_line('front',(4,33),(4,30))
        self.add_arc('nose',(4,30),(14,20),radius_x=10)
        self.add_line('top',(14,20),(44,20))
        self.add_line('back',(44,20),(44,33))
        self.add_contour('body','front','nose','top','back')

        for name,x in [('rear',11),('front',37)]:
            self.add_arc(name+'-a',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(name+'-b',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(name+'-wheel',name+'-a',name+'-b',closed=True)
        self.add_line('chassis',(18,33),(30,33))
        for name in ['rear-wheel','front-wheel']:
            self.relate('connect','body',name)
            self.relate('connect','chassis',name)

        self.add_polyline('cabin',(14,20),(22,8),(40,8),(44,20))
        self.relate('connect','cabin','body')
