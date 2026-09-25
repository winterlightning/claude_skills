"""A rounded square frame holds an outlined arch-shaped n with two curved signal arcs rising over its upper right.

Symbol plan: Rounded badge containing arch n and one signal arc; extremes (6,6)-(42,42).
Review notes: Lucide wifi and square inform broadcast arc and badge. Keeps the square distinction; reduces the n to a stroke and two signals to one to preserve spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4756ef8f-9e20-4e8e-a498-fb1e7e5ede67'
SOURCE_PATH = 'pictographic-primitives/logos/nintendo network logo 1_4756ef8f-9e20-4e8e-a498-fb1e7e5ede67.svg'
AUTHOR = 'gpt-6'

class NintendoNetworkLogoSquare(Solo48):
    icon_id = 'nintendo-network-logo-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('nintendo-network', 'nintendo', 'gaming', 'online', 'logo', 'brand', 'signal')

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
        rounded('frame',6,6,42,42,6)
        self.add_line('n-left',(15,33),(15,32));self.add_arc('n-arch',(15,32),(27,32),radius_x=6)
        self.add_line('n-right',(27,32),(27,33));self.add_contour('n','n-left','n-arch','n-right')
        self.add_bezier('signal',(15,15),((22,13),(29,16),(33,22)))
