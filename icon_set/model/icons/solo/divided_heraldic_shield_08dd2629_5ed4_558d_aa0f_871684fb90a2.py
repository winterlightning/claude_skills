"""A heraldic shield is divided vertically. Lucide shield-half informs the shared axis and division. Drop inset border to leave two readable fields."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08dd2629-5ed4-558d-aa0f-871684fb90a2'
SOURCE_PATH = 'pictographic-primitives/protection/protection shield_08dd2629-5ed4-558d-aa0f-871684fb90a2.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'divided-heraldic-shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    aliases = ()
    keywords = ('shield', 'heraldic', 'divided', 'crest', 'defence', 'protection', 'security', 'armour')

    def build(self):
        # VRECT_L centerline extremes: (8,4)-(40,44).

        # Shared vertical axis; two side curves meet the pointed foot.
        points = [(8,20),(8,10),(24,4),(40,10),(40,20)]
        for i, (a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line('crown-'+str(i),a,b)
        self.add_arc('right',(40,20),(24,44),radius_x=26)
        self.add_arc('left',(24,44),(8,20),radius_x=26)
        self.add_contour('outline','crown-1','crown-2','crown-3','crown-4','right','left',closed=True)
        self.add_line('division',(24,4),(24,44))
        self.relate('connect','division','outline')
