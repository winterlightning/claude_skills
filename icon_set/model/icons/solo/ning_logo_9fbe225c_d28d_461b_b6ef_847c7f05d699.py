"""A branching network of seven round nodes joined by straight links, spreading from a central junction toward the corners.

Symbol plan: Two branching node groups, eight small circles from the rendered reference; extremes (6,6)-(42,42).
Review notes: Actual source has eight nodes, despite the seven-node brief. Keeps eight small circles and both branch groups; rings become dot-like at native size. Earlier Lucide circle construction informs the nodes; uneven branching follows the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fbe225c-d28d-461b-b6ef-847c7f05d699'
SOURCE_PATH = 'pictographic-primitives/logos/ning logo_9fbe225c-d28d-461b-b6ef-847c7f05d699.svg'
AUTHOR = 'gpt-6'

class NingLogo(Solo48):
    icon_id = 'ning-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('ning', 'social-network', 'nodes', 'logo', 'brand', 'community', 'network')

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
        nodes={'tl':(14,8),'tr':(34,8),'tc':(24,18),'l':(8,24),'c':(18,30),'bl':(8,40),'br':(34,40),'r':(40,24)}
        for n,(x,y) in nodes.items():ring(n,x,y,2)
        for i,(a,b) in enumerate([('tl','tc'),('tc','tr'),('l','c'),('bl','c'),('c','br'),('br','r')]):
         x,y=nodes[a];u,v=nodes[b];direction=1 if u>x else -1
         self.add_line(f'link-{i}',(x+direction*2,y),(u-direction*2,v))
         for n in [a,b]:
          for half in ['top','bottom']:self.relate('connect',f'link-{i}',n+'-'+half)
