"""The rejected portrait loses the long hair and garment and leaves disconnected side strokes. Restore a full circular jaw, long hair and rounded shoulders under the halo.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and smooth shoulders with touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='51d30682-39f9-5a08-95aa-4743470a5b0c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__woman-with-halo/20260929T145934Z-thuan-mac/reference/female_51d30682-39f9-5a08-95aa-4743470a5b0c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='woman-with-halo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('woman', 'with', 'halo')
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

        oval('halo',24,8,16,4)
        path('jaw',(31,22),[('A',(17,22),7,7,True)])
        path('fringe',(17,22),[('C',(24,20),(20,23),(22,22)),('C',(31,22),(26,22),(28,23))]);join('jaw','fringe')
        path('body',(8,44),[('A',(24,33),16,11,True),('A',(40,44),16,11,True)]);join('body','jaw')
        for n,x in [('left',8),('right',40)]:
         path(n+'hair',(x,21),[('L',(x,32)),('L',(x,44))]);join(n+'hair','body')
