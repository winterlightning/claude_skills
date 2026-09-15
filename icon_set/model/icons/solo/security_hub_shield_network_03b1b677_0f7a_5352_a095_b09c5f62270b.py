"""Security Hub Shield Network.

Plan: SQUARE centerlines (6,6)-(42,42); a central shield owns four symmetric network spokes and identical corner nodes.
Construction references: Lucide shield: dominant shield silhouette; supplied reference supplies the four-node network.
Reduction: Removed the shield’s central divider and simplified hexagonal nodes to small circular outlines to fit the 48px spacing budget.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03b1b677-0f7a-5352-a095-b09c5f62270b'
SOURCE_PATH = 'pictographic-primitives/apps/amazon web service security hub shield_03b1b677-0f7a-5352-a095-b09c5f62270b.svg'
SOURCE_ICON_IDS = ('03b1b677-0f7a-5352-a095-b09c5f62270b',)
SOURCE_PATHS = ('pictographic-primitives/apps/amazon web service security hub shield_03b1b677-0f7a-5352-a095-b09c5f62270b.svg',)
AUTHOR = 'gpt-6'


class SecurityHubShieldNetwork(Solo48):
    icon_id = 'security-hub-shield-network'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    aliases = ()
    keywords = ('security', 'hub', 'shield', 'network')

    def build(self) -> None:
        axis=24
        self.add_polyline("shield",(16,17),(24,14),(32,17),(32,26),(24,34),(16,26),closed=True)
        for row,y in enumerate((9,39)):
            for col,x in enumerate((9,39)):
                k=f"node-{row}-{col}"
                r=3
                self.add_arc(k+"-top",(x-r,y),(x+r,y),radius_x=r)
                self.add_arc(k+"-bottom",(x+r,y),(x-r,y),radius_x=r)
                self.add_contour(k,k+"-top",k+"-bottom",closed=True)
                start=(x+r,y) if col==0 else (x-r,y)
                end=(16 if col==0 else 32,17 if row==0 else 26)
                self.add_line(k+"-spoke",start,end)
                self.relate("connect",k,k+"-spoke")
                self.relate("connect","shield",k+"-spoke")
