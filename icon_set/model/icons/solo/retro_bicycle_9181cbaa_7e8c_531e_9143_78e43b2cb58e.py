"""A retro bicycle with a diamond frame, saddle and hooked handlebar. SQUARE ink (6,6)-(42,42). Lucide bike informs equal wheels; separate struts join the frame to wheel tops to keep the spokes and crossing wedges out of the small drawing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9181cbaa-7e8c-531e-9143-78e43b2cb58e'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle retro_9181cbaa-7e8c-531e-9143-78e43b2cb58e.svg'
AUTHOR = 'gpt-6'

class RetroBicycle(Solo48):
    icon_id = 'retro-bicycle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('bicycle', 'bike', 'retro', 'cycling', 'vintage', 'pedal', 'transport', 'two wheels')

    def build(self) -> None:
        # Two clear wheel loops; separate open struts connect the diamond to them.
        wheel_y, radius = 36, 6
        for side,x in [('rear',12),('front',36)]:
            self.add_arc(side+'-right',(x,30),(x,42),radius_x=radius)
            self.add_arc(side+'-left',(x,42),(x,30),radius_x=radius)
            self.add_contour(side+'-wheel',side+'-right',side+'-left',closed=True)
        self.add_polyline('frame',(12,21),(20,10),(30,10),(25,21),(12,21),closed=True)
        self.add_line('seat-tube',(20,10),(25,21))
        self.add_line('rear-strut',(12,21),(12,30))
        self.add_polyline('fork',(36,30),(30,10),(28,6),(40,6))
        self.add_arc('bar-curl',(40,6),(40,10),radius_x=2)
        self.add_line('seat-post',(20,10),(16,6))
        self.add_polyline('saddle',(12,6),(16,6),(20,6))
        for a,b in [('frame','seat-tube'),('frame','fork'),('fork','bar-curl'),('frame','seat-post'),('seat-post','saddle'),('rear-strut','frame'),('rear-strut','rear-wheel'),('fork','front-wheel')]:
            self.relate('connect',a,b)
