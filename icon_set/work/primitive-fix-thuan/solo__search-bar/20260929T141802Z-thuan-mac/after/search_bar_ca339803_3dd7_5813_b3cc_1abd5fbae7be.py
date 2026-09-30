"""The rejected search field is too tall and its magnifier handle is a bump. Widen the field and give its circular lens a distinct diagonal handle.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide search: circular lens with a diagonal handle meeting the rim at an exact point.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='ca339803-3dd7-5813-b3cc-1abd5fbae7be'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__search-bar/20260929T141802Z-thuan-mac/reference/search bar_ca339803-3dd7-5813-b3cc-1abd5fbae7be.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='search-bar'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('search', 'bar')
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

        box('field',4,8,44,40,12)
        path('lens',(23,22),[('A',(28,17),5,5,True),('A',(33,22),5,5,True),('A',(31,26),5,5,True),('A',(23,22),5,5,True)],True)
        line('handle',(31,26),(34,30));join('handle','lens')
