"""Centered triangle and outlined bar; Lucide eject construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '694dcc2b-70cd-59a2-be97-3040ff8cca91'
SOURCE_PATH = 'pictographic-primitives/video/controls eject_694dcc2b-70cd-59a2-be97-3040ff8cca91.svg'
AUTHOR = 'gpt-6'

class Eject(Solo48):
    icon_id = 'eject'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('eject', 'media', 'control', 'triangle', 'playback', 'button', 'disc')

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
        # Centered triangle and outlined bar; Lucide eject construction.
        self.add_polyline('triangle',(6,26),(24,6),(42,26),closed=True)
        self.add_polyline('bar',(6,34),(42,34),(42,42),(6,42),closed=True)
