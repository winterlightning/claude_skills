"""A large circle holds a lowercase m whose left stem rises tall and rounds into the letter base, forming the letters lm.

Symbol plan: Circular enclosure around l and two repeated m arches; radial centerline radius20.
Review notes: Lucide circle supplies enclosure construction. lm monogram is retained; repeated arches share radius and baseline. Tight internal holes must remain visible in validation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9994f6d-ad31-4072-aab3-5017255d6cab'
SOURCE_PATH = 'pictographic-primitives/logos/linux mint logo 1_e9994f6d-ad31-4072-aab3-5017255d6cab.svg'
AUTHOR = 'gpt-6'

class LinuxMintLogoCircle(Solo48):
    icon_id = 'linux-mint-logo-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('linux-mint', 'linux', 'operating-system', 'lm', 'logo', 'brand', 'circle')

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
        ring('frame',24,24,20)

        self.add_polyline('l',(16,15),(16,31),(32,31))
        self.add_arc('m-left',(22,26),(28,26),radius_x=3)
        self.add_arc('m-right',(28,26),(34,26),radius_x=3)
        self.add_line('m-left-stem',(22,26),(22,31))
        self.add_line('m-middle',(28,26),(28,31))
        self.add_line('m-right-stem',(34,26),(34,31))
        for a,b in [('m-left','m-right'),('m-left','m-left-stem'),('m-left','m-middle'),('m-right','m-middle'),('m-right','m-right-stem')]:self.relate('connect',a,b)
