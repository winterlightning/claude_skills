"""Widened neck to 8-unit centerline separation; exact quarter-ellipse throat. VRECT_L bounds retained. Lucide bird informs the sparse silhouette; asymmetric pose retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0fcbdb00-a505-4fa6-95a8-0fa24ac7895a'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird vulture_0fcbdb00-a505-4fa6-95a8-0fa24ac7895a.svg'
AUTHOR = 'gpt-6'

class Vulture(Solo48):
    icon_id = 'vulture'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('vulture', 'scavenger', 'bird', 'neck', 'beak', 'standing', 'carrion', 'wildlife')

    def build(self):
        # One continuous silhouette joins nape, back, wing and head.
        # Remove the redundant closed wing boundary; preserve the standing profile.
        self.add_arc('head',(26,11),(40,11),radius_x=7)
        self.add_line('beak',(40,11),(40,17))
        self.add_line('chin',(40,17),(34,17))
        self.add_line('neck',(34,17),(34,23))
        self.add_arc('throat',(34,23),(25,30),radius_x=9,radius_y=7)
        self.add_arc('wing-front',(25,30),(23,36),radius_x=10,sweep=True)
        self.add_line('wing-tip',(23,36),(8,42))
        self.add_arc('back',(8,42),(18,18),radius_x=40,sweep=True)
        self.add_line('shoulder',(18,18),(26,19))
        self.add_line('nape',(26,19),(26,11))
        self.add_contour('silhouette','head','beak','chin','neck','throat','wing-front','wing-tip','back','shoulder','nape',closed=True)
        self.add_polyline('leg',(23,36),(26,44),(34,44))
        self.relate('connect','silhouette','leg')
