"""The rejected stacks have squashed black top rims and a crowded tall cylinder. Use wider coins, clear elliptical tops and fewer evenly spaced layers.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide coins: clear circular/elliptic outlines; original supplies stacked cylinders.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4b825437-3303-4449-b127-dc34838cb089'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-coin-stacks/20260929T145934Z-thuan-mac/reference/accounting coins stack 1_4b825437-3303-4449-b127-dc34838cb089.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-coin-stacks'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'coin', 'stacks')
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

        for n,l,r,t,b in [('tall',4,20,12,36),('short',28,44,24,36)]:
         cx=(l+r)//2;oval(n+'top',cx,t,8,4)
         path(n+'body',(l,t),[('L',(l,b)),('A',(r,b),8,4,False),('L',(r,t))]);join(n+'top',n+'body')
         if n=='tall':path('layer',(l,24),[('A',(r,24),8,4,False)]);join('layer',n+'body')
