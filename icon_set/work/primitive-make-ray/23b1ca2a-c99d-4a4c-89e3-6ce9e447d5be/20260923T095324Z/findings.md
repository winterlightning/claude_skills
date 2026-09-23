A perspective cube displayed on a mobile phone with a bottom divider.
Keyshape: VRECT_L — VRECT_L preserves the upright phone silhouette.
Both themes and sizes inspected. Phone and cube are readable, but cube face openings are too tight. MIC failures remain on cube edges, seams and footer. Retained for manual review.
Phone and cube are mirrored about x=24; perspective face arrangement follows the reference.
Omissions: no semantic components omitted. Reference stroke weight and enclosure proportions recomposed for SOLO48.
Construction references:
Supplied reference: retained phone, bottom divider and three cube faces.
Lucide smartphone and box originals and atomic-debug: rounded phone corners and shared cube vertices.

status: invalid
  ERROR  mic [cube]: parallel straight edges cube-2 and cube-front-seam are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cube-front-seam]: parallel straight edges cube-front-seam and cube-5 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cube]: parallel straight edges cube-6 and cube-top-seam-2 are 6.94595 apart on centerlines (ink gap 2.94595); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [cube-top-seam]: parallel straight edges cube-top-seam-2 and cube-3 are 6.94595 apart on centerlines (ink gap 2.94595); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [cube]: parallel straight edges cube-1 and cube-top-seam-1 are 6.94595 apart on centerlines (ink gap 2.94595); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [cube-top-seam]: parallel straight edges cube-top-seam-1 and cube-4 are 6.94595 apart on centerlines (ink gap 2.94595); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [footer]: footer and cube are 7 apart on centerlines nearest (24, 36)<->(24, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship