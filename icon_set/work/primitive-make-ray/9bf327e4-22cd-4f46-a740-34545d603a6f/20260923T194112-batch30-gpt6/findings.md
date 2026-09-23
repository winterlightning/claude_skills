# ocd disorder symptoms 2

A head silhouette containing an obsessive checklist.

Keyshape: VRECT_L. Upright page or profile; target centerline extremes (8,4)-(40,44).

Plan: Left-facing profile with checklist inside; deliberate anatomical asymmetry.

References: No useful Lucide match; supplied reference defines checklist profile.

Omissions: Three writing rules reduced to two; small empty checkbox retained as a validation-risk feature.

Visual review: Head and checklist remain visible, but empty checkbox closes up and checks crowd the profile. Not visually approved.

Human construction: human_ref/user.svg inspected for contour economy. This is a connected head/neck profile, not a detached stick figure; no detached-head gap applies.

```text
status: invalid
  ERROR  canvas/keyshape bounds: visible ink (6, 2, 42, 46) does not match the VRECT_L envelope (6, 2, 42, 46) (deltas [0.0, 0.0, 0.0, 0.0], tolerance 0.0)
  ERROR  mic [profile-top]: parallel straight edges neck-back and empty-box-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [empty-box]: parallel straight edges empty-box-2 and empty-box-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [empty-box]: parallel straight edges empty-box-4 and face-neck-5 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [empty-box]: parallel straight edges empty-box-1 and empty-box-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [profile-top]: profile-top and check-0 are 5.92012 apart on centerlines nearest (13.6233, 12.5223)<->(19, 15); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [profile-top]: profile-top and text-0 are 5.92012 apart on centerlines nearest (38.3767, 12.5223)<->(33, 15); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [profile-top]: profile-top and text-1 are 6.48482 apart on centerlines nearest (39.2631, 25.6812)<->(33, 24); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [face-neck]: face-neck and empty-box are 5 apart on centerlines nearest (20, 34)<->(25, 34); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [check-0]: check-0 and check-1 are 5.83095 apart on centerlines nearest (21, 17)<->(24, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
