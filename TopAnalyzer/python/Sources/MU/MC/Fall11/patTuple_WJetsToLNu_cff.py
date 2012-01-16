import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = readFiles
)
readFiles.extend([
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_1_3_OlD.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_2_2_5Qn.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_3_2_NzZ.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_4_4_Wt1.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_5_0_gdB.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_6_0_RnC.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_8_0_hnz.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_10_0_TdC.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_12_2_rZN.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_14_3_wQW.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_15_4_uzo.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_16_4_in9.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_17_0_7Rs.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_18_0_toN.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_21_0_aT4.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_23_0_fsT.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_24_0_nGf.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_25_1_fh5.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_26_1_86M.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_27_1_gMy.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_28_1_NQ9.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_29_1_Mgs.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_30_0_fO3.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_31_0_ox4.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_34_0_GP1.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_36_0_TMx.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_37_0_CIf.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_38_0_9xW.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_39_0_6ST.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_41_0_W6u.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_46_0_wUS.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_49_1_Fic.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_53_0_nrJ.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_54_2_mp7.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_57_2_yOz.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_59_4_TYP.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_61_3_wXX.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_62_0_QFg.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_65_0_uAx.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_66_0_gkX.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_67_2_AxT.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_69_1_boL.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_70_0_cMz.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_72_0_myk.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_73_0_AFD.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_75_0_p2E.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_77_1_aR5.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_78_0_tyw.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_80_0_fsH.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_81_0_imt.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_82_0_s1N.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_84_0_pWl.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_85_0_Pqq.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_87_3_gki.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_89_4_SRl.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_90_2_CoG.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_91_2_OYU.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_92_3_hGH.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_93_2_gki.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_94_2_krq.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_96_2_Sla.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_97_2_oNT.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_102_0_Mpl.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_105_2_7tJ.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_106_0_GyF.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_108_0_yYn.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_109_1_A0w.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_113_1_Zh7.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_116_0_pzl.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_117_0_zVk.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_119_5_xqC.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_120_3_pLg.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_121_3_hzY.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_122_1_PWg.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_124_1_t17.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_125_2_ukB.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_126_1_o7N.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_127_0_skn.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_131_2_Q4k.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_132_1_RDm.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_133_1_kHr.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_135_2_1Qh.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_137_1_3SP.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_138_0_rfZ.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_139_1_6KE.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_141_1_pLH.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_143_2_Zug.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_146_1_0I5.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_147_0_06N.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_149_0_6Kc.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_151_0_Qgo.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_153_0_JSU.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_154_0_gQY.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_155_1_UAe.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_156_2_zuW.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_157_3_bHS.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_159_2_RcH.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_160_1_z9k.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_161_0_Ix1.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_163_1_Dek.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_165_1_Phd.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_167_1_n4X.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_169_1_dyh.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_171_1_fWm.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_172_3_6WR.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_173_2_zpI.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_174_2_OK7.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_175_5_yz8.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_176_0_qYa.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_178_0_17p.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_179_0_DaO.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_181_0_c8H.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_182_2_RKM.root",
"rfio:/castor/cern.ch/cms/store/user/jhgoh/TopAnalysis/pat/MC/20111213_1/WJetsToLNu_1/patTuple_skim_183_1_3bd.root",
])