"""The rejected shoe is a box with a wavy top and the rack has heavy rectangular divisions. Restore a recognizable shoe heel, raised tongue and sloping toe on the shelf.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match for this shoe-and-rack scene.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='28268293-e5fb-4119-b758-b0cd92d8e4dd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__shoe-resting-on-open-rack/20260929T141820Z-thuan-mac/reference/shoe rack_28268293-e5fb-4119-b758-b0cd92d8e4dd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='shoe-resting-on-open-rack'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('shoe', 'resting', 'on', 'open', 'rack')
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

        poly('rack',(6,42),(6,34),(6,14),(6,6),(42,6),(42,14),(42,34),(42,42))
        for y in (14,34,42):line('shelf'+str(y),(6,y),(42,y));join('shelf'+str(y),'rack')
        path('shoe',(14,34),[('L',(14,23)),('C',(23,23),(18,26),(19,26)),('C',(34,25),(27,23),(28,24)),('L',(34,34))]);join('shoe','shelf34')
