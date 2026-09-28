# Accepted main-icon exceptions

Applied drawing-specific user exceptions to 47 repaired main icons. All 47 exported successfully and the live gallery reports 47 exception tags for them. The catalog validation-failing main count changed from 22 to 0.

The visible Needs fix filter still includes 130 other source entries with review flags. No unrelated review flags were cleared. The three flags previously observed on repaired drawings were no longer active after the drawing hashes changed, so no manual review update was needed.

The custom 60×46 alphabet-monitor output remains in its work folder. Its registered 48px drawing received the exception; the custom output was not imported as SOLO48.

Validation evidence is retained. SVG changes invalidate approval. Family/canvas/stroke mismatches and checker errors remain blocking.

## Verification

- Exception tests: 8 passed, including SOLO48 acceptance and expiry when artwork changes.
- Selected build: 47 checked, 0 failed.
- Workflow, publish, generation and metadata tests: 50 passed, 1 unrelated failure. The runtime-capabilities fixture omits the existing `production_api` response field.
- The three text modules now embed the exact used glyphs from their snapshots, preserving their SVG hashes after promotion.

## Accepted drawings

| Drawing | Automatic result | Registered source |
|---|---|---|
| open-palm-hand-gesture-solo-b002-11 | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/open_palm_hand_gesture_solo_b002_11_a322931e_aa9b_59e9_8a03_20657747f732.py) |
| seven-lobed-cannabis-leaf | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/seven_lobed_cannabis_leaf_487f3a05_de28_44cf_9e49_3130e24b6363.py) |
| smart-watch-yuan-symbol | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/smart_watch_yuan_symbol_b1f2ce85_d591_4522_b2a6_64d3fc5c75f6.py) |
| smartwatch-dollar-sign | review | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/smartwatch_dollar_sign_6b9fab53_d945_4f18_86b9_fcc5bd5840ce.py) |
| browser-with-18-plus-text | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/browser_with_18_plus_text_fc5ffdff_80e9_4119_bf62_fb7c515c5aad.py) |
| house-lock | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/house_lock_a7f1734e_4fae_4c0a_9d33_80bf4a3da78f.py) |
| monitor-small-squares | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/monitor_small_squares_1aef3c2a_6d0d_43a2_9616_698d70dc5298.py) |
| laptop-skull | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/laptop_skull_44a8272b_04c4_4a7c_b200_ee122a35ef32.py) |
| square-woman | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/square_woman_7f5b5d3c_bed1_4393_a918_ca1a7b2fc9f1.py) |
| plane-1-solo | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/plane_1_44d3d80b_4240_42cf_9ac4_2237f7c5d0aa.py) |
| climbing-airplane-rounded-nose | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/climbing_airplane_rounded_nose_8fe19626_3dae_5f95_be02_4dbe10f65534.py) |
| car-e1ae9ac1 | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/car_e1ae9ac1_e1ae9ac1_dad6_526e_975f_e2ee61a2940d.py) |
| car-transportation | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/car_transportation_38792ded_1850_5f89_8b9a_dc4c3354c564.py) |
| monitor-letters | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/monitor_letters_dd80ecbb_13f8_47dc_9883_44bd19aa7cc6.py) |
| time-clock-file-1 | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/time_clock_file_1_e7ce785e_158f_41d6_9e8b_dcba4879acac.py) |
| laptop-small-squares | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/laptop_small_squares_71714a04_dd1b_4fab_90a6_dbd391dacaf5.py) |
| tv-circle-check | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/tv_circle_check_91199cb3_6e0d_41e0_9c27_12e09942eed6.py) |
| bubble-message-pm-text | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/bubble_message_pm_text_39d51711_cb0a_4cf4_bdca_37c1fe832458.py) |
| rectangle-like-text | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/rectangle_like_text_3d250c41_6017_4d1f_9278_42fadf1fc93d.py) |
| star | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/star_fc535717_5e07_564a_aad9_923ace667ffb.py) |
| rectangle-sub-text | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/rectangle_sub_text_dd1e6365_7d94_41e2_84d6_66c8ad75ede1.py) |
| ui-webpage-ad-text | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/ui_webpage_ad_text_24fe2386_b951_48d1_8a50_9d4e65f27e91.py) |
| landscape-picture-file | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/landscape_picture_file_41f3ad63_cd17_441d_b26d_945da63c6f7c.py) |
| source-code-file | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/source_code_file_a7885b17_70fa_431a_8397_cf8f653fa82c.py) |
| document-bar-chart | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/document_bar_chart_d48f86f5_12a6_47ce_a5d0_968db65faf5e.py) |
| cardboard-shipping-box | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/cardboard_shipping_box_25bec113_9501_56df_8f1c_88dce76cb03d.py) |
| open-book-empty-pages | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/open_book_empty_pages_b5768591_30d0_458a_8f42_f8fa19890c4e.py) |
| girl-full-body | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/girl_full_body_45881775_2179_41cc_98a1_78a598c550c1.py) |
| document-with-clock-symbol | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/document_with_clock_symbol_0ef08051_f8cf_452c_9504_27f2eb99eb1b.py) |
| briefcase-dollar | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/briefcase_dollar_07459f9b_1db4_4f1f_aeee_4e5113b2f2f4.py) |
| browser-dollar-sign-right | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/browser_dollar_sign_right_150d4701_3c3f_45a7_a26d_8c580a891da1.py) |
| calendar-pie | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/calendar_pie_8c9afa4f_6b92_41b3_8bcd_f538c69afde6.py) |
| calendar-math | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/calendar_math_14b5dacf_2ae7_4b43_b032_7129b3d49037.py) |
| monitor-math | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/monitor_math_6cbe1bf6_f7d0_4add_99b4_0d1a57f47f13.py) |
| phone-book | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/phone_book_b18b4462_5e10_44fd_99e3_3fb256fb4f34.py) |
| common-file-text | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/common_file_text_5aeb0892_b41b_5c32_97fe_0a13b74d6d80.py) |
| car-flash | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/car_flash_3cb36a1f_8edb_4e21_9623_b8c8fac724c3.py) |
| female-user-profile | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/female_user_profile_b7558322_6681_447e_8b8a_0f4a588a3f0e.py) |
| house-phone | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/house_phone_7c7ae497_e683_4449_9d47_32e2c0e677e7.py) |
| house-music | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/house_music_3640f2f0_b0c0_4dbd_9d92_86762ff6cfbb.py) |
| ui-webpage-skull | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/ui_webpage_skull_9ab7c5fa_7d54_4c5c_8f9e_b01743e34909.py) |
| blood-bag-solo | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/blood_bag_7d002be2_8db0_591d_9e62_868a56fdf240.py) |
| prescription-drug-paper | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/prescription_drug_paper_e0b1e330_cc81_522c_9a29_44fd4f8881cf.py) |
| movie-production-clapperboard | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/movie_production_clapperboard_7812933e_4da0_4067_9131_d948a045fef8.py) |
| lock-person | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/lock_person_ca0b86cd_f823_4251_8d27_7775eddb1f7a.py) |
| travel-passport-with-globe | fail | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/travel_passport_with_globe_1f180a84_a846_4671_b767_dbb6041f800a.py) |
| webpage-user-profile | pass | [source](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/webpage_user_profile_6765de1f_1adc_4a6a_bbb4_c497deffd007.py) |
