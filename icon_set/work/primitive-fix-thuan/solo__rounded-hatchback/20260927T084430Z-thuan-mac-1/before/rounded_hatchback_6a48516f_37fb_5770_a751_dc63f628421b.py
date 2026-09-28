"""A left-facing hatchback with a rounded rear roof and one long window. Broad envelope preserves the low bonnet. Lucide car informed shared wheel/body joins; hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a48516f-37fb-5770-a751-dc63f628421b'
SOURCE_PATH = 'pictographic-primitives/transportation/car voyage_6a48516f-37fb-5770-a751-dc63f628421b.svg'
SOURCE_REFERENCES = (('6a48516f-37fb-5770-a751-dc63f628421b', 'pictographic-primitives/transportation/car voyage_6a48516f-37fb-5770-a751-dc63f628421b.svg'),)
AUTHOR = 'gpt-6'

class RoundedHatchback(Solo48):
    icon_id = 'rounded-hatchback'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('car', 'hatchback', 'suv', 'vehicle', 'side view', 'automobile', 'voyage', 'travel')

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

        self.add_polyline('cabin-front',(14,20),(22,8),(32,8))
        self.add_arc('cabin-rear',(32,8),(44,20),radius_x=12)
        self.relate('connect','cabin-front','cabin-rear')
        self.relate('connect','cabin-front','body')
        self.relate('connect','cabin-rear','body')
