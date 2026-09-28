"""A diagonal racket paired with its shuttlecock: one natural sports equipment group.
HRECT_L extremes 4,8–44,40. Racket rim owns a sparse string cross; handle meets
an exact 6-8-10 circle point. Shuttle is a single flared feather/cork silhouette.
Source supplies arrangement. No local Lucide racket match; omit dense string mesh.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "de6f8f15-e075-4e2c-853a-cbcc18e0b3cc"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/badminton shuttlecock racquet_de6f8f15-e075-4e2c-853a-cbcc18e0b3cc.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "badminton-racket-beside-a-shuttlecock"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Badminton Racket and Shuttlecock"]
    keywords = ["badminton", "racket", "shuttlecock", "strings", "sport", "handle", "cork"]
    def build(self):
        pts=[(34,8),(44,18),(34,28),(28,26),(24,18),(34,8)]
        rim=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            uid=f"rim-{i}";self.add_arc(uid,a,b,radius_x=10);rim.append(uid)
        self.add_contour("rim",*rim,closed=True)
        self.add_line("handle",(28,26),(4,40))
        self.relate("connect","handle","rim")
        self.add_line("strings-vertical",(34,8),(34,28))
        self.add_line("strings-horizontal",(24,18),(44,18))
        self.relate("connect","strings-vertical","rim")
        self.relate("connect","strings-horizontal","rim")
        self.add_line("feather-top",(4,8),(16,8))
        self.add_line("feather-right",(16,8),(14,20))
        self.add_arc("cork",(14,20),(6,20),radius_x=4)
        self.add_line("feather-left",(6,20),(4,8))
        self.add_contour("shuttle","feather-top","feather-right","cork","feather-left",closed=True)
