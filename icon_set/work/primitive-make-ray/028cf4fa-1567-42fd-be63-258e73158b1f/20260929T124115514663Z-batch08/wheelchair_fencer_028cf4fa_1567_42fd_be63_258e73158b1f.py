'The rejected fencer has a flattened wheel and a short upward stub for the blade.\nSymbol plan: Restore a round rear wheel arc and a longer fencing blade with a compact upright guard.\nConstruction: human_ref/full_body_ref.png: head bottom14 to torso22 gives exact4-unit ink gap. Lucide accessibility and sword original/atomic-debug: open round wheel and visible blade.\nOmissions: Lower sword guard and wheel spokes omitted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '028cf4fa-1567-42fd-be63-258e73158b1f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wheelchair-fencer/20260929T122733Z-thuan-mac/reference/fencing 1_028cf4fa-1567-42fd-be63-258e73158b1f.svg'
AUTHOR = 'gpt-6'

def path(m,n,start,*steps,closed=False):
    names=[]; here=start
    for j,(kind,end,*args) in enumerate(steps):
        k=f'{n}-{j}'
        if kind=='L':m.add_line(k,here,end)
        elif kind=='C':m.add_bezier(k,here,(args[0],args[1],end))
        elif kind=='A':m.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        names.append(k);here=end
    m.add_contour(n,*names,closed=closed)
def circle(m,n,x,y,r):
    path(m,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)
def oval(m,n,x,y,rx,ry):
    path(m,n,(x-rx,y),('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),closed=True)
def box(m,n,l,t,r,b,rad):
    path(m,n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)

class Drawing(Solo48):
    icon_id = 'wheelchair-fencer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wheelchair', 'fencer')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        circle(m,'head',16,10,4);line('torso',(16,22),(16,30));m.mark_human_figure('fencer',head='head',torso='torso',torso_junction='start')
        poly('leg',(16,30),(28,30),(32,42));join('torso','leg')
        line('arm',(16,22),(28,22));line('guard',(28,18),(28,22));line('sword',(28,22),(42,14));join('arm','torso');join('arm','guard');join('arm','sword');join('guard','sword')
        path(m,'wheel',(16,22),('A',(6,32),10,10,False),('A',(16,42),10,10,False),('A',(22,40),10,10,False));join('wheel','torso');join('wheel','arm')
