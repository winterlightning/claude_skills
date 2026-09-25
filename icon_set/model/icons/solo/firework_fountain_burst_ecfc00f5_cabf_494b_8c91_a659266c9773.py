"""Celebration Fireworks Burst.
Plan: Fountain is a mirrored fan of three smooth cubic pairs sharing the burst node; vertical spine. Centerline extremes (4,8)-(44,40).
Reference: No useful local Lucide fountain match; mirrored smooth trails.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecfc00f5-cabf-494b-8c91-a659266c9773'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/fireworks_ecfc00f5-cabf-494b-8c91-a659266c9773.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'firework-fountain-burst'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    aliases = ()
    keywords = ('celebration', 'fireworks', 'burst')

    def build(self):
        origin=(24,30)
        self.add_polyline('spine',(24,8),origin,(24,40))
        # Shared cubic definitions preserve the outward fan and tangent flow.
        definitions=(((20,16),(15,11),(8,8)),((16,20),(8,20),(4,24)),((16,28),(12,32),(10,40)))
        trails=[]
        for i,controls in enumerate(definitions):
            for side in ('left','right'):
                points=controls if side=='left' else tuple((48-x,y) for x,y in controls)
                name=f'trail-{side}-{i}'
                self.add_bezier(name,origin,points)
                trails.append(name)
        parts=['spine']+trails
        for i,a in enumerate(parts):
            for b in parts[i+1:]: self.relate('connect',a,b)
