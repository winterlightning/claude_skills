"""A large circle holds a capital M beside a downward arrow.

Symbol plan: Standalone M and downward arrow; extremes (4,8)-(44,40).
Review notes: The generic surrounding circle is omitted to keep the identifying M and down arrow readable with legal spacing. No useful Lucide brand match; the arrow is symmetric and points down as in the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a9e9818-711c-4a19-bb61-67da1016ea24'
SOURCE_PATH = 'pictographic-primitives/logos/markdown logo_8a9e9818-711c-4a19-bb61-67da1016ea24.svg'
AUTHOR = 'gpt-6'

class MarkdownLogo(Solo48):
    icon_id = 'markdown-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('markdown', 'md', 'text', 'format', 'logo', 'brand', 'circle')

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
        self.add_polyline('m',(4,40),(4,8),(12,24),(20,8),(20,40))
        self.add_line('arrow-stem',(36,8),(36,40))
        self.add_polyline('arrow-head',(28,32),(36,40),(44,32))
        for member in ['arrow-head-1','arrow-head-2']:self.relate('connect','arrow-stem',member)
