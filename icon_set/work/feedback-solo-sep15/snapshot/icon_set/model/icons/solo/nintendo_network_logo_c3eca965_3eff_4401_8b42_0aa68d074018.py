"""An outlined arch-shaped lowercase n with two large curved signal arcs rising over its upper right.

Symbol plan: Arch n with two expanding upper-right signal arcs; extremes (8,4)-(40,44).
Review notes: Lucide wifi informs nested signal curves. Reduces outlined n to one stroke and retains both broadcast arcs. The rightward broadcast direction is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3eca965-3eff-4401-8b42-0aa68d074018'
SOURCE_PATH = 'pictographic-primitives/logos/nintendo network logo_c3eca965-3eff-4401-8b42-0aa68d074018.svg'
AUTHOR = 'gpt-6'

class NintendoNetworkLogo(Solo48):
    icon_id = 'nintendo-network-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
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
        self.add_line('n-left',(8,44),(8,34))
        self.add_arc('n-arch',(8,34),(28,34),radius_x=10)
        self.add_line('n-right',(28,34),(28,44))
        self.add_contour('n','n-left','n-arch','n-right')
        self.add_arc('signal-inner',(18,14),(38,34),radius_x=20)
        self.add_bezier('signal-outer',(18,4),((28,4),(36,8),(40,16)))
