"""A starburst of eight straight rays radiates from a small rounded octagon at its centre.

Symbol plan: Eight attached rays derived from common center and an octagonal hub; radial maximum20.
Review notes: Lucide sun informs eight-way repetition, while the attached rays and central octagon follow the Loom reference. All rays and opposite hub vertices share parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b228909-c40f-4cd0-8bd0-0cce871f24de'
SOURCE_PATH = 'pictographic-primitives/logos/loom logo_5b228909-c40f-4cd0-8bd0-0cce871f24de.svg'
AUTHOR = 'gpt-6'

class LoomLogo(Solo48):
    icon_id = 'loom-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('loom', 'video', 'recording', 'starburst', 'logo', 'brand', 'screen-recording')

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
        axis=24
        hub=[(-4,-8),(0,-8),(4,-8),(6,-6),(8,-4),(8,0),(8,4),(6,6),(4,8),(0,8),(-4,8),(-6,6),(-8,4),(-8,0),(-8,-4),(-6,-6)]
        self.add_polyline('hub',*[(axis+x,axis+y) for x,y in hub],closed=True)
        starts=[(0,-8),(6,-6),(8,0),(6,6),(0,8),(-6,6),(-8,0),(-6,-6)]
        ends=[(0,-20),(14,-14),(20,0),(14,14),(0,20),(-14,14),(-20,0),(-14,-14)]
        for i,(start,end) in enumerate(zip(starts,ends)):
            name=f'ray-{i}';self.add_line(name,(axis+start[0],axis+start[1]),(axis+end[0],axis+end[1]))
            node=hub.index(start)
            for edge in [node or len(hub),node+1]:self.relate('connect',name,f'hub-{edge}')
