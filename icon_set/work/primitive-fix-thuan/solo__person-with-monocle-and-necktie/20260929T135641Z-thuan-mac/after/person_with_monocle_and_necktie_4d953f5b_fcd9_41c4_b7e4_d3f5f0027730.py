"""The rejected portrait has a short bar for a necktie and reads as a circular symbol. Preserve its single eyeglass and add a pointed outlined necktie beneath a circular face.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular face and broad rounded shoulders; touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4d953f5b-fcd9-41c4-b7e4-d3f5f0027730'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-monocle-and-necktie/20260929T135641Z-thuan-mac/reference/snob_4d953f5b-fcd9-41c4-b7e4-d3f5f0027730.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-with-monocle-and-necktie'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'with', 'monocle', 'and', 'necktie')
    human_construction = "bust"
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

        oval('face',24,17,13,13)
        path('shoulders',(8,44),[('A',(24,34),16,10,True),('A',(40,44),16,10,True)]);join('face','shoulders')
        oval('monocle',25,17,3,3);line('temple',(28,17),(37,17));join('temple','face');join('temple','monocle')
        poly('tie',(24,34),(16,39),(24,44),(32,39),(24,34));join('tie','shoulders')
