"""A plain shield has an arched top and pointed foot. This source duplicates the other plain shield; preserve its own UUID. Lucide shield informs paired lower curves; no details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '145e466e-63e6-4d0e-b04e-27f1805aaa6d'
SOURCE_PATH = 'pictographic-primitives/protection/shield_145e466e-63e6-4d0e-b04e-27f1805aaa6d.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'shield-145e466e'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('shield', 'defence', 'protection', 'security', 'guard', 'badge', 'armour', 'safe')

    def build(self):
        # VRECT_L centerline extremes (8, 4, 40, 44).

        # Mirrored face: shallow elliptical crown and tangent lower circular sides.
        self.add_arc('crown',(8,10),(40,10),radius_x=16,radius_y=6)
        self.add_line('right-wall',(40,10),(40,20))
        self.add_arc('right-foot',(40,20),(24,44),radius_x=26)
        self.add_arc('left-foot',(24,44),(8,20),radius_x=26)
        self.add_line('left-wall',(8,20),(8,10))
        self.add_contour('outline','crown','right-wall','right-foot','left-foot','left-wall',closed=True)
