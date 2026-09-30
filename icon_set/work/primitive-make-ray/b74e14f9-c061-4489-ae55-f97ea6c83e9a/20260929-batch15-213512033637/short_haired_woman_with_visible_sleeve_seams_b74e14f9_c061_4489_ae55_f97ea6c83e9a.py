"""The rejected portrait omits the named sleeve seams and reduces the bob to a hair arch. Extend the bob, retain the swept fringe and restore two visible sleeve seams on a closed blouse.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and rounded shoulders with touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b74e14f9-c061-4489-ae55-f97ea6c83e9a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__short-haired-woman-with-visible-sleeve-seams/20260929T141825Z-thuan-mac/reference/step mother_b74e14f9-c061-4489-ae55-f97ea6c83e9a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='short-haired-woman-with-visible-sleeve-seams'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('short', 'haired', 'woman', 'with', 'visible', 'sleeve', 'seams')
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

        path('face',(17,15),[('A',(31,15),7,7,False),('C',(26,13),(29,15),(28,14)),('C',(17,15),(24,15),(20,15))],True)
        path('hair',(8,24),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,24))])
        path('body',(8,44),[('L',(8,34)),('A',(24,26),16,8,True),('A',(40,34),16,8,True),('L',(40,44)),('L',(32,44)),('L',(16,44)),('L',(8,44))],True);join('face','body')
        for x in (16,32):line('sleeve'+str(x),(x,36),(x,44));join('sleeve'+str(x),'body')
