"""Oxygen Cylinder with T Valve.

Symbol plan: Rounded upright cylinder with a simple T valve, centered on the same axis. Drop the extra neck seam.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f86557da-1cc7-4eae-8fd9-4d5f68f015ce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__oxygen-cylinder-with-t-valve/20260927T133654Z-thuan-mac-1/reference/oxygen tank_f86557da-1cc7-4eae-8fd9-4d5f68f015ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'liquid-soap-dispenser'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('oxygen', 'cylinder', 'tank', 'gas', 'valve', 'medical', 'storage', 'equipment')

    def build(self) -> None:
        # The narrow stepped neck is part of the tank outline, avoiding a
        # crowded little square loop beneath the T valve.
        self.add_line('neck-left',(20,18),(20,12))
        self.add_line('neck-top-left',(20,12),(24,12))
        self.add_line('neck-top-right',(24,12),(28,12))
        self.add_line('neck-right',(28,12),(28,18))
        self.add_line('shoulder-flat-right',(28,18),(30,18))
        self.add_arc('shoulder-right',(30,18),(38,26),radius_x=8)
        self.add_line('body-right',(38,26),(38,36))
        self.add_arc('base-right',(38,36),(30,44),radius_x=8)
        self.add_line('base',(30,44),(18,44))
        self.add_arc('base-left',(18,44),(10,36),radius_x=8)
        self.add_line('body-left',(10,36),(10,26))
        self.add_arc('shoulder-left',(10,26),(18,18),radius_x=8)
        self.add_line('shoulder-flat-left',(18,18),(20,18))
        self.add_contour('tank','neck-left','neck-top-left','neck-top-right',
                         'neck-right','shoulder-flat-right','shoulder-right',
                         'body-right','base-right','base','base-left','body-left',
                         'shoulder-left','shoulder-flat-left',closed=True)
        self.add_polyline('valve',(16,4),(24,4),(32,4))
        self.add_line('valve-stem',(24,4),(24,12))
        self.relate('connect','valve','valve-stem')
        self.relate('connect','tank','valve-stem')
