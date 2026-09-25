'A thin upright mast ends in a small circular tip beneath three nested signal arcs. The arcs spread broadly above the mast, while their open ends remain separate on both sides.\nPlan: Nested circular broadcast arcs share center24,28; reduce three waves to two to retain hollow tip and mast. Extrema4,8,44,40.\nConstruction reference: Lucide wifi and radio-tower: concentric open signal arcs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac67e3fa-a33c-4cbd-95e0-a1c4af45f52d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/signal_ac67e3fa-a33c-4cbd-95e0-a1c4af45f52d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'radio-mast-beneath-three-signal-arcs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('radio', 'mast', 'beneath', 'three', 'signal', 'arcs')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        for n,r in enumerate((20,11)):path(f'wave-{n}',(24-r,28),[('A',(24,28-r),r,r,True),('A',(24+r,28),r,r,True)])
        circle('tip',24,30,3);line('mast',(24,33),(24,40));join('tip','mast')
