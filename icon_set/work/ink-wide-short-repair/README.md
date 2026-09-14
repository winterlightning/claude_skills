# Keyshape bounds repair — 30 original modules

All 30 icons validate without warnings, are published in the SOLO48 manifest, and are absent from the rebuilt Failed build gallery. The matching “Ink box too wide & too short” failure group is gone.

## Construction and review

The 19 upright subjects use VRECT_L: ink (6,2)–(42,46), centerlines (8,4)–(40,44). The 11 wide subjects use HRECT_L: ink (2,6)–(46,42), centerlines (4,8)–(44,40). These preserve their vertical and horizontal subject proportions. Legacy keyshape aliases and obsolete bounds comments were updated in the original Python files. Source IDs and paths remain intact; AUTHOR is gpt-6.

The interrupted geometry repairs were retained, then the Eiffel Tower's lower deck was raised to y=29 with its shared leg junctions, with a shallow elliptical base arch, giving it the required clearance. The pregnancy icon's cradling arm was made shallower using a shared vertical radius, with rebalanced heart lobes preserving the heart and belly. No further details were removed in this completion pass. No contracts, tolerances or validation rules were changed by this task.

Inspected Lucide glasses original and atomic-debug geometry for paired lenses, open temples and bridge construction; inspected Lucide heart original and atomic-debug geometry for mirrored lobes and flowing shoulders. The shared full_body_ref.png informed rounded, simplified human strokes; the pregnancy icon is a cropped torso with no detached head, so the head-to-body gap is not applicable. Natural asymmetry is retained in the pregnancy profile, wolf, bird and architectural scenes. No additional useful Lucide matches were inspected for the remaining subjects.

Both after-light.png and after-dark.png were visually reviewed, including the native 48-pixel drawings beside each enlarged preview.

## Build

The solo build published all 30 repaired targets. It exits 1 because 698 other icons fail validation (previously 728). None of these 30 remains in the failed list. The overall test suite is not green: Ran 339 tests in 195.767s; FAILED (failures=793, errors=26, skipped=1). Server tests include sandbox socket permission errors; other tests include existing library failures. See tests.log for details.

## Per-icon validation

| Icon / subject | Keyshape | Status | Original source |
|---|---|---|---|
| ant | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/ant_4dc29185_dc5f_4ffe_94d4_dbda6690888c.py` |
| aquarius-zodiac-symbol | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/aquarius_zodiac_symbol_6a7d7977_2fda_5703_aeaa_a73c4a23525e.py` |
| beetle | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/beetle_82fb3003_56b5_5594_a35c_f4552fbc42d8.py` |
| bow-tie | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/bow_tie.py` |
| bug-head-with-antennae | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/insect_e62c082c_5d5e_5688_8d97_71a37ce00782.py` |
| fedora-hat | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/fedora_hat_59a69ae5_2ca0_4282_b84e_f7e0df2d8229.py` |
| hanging-bassinet | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/hanging_bassinet_cac28c98_7a13_413c_8246_fe935c1db139.py` |
| hanging-spider | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/spider_hang_c5352ba7_8705_433f_bfb4_5f356398c838.py` |
| jellyfish | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/jellyfish_box_e6bd915b_edf6_50c2_9697_5ba2b96a4673.py` |
| passenger-bus | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/passenger_bus.py` |
| pointed-crystal-cluster | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/pointed_crystal_cluster_ad287d09_ed0b_449e_9e30_f234e0f18b97.py` |
| round-eyeglasses | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/round_eyeglasses_41550461_e3b5_5afa_9c94_f00a4eb2aa3a.py` |
| round-glasses | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/round_glasses_470b6a50_6961_58f3_a538_29fd0c973118.py` |
| round-spectacles | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/round_spectacles_136a421d_0aa5_57f0_bc5e_ab9d19e5eca4.py` |
| round-sunglasses | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/round_sunglasses_30c30b8f_1761_4b11_b367_77273103d6f1.py` |
| shanty-house-cluster | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/shanty_house_cluster_692b62a9_93a0_402d_97e9_80a82768c730.py` |
| ski-goggles | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/ski_goggles_63a44219_0af5_5214_abed_771271356b20.py` |
| ski-goggles-with-brow-band | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/ski_goggles_with_brow_band_a177b70f_0c0f_5d94_9d0e_e53300456681.py` |
| trailing-hanging-planter | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/trailing_hanging_planter_648d5f22_ccb1_4224_9894_c373442f1825.py` |
| wide-ski-goggles | HRECT_L | valid, zero warnings | `icon_set/model/icons/solo/wide_ski_goggles_dc9fedbc_8058_5e3a_8a22_47f1828e3da5.py` |
| wolf-head | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/wolf_head_5980d529_a023_5a54_8f17_b3538741399a.py` |
| woodpecker-on-trunk | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/wild_bird_woodpecker_cc845c7b_ac9f_42ef_b9a7_61abf8646ba9.py` |
| eiffel-tower | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/eiffel_tower_1ee658b0_6de1_498b_ade7_e3bf20134722.py` |
| lighthouse-in-waves | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/lighthouse_in_waves_f1f0889a_aadc_4091_827d_5525edb8fcb3.py` |
| pregnant-belly-with-heart | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/pregnant_belly_with_heart_d8bedcbd_494e_5cf0_967f_4c5dac6cee67.py` |
| stepped-office-block-with-flag | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/stepped_office_block_with_flag.py` |
| windmill | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/windmill_95c449a5_8e44_5a99_9486_caf1e3e38105.py` |
| house-shaped-pendulum-clock | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/house_shaped_pendulum_clock_4034b865_e266_493a_bb67_569bf497aecd.py` |
| painted-wall-mural-panel | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/painted_wall_mural_panel.py` |
| tabletop-three-arm-candelabra | VRECT_L | valid, zero warnings | `icon_set/model/icons/solo/tabletop_three_arm_candelabra_1fd0448b_e249_5adc_9797_e731d5823281.py` |
