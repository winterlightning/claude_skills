"""A front-view floating buoy with a round ring, tapered frame and wide float on water. SQUARE ink (6,6)-(42,42). No useful exact Lucide match; mirrored supports and tangent wave arcs preserve balance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdf0e327-3c90-5116-a915-75c60283d533'
SOURCE_PATH = 'pictographic-primitives/transportation/buoy_bdf0e327-3c90-5116-a915-75c60283d533.svg'
SOURCE_REFERENCES = (('bdf0e327-3c90-5116-a915-75c60283d533', 'pictographic-primitives/transportation/buoy_bdf0e327-3c90-5116-a915-75c60283d533.svg'),)
AUTHOR = 'gpt-6'

class FloatingBuoy(Solo48):
    icon_id = 'floating-buoy'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('buoy', 'float', 'marker', 'sea', 'marine', 'navigation', 'water', 'harbour')

    def build(self) -> None:
        # A radius-five ring exposes exact 3-4-5 attachment points for the frame legs.
        self.add_arc('ring-top',(21,15),(27,15),radius_x=5,large_arc=True)
        self.add_arc('ring-bottom',(27,15),(21,15),radius_x=5)
        self.add_contour('ring','ring-top','ring-bottom',closed=True)
        self.add_line('frame-left',(21,15),(15,27))
        self.add_line('frame-right',(27,15),(33,27))
        self.add_polyline('float',(12,38),(6,29),(15,27),(24,25),(33,27),(42,29),(36,38))
        for a in ['frame-left','frame-right']:
            self.relate('connect',a,'ring')
            self.relate('connect',a,'float')
        self.add_arc('wave-l',(6,42),(12,38),radius_x=6,radius_y=4)
        self.add_arc('wave-lm',(12,38),(18,39),radius_x=6,radius_y=1)
        self.add_arc('wave-lc',(18,39),(24,40),radius_x=6,radius_y=1,sweep=False)
        self.add_arc('wave-rc',(24,40),(30,39),radius_x=6,radius_y=1,sweep=False)
        self.add_arc('wave-rm',(30,39),(36,38),radius_x=6,radius_y=1)
        self.add_arc('wave-r',(36,38),(42,42),radius_x=6,radius_y=4)
        self.add_contour('wave','wave-l','wave-lm','wave-lc','wave-rc','wave-rm','wave-r')
        self.relate('connect','float','wave')
