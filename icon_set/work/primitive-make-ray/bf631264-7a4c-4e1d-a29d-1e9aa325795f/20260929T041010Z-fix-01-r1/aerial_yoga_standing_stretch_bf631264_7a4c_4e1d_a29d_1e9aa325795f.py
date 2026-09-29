"""Rejected diagonal stick and pole omit the lifted arms and fabric. Restore a standing lunge with raised arms and two hanging fabric edges."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='bf631264-7a4c-4e1d-a29d-1e9aa325795f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__aerial-yoga-standing-stretch/20260929T041010Z-thuan-mac/reference/aerial yoga basic pose_bf631264-7a4c-4e1d-a29d-1e9aa325795f.svg'
AUTHOR='gpt-6'
PLAN='Rejected diagonal stick and pole omit the lifted arms and fabric. Restore a standing lunge with raised arms and two hanging fabric edges.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='aerial-yoga-standing-stretch'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('head',22,14,4)
        self.add_bezier('torso',(22,26),((22,29),(21,31),(18,34)))
        self.add_polyline('left-leg',(18,34),(8,42),(6,42))
        self.add_polyline('right-leg',(18,34),(27,36),(27,42))
        self.add_polyline('arms',(22,26),(34,22),(34,6))
        self.add_line('fabric',(42,6),(42,28))
        self.relate('connect','torso','left-leg','right-leg','arms')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
