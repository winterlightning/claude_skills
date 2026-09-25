"""Left-facing duckling with circular head, short beak, curved belly, raised tail, and paired legs. Centerline bounds6,6 to42,42.
Construction reference: Lucide bird: coherent silhouette, short attached feet.
Omissions: Eye and wing absent in source; no extra details.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f96d275-e002-410c-8e4f-d4365a7661ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gosling_2f96d275-e002-410c-8e4f-d4365a7661ad.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-duckling-profile-batch-057'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('gosling',)
    def build(self):
        self.path('duck',(12,15),[('A',(30,15),9,9,True),('C',(26,24),(30,19),(28,22)),('C',(42,24),(34,26),(38,28)),('C',(29,36),(42,32),(37,36)),('L',(21,36)),('C',(17,24),(9,34),(11,28)),('L',(6,20)),('L',(12,15))],True)
        for x in (21,29):
            self.add_line('leg-'+str(x),(x,36),(x,42));self.relate('connect','leg-'+str(x),'duck')
        self.add_line('foot',(17,42),(21,42));self.relate('connect','foot','leg-21')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
