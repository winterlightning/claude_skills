# passwords correct

A password field displaying three X characters.

Keyshape: HRECT_M. Wide password field; target centerline box (4,10)-(44,38).

Plan: Three identical diagonal crosses spaced on a common baseline inside a wide rectangle.

Construction: No useful Lucide match; repeated crosses and field are reconstructed from the supplied reference.

Omissions: None.

Visual review: Three X characters remain legible; margins and inter-character gaps are below the profile minimum. Not approved under the spacing rule.

```text
status: invalid
  ERROR  mic [field]: field and x-0-0 are 5 apart on centerlines nearest (4, 21)<->(9, 21); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [field]: field and x-2-1 are 5 apart on centerlines nearest (44, 27)<->(39, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [x-0-1]: x-0-1 and x-1-2 are 6 apart on centerlines nearest (15, 27)<->(21, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [x-1-1]: x-1-1 and x-2-2 are 6 apart on centerlines nearest (27, 27)<->(33, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
