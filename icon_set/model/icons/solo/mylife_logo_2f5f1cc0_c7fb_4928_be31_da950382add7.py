"""A small ring floats above a long gentle arc that rises from the lower left and levels off at the right, like a sun over a hill.

Symbol plan: Small ring above an asymmetric rising horizon; extremes (4,8)-(44,40).
Review notes: Keeps the ring and gentle rising arc. Circle construction informs the ring; the horizon deliberately rises from the lower left. This abstract sun/horizon reading has no human anatomy to reconstruct.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f5f1cc0-c7fb-4928-be31-da950382add7'
SOURCE_PATH = 'pictographic-primitives/logos/mylife logo_2f5f1cc0-c7fb-4928-be31-da950382add7.svg'
AUTHOR = 'gpt-6'

class MylifeLogo(Solo48):
    icon_id = 'mylife-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('mylife', 'person', 'horizon', 'logo', 'brand', 'people-search', 'arc')

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
        ring('ring',18,14,6)
        self.add_bezier('horizon',(4,40),((14,30),(30,26),(44,30)))
