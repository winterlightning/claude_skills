'Left-facing Merlion with eye, mane, fish-tail silhouette and water spout. SQUARE accommodates the water. Source profile retained; Lucide fish informs sparse identity details. Deliberately asymmetric.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d6b18c3-9c28-4f4a-8e22-8679e1c298f6'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/merlion statue_4d6b18c3-9c28-4f4a-8e22-8679e1c298f6.svg'
AUTHOR = 'gpt-6'

class MerlionStatue(Solo48):
    icon_id = 'merlion-statue'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('merlion', 'singapore', 'statue', 'lion', 'fish', 'landmark', 'monument', 'mascot')

    def build(self) -> None:
        # SQUARE extremes (6,6)-(42,42); left-facing lion spouting water.
        self.add_line('brow-1',(16,14),(22,14))
        self.add_line('brow-2',(22,14),(22,6))
        self.add_line('brow-3',(22,6),(32,6))
        self.add_arc('mane-top',(32,6),(42,16),radius_x=14)
        self.add_line('back',(42,16),(42,30))
        self.add_arc('fish-body',(42,30),(30,42),radius_x=16)
        self.add_line('tail-1',(30,42),(16,42))
        self.add_line('tail-2',(16,42),(24,34))
        self.add_line('tail-3',(24,34),(24,26))
        self.add_line('tail-4',(24,26),(16,26))
        self.add_arc('muzzle-lower',(16,26),(10,20),radius_x=6)
        self.add_arc('muzzle-upper',(10,20),(16,14),radius_x=6)
        self.add_contour('outline','brow-1','brow-2','brow-3','mane-top','back','fish-body','tail-1','tail-2','tail-3','tail-4','muzzle-lower','muzzle-upper',closed=True)
        self.add_dot('eye',(30,12))
        self.add_arc('mane',(34,20),(34,30),radius_x=5)
        self.add_arc('water',(10,20),(6,36),radius_x=8,radius_y=16,sweep=False)
        self.relate('connect','water','outline')
