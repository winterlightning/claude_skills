"""A windowless sedan with integrated rounded U tyres. Broad envelope preserves the cabin and long body. Lucide car informed silhouette reduction; no window or full wheel circles added."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fdb13eb-bc4d-44a6-bca4-d87dd2adb768'
SOURCE_PATH = 'pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg'
SOURCE_REFERENCES = (('1fdb13eb-bc4d-44a6-bca4-d87dd2adb768', 'pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg'),)
AUTHOR = 'gpt-6'

class SedanSilhouette(Solo48):
    icon_id = 'sedan-silhouette'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('car', 'sedan', 'vehicle', 'silhouette', 'automobile', 'side view', 'saloon', 'driving')

    def build(self) -> None:
        self.add_line('rear',(4,32),(4,24))
        self.add_arc('rear-corner',(4,24),(8,20),radius_x=4)
        self.add_line('upper-a',(8,20),(12,20))
        self.add_line('upper-b',(12,20),(18,12))
        self.add_arc('roof-rear',(18,12),(26,8),radius_x=10)
        self.add_line('upper-c',(26,8),(28,8))
        self.add_arc('roof-front',(28,8),(32,10),radius_x=5)
        self.add_line('upper-d',(32,10),(38,18))
        self.add_line('upper-e',(38,18),(40,20))
        self.add_arc('front-corner',(40,20),(44,24),radius_x=4)
        self.add_line('front',(44,24),(44,32))
        self.add_line('lower-a',(44,32),(40,32))
        self.add_line('tyre-front-a',(40,32),(40,35))
        self.add_arc('tyre-front-b',(40,35),(30,35),radius_x=5)
        self.add_line('tyre-front-c',(30,35),(30,32))
        self.add_line('sill',(30,32),(18,32))
        self.add_line('tyre-rear-a',(18,32),(18,35))
        self.add_arc('tyre-rear-b',(18,35),(8,35),radius_x=5)
        self.add_line('tyre-rear-c',(8,35),(8,32))
        self.add_line('lower-b',(8,32),(4,32))
        self.add_contour('silhouette','rear','rear-corner','upper-a','upper-b','roof-rear','upper-c','roof-front','upper-d','upper-e','front-corner','front','lower-a','tyre-front-a','tyre-front-b','tyre-front-c','sill','tyre-rear-a','tyre-rear-b','tyre-rear-c','lower-b',closed=True)
