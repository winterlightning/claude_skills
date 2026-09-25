"""A side-profile face beside an upright phone, with smooth forehead, nose and rounded mouth hollow; straight left cut indicates a cropped head.
Construction: Lucide smartphone: rounded housing; human user.svg and full_body_ref.png inform smooth human curves. Cropped continuous profile has no detached head.
Omissions: Omit the short eye stroke to keep the narrow facial region clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'db06f924-0c4e-4528-9bef-c6b4cb179003'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/fashion design shoes_db06f924-0c4e-4528-9bef-c6b4cb179003.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'face-beside-mobile-scanner'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "footwear"
    categories = ("primitives", "footwear")
    aliases = ()
    keywords = ('fashion', 'design', 'shoes')

    def build(self):
        # Symbol plan: A side-profile face beside an upright phone, with smooth forehead, nose and rounded mouth hollow; straight left cut indicates a cropped head.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('face',(4,40),[('L',(4,8)),('L',(7,8)),('C',(14,13),(10,8),(12,9)),('L',(21,25)),('C',(15,30),(17,26),(15,27)),('C',(19,36),(15,34),(16,35)),('C',(17,40),(21,38),(20,40)),('L',(4,40))],True)
        p('phone',(33,12),[('L',(40,12)),('A',(44,16),4,4,True),('L',(44,31)),('L',(44,36)),('A',(40,40),4,4,True),('L',(33,40)),('A',(29,36),4,4,True),('L',(29,31)),('L',(29,16)),('A',(33,12),4,4,True)],True)
        line('screen-edge',(29,31),(44,31));join('screen-edge','phone')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            n=f'{name}-{i}'
            if kind=='L': self.add_line(n,start,end)
            elif kind=='A': self.add_arc(n,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(n,start,(args[0],args[1],end))
            members.append(n);start=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def mirror(self,n,start,commands,closed=True):
        axis=24
        m=lambda p:(2*axis-p[0],p[1])
        nodes=[start]+[c[1] for c in commands]
        rev=[]
        for i,c in reversed(list(enumerate(commands))):
            k,end,*args=c
            if k=='C':rev.append((k,m(nodes[i]),m(args[1]),m(args[0])))
            elif k=='A':rev.append((k,m(nodes[i]),*args))
            else:rev.append((k,m(nodes[i])))
        self.path(n,start,commands+rev,closed)
