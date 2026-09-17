"""Manual Citrus Juicer.

Plan: Pointed ridged citrus reamer on a low collecting jug, with left lip and open right handle. Bounds (4,8)-(44,40).
Construction reference: Lucide funnel: tapered functional upper part; coffee: curved lower jug.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '90890c3c-16d8-46db-a19b-502561eebc19'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/juicer_90890c3c-16d8-46db-a19b-502561eebc19.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'manual-citrus-juicer-with-pointed-reamer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('manual', 'citrus', 'juicer')

    def build(self):
        poly(self,'reamer',(10,24),(14,16),(22,8),(30,16),(34,24))
        line(self,'ridge',(22,8),(22,24))
        path(self,'jug',(4,24),('L',(10,24)),('L',(22,24)),('L',(34,24)),('L',(36,24)),('L',(36,36)),('A',4,4,True,(32,40)),('L',(14,40)),('A',4,4,True,(10,36)),('L',(10,32)),('L',(4,24)),closed=True)
        path(self,'handle',(36,24),('A',8,8,True,(44,32)),('L',(44,36)))
        contacts(self)
