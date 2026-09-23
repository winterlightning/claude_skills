"""An empty manga action bubble has a scalloped burst outline and external emphasis rays.
Construction reference: none.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '090839a1-55f5-53c5-9d3e-f5849a8b9898'
SOURCE_PATH = 'icon_set/work/todo-references/kawaii manga screentone effect action text bubble_090839a1-55f5-53c5-9d3e-f5849a8b9898.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'kawaii-manga-screentone-effect-action-text-bubble'
    keyshape = Keyshape.SQUARE
    # Visible ink extremes: (4, 4, 44, 44).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('kawaii', 'manga', 'screentone', 'effect', 'action', 'text', 'bubble')

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

        # Plan: mirrored scalloped outline, four diagonal rays and two axial rays.
        # Concave curves retain the reference's scalloped action-bubble silhouette.
        self.add_bezier('burst',(16,12),((20,17),(28,17),(32,12)),
            ((33,18),(36,20),(40,18)),((37,22),(39,23),(42,24)),
            ((39,25),(37,28),(40,30)),((36,28),(33,30),(32,36)),
            ((28,31),(20,31),(16,36)),((15,30),(12,28),(8,30)),
            ((11,28),(9,25),(6,24)),((9,23),(11,22),(8,18)),
            ((12,20),(15,18),(16,12)))
        self.add_contour('bubble','burst',closed=True)
        self.add_line('ray-top',(24,6),(24,7))
        self.add_line('ray-bottom',(24,41),(24,42))
        for x,dx in [(8,1),(40,-1)]:
            self.add_line(f'ray-top-{x}',(x,6),(x+dx,7))
            self.add_line(f'ray-bottom-{x}',(x,42),(x+dx,41))
