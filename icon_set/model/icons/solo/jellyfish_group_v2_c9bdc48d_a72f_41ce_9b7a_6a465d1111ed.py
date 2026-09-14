# Variant of jellyfish-group; parent file remains unchanged.
'Jellyfish group: independent spacing revision.\n\nThree dome bells with short tentacles; narrow lower bells to leave twelve units between curved edges.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c9bdc48d-a72f-41ce-9b7a-6a465d1111ed'
SOURCE_PATH = 'pictographic-primitives/animals/jellyfish group_c9bdc48d-a72f-41ce-9b7a-6a465d1111ed.svg'
AUTHOR = 'gpt-6'

class JellyfishGroupVariant2(Solo48):
    icon_id = 'jellyfish-group-v2'
    variant_of = 'jellyfish-group'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('jellyfish', 'group', 'three', 'swarm', 'sea', 'ocean', 'marine', 'bloom')

    def build(self):
        self.add_arc('upper-bell',(16, 16),(32, 16),radius_x=8,radius_y=8,sweep=True)
        self.add_line('upper-rim',(16, 16),(32, 16))
        self.add_line('upper-left',(16, 16),(16, 20))
        self.add_line('upper-right',(32, 16),(32, 20))
        self.relate('connect','upper-bell','upper-rim')
        self.relate('connect','upper-rim','upper-left')
        self.relate('connect','upper-rim','upper-right')
        self.add_line('upper-middle',(24, 16),(24, 20))
        self.relate('connect','upper-middle','upper-rim')
        self.add_arc('left-bell',(4, 36),(18, 36),radius_x=7,radius_y=8,sweep=True)
        self.add_line('left-rim',(4, 36),(18, 36))
        self.add_line('left-left',(4, 36),(4, 40))
        self.add_line('left-right',(18, 36),(18, 40))
        self.relate('connect','left-bell','left-rim')
        self.relate('connect','left-rim','left-left')
        self.relate('connect','left-rim','left-right')
        self.add_arc('right-bell',(30, 36),(44, 36),radius_x=7,radius_y=8,sweep=True)
        self.add_line('right-rim',(30, 36),(44, 36))
        self.add_line('right-left',(30, 36),(30, 40))
        self.add_line('right-right',(44, 36),(44, 40))
        self.relate('connect','right-bell','right-rim')
        self.relate('connect','right-rim','right-left')
        self.relate('connect','right-rim','right-right')
