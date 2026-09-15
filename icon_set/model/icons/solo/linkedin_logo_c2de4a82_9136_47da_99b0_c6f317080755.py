"""The letters in drawn as thick outlines: a dotted i with a round dot at the upper left beside a rounded n.

Symbol plan: Left i ring and stem; right n arch and shared stem junction. Extremes (6,6)-(42,42).
Review notes: Outlined thick letter stems reduce to single strokes. The i dot stays circular and the n remains a tangent arch. Lucide circle supplies ring construction; no local LinkedIn original exists.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2de4a82-9136-47da-99b0-c6f317080755'
SOURCE_PATH = 'pictographic-primitives/logos/linkedin logo_c2de4a82-9136-47da-99b0-c6f317080755.svg'
AUTHOR = 'gpt-6'

class LinkedinLogo(Solo48):
    icon_id = 'linkedin-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('linkedin', 'social', 'professional', 'in', 'logo', 'brand', 'network')

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
        ring('i-dot',9,9,3)
        self.add_line('i-stem',(6,22),(6,42))
        junction=(22,28)
        self.add_line('n-top',(22,20),junction)
        self.add_line('n-stem',junction,(22,42))
        self.add_arc('n-arch',junction,(42,28),radius_x=10)
        self.add_line('n-right',(42,28),(42,42))
        self.add_contour('n-shoulder','n-arch','n-right')
        for a,b in [('n-top','n-stem'),('n-top','n-arch'),('n-stem','n-arch')]:self.relate('connect',a,b)
