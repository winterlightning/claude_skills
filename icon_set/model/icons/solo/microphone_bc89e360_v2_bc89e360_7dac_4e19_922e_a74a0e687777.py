'microphone-bc89e360: distinct review variant.\n\nConstruction: Microphone with a capsule head, U-shaped suspension and short central stand; preserve circular cap geometry.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nConstruction reference: audio-lines from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'bc89e360-7dac-4e19-922e-a74a0e687777'
SOURCE_PATH = 'pictographic-primitives/audio/microphone_bc89e360-7dac-4e19-922e-a74a0e687777.svg'
AUTHOR = 'gpt-6'


class MicrophoneBc89e360Variant2(Solo48):
    icon_id = 'microphone-bc89e360-v2'
    variant_of = 'microphone-bc89e360'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')
    keyshape = Keyshape.VRECT_L

    def build(self):
        box(self,'capsule',17,4,31,28,7)
        path(self,'suspension',(8,18),('L',(8,25)),('A',16,13,False,(24,38)),('A',16,13,False,(40,25)),('L',(40,18)))
        line(self,'stand',(24,38),(24,44))
        contacts(self)
