"""Sparking Firework Rocket.
Plan: Diagonal rocket body, detached open cap and attached stick; surrounding sparks are separated. Extrema (6,6)-(42,42).
Reference: No useful Lucide stick-rocket match; clear diagonal body and separated sparks.
Reduction: Spark count reduced to four.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '918c0ef7-9e8f-541d-8e40-52c79fce54e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/fireworks stick_918c0ef7-9e8f-541d-8e40-52c79fce54e0.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'firework-rocket-radiating-sparks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    aliases = ()
    keywords = ('sparking', 'firework', 'rocket')

    def build(self):

        self.add_polyline('body',(14,26),(26,14),(34,22),(22,34),(18,30),closed=True)
        self.add_line('stick',(18,30),(6,42))
        self.relate('connect','body','stick')
        self.add_polyline('cap',(30,6),(42,6),(42,18))
        for name,a,b in (('spark-left',(6,18),(10,18)),('spark-top',(10,6),(14,10)),('spark-right',(38,34),(42,38)),('spark-bottom',(30,38),(30,42))):self.add_line(name,a,b)
