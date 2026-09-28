"""Satellite ground station: two distinct signal arcs above a ring receiver, dish and feet.
The reference establishes the symmetric signal and bowl hierarchy; Lucide satellite-dish informs the bowl and receiver connection.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ee4f75c-d7c9-4b11-aa15-e729c0506f3f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__satellite-ground-station/20260927T084430Z-thuan-mac-1/reference/ground station_8ee4f75c-d7c9-4b11-aa15-e729c0506f3f.svg'
AUTHOR = "gpt-6"

class SatelliteGroundStation(Solo48):
    icon_id = "satellite-ground-station"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology"
    categories = ("primitives", "technology")
    aliases = ()
    keywords = ("ground station", "satellite dish", "antenna", "receiver", "signal")

    def build(self):
        self.add_arc("outer-left",(8,8),(24,4),radius_x=16,radius_y=4)
        self.add_arc("outer-right",(24,4),(40,8),radius_x=16,radius_y=4)
        self.add_contour("outer-signal","outer-left","outer-right")
        self.add_arc("inner-left",(16,17),(24,13),radius_x=8,radius_y=4)
        self.add_arc("inner-right",(24,13),(32,17),radius_x=8,radius_y=4)
        self.add_contour("inner-signal","inner-left","inner-right")
        self.add_arc("receiver-left",(21,25),(27,25),radius_x=3)
        self.add_arc("receiver-right",(27,25),(21,25),radius_x=3)
        self.add_contour("receiver","receiver-left","receiver-right",closed=True)
        self.add_line("stem",(24,28),(24,32))
        self.relate("connect","stem","receiver")
        self.add_line("rim-1",(8,32),(24,32))
        self.add_line("rim-2",(24,32),(40,32))
        self.add_arc("dish-right",(40,32),(30,42),radius_x=10)
        self.add_line("dish-base",(30,42),(18,42))
        self.add_arc("dish-left",(18,42),(8,32),radius_x=10)
        self.add_contour("dish","rim-1","rim-2","dish-right","dish-base","dish-left",closed=True)
        self.relate("connect","stem","dish")
        for x in (18,30):
            self.add_line(f"foot-{x}",(x,42),(x,44))
            self.relate("connect",f"foot-{x}","dish")
