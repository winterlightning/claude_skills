"""A rounded speech-bubble shape with a curled tail at the lower left holds a lowercase m.

Symbol plan: Rounded speech bubble with lower-left tail and an m made from two identical arches. Extremes (6,6)-(42,42).
Review notes: Lucide message-circle and square inform one rounded bubble contour. The secondary curled underline reduces to a single lower-left tail; the lowercase m remains intact and symmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7c5c800-14c9-48d1-b6c4-21733a813736'
SOURCE_PATH = 'pictographic-primitives/logos/mastodon logo 2_e7c5c800-14c9-48d1-b6c4-21733a813736.svg'
AUTHOR = 'gpt-6'

class MastodonLogo(Solo48):
    icon_id = 'mastodon-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('mastodon', 'social', 'fediverse', 'letter-m', 'logo', 'brand', 'decentralized')

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
        self.add_line('top',(18,6),(30,6))
        self.add_arc('top-right',(30,6),(42,18),radius_x=12)
        self.add_line('right',(42,18),(42,22))
        self.add_arc('lower-right',(42,22),(30,34),radius_x=12)
        chain('tail',(30,34),(16,34),(16,42),(6,34),(6,18))
        self.add_arc('top-left',(6,18),(18,6),radius_x=12)
        self.add_contour('bubble','top','top-right','right','lower-right',*[f'tail-{i}' for i in range(1,5)],'top-left',closed=True)
        for i,x in enumerate((16,24,32)):
            self.add_line(f'm-stem-{i}',(x,19),(x,25))
        for i,x in enumerate((16,24)):
            self.add_arc(f'm-arch-{i}',(x,19),(x+8,19),radius_x=4)
            self.relate('connect',f'm-arch-{i}',f'm-stem-{i}')
            self.relate('connect',f'm-arch-{i}',f'm-stem-{i+1}')
        self.relate('connect','m-arch-0','m-arch-1')
