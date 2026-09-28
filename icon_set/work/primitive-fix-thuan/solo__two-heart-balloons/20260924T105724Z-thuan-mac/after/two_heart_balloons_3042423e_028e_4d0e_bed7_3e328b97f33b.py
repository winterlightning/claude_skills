"""Smoothed the heart shoulder curves into their lobe extrema and replaced the rear string arc with a gentle flowing curve. Preserved larger rear/smaller front overlap and both strings. Lucide heart informed the lobes; knots omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3042423e-028e-4d0e-bed7-3e328b97f33b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-heart-balloons/20260924T105724Z-thuan-mac/reference/love heart balloons_3042423e-028e-4d0e-bed7-3e328b97f33b.svg'
AUTHOR = 'gpt-6'


class TwoHeartBalloons(Solo48):
    icon_id = 'two-heart-balloons'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('heart', 'balloons', 'pair', 'party', 'romance', 'celebration')

    def build(self) -> None:
        def heart(n,cx,y,r,tip):
            self.add_arc(n+'-l',(cx,y),(cx-2*r,y),radius_x=r,sweep=False)
            self.add_arc(n+'-shl',(cx-2*r,y),(cx-2*r+2,y+4),radius_x=5,sweep=False)
            self.add_line(n+'-sl',(cx-2*r+2,y+4),(cx,tip))
            self.add_line(n+'-sr',(cx,tip),(cx+2*r-2,y+4))
            self.add_arc(n+'-shr',(cx+2*r-2,y+4),(cx+2*r,y),radius_x=5,sweep=False)
            self.add_arc(n+'-r',(cx+2*r,y),(cx,y),radius_x=r,sweep=False)
            self.add_contour(n,n+'-l',n+'-shl',n+'-sl',n+'-sr',n+'-shr',n+'-r',closed=True)

        self.add_arc('large-lobe-l',(20,10),(8,10),radius_x=6,sweep=False)
        self.add_bezier('large-shoulder-l',(8,10),((8,12),(9,13),(10,14)))
        self.add_line('large-side-l',(10,14),(20,27))
        self.add_line('large-bottom',(20,27),(24,26))
        self.add_arc('large-lobe-r',(32,10),(20,10),radius_x=6,sweep=False)
        self.add_bezier('large-shoulder-r',(30,14),((31,13),(32,12),(32,10)))
        self.add_line('large-side-r',(28,22),(30,14))
        self.add_contour('rear-left','large-lobe-l','large-shoulder-l','large-side-l','large-bottom')
        self.add_contour('rear-right','large-side-r','large-shoulder-r','large-lobe-r')
        self.relate('connect','rear-left','rear-right')
        self.add_arc('small-l1',(32,26),(28,22),radius_x=4,sweep=False)
        self.add_arc('small-l2',(28,22),(24,26),radius_x=4,sweep=False)
        self.add_bezier('small-shl',(24,26),((24,28),(25,29),(26,30)))
        self.add_line('small-sl',(26,30),(32,38))
        self.add_line('small-sr',(32,38),(38,30))
        self.add_bezier('small-shr',(38,30),((39,29),(40,28),(40,26)))
        self.add_arc('small-r',(40,26),(32,26),radius_x=4,sweep=False)
        self.add_contour('small','small-l1','small-l2','small-shl','small-sl','small-sr','small-shr','small-r',closed=True)
        self.relate('connect','rear-left','small')
        self.relate('connect','rear-right','small')
        self.add_bezier('string-l',(20,27),((20,35),(18,41),(14,44)))
        self.add_arc('string-r',(32,38),(30,44),radius_x=10)
        self.relate('connect','rear-left','string-l')
        self.relate('connect','small','string-r')
