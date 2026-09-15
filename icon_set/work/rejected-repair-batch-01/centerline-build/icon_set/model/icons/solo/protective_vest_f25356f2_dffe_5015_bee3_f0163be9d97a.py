"""A protective vest has a scooped neck and two side fasteners. Lucide shirt informs the continuous garment contour and neckline. Retain matching tabs; remove seam detail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f25356f2-dffe-5015-bee3-f0163be9d97a'
SOURCE_PATH = 'pictographic-primitives/protection/protection vest_f25356f2-dffe-5015-bee3-f0163be9d97a.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'protective-vest'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('vest', 'body armour', 'bulletproof', 'protective', 'garment', 'police', 'safety', 'tactical')

    def build(self):
        # VRECT_L centerline extremes: (8,4)-(40,44).

        # Front garment owns scoop, mirrored armholes and equal side fasteners.
        self.add_line('shoulder-left',(8,4),(16,4))
        self.add_arc('neck',(16,4),(32,4),radius_x=8,sweep=False)
        self.add_line('shoulder-right',(32,4),(40,4))
        self.add_line('arm-right-top',(40,4),(40,12))
        self.add_arc('arm-right',(40,12),(40,24),radius_x=8,sweep=False)
        points = [(40,24),(40,28),(40,36),(40,44),(8,44),(8,36),(8,28),(8,24)]
        for i, (a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line('hem-'+str(i),a,b)
        self.add_arc('arm-left',(8,24),(8,12),radius_x=8,sweep=False)
        self.add_line('arm-left-top',(8,12),(8,4))
        self.add_contour('outline','shoulder-left','neck','shoulder-right','arm-right-top','arm-right',*[f'hem-{i}' for i in range(1,8)],'arm-left','arm-left-top',closed=True)
        for side,x,inside in [('left',8,16),('right',40,32)]:
            self.add_polyline('tab-'+side,(x,28),(inside,28),(inside,36),(x,36))
            self.relate('connect','tab-'+side,'outline')
