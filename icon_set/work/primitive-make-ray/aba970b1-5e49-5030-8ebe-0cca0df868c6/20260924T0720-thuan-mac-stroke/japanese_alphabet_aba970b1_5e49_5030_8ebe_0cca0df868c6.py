"""Japanese hiragana a (あ): three coherent pen strokes with an upright crossing bar and a flowing loop. Split real intersections at shared integer nodes.
Construction: No useful Lucide glyph match; preserve the three source pen strokes.
Omissions: None; crossings are deliberate parts of the character.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aba970b1-5e49-5030-8ebe-0cca0df868c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__japanese-alphabet/20260924T071425Z-thuan-mac/reference/japanese alphabet_aba970b1-5e49-5030-8ebe-0cca0df868c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'japanese-alphabet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('japanese', 'alphabet')

    def build(self):
        # Symbol plan: Japanese hiragana a (あ): three coherent pen strokes with an upright crossing bar and a flowing loop. Split real intersections at shared integer nodes.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('top-bar',(6,12),[('L',(19,12)),('L',(42,12))])
        p('stem',(19,6),[('L',(19,12)),('L',(19,23)),('C',(20,35),(19,28),(19,32)),('C',(24,42),(21,38),(22,40))])
        p('loop',(32,18),[('C',(20,35),(30,24),(25,31)),('C',(7,39),(15,40),(10,42)),('C',(6,34),(6,38),(6,36)),('C',(19,23),(6,29),(12,24)),('C',(29,22),(22,22),(25,22)),('C',(42,32),(37,22),(42,26)),('C',(32,42),(42,38),(38,41))])
        join('top-bar','stem');join('loop','stem')

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
