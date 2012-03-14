
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_10_0_3Go.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_11_1_MDG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_13_1_3ga.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_14_1_VhY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_15_1_GBG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_16_1_c4X.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_18_1_3Py.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_1_1_kZm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_20_2_Vqp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_22_1_siO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_2_1_rjX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_3_1_SCV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_4_1_pF3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_5_1_74l.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_6_1_qZ2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_7_1_T4A.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_8_1_EYe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-05Aug2011-v1/patTuple_skim_9_1_1z9.root',

	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_10_2_CZ6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_12_0_Zd8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_13_1_qip.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_14_1_bAV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_15_1_Ngx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_18_0_04S.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_19_1_lbl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_1_1_dEy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_21_0_NXL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_22_1_rqg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_25_1_Odr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_26_1_nig.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_29_0_dUf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_2_1_cEo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_30_2_grT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_34_1_gLB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_36_1_fbt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_39_1_0aG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_3_1_DEG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_41_0_BX9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_42_1_pya.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_43_2_1eM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_45_1_Pl8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_46_2_0ye.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_49_1_6x7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_50_1_8nJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_51_0_puf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_52_1_8nJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_54_1_rKJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_56_1_Rsm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_59_1_KlX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_61_1_Xif.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_63_1_E2k.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_64_1_8LR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_65_1_cvy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_66_2_f5R.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_67_0_q1I.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_69_2_K6V.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_69_3_AMW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_71_1_p5z.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_72_1_DCM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_73_1_gWb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_74_2_nzm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_75_1_pTE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_78_2_GVx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_7_2_hPG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_81_0_Syo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-May10ReReco-v1/patTuple_skim_9_1_8m3.root',

	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_100_0_dWS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_107_0_dW2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_108_0_mKv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_113_0_YWN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_124_0_ozG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_125_0_UxV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_128_0_Z0K.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_130_0_G7l.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_132_0_NWO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_144_0_br9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_15_0_Xdt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_16_0_P8d.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_17_0_2B0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_19_0_TfV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_20_0_ttD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_22_0_crZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_23_0_C7d.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_28_1_skB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_33_1_pXD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_37_0_8Es.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_43_1_hXw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_46_0_uJV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_47_0_TAy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_49_0_7w9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_51_0_d1i.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_56_0_qD6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_64_0_NyS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_65_0_BMP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_68_0_Anz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_6_0_GFI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_82_1_Ebh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v4/patTuple_skim_90_0_cVm.root',

	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_10_0_DYo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_11_1_QAC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_12_1_mWx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_13_1_DK9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_14_1_eHx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_15_1_TRh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_16_1_1Fi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_17_0_hqb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_18_0_vUm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_19_0_DEw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_1_1_Dge.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_20_0_iOc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_21_0_UZn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_22_0_0yA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_23_0_gDO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_24_1_QFW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_25_1_gAX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_26_1_pVx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_27_1_rsk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_28_1_aeu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_29_1_zmN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_30_1_zd4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_31_0_Sk5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_32_0_Bt1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_33_0_g80.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_34_0_rdt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_35_1_ZKz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_36_1_6Wz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_37_1_71C.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_38_1_B6e.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_39_1_9iE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_3_0_Xps.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_40_1_31o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_41_1_XH1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_42_0_HU7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_43_0_6BL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_44_1_j4r.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_45_1_Cuy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_46_1_RGP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_47_1_uwt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_49_1_Xdq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_50_0_IoZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_51_1_4o5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_53_1_Og6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_56_0_8QK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_57_1_1nM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_60_1_vaX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_62_1_Rgu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011A-PromptReco-v6/patTuple_skim_9_0_TA2.root',

	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_100_2_rz5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_103_1_mbq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_113_1_S4U.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_117_2_HCT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_121_1_5eG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_127_2_sVx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_131_2_t7Y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_136_2_geT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_138_2_GAr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_13_1_MiZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_143_2_EbP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_146_2_0Lx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_147_2_8Ep.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_19_2_b8m.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_22_1_Tk5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_24_1_Sfu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_25_1_saf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_30_2_yEV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_33_2_QcH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_34_2_aaK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_35_2_oTi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_37_2_ByU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_45_2_sKm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_50_2_4or.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_55_1_0j0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_5_1_deQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_62_1_QCd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_67_2_Elh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_76_1_M7m.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_79_1_fVb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_81_2_oQF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_83_1_xGh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_85_2_e4N.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_8_2_RB4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_91_2_ost.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_93_1_Lr5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/Mar13_DecoupledIso/Run2011B-PromptReco-v1/patTuple_skim_98_2_Kuq.root',
]
        )
