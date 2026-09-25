"""An upright document with a folded top right corner holds a capital M beside a downward arrow.

Symbol plan: Cut-corner document with M above a downward arrow. Extremes (8,4)-(40,44).
Review notes: Rebalanced the M and down arrow into two rows to preserve all identifying content. The redundant inner fold divider is omitted while the cut corner remains. The side-by-side attempt could not fit; this stacked file-type treatment uses the full document interior.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cf67d68-8635-4534-9a24-0a77d9ba0b11'
SOURCE_PATH = 'pictographic-primitives/logos/markdown logo 1_6cf67d68-8635-4534-9a24-0a77d9ba0b11.svg'
AUTHOR = 'gpt-6'

class MarkdownDocumentLogo(Solo48):
    icon_id = 'markdown-document-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('markdown', 'document', 'md', 'text', 'logo', 'brand', 'format')

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
        self.add_polyline('page',(8,4),(32,4),(40,12),(40,44),(8,44),closed=True)
        self.add_polyline('m',(18,22),(18,14),(24,20),(30,14),(30,22))
        self.add_line('arrow-stem',(24,28),(24,36))
        self.add_polyline('arrow-head',(20,32),(24,36),(28,32))
        for member in ['arrow-head-1','arrow-head-2']:self.relate('connect','arrow-stem',member)
