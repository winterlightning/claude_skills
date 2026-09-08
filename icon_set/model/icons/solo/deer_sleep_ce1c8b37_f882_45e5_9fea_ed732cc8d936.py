"""A curled sleeping deer with a single forked antler and sleep mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce1c8b37-f882-45e5-9fea-ed732cc8d936'
SOURCE_PATH = 'pictographic-primitives/animals/deer sleep_ce1c8b37-f882-45e5-9fea-ed732cc8d936.svg'
AUTHOR = 'gpt-6'


class SleepingDeer(Solo48):
    icon_id = 'sleeping-deer'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('deer', 'sleep', 'rest', 'curled', 'antlers', 'night', 'zzz', 'animal')

    def build(self) -> None:
        # Centerline extremes: (2,5)-(46,43).
        self.add_arc("rump",(12,25),(12,43),radius_x=10,radius_y=9,sweep=False)
        self.add_arc("underside",(12,43),(42,25),radius_x=30,radius_y=18,sweep=False)
        self.add_arc("neck",(42,25),(34,15),radius_x=14,sweep=False)
        self.add_line("face-1",(34,15),(34,11))
        self.add_line("face-2",(34,11),(18,17))
        self.add_arc("muzzle",(18,17),(18,25),radius_x=4,sweep=False)
        self.add_line("tuck",(18,25),(12,25))
        self.add_contour("deer","rump","underside","neck","face-1","face-2","muzzle","tuck",closed=True)
        self.add_polyline("antler",(22,15),(18,9),(18,5))
        self.relate("connect","deer","antler")
        self.add_line("tine",(18,9),(10,7))
        self.relate("connect","antler","tine")
        self.add_polyline("sleep",(41,5),(46,5),(41,11),(46,11))
