"""Subtitle bubble with two text rows; four fragments merged into two legible lines; Lucide message-square-text informs corners and text; tail intentionally left."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19b43523-8c2d-4db2-b1a0-f99382395738'
SOURCE_PATH = 'pictographic-primitives/video/subtitles_19b43523-8c2d-4db2-b1a0-f99382395738.svg'
AUTHOR = 'gpt-6'

class SubtitleSpeechBubble(Solo48):
    icon_id = 'subtitle-speech-bubble'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('subtitle', 'speech', 'bubble', 'text', 'caption', 'dialogue', 'language')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded(self, name, x, y, w, h, r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; ident=name+'-'+str(i);ids.append(ident)
            if i%2:self.add_arc(ident,a,b,radius_x=r)
            else:self.add_line(ident,a,b)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Subtitle bubble with two text rows; four fragments merged into two legible lines; Lucide message-square-text informs corners and text; tail intentionally left.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,32))
        self.add_arc('br',(42,32),(38,36),radius_x=4)
        tail = [(38,36),(20,36),(10,42),(10,36)]
        for n,(a,b) in enumerate(zip(tail,tail[1:]),1):
            self.add_line(f'tail-{n}',a,b)
        self.add_arc('bl',(10,36),(6,32),radius_x=4)
        self.add_line('left',(6,32),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('bubble','top','tr','right','br','tail-1','tail-2','tail-3','bl','left','tl',closed=True)
        self.add_line('text-upper',(15,18),(33,18))
        self.add_line('text-lower',(15,26),(29,26))
