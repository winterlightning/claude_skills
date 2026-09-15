"""A smaller shield outline sits concentrically inside a larger shield. Read as a layered border. Lucide shield informs the outer contour; simplify inner curvature and widen separation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8cab393f-9c38-48a5-b7c5-777af0e5d433'
SOURCE_PATH = 'pictographic-primitives/protection/shield_8cab393f-9c38-48a5-b7c5-777af0e5d433.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'shield-within-shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('shield', 'nested', 'defence', 'protection', 'security', 'layers', 'guard', 'badge')

    def build(self):
        # VRECT_L centerline extremes (8, 4, 40, 44).

        # Concentric shield outlines describe a physical border, not a status glyph.
        nodes=[(8,20),(8,10),(24,4),(40,10),(40,20)]
        for i,(a,b) in enumerate(zip(nodes,nodes[1:]),1):self.add_line('crown-'+str(i),a,b)
        self.add_arc('right',(40,20),(24,44),radius_x=26)
        self.add_arc('left',(24,44),(8,20),radius_x=26)
        self.add_contour('outline',*[f'crown-{i}' for i in range(1,5)],'right','left',closed=True)
        self.add_polyline('inner',(17,18),(24,14),(31,18),(31,23),(24,34),(17,23),closed=True)
