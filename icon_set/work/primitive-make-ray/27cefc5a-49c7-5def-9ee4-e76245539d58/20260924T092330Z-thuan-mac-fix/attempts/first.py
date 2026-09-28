"""Human user.svg and Lucide glasses: circular jaw, touching shoulder ink, equal lenses and side-parted outer hair. Hair and eyewear retained; no detached human gap applies to connected portrait.
Fresh bad-stroke revision; fixed SOLO48 stroke4, integer grid. Keyshape VRECT_L."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '27cefc5a-49c7-5def-9ee4-e76245539d58'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-side-parted-hair-and-glasses/20260924T092330Z-thuan-mac/reference/woman glasses_27cefc5a-49c7-5def-9ee4-e76245539d58.svg'
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
    icon_id = 'person-with-side-parted-hair-and-glasses'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('woman', 'glasses')
    def build(self):
        s = self
        path(s,'hair',(8,34),('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,34)))
        path(s,'fringe',(12,20),('A',(28,12),16,8,False),('L',(36,20)))
        s.add_arc('jaw',(36,20),(12,20),radius_x=12);s.relate('connect','jaw','fringe')
        for x in (17,31): circle(s,'lens-'+str(x),x,22,3)
        s.add_line('bridge',(20,22),(28,22));s.relate('connect','bridge','lens-17');s.relate('connect','bridge','lens-31')
        path(s,'shoulders',(8,44),('A',(16,36),8,8,True),('L',(32,36)),('A',(40,44),8,8,True))
        s.relate('connect','jaw','shoulders')
