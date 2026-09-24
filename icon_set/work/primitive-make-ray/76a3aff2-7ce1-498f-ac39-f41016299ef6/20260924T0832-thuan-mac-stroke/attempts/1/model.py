"""Two diagonally arranged hearts with smooth lobes and coherent tapered sides. Restore the larger heart upper-right lobe and preserve the small upper-right heart.
Construction: Lucide heart: smooth lobes flowing into tapered sides.
Omissions: The large upper-right edge remains partially occluded behind the smaller heart; no detached hook substituted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '76a3aff2-7ce1-498f-ac39-f41016299ef6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hearts-two/20260924T083118Z-thuan-mac/reference/heart and hook_76a3aff2-7ce1-498f-ac39-f41016299ef6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hearts-two'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('heart', 'and', 'hook')

    def build(self):
        # Symbol plan: Two diagonally arranged hearts with smooth lobes and coherent tapered sides. Restore the larger heart upper-right lobe and preserve the small upper-right heart.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('large',(18,24),[('C',(12,19),(16,21),(15,19)),('C',(6,25),(8,19),(6,21)),('C',(18,42),(6,31),(12,37)),('C',(30,29),(25,36),(30,32))])
        p('large-right-lobe',(18,24),[('C',(23,19),(20,20),(22,19))]);join('large','large-right-lobe')
        p('small',(33,10),[('C',(28,6),(31,7),(30,6)),('C',(24,11),(25,6),(24,8)),('C',(33,22),(24,14),(28,18)),('C',(42,11),(38,18),(42,14)),('C',(38,6),(42,8),(41,6)),('C',(33,10),(36,6),(35,7))],True)

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
