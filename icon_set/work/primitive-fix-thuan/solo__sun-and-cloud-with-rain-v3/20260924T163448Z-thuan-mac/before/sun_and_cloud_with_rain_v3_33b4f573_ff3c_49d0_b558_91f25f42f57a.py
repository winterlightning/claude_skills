"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33b4f573-ff3c-49d0-b558-91f25f42f57a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/cloud sun rain_33b4f573-ff3c-49d0-b558-91f25f42f57a.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'sun-and-cloud-with-rain-v3'
    variant_of = 'sun-and-cloud-with-rain'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/weather'
    aliases = ()
    keywords = ('sun', 'and', 'cloud', 'with', 'rain')

    def build(self):
        # Plan: cloud owns two lobes and an open lower edge; sun behind; rain series.
        # SQUARE extremes (6,6)-(42,42). Lucide cloud-sun-rain's reduced lobes.
        self.add_bezier('cloud-upper', (6,25), ((6,21),(9,19),(12,19)), ((12,11),(19,10),(22,16)))
        self.add_bezier('cloud-shoulder',(22,16),((24,20),(20,26),(28,26)),((30,26),(32,26),(34,28)))
        self.add_bezier('cloud-right', (34,28), ((34,30),(32,32),(30,32)))
        self.add_line('cloud-base', (18,32), (13,32))
        self.add_bezier('cloud-left', (13,32), ((9,32),(6,29),(6,25)))
        self.add_contour('cloud', 'cloud-base','cloud-left','cloud-upper','cloud-shoulder','cloud-right')
        self.add_arc('sun', (22,16), (34,28),radius_x=12)
        self.relate('connect','sun','cloud')
        for name,a,b in [('ray-top',(27,6),(27,7)),('ray-diagonal',(39,9),(41,7)),('ray-right',(42,22),(42,24))]:
            self.add_line(name,a,b)
        for i,x in enumerate((14,24,34)):
            self.add_line(f'rain-{i}',(x,40),(x-1,42))
