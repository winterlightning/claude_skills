"""A flat-topped hexagon outline holds a small triangle of three round nodes joined by straight links.

Symbol plan: Pointed hexagon with a triangular three-node graph; extremes (8,4)-(40,44).
Review notes: Keeps the enclosing hexagon and triangular three-node network. The small node rings are reduced to rounded point junctions because their tiny enclosed holes failed full QA. Source is point-topped despite the flat-topped wording in the brief; no useful local Lucide brand match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de3f57a3-1388-41ad-8701-c51243f2be71'
SOURCE_PATH = 'pictographic-primitives/logos/nodesj logo_de3f57a3-1388-41ad-8701-c51243f2be71.svg'
AUTHOR = 'gpt-6'

class NodeHexagonLogo(Solo48):
    icon_id = 'node-hexagon-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('nodejs', 'node', 'hexagon', 'javascript', 'logo', 'brand', 'network')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        self.add_polyline('hexagon',(24,4),(40,14),(40,34),(24,44),(8,34),(8,14),closed=True)
        self.add_polyline('network',(24,16),(17,29),(31,29),closed=True)
        for i,point in enumerate([(24,16),(17,29),(31,29)]):
         name=f'node-{i}';self.add_dot(name,point)
         for edge in [i+1,3 if i==0 else i]:self.relate('connect',name,f'network-{edge}')
