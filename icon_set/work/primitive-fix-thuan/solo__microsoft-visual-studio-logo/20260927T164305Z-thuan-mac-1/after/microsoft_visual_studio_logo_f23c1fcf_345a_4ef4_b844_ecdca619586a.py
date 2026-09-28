"""Visual Studio bowtie mark; paired smooth-ended loops cross at the centre.
Plan: mirror one tapered closed loop around x=24; preserve the source's thin diagonal crossing.
Keyshape HRECT_L, centreline (4,8)-(44,40).
Lucide infinity supplies balanced loop construction; ends remain distinctively vertical.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "f23c1fcf-345a-4ef4-b844-ecdca619586a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__microsoft-visual-studio-logo/20260927T164305Z-thuan-mac-1/reference/microsoft visual studio logo_f23c1fcf-345a-4ef4-b844-ecdca619586a.svg"
AUTHOR = "gpt-6"
class MicrosoftVisualStudioLogo(Solo48):
 icon_id = "microsoft-visual-studio-logo"
 keyshape = Keyshape.HRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "logos"
 aliases = ()
 keywords = ("microsoft", "visual", "studio", "logo")
 def build(self):
  for label,mirror in (("left",False),("right",True)):
   def pt(x,y): return (48-x if mirror else x,y)
   self.add_bezier(label+"-upper",pt(4,14),((pt(4,10),pt(7,8),pt(10,8))))
   self.add_line(label+"-diagonal-up",pt(10,8),pt(24,24))
   self.add_line(label+"-diagonal-down",pt(24,24),pt(10,40))
   self.add_bezier(label+"-lower",pt(10,40),((pt(7,40),pt(4,38),pt(4,34))))
   self.add_line(label+"-end",pt(4,34),pt(4,14))
   self.add_contour(label,*(label+"-"+part for part in ("upper","diagonal-up","diagonal-down","lower","end")),closed=True)
  self.relate("connect","left","right")
