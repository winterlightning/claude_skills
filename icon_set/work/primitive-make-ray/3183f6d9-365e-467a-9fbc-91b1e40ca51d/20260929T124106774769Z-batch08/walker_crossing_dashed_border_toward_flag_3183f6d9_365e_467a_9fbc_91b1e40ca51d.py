'The rejected border walker has a stiff symmetrical stride and a vertical upper boundary dash.\nSymbol plan: Bend the forward knee, reach the front arm and align both boundary marks diagonally.\nConstruction: human_ref/full_body_ref.png: circular head and coherent limbs, head bottom16 to torso24 =8 centerline units. Lucide flag: joined pole and flag.\nOmissions: Outline body reduced to strokes; two border dashes retained.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3183f6d9-365e-467a-9fbc-91b1e40ca51d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walker-crossing-dashed-border-toward-flag/20260929T122733Z-thuan-mac/reference/cross the border_3183f6d9-365e-467a-9fbc-91b1e40ca51d.svg'
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
    icon_id = 'walker-crossing-dashed-border-toward-flag'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('walker', 'crossing', 'dashed', 'border', 'toward', 'flag')
    def build(self):
        m=self
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        circle(m,'head',18,12,4)
        line('torso',(18,24),(18,32))
        poly('arms',(6,28),(10,24),(18,24),(24,26))
        poly('legs',(8,40),(18,32),(26,36),(28,40))
        poly('flag',(32,28),(32,8),(44,14),(32,20))
        line('boundary-a',(4,8),(6,10));line('boundary-b',(38,36),(44,40))
        join('torso','arms');join('torso','legs')
        m.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
