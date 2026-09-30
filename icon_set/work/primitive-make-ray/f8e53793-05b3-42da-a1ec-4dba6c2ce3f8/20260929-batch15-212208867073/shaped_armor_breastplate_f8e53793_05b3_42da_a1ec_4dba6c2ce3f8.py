"""The rejected breastplate has a W-shaped chest mark and an angular straight hem. Restore paired breast curves, a scooped neckline and a curved lower armor band.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match; source owns the shaped armor silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f8e53793-05b3-42da-a1ec-4dba6c2ce3f8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__shaped-armor-breastplate/20260929T141812Z-thuan-mac/reference/breastplate_f8e53793-05b3-42da-a1ec-4dba6c2ce3f8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='shaped-armor-breastplate'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('shaped', 'armor', 'breastplate')
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

        path('armor',(8,6),[('L',(16,4)),('A',(32,4),8,8,False),('L',(40,6)),('C',(40,20),(38,12),(38,16)),('L',(36,34)),('L',(40,40)),('A',(8,40),16,4,True),('L',(12,34)),('L',(8,20)),('C',(8,6),(10,16),(10,12))],True)
        path('breast',(17,22),[('C',(24,22),(17,28),(24,28)),('C',(31,22),(24,28),(31,28))])
        path('hem',(12,34),[('C',(36,34),(20,36),(28,36))]);join('hem','armor')
