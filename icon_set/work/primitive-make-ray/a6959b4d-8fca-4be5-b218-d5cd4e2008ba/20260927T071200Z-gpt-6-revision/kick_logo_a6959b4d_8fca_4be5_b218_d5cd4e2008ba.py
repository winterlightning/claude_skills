"""A blocky capital K built from stepped square segments, like a pixelated letter with notched diagonals.

Symbol plan: Stepped K silhouette with shared 9-unit pixel grid. Extremes (6,6)-(42,42).
Review notes: Retains the block outline and top/bottom steps; the central notch becomes a diagonal V so the result reads K, with nine-unit step spacing. No useful Lucide brand match; deliberate letter asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a6959b4d-8fca-4be5-b218-d5cd4e2008ba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kick-logo/20260927T070927Z-thuan-mac-1/reference/kick logo_a6959b4d-8fca-4be5-b218-d5cd4e2008ba.svg'
AUTHOR = "gpt-6"

class KickLogo(Solo48):
    icon_id = 'kick-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('kick', 'streaming', 'letter-k', 'logo', 'brand', 'gaming', 'pixel')

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
        xs={0:6,1:18,2:28,4:42}; ys={0:6,1:16,2:24,3:32,4:42}
        nodes=[(0,0),(1,0),(1,1),(2,1),(2,0),(4,0),(4,1),(2,2),(4,3),(4,4),(2,4),(2,3),(1,3),(1,4),(0,4)]
        self.add_polyline('pixel-k',*[(xs[a],ys[b]) for a,b in nodes],closed=True)
