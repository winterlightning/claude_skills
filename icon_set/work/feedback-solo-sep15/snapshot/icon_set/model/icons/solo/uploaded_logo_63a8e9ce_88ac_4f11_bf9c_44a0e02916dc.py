"""Open cupped hook cradling one ring. Reduce the broad ribbon outline to a smooth asymmetric stroke while retaining the inner circle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63a8e9ce-88ac-4f11-bf9c-44a0e02916dc'
SOURCE_PATH = 'pictographic-primitives/logos/uploaded logo_63a8e9ce-88ac-4f11-bf9c-44a0e02916dc.svg'
AUTHOR = 'gpt-6'

class UploadedLogo(Solo48):
    icon_id = 'uploaded-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('uploaded', 'file-hosting', 'hook', 'upload', 'logo', 'brand', 'cloud')

    def build(self):
        # Plan: Open cupped hook cradling one ring. Reduce the broad ribbon outline to a smooth asymmetric stroke while retaining the inner circle.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_bezier('hook',(20,6),((20,16),(6,18),(6,30)),((6,36),(14,42),(24,42)),((32,42),(36,32),(42,30)))
        circle('core',25,26,5)

