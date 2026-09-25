"""A pointed shield contains an inset shield border. Lucide shield informs mirrored side flow. Widen border spacing and simplify the inner curves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cc1ee42-eca4-50ff-a5e5-9b332ae428a9'
SOURCE_PATH = 'pictographic-primitives/protection/protection shield_6cc1ee42-eca4-50ff-a5e5-9b332ae428a9.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'shield-with-inset-border'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    aliases = ()
    keywords = ('shield', 'border', 'outline', 'defence', 'protection', 'security', 'guard', 'badge')

    def build(self):
        # VRECT_L centerline extremes: (8,4)-(40,44).

        points = [(8,20),(8,10),(24,4),(40,10),(40,20)]
        for i, (a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line('crown-'+str(i),a,b)
        self.add_arc('right',(40,20),(24,44),radius_x=26)
        self.add_arc('left',(24,44),(8,20),radius_x=26)
        self.add_contour('outline','crown-1','crown-2','crown-3','crown-4','right','left',closed=True)
        self.add_polyline('inset',(17,18),(24,14),(31,18),(31,23),(24,34),(17,23),closed=True)
