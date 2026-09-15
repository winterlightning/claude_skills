'Torii gate with the two inner posts removed. HRECT_L preserves the broad upturned lintel. Lucide landmark informs the structural rhythm.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32e3b1cc-fbf3-4478-858a-ce86e17b4058'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/shrine of itsukushima_32e3b1cc-fbf3-4478-858a-ce86e17b4058.svg'
AUTHOR = 'gpt-6'

class ItsukushimaToriiGate(Solo48):
    icon_id = 'itsukushima-torii-gate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('itsukushima', 'torii', 'gate', 'shrine', 'japan', 'shinto', 'miyajima', 'landmark')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('eave-left',(4, 8),*(((4, 9.10876678), (4.30973859, 10.27111995), (6, 11)),))
        self.add_line('lintel-1',(6, 11),(9, 11))
        self.add_line('lintel-2',(9, 11),(24, 11))
        self.add_line('lintel-3',(24, 11),(39, 11))
        self.add_line('lintel-4',(39, 11),(42, 11))
        self.add_bezier('eave-right',(42, 11),*(((43.69026141, 10.27111995), (44, 9.10876678), (44, 8)),))
        self.add_line('beam-1',(4, 21),(9, 21))
        self.add_line('beam-2',(9, 21),(18, 21))
        self.add_line('beam-3',(18, 21),(30, 21))
        self.add_line('beam-4',(30, 21),(39, 21))
        self.add_line('beam-5',(39, 21),(44, 21))
        self.add_line('post-left-1',(9, 11),(9, 21))
        self.add_line('post-left-2',(9, 21),(9, 40))
        self.add_line('post-right-1',(39, 11),(39, 21))
        self.add_line('post-right-2',(39, 21),(39, 40))
        self.add_contour('roof',*('eave-left', 'lintel-1', 'lintel-2', 'lintel-3', 'lintel-4', 'eave-right'),closed=False)
        self.add_contour('beam',*('beam-1', 'beam-2', 'beam-3', 'beam-4', 'beam-5'),closed=False)
        self.add_contour('post-left',*('post-left-1', 'post-left-2'),closed=False)
        self.add_contour('post-right',*('post-right-1', 'post-right-2'),closed=False)
        self.relate('connect',*('roof', 'post-left'))
        self.relate('connect',*('beam', 'post-left'))
        self.relate('connect',*('roof', 'post-right'))
        self.relate('connect',*('beam', 'post-right'))
