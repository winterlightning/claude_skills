"""Open hooked canopy no longer reads as a tree. Restore a full leafy canopy and suspended seat.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: tree-deciduous: lobed canopy; source swing geometry
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tree-with-hanging-swing-solo-b016-r02/20260929T131521Z-thuan-mac/reference/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tree-with-hanging-swing-solo-b016-r02'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('tree', 'with', 'hanging', 'swing', 'solo', 'b016', 'r02')
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

        path('canopy',(14,27),[('C',(6,20),(8,27),(6,24)),('C',(12,12),(6,15),(8,12)),('C',(23,6),(12,7),(18,6)),('C',(34,12),(29,6),(34,8)),('C',(40,20),(38,12),(40,15)),('C',(33,27),(40,25),(37,27))])
        poly('trunk',(18,18),(18,30),(18,42))
        line('branch',(18,30),(33,27));join('branch','trunk');join('branch','canopy')
        poly('swing',(30,28),(30,42),(42,42),(42,28));join('swing','branch')
