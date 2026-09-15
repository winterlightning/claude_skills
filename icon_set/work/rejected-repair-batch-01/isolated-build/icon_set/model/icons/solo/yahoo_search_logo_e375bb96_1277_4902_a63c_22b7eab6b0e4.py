"""Complete lowercase yahoo wordmark reflowed as yah above oo. Retain the descending y, the a counter and two matching o counters; omit heavy outline weight."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e375bb96-1277-4902-a63c-22b7eab6b0e4'
SOURCE_PATH = 'pictographic-primitives/logos/yahoo search logo_e375bb96-1277-4902-a63c-22b7eab6b0e4.svg'
AUTHOR = 'gpt-6'

class YahooSearchLogo(Solo48):
    icon_id = 'yahoo-search-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('yahoo', 'search', 'wordmark', 'web', 'logo', 'brand', 'portal')

    def build(self):
        # Plan: Complete lowercase yahoo wordmark reflowed as yah above oo. Retain the descending y, the a counter and two matching o counters; omit heavy outline weight.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('y-upper',(4,8),(6,14),(8,8));self.add_line('y-tail',(6,14),(4,20));self.relate('connect','y-upper','y-tail')
        circle('a',22,13,5);self.add_line('a-tail',(27,13),(27,20));self.relate('connect','a','a-tail')
        self.add_polyline('h-stem',(36,8),(36,16),(36,20));self.add_arc('h-top',(36,16),(44,16),radius_x=4);self.add_line('h-end',(44,16),(44,20));self.relate('connect','h-stem','h-top');self.relate('connect','h-top','h-end')
        for j,x in enumerate((14,34)):circle('o-'+str(j),x,34,6)

