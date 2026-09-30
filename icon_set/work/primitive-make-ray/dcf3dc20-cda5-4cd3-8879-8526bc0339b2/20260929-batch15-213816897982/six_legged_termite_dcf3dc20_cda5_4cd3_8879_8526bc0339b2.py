"""The rejected termite loses the thorax and gathers straight legs at one point. Restore three body regions and six legs attached at separate levels, with bent outer legs.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No additional Lucide match; source owns the three-part termite body.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='dcf3dc20-cda5-4cd3-8879-8526bc0339b2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__six-legged-termite/20260929T141901Z-thuan-mac/reference/termite_dcf3dc20-cda5-4cd3-8879-8526bc0339b2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='six-legged-termite'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('six', 'legged', 'termite')
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

        path('insect',(24,7),[('C',(30,12),(28,7),(30,8)),('C',(28,16),(30,14),(30,15)),('C',(32,20),(30,17),(32,18)),('L',(32,28)),('L',(32,36)),('A',(24,44),8,8,True),('A',(16,36),8,8,True),('L',(16,28)),('L',(16,20)),('C',(20,16),(16,18),(18,17)),('C',(18,12),(18,15),(18,14)),('C',(24,7),(18,8),(20,7))],True)
        line('neck',(20,16),(28,16));line('thorax',(16,28),(32,28));join('neck','insect');join('thorax','insect')
        poly('antennae',(18,4),(24,7),(30,4));join('antennae','insect')
        for side,x,end in [('l',16,8),('r',32,40)]:
         poly(side+'upper',(x,20),(end,20),(end,10));line(side+'middle',(x,28),(end,28));poly(side+'lower',(x,36),(end,40),(end,44))
         for n in ('upper','middle','lower'):join(side+n,'insect')
