"""The available reference is the rejected drawing itself. Its lower pin is narrow and the internal diagonal bend is cramped. Broaden the pin and separate the diagonal bands.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match for this striped pin emblem.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7e5f0d85-7150-5db7-aafa-d96e4d3d4cde'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__map-location-pin-marker-upload-5e650aa4122b9417/20260929T135604Z-thuan-mac/reference/map-location-pin-marker-upload-5e650aa4122b9417_7e5f0d85-7150-5db7-aafa-d96e4d3d4cde.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='map-location-pin-marker-upload-5e650aa4122b9417'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('map', 'location', 'pin', 'marker', 'upload', '5e650aa4122b9417')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('pin',(24,6),[('C',(36,10),(29,6),(33,7)),('C',(42,24),(40,13),(42,18)),('C',(34,35),(42,29),(38,32)),('C',(24,42),(30,39),(27,42)),('C',(17,38),(22,42),(19,40)),('C',(10,32),(14,36),(12,34)),('C',(6,24),(7,29),(6,27)),('C',(24,6),(6,14),(12,6))],True)
        poly('slash',(10,32),(23,21),(36,10));join('slash','pin')
        poly('bend',(23,21),(29,27),(17,38));join('bend','slash');join('bend','pin')
