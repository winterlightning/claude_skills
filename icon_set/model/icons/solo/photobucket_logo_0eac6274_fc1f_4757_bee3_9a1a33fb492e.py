"""Camera body and centered circular lens with enlarged surrounding clearance. Lucide camera informs body/lens hierarchy. Omit the highlight and tiny flash to preserve clear openings."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0eac6274-fc1f-4757-bee3-9a1a33fb492e'
SOURCE_PATH = 'pictographic-primitives/logos/photobucket logo_0eac6274-fc1f-4757-bee3-9a1a33fb492e.svg'
AUTHOR = 'gpt-6'

class PhotobucketLogo(Solo48):
    icon_id = 'photobucket-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('photobucket', 'camera', 'photos', 'logo', 'brand', 'hosting', 'images')

    def build(self):
        # Plan: Camera body and centered circular lens with enlarged surrounding clearance. Lucide camera informs body/lens hierarchy. Omit the highlight and tiny flash to preserve clear openings.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        for name,a,b in [('top',(8,8),(40,8)),('right',(44,12),(44,36)),('bottom',(40,40),(8,40)),('left',(4,36),(4,12))]:
            self.add_line(name,a,b)
        for name,a,b in [('tr',(40,8),(44,12)),('br',(44,36),(40,40)),('bl',(8,40),(4,36)),('tl',(4,12),(8,8))]:
            self.add_arc(name,a,b,radius_x=4)
        self.add_contour('body','top','tr','right','br','bottom','bl','left','tl',closed=True)
        circle('lens',24,24,7)

