"""A large circle holds the lowercase letters ln in a light rounded typeface.

Symbol plan: Outer circle radius20; lowercase l and n with shared shoulder nodes. Radial extreme20.
Review notes: Retains circle and ln initials, using single letter strokes and a circular n shoulder. Lucide circle informs the enclosure. The asymmetric letter heights preserve the wordmark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a782c8ea-2e59-41b0-8aaf-60380cca7d8a'
SOURCE_PATH = 'pictographic-primitives/logos/logmein logo_a782c8ea-2e59-41b0-8aaf-60380cca7d8a.svg'
AUTHOR = 'gpt-6'

class LogmeinLogo(Solo48):
    icon_id = 'logmein-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('logmein', 'remote-access', 'ln', 'logo', 'brand', 'support', 'circle')

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
        self.add_line('l',(16,16),(16,30))
        j=(24,24)
        self.add_line('n-top',(24,20),j)
        self.add_line('n-left',j,(24,30))
        self.add_arc('n-arch',j,(32,24),radius_x=4)
        self.add_line('n-right',(32,24),(32,30))
        self.add_contour('n-shoulder','n-arch','n-right')
        for a,b in [('n-top','n-left'),('n-top','n-arch'),('n-left','n-arch')]:self.relate('connect',a,b)
