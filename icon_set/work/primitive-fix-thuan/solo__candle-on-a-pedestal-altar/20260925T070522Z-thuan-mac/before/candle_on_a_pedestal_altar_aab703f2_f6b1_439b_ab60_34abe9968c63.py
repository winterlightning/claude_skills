"""A lit candle stands on a broad pedestal altar. Flame and candle share the vertical axis; pedestal outline owns its sloped foot. Lucide church contributes continuous architectural outlines; source supplies candle and altar. Omit thin tabletop rim and wick.
Plan: exact VRECT_L envelope; stroke 4, integer points, shared attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aab703f2-f6b1-439b-ab60-34abe9968c63'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/altar_aab703f2-f6b1-439b-ab60-34abe9968c63.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'candle-on-a-pedestal-altar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = []
    keywords = ['candle', 'on', 'a', 'pedestal', 'altar']

    def build(self):
        self.add_bezier('flame',(24,4),((21,7),(20,8),(20,10)),((20,12),(28,12),(28,10)),((28,8),(27,7),(24,4)))
        self.add_polyline('candle',(20,28),(20,20),(28,20),(28,28))
        xs=[8,14,20,28,34,40]
        for i,(a,b) in enumerate(zip(xs,xs[1:])): self.add_line(f'top-{i}',(a,28),(b,28))
        self.add_contour('top',*[f'top-{i}' for i in range(5)])
        self.add_polyline('pedestal',(14,28),(14,36),(8,44),(40,44),(34,36),(34,28))
        self.relate('connect','candle','top-1','top-2','top-3')
        self.relate('connect','pedestal','top-0','top-1','top-3','top-4')
