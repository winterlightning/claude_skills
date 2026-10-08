"""Corner detection and the round / sharp toggles for 48x48 stroke icons.

  detect        corner detection (sharp / round corners, junctions, kinks, curves)
  toggle        all-round and all-sharp outputs, with the re-detection check
  keyshape      each icon's keyshape, detected from its ink, and how far outputs reach past it
  keyshape_fit  keyshape geometry used by the sharp output (slicing, allowances)
  locks         the review lock list (locks.json)
  fetch         re-download the approved icon set from the review Worker
  svg_io        SVG reading helpers
  paths         where the input set, outputs, locks and fixes live
"""
