"""Three input ring nodes and two output ring nodes with crossing connections. Lucide network informs equal nodes and explicit contacts. The right column is spread vertically; the middle input joins the central crossing instead of a dense extra diagonal. Five nodes retained.
SOLO48 SQUARE; authored directly against the live contract, never scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='7e75fbd6-3a21-50f8-aff0-6aa26d0669a8'
SOURCE_PATH='pictographic-primitives/programing/deep learning frameworks_7e75fbd6-3a21-50f8-aff0-6aa26d0669a8.svg'
AUTHOR='gpt-6'

class NeuralNetworkNodes(Solo48):
    icon_id='neural-network-nodes'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('neural', 'network', 'nodes', 'deep-learning', 'ai', 'graph', 'layers', 'model')

    def build(self) -> None:
        def oval(name,x,y,rx,ry):
            self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        for name,x,y in (('input-top',9,9),('input-middle',9,24),('input-bottom',9,39),('output-top',39,9),('output-bottom',39,39)):
            oval(name,x,y,3,3)
        self.add_line('top-link',(12,9),(36,9))
        self.add_line('bottom-link',(12,39),(36,39))
        self.add_line('down-left',(12,9),(24,24))
        self.add_line('down-right',(24,24),(36,39))
        self.add_line('up-left',(12,39),(24,24))
        self.add_line('up-right',(24,24),(36,9))
        self.add_line('middle-link',(12,24),(24,24))
        node_links={'input-top':('top-link','down-left'),'input-middle':('middle-link',),'input-bottom':('bottom-link','up-left'),'output-top':('top-link','up-right'),'output-bottom':('bottom-link','down-right')}
        from itertools import combinations
        for node,links in node_links.items():
            for link in links: self.relate('connect',node,link)
            for a,b in combinations(links,2): self.relate('connect',a,b)
        for a,b in combinations(('down-left','down-right','up-left','up-right','middle-link'),2):
            self.relate('connect',a,b)
