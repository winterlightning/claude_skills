"""Server and Network Hub — batch 53."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '817a8716-0dc9-49ba-a36f-b471f6d798d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/internet/elemental live_817a8716-0dc9-49ba-a36f-b471f6d798d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'server-and-network-hub'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'internet'
    categories = ('internet', 'primitives')
    aliases = ()
    keywords = ('server', 'and', 'network', 'hub')

    def build(self):
        # Plan: rounded server with a horizontal slot, connected hexagonal hub and three branches.
        # VRECT_L extremes8,4,40,44. Lucide server/network inform case and node links.
        # Drop tiny circular indicator; one clear slot preserves server identity.
        self.box('server',8,4,32,20,4)
        self.add_line('slot',(18,14),(30,14))
        self.add_polyline('hub',(24,28),(30,32),(30,35),(30,38),(24,42),(18,38),(18,35),(18,32),closed=True)
        for n,a,z in [('upper',(24,24),(24,28)),('left',(18,35),(8,35)),('right',(30,35),(40,35)),('lower',(24,42),(24,44))]:self.add_line(n,a,z)
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

