"""A right-pointing triangle outline made of angled planes, with a shorter inner stroke folding back from its upper left edge.

Symbol plan: Two right-pointing planes with a folded upper-left stroke and a shared lower-left/right junction. Extremes (8,4)-(40,44).
Review notes: Keeps the folded triangle and lower perspective plane. The left opening is enlarged for clearance. No useful Lucide brand match; angular direction and asymmetry carry the logo identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84417f93-1339-43a5-9ec0-4bf0626b254d'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft dynamics logo_84417f93-1339-43a5-9ec0-4bf0626b254d.svg'
AUTHOR = 'gpt-6'

class MicrosoftDynamicsLogo(Solo48):
    icon_id = 'microsoft-dynamics-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('microsoft-dynamics', 'dynamics', 'microsoft', 'crm', 'logo', 'brand', 'business')

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
        self.add_polyline('main',(8,24),(8,44),(40,18),(8,4),(8,14),(22,22))
        self.add_polyline('lower',(8,44),(40,28),(40,18))
        for a,b in [('lower-1','main-1'),('lower-1','main-2'),('lower-2','main-2'),('lower-2','main-3')]:self.relate('connect',a,b)
