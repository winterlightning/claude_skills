"""A centered play triangle beside a regular three-row playlist.
Reference comparison: Current playlist triangle has a pointed bump at the upper-left corner and uneven bar spacing. Use a balanced play triangle and three aligned bars.
Construction reference: Lucide mountain: simple coherent triangular contour.
SOLO48 keyshape HRECT_M; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='aa83f82a-d435-56a8-a44a-f2497ad79910'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__play-last-playlist/20260928T172849Z-thuan-mac/reference/play last playlist_aa83f82a-d435-56a8-a44a-f2497ad79910.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='play-last-playlist'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('play', 'last', 'playlist')

    def build(self):

        # Typed path helpers own continuous contours, repeated radii and real junctions.
        def path(name,start,commands,closed=False):
            here=start;members=[]
            for i,c in enumerate(commands):
                kind,end,*args=c; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C':
                    c1,c2=args
                    self.add_bezier(ident,here,(c1,c2,end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        poly('play',(4,10),(20,24),(4,38),closed=True)
        for i,x1 in enumerate([44,40,44]):line('row-'+str(i),(29,14+10*i),(x1,14+10*i))
