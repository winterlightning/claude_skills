"""Round-headed infant in a diagonal wrap. VRECT_L supplies the tall envelope. Source supplies large circular head and fold; human user.svg supplies circular head construction. Head center(24,14) radius10; blanket top32 gives exact8 centerline gap. Unresolved curved-distance review and undersized folded blanket hole. A curved blanket-top layout was tried first; it also returned review. Reducing the head or deleting the fold loses the requested distinction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ec8badad-3b98-4a32-bca0-d815508f5700'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/04-swaddled-newborn-baby/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-headed-baby-in-a-diagonal-wrap-v2'
    variant_of = 'round-headed-baby-in-a-diagonal-wrap'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('round', 'headed', 'baby', 'in', 'a', 'diagonal', 'wrap', 'v2')

    def build(self):
        def circle(name, x, y, r):
            pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r)]
            for i in range(4): self.add_arc(f'{name}-{i}',pts[i],pts[(i+1)%4],radius_x=r)
            self.add_contour(name,*[f'{name}-{i}' for i in range(4)],closed=True)
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                part=f'{name}-{i}'
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A': self.add_arc(part,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                else: self.add_bezier(part,here,(args[0],args[1],end))
                here=end; members.append(part)
            self.add_contour(name,*members,closed=closed)
        circle('head',24,14,10)
        path('blanket',(8,32),[('L',(40,32)),('A',(24,44),16,12,True),('A',(8,32),16,12,True)],True)
        self.add_line('fold',(8,32),(24,44))
        self.relate('connect','fold','blanket')
