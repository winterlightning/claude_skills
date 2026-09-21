"""Capital W with central peak and detached underline. Lucide type informs monoline lettering; shared paired valleys preserve the letter.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='793dd4fe-ce02-4596-b689-c68a21e6544d'
SOURCE_PATH='pictographic-primitives/symbol/w (text u)_793dd4fe-ce02-4596-b689-c68a21e6544d.svg'
AUTHOR='gpt-6'

class WLetterUnderlined(Solo48):
    icon_id='w-letter-underlined'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('w', 'letter', 'text', 'underline', 'typography', 'alphabet', 'language')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('w',[(6,6),(14,32),(24,12),(34,32),(42,6)])
        self.add_line('underline',(6,42),(42,42))
