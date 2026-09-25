"""A rounded square with a capital W overlaps the left side of a larger document holding three horizontal text lines.

Symbol plan: Wide W beside three text lines within the radius20 envelope.
Review notes: Omits the tile and document frames to widen the W and retain all three text lines with legal spacing. The radial envelope accommodates the wide letter and text group.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5b0095a-2b79-4f95-90f3-66a1c887ac95'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft word logo_c5b0095a-2b79-4f95-90f3-66a1c887ac95.svg'
AUTHOR = 'gpt-6'

class MicrosoftWordLogo(Solo48):
    icon_id = 'microsoft-word-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('microsoft-word', 'word', 'microsoft', 'document', 'office', 'logo', 'brand')

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
        self.add_polyline('w',(6,16),(12,32),(18,22),(24,32),(30,16))
        for i,y in enumerate((16,24,32)):self.add_line(f'text-{i}',(38,y),(44 if y==24 else 42,y))
