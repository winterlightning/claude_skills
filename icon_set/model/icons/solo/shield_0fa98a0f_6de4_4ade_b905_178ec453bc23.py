"""A plain shield has an arched top and pointed foot. Lucide shield informs paired lower curves and straight upper sides. Preserve the empty interior and all main silhouette features."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fa98a0f-6de4-4ade-b905-178ec453bc23'
SOURCE_PATH = 'pictographic-primitives/protection/shield_0fa98a0f-6de4-4ade-b905-178ec453bc23.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
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
