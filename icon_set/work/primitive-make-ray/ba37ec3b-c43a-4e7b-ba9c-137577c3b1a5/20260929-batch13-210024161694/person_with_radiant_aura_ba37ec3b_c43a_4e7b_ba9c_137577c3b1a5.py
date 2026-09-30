"""Small head and short flat rays understate the radiant bust. Enlarge circular head and spread diagonal rays around it.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular head with smooth shoulders; bust ink contact
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ba37ec3b-c43a-4e7b-ba9c-137577c3b1a5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-radiant-aura/20260929T135610Z-thuan-mac/reference/roleplay game aura_ba37ec3b-c43a-4e7b-ba9c-137577c3b1a5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-with-radiant-aura'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'with', 'radiant', 'aura')
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

        oval('head',24,24,8,8)
        path('body',(10,42),[('A',(24,36),14,6,True),('A',(38,42),14,6,True)])
        join('head','body')
        for j,(p,q) in enumerate([((24,6),(24,8)),((6,12),(9,14)),((42,12),(39,14)),((6,28),(9,27)),((42,28),(39,27))]):line(f'ray{j}',p,q)
