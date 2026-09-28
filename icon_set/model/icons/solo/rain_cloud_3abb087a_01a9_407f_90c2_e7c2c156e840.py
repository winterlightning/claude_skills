"""Restored a tall circular cloud crown and two smaller lobes above parallel diagonal rain strokes; omitted the tiny extra source lobe.
Construction: Lucide cloud-rain: circular crown and smaller side lobes. Closed three-lobed cloud above two parallel diagonal rain strokes; omit tiny extra right lobe.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3abb087a-01a9-407f-90c2-e7c2c156e840'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud rain_3abb087a-01a9-407f-90c2-e7c2c156e840.svg'
AUTHOR = "gpt-6"

def path(s,n,start,*steps,closed=False):
    ids=[]; here=start
    for i,c in enumerate(steps):
        k,end,*args=c; ident=f'{n}-{i}'
        if k=='L': s.add_line(ident,here,end)
        else: s.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        ids.append(ident);here=end
    s.add_contour(n,*ids,closed=closed)

def circle(s,n,x,y,r):
    path(s,n,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

def box(s,n,l,t,r,b,k=3):
    path(s,n,(l+k,t),('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True),closed=True)

class Drawing(Solo48):
    icon_id = 'rain-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('weather', 'cloud', 'rain')
    def build(self):
        s = self
        path(s,'cloud',(14,16),('A',(34,16),10,10,True),('L',(36,16)),('A',(36,28),6,6,True),('L',(14,28)),('A',(14,16),8,6,True),closed=True)
        for j,x in enumerate((18,32)): s.add_line('rain-'+str(j),(x,37),(x-5,42))
