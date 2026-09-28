"""K plus R, the kiss-and-ride designation.
Plan: HRECT_M gives each glyph and the plus room across the canvas.
Reduction: No glyph omitted; R leg moved to the shared stem/bowl junction to open its lower gap.
Construction: Source lettering; no useful exact Lucide construction match.
Layout: K and R are deliberately different letterforms; plus strokes meet at an explicit central node."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b90f680f-f022-4110-b907-97ad0bbc7f46'
SOURCE_PATH = 'pictographic-primitives/transportation/kiss and ride_b90f680f-f022-4110-b907-97ad0bbc7f46.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'kiss-and-ride'
    keyshape = Keyshape.HRECT_M
    # Visible ink extremes: (2, 8, 46, 40).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('kiss', 'and', 'ride')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: monoline letterforms on shared cap and baseline; plus at midheight.
        self.add_polyline('k-stem',(4,10),(4,24),(4,38))
        self.add_polyline('k-arms',(16,10),(4,24),(16,38))
        self.relate('connect','k-stem','k-arms')
        self.add_polyline('plus-h',(20,24),(23,24),(26,24))
        self.add_polyline('plus-v',(23,18),(23,24),(23,30))
        self.relate('connect','plus-h','plus-v')
        self.add_polyline('r-stem',(34,38),(34,26),(34,10),(38,10))
        self.add_arc('r-bowl',(38,10),(38,26),radius_x=6,radius_y=8)
        self.add_line('r-bar',(38,26),(34,26))
        self.add_line('r-leg',(34,26),(44,38))
        self.relate('connect','r-stem','r-bowl')
        self.relate('connect','r-stem','r-bar')
        self.relate('connect','r-bowl','r-bar');self.relate('connect','r-leg','r-bar');self.relate('connect','r-leg','r-stem')
