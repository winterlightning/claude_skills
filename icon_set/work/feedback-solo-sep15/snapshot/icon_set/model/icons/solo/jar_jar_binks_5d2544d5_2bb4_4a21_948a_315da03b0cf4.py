"""Gungan head with tall eyes, broad muzzle and long side ears; no useful Lucide character match; ear stripes, pupils and lower mouth mark omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d2544d5-2bb4-4a21-948a-315da03b0cf4'
SOURCE_PATH = 'pictographic-primitives/video/jar jar binks gungan_5d2544d5-2bb4-4a21-948a-315da03b0cf4.svg'
AUTHOR = 'gpt-6'

class JarJarBinks(Solo48):
    icon_id = 'jar-jar-binks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('jar jar binks', 'gungan', 'character', 'face', 'alien', 'ears', 'star wars')

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
        # Gungan head with tall eyes, broad muzzle and long side ears; no useful Lucide character match; ear stripes, pupils and lower mouth mark omitted.
        self.add_arc('eye-left',(12,16),(22,16),radius_x=5,radius_y=10)
        self.add_arc('brow',(22,16),(26,16),radius_x=3,sweep=True)
        self.add_arc('eye-right',(26,16),(36,16),radius_x=5,radius_y=10)
        self.add_arc('cheek-right',(36,16),(32,38),radius_x=22)
        self.add_arc('chin',(32,38),(16,38),radius_x=10)
        self.add_arc('cheek-left',(16,38),(12,16),radius_x=22)
        self.add_contour('face','eye-left','brow','eye-right','cheek-right','chin','cheek-left',closed=True)
        self.add_polyline('left-ear',(12,16),(6,42),(14,42))
        self.add_polyline('right-ear',(36,16),(42,42),(34,42))
        self.relate('connect','left-ear','eye-left');self.relate('connect','left-ear','cheek-left')
        self.relate('connect','right-ear','eye-right');self.relate('connect','right-ear','cheek-right')
        self.add_arc('smile',(21,28),(27,28),radius_x=4,sweep=False)
