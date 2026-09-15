"""An isometric cube with its top face plain, the left face striped by two horizontal slots and the right face by two vertical slots.

Symbol plan: Isometric cube with horizontal left stripe and vertical right stripe; extremes (8,4)-(40,44).
Review notes: Keeps the isometric cube and different stripe directions, reducing each face to one stripe. Walls split at every stripe junction; asymmetric stripe orientations are identifying features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86055bde-16cd-42c5-9fbb-7eb9187bb65b'
SOURCE_PATH = 'pictographic-primitives/logos/openbedge logo_86055bde-16cd-42c5-9fbb-7eb9187bb65b.svg'
AUTHOR = 'gpt-6'

class OpenbadgesLogo(Solo48):
    icon_id = 'openbadges-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('openbadges', 'badges', 'cube', 'logo', 'brand', 'credentials', 'education')

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
        groups={'outline':[(24,4),(40,14),(40,34),(32,39),(24,44),(8,34),(8,24),(8,14),(24,4)],'seams':[(8,14),(24,24),(32,19),(40,14)],'spine':[(24,24),(24,34),(24,44)],'left-stripe':[(8,24),(24,34)],'right-stripe':[(32,19),(32,39)]}
        edges=[]
        for name,points in groups.items():
         members=[]
         for i,(a,b) in enumerate(zip(points,points[1:])):
          n=f'{name}-{i}';self.add_line(n,a,b);members.append(n);edges.append((n,a,b))
         self.add_contour(name,*members,closed=name=='outline')
        for i,(a,p,q) in enumerate(edges):
         for b,r,t in edges[i+1:]:
          if {p,q}&{r,t}:self.relate('connect',a,b)
