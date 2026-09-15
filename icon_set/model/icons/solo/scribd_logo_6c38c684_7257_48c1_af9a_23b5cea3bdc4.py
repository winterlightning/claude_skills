"""Large rounded S with a detached lower-right ring. Reduce the bold outline to a single stroke, keeping the distinctive separate period."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c38c684-7257-48c1-af9a-23b5cea3bdc4'
SOURCE_PATH = 'pictographic-primitives/logos/scribd logo_6c38c684-7257-48c1-af9a-23b5cea3bdc4.svg'
AUTHOR = 'gpt-6'

class ScribdLogo(Solo48):
    icon_id = 'scribd-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('scribd', 'documents', 'reading', 'letter-s', 'logo', 'brand', 'books')

    def build(self):
        # Plan: Large rounded S with a detached lower-right ring. Reduce the bold outline to a single stroke, keeping the distinctive separate period.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_bezier('s',(30,10),((30,6),(26,6),(20,6)),((12,6),(6,10),(6,16)),((6,22),(12,22),(18,24)),((24,26),(28,28),(28,34)),((28,40),(24,42),(18,42)),((10,42),(6,40),(6,34)))
        circle('period',39,38,3)

