"""Fresh SOLO48 revision of clover from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '15eae920-a828-4e82-80ae-2bcb9cd7a2f2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clover/20260927T071330Z-thuan-mac-1/reference/clover_15eae920-a828-4e82-80ae-2bcb9cd7a2f2.svg'
AUTHOR = 'gpt-6'

class Clover(Solo48):
    icon_id = 'clover'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('clover', 'state', 'solo-ai-next100')

    def build(self) -> None:

        # Distinct standalone clover: four heart leaves and a visible lower stem.
        shape=[('L',(14,14)),('C',(14,8),(16,6),(19,6)),
               ('C',(22,6),(24,9),(24,11)),
               ('C',(24,9),(26,6),(29,6)),
               ('C',(32,6),(34,8),(34,14)),('L',(24,24))]
        def turn(p,n):
            for _ in range(n):p=(48-p[1],p[0])
            if n==2 and p[1]>24:p=(p[0],24+round((p[1]-24)*0.55))
            return p
        for n in range(4):
            commands=[]
            for item in shape:
                kind,*points=item
                commands.append(tuple([kind]+[turn(p,n) for p in points]))
            path(self,f'leaf-{n}',(24,24),*commands,closed=True)
        line(self,'stem',(29,34),(30,42))
        contacts(self)
