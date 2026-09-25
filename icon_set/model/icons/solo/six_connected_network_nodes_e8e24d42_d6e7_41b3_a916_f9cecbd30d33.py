"""Six Connected Network Nodes — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e8e24d42-d6e7-41b3-a916-f9cecbd30d33'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/internet/crypto blockchain technology_e8e24d42-d6e7-41b3-a916-f9cecbd30d33.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'six-connected-network-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'internet'
    categories = ('internet', 'primitives')
    aliases = ()
    keywords = ('six', 'connected', 'network', 'nodes')

    def build(self):
        # Plan: a 2-by-3 repeat of equal rounded square nodes with orthogonal shared links.
        # HRECT_L extremes4,8,44,40. Lucide network informs split node attachment edges.
        for j,y in enumerate((8,32)):
            for i,x in enumerate((4,20,36)):self.box(f'node-{i}-{j}',x,y,8,8)
            for i,x in enumerate((12,28)):self.add_line(f'h-{i}-{j}',(x,y+4),(x+8,y+4))
        for i,x in enumerate((8,24,40)):self.add_line(f'v-{i}',(x,16),(x,32))
        self.join_shared()


    def circle(self,n,x,y,r,attachments=()):
        from math import atan2
        pts=list(dict.fromkeys([(x+r,y),(x,y+r),(x-r,y),(x,y-r)]+list(attachments)))
        pts.sort(key=lambda p:atan2(p[1]-y,p[0]-x))
        for j in range(len(pts)):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%len(pts)],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(len(pts))],closed=True)

    def box(self,n,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h//2),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+h//2),(x,y+r)]
        ids=[]
        for i,(a,z) in enumerate(zip(pts,pts[1:]+pts[:1])):
            if a==z:continue
            name=f'{n}-{i}';ids.append(name)
            if i in (2,5,8,11):self.add_arc(name,a,z,radius_x=r)
            else:self.add_line(name,a,z)
        self.add_contour(n,*ids,closed=True)

    def join_shared(self):
        from icon_set.renderers.svg import build_paths
        paths=build_paths(self.draw())
        for i,a in enumerate(paths):
            ap={(p.start.x,p.start.y) for p in a['primitives']}|{(p.end.x,p.end.y) for p in a['primitives']}
            for z in paths[i+1:]:
                zp={(p.start.x,p.start.y) for p in z['primitives']}|{(p.end.x,p.end.y) for p in z['primitives']}
                if ap & zp:self.relate('connect',a['id'],z['id'])

