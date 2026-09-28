'Poisoned Dagger with Drops.\n\nSymbol plan: Diagonal dagger with transverse guard and three surrounding drop marks. Hollow drop details and pommel ring omitted for spacing; no specific poison meaning assigned.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a44c8381-f482-4b4b-995e-3d8b71f84688'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dagger-beside-three-pointed-droplets/20260927T174057Z-thuan-mac-1/reference/fantasy medieval assassins knife poison_a44c8381-f482-4b4b-995e-3d8b71f84688.svg'
AUTHOR = "gpt-6-astra"

class DaggerBesideThreePointedDroplets(Solo48):
    icon_id = 'dagger-beside-three-pointed-droplets'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dagger', 'beside', 'three', 'pointed', 'droplets')

    def build(self):
        self.add_arc('pommel-top',(6,11),(16,11),radius_x=5)
        self.add_arc('pommel-bottom',(16,11),(6,11),radius_x=5)
        self.add_contour('pommel','pommel-top','pommel-bottom',closed=True)
        self.add_line('grip',(16,11),(24,20))
        self.add_line('guard',(14,30),(30,14))
        self.add_polyline('blade',(24,20),(42,42),(30,26))
        self.relate('connect','pommel','grip')
        self.relate('connect','grip','guard','blade')
        self.add_polyline('drop-upper',(36,7),(38,10),(40,7))
        self.add_polyline('drop-middle',(38,20),(40,23),(42,20))
        self.add_polyline('drop-lower',(6,38),(8,42),(10,38))
