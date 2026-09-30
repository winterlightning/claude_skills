'The rejected sun has become an internal crescent in the cloud and the weather symbol reads as one lumpy mass.\nSymbol plan: Separate the exposed upper-left sun from a broad lower cloud and preserve a ray outside both.\nConstruction: Lucide cloud-sun informs overlapping outlines with real contacts; intentionally asymmetric sun placement.\nOmissions: One long ray replaces the crowded small rays.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6f54dfef-a732-45c0-83af-be8ae5456b79'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__partly-cloudy/20260929T125815Z-thuan-mac/reference/weather snow_6f54dfef-a732-45c0-83af-be8ae5456b79.svg'
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
    icon_id = 'partly-cloudy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('partly', 'cloudy')
    def build(self):
        m=self
        line=self.add_line
        poly=lambda n,pts:self.add_polyline(n,*pts)
        join=lambda a,b:self.relate('connect',a,b)
        path(m,'cloud',(14,26),('C',(26,16),(14,17),(20,13)),('C',(38,26),(32,13),(38,18)),('C',(44,32),(42,26),(44,29)),('C',(36,40),(44,37),(41,40)),('L',(14,40)),('C',(4,33),(8,40),(4,37)),('C',(14,26),(4,29),(8,26)),closed=True)
        path(m,'sun',(14,26),('C',(14,12),(7,24),(7,15)),('C',(26,16),(21,8),(26,11)))
        join('sun','cloud')
        line('ray',(4,8),(5,8))
