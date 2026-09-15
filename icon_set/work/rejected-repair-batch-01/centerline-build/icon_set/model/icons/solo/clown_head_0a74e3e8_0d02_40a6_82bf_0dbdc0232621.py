"""Clown Head. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a74e3e8-0d02-40a6-82bf-0dbdc0232621'
SOURCE_PATH = 'pictographic-primitives/smileys/clown face_0a74e3e8-0d02-40a6-82bf-0dbdc0232621.svg'
AUTHOR = 'gpt-6'


class ClownHead(Solo48):
    icon_id = 'clown-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/emotions"
    aliases = ()
    keywords = ('clown', 'head', 'hair', 'circus', 'face', 'emoji')

    def build(self) -> None:

        # HRECT_XL ink (2,6)-(46,42); circle head and paired hair lobes.
        points=[(9,25),(15,13),(33,13),(39,25),(24,40),(9,25)]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            self.add_arc(f"face-{i}",a,b,radius_x=15)
        self.add_contour("face",*(f"face-{i}" for i in range(5)),closed=True)
        for side,sign in (("left",1),("right",-1)):
            def p(x,y): return (24+sign*(x-24),y)
            self.add_arc(f"hair-{side}-a",p(15,13),p(10,8),radius_x=5,sweep=sign<0)
            self.add_arc(f"hair-{side}-b",p(10,8),p(4,14),radius_x=6,sweep=sign<0)
            self.add_arc(f"hair-{side}-c",p(4,14),p(9,25),radius_x=5,radius_y=11,sweep=sign<0)
            self.add_contour(f"hair-{side}",*(f"hair-{side}-{c}" for c in "abc"))
            for face in (("face-0","face-1") if side=="left" else ("face-1","face-2")):
                self.relate("connect",f"hair-{side}-a",face)
            for face in (("face-0","face-4") if side=="left" else ("face-2","face-3")):
                self.relate("connect",f"hair-{side}-c",face)
