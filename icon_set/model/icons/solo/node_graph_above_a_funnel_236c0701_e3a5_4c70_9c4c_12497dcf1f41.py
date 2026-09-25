'A four-node graph sits above a filter funnel. Natural data filtering diagram, no corner modifier. HRECT_L budgets two rows. Lucide funnel contributes the continuous taper-and-outlet silhouette. Hollow graph nodes reduced to diameter four; shared graph vertices.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '236c0701-e3a5-4c70-9c4c-12497dcf1f41'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon manage service for prometeus_236c0701-e3a5-4c70-9c4c-12497dcf1f41.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'node-graph-above-a-funnel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Data Metrics Funnel']
    keywords = ['funnel', 'graph', 'nodes', 'filter', 'data', 'metrics', 'network']
    def build(self):
        points=[(6,10),(18,16),(30,10),(42,16)]
        for j,(x,y) in enumerate(points):
            self.add_arc(f'node-{j}-a',(x-2,y),(x+2,y),radius_x=2)
            self.add_arc(f'node-{j}-b',(x+2,y),(x-2,y),radius_x=2)
            self.add_contour(f'node-{j}',f'node-{j}-a',f'node-{j}-b',closed=True)
            if j:
                px,py=points[j-1]
                self.add_line(f'link-{j}',(px+2,py),(x-2,y))
                self.relate('connect',f'link-{j}',f'node-{j-1}')
                self.relate('connect',f'link-{j}',f'node-{j}')
        self.add_polyline('funnel',(8,26),(40,26),(28,34),(28,40),(20,40),(20,34),closed=True)
