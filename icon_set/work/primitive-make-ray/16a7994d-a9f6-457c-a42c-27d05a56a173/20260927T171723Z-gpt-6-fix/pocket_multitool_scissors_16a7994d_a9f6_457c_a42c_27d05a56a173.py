"""Pocket multitool with two distinct unfolded implements instead of crossed scissor sticks.
Plan: a horizontal capsule handle owns a slanted left blade and a hooked pointed right blade; the tools remain asymmetric as in the source.
Keyshape SQUARE centerline (6,6)-(42,42). Lucide pocket-knife and scissors informed compact handle/blade construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "16a7994d-a9f6-457c-a42c-27d05a56a173"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pocket-multitool-scissors/20260927T170245Z-thuan-mac-1/reference/swiss army knife scissors_16a7994d-a9f6-457c-a42c-27d05a56a173.svg"
AUTHOR = "gpt-6"
class PocketMultitoolScissors(Solo48):
 icon_id = "pocket-multitool-scissors"
 keyshape = Keyshape.SQUARE
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "tools"
 aliases = ("swiss-army-knife",)
 keywords = ("pocket", "multitool", "scissors", "knife")
 def build(self):
  body=((12,30),(16,30),(32,30),(36,30),(42,36),(36,42),(12,42),(6,36))
  parts=[]
  for j,a in enumerate(body):
   b=body[(j+1)%len(body)];n=f"body-{j}";parts.append(n)
   if j in (3,4,6,7):self.add_arc(n,a,b,radius_x=6,sweep=True)
   else:self.add_line(n,a,b)
  self.add_contour("body",*parts,closed=True)
  self.add_line("blade-left",(16,30),(20,6))
  self.add_polyline("blade-right",(32,30),(32,18),(28,16),(36,6),(40,12),(40,30))
  self.relate("connect","body","blade-left")
  self.relate("connect","body","blade-right")
