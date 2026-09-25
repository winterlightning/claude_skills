"""A rounded square frame holds a thick outlined capital N.

Symbol plan: Rounded square with a single-stroke N; extremes (6,6)-(42,42).
Review notes: Lucide square informs equal rounded corners. Reduces the outlined N to one coherent stroke so the diagonal and both uprights remain distinct inside the frame.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a81d0943-fd61-496a-836e-23179f5c721e'
SOURCE_PATH = 'pictographic-primitives/logos/nativescript logo_a81d0943-fd61-496a-836e-23179f5c721e.svg'
AUTHOR = 'gpt-6'

class NativescriptLogo(Solo48):
    icon_id = 'nativescript-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('nativescript', 'mobile', 'framework', 'letter-n', 'logo', 'brand', 'developer')

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
        self.add_polyline('n',(15,33),(15,15),(33,33),(33,15))
