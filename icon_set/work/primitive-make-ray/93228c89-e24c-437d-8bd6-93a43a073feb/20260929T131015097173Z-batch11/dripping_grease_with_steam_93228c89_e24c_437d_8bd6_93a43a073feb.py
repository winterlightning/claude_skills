'The rejected steam has collapsed into dots and the grease drop is short and flat.\nSymbol plan: Draw a full teardrop below an open tray and three short S-shaped steam strokes.\nConstruction: Lucide flame informs the teardrop silhouette; repeated steam curves share one definition.\nOmissions: Open tray replaces the closed slot to provide space for a readable drop and steam.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '93228c89-e24c-437d-8bd6-93a43a073feb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dripping-grease-with-steam/20260929T125815Z-thuan-mac/reference/grease_93228c89-e24c-437d-8bd6-93a43a073feb.svg'
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
    icon_id = 'dripping-grease-with-steam'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('dripping', 'grease', 'with', 'steam')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        poly('tray',((8,4),(8,8),(40,8),(40,4)))
        path(m,'drop',(24,16),('C',(30,28),(28,22),(33,24)),('C',(18,28),(28,30),(20,30)),('C',(24,16),(15,24),(20,22)),closed=True)
        for n,x in enumerate((14,24,34)):
         path(m,'steam'+str(n),(x,39),('C',(x,44),(x-3,40),(x+3,43)))
