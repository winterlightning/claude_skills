"""An almost-closed circle opens at the upper right, where a small ring sits in the gap. A medium ring sits at the centre.

Symbol plan: Three concentric/radially related rings: open radius20 orbit, central radius6 ring, radius2 satellite at (36,12).
Review notes: Retains all three rings and the upper-right orbit opening. Lucide circle supplies circle construction; asymmetry belongs to the satellite position.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '762da34f-a3c1-4257-b54c-7706a38e934c'
SOURCE_PATH = 'pictographic-primitives/logos/lonic logo_762da34f-a3c1-4257-b54c-7706a38e934c.svg'
AUTHOR = 'gpt-6'

class IonicLogo(Solo48):
    icon_id = 'ionic-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('ionic', 'framework', 'mobile', 'rings', 'logo', 'brand', 'developer')

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
        self.add_arc('orbit',(44,24),(24,4),radius_x=20,large_arc=True)
        ring('core',24,24,6)
        ring('satellite',36,12,2)
