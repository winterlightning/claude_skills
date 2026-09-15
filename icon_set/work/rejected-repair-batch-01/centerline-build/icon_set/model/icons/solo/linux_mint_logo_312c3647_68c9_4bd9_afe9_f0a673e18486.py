"""A rounded leaf-like square with a notch at its upper left holds the letters lm, the l rising from the notch into a lowercase m.

Symbol plan: Leaf-shaped enclosure with upper-left notch and lm monogram. Extremes (6,6)-(42,42).
Review notes: Retains the notched leaf frame and lm lettering, with paired circular m arches. Lucide square informs tangent corner construction. This dense nested candidate may need manual review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '312c3647-68c9-4bd9-afe9-f0a673e18486'
SOURCE_PATH = 'pictographic-primitives/logos/linux mint logo_312c3647-68c9-4bd9-afe9-f0a673e18486.svg'
AUTHOR = 'gpt-6'

class LinuxMintLogo(Solo48):
    icon_id = 'linux-mint-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('linux-mint', 'linux', 'operating-system', 'lm', 'logo', 'brand', 'open-source')

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
        chain('frame-start',(6,6),(24,6))
        self.add_arc('frame-round',(24,6),(42,24),radius_x=18)
        chain('frame-end',(42,24),(42,42),(24,42))
        self.add_arc('frame-base',(24,42),(12,30),radius_x=12)
        chain('frame-notch',(12,30),(12,14),(6,14),(6,6))
        self.add_contour('frame','frame-start-1','frame-round','frame-end-1','frame-end-2','frame-base','frame-notch-1','frame-notch-2','frame-notch-3',closed=True)

        self.add_polyline('l',(16,15),(16,31),(32,31))
        self.add_arc('m-left',(22,26),(28,26),radius_x=3)
        self.add_arc('m-right',(28,26),(34,26),radius_x=3)
        self.add_line('m-left-stem',(22,26),(22,31))
        self.add_line('m-middle',(28,26),(28,31))
        self.add_line('m-right-stem',(34,26),(34,31))
        for a,b in [('m-left','m-right'),('m-left','m-left-stem'),('m-left','m-middle'),('m-right','m-middle'),('m-right','m-right-stem')]:self.relate('connect',a,b)
