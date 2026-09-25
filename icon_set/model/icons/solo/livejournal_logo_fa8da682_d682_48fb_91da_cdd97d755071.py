"""A pencil lies on a diagonal pointing to the lower right, its body overlapping and extending past the upper left edge of a circle.

Symbol plan: One diagonal pencil intersects an open background circle at two shared integer nodes. Extremes (6,6)-(42,42).
Review notes: Lucide pencil informs the diagonal barrel and nib. The reference circle is rebuilt with center (29,29), radius13 and exact junctions. A small nib divider is omitted; pencil direction remains lower-right.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa8da682-d682-48fb-91da-cdd97d755071'
SOURCE_PATH = 'pictographic-primitives/logos/livejournal logo_fa8da682-d682-48fb-91da-cdd97d755071.svg'
AUTHOR = 'gpt-6'

class LivejournalLogo(Solo48):
    icon_id = 'livejournal-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('livejournal', 'blog', 'pencil', 'journal', 'logo', 'brand', 'writing')

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
        points=[(6,13),(13,6),(24,17),(26,19),(32,32),(19,26),(17,24)]
        self.add_polyline('pencil',*points,closed=True)
        self.add_arc('journal',(24,17),(17,24),radius_x=13,large_arc=True)
        for member in ['pencil-2','pencil-3','pencil-6','pencil-7']:
            self.relate('connect','journal',member)
