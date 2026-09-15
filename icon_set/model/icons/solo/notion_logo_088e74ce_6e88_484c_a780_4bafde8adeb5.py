"""A square frame holds a serif capital N with a diagonal stroke and short horizontal serifs.

Symbol plan: Square frame with serif N, stems x18 and30; extremes (6,6)-(42,42).
Review notes: Retains the square, diagonal N and two identifying slab serifs. Reduces remaining serif detail to keep legal gaps. Earlier Lucide square informs the enclosure.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '088e74ce-6e88-484c-a780-4bafde8adeb5'
SOURCE_PATH = 'pictographic-primitives/logos/notion logo_088e74ce-6e88-484c-a780-4bafde8adeb5.svg'
AUTHOR = 'gpt-6'

class NotionLogo(Solo48):
    icon_id = 'notion-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('notion', 'notes', 'letter-n', 'logo', 'brand', 'productivity', 'workspace')

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
        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_polyline('n',(18,33),(18,15),(30,33),(30,15))
        self.add_polyline('serif-bottom',(15,33),(18,33),(21,33))
        self.add_polyline('serif-top',(27,15),(30,15),(33,15))
        for a in ['serif-bottom-1','serif-bottom-2']:self.relate('connect',a,'n-1')
        for a in ['serif-top-1','serif-top-2']:self.relate('connect',a,'n-3')
