"""A surgical face mask has ear loops and a central pleat. No useful exact Lucide match; use mirrored elliptical loops. Reduce two pleats to one."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca479623-685a-50f7-b79c-95ae041dea54'
SOURCE_PATH = 'pictographic-primitives/protection/protection mask_ca479623-685a-50f7-b79c-95ae041dea54.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'surgical-face-mask'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('face mask', 'surgical', 'medical', 'mask', 'health', 'hygiene', 'protection', 'virus')

    def build(self):
        # HRECT_L centerline extremes: (4,8)-(44,40).

        # Face panel and ear loops share upper/lower attachment nodes.
        points = [(12,28),(12,12),(24,8),(36,12),(36,28)]
        for i, (a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line('upper-'+str(i),a,b)
        self.add_arc('lower-right',(36,28),(24,40),radius_x=12,radius_y=12)
        self.add_arc('lower-left',(24,40),(12,28),radius_x=12,radius_y=12)
        self.add_contour('panel',*[f'upper-{i}' for i in range(1,5)],'lower-right','lower-left',closed=True)
        self.add_arc('loop-left',(12,28),(12,12),radius_x=8,radius_y=8)
        self.add_arc('loop-right',(36,12),(36,28),radius_x=8,radius_y=8)
        self.relate('connect','loop-left','panel')
        self.relate('connect','loop-right','panel')
        self.add_line('pleat',(21,24),(27,24))
