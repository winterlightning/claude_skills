from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='ff7e8050-8817-4660-b5a8-3ebce79568b0'
SOURCE_PATH='pictographic-primitives/state/slash sperm_ff7e8050-8817-4660-b5a8-3ebce79568b0.svg'
AUTHOR='gpt-6'
PLAN='Circular prohibition rim with separated slash ends surrounds a circular sperm head and attached curved tail.'
CONSTRUCTION_REFERENCES='No useful Lucide organic-cell match; supplied reference governs the sperm and interrupted slash.'
OMISSIONS=['Irregular egg-shaped head simplified to a circular head.']
class Drawing(Solo48):
    icon_id='slash-sperm'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'state'
    categories = ('state',)
    aliases=()
    keywords=('slash', 'sperm')

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        self.path('ring',(12,40),[('A',(36,8),20,20,True),('A',(12,40),20,20,True)],True)
        self.add_line('slash-low',(12,40),(16,36));self.relate('connect','ring','slash-low')
        self.add_line('slash-high',(31,13),(36,8));self.relate('connect','ring','slash-high')
        self.path('cell',(22,24),[('A',(16,16),5,5,True),('A',(22,24),5,5,True)],True)
        self.path('tail',(22,24),[('C',(27,31),(28,26),(31,28)),('C',(29,34),(23,34),(25,34))])
        self.relate('connect','cell','tail')
