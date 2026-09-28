from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID="15cdcedc-403b-4401-be0b-ba02e4b22811"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__performance-increase-mail/20260926T163748Z-thuan-mac/reference/performance increase mail_15cdcedc-403b-4401-be0b-ba02e4b22811.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="performance-increase-mail"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="business"
 aliases=()
 keywords=("performance","increase","mail","envelope","chart")
 def build(self):
  self.add_line("bar-short",(8,16),(8,22))
  self.add_line("bar-middle",(16,12),(16,22))
  self.add_line("bar-tall",(24,8),(24,22))
  self.add_polyline("growth-arrow",(32,12),(40,6),(40,12))
  self.add_line("envelope-left",(6,30),(6,42))
  self.add_line("envelope-bottom",(6,42),(42,42))
  self.add_line("envelope-right",(42,42),(42,30))
  self.add_line("envelope-fold-left",(42,30),(24,34))
  self.add_line("envelope-fold-right",(24,34),(6,30))
  self.add_contour("envelope","envelope-left","envelope-bottom","envelope-right","envelope-fold-left","envelope-fold-right",closed=True)
