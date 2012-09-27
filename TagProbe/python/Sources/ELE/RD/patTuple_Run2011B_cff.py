
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_100_2_TIj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_101_1_oHS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_102_1_7yW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_103_1_FGO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_104_1_XzP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_105_1_jMT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_106_1_T3r.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_107_1_jhW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_108_1_VVg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_109_1_aFu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_10_1_NCI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_110_1_KpR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_111_1_tMR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_112_1_nEJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_113_1_5u3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_114_2_1Kp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_115_1_9K7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_116_1_FAg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_117_1_UJz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_118_1_KO2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_119_1_seW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_11_1_91B.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_120_1_TcM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_121_1_ymu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_122_1_D9p.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_123_1_57A.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_124_2_awe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_125_1_Gfl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_126_1_kMu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_127_1_nLt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_128_1_CsA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_129_1_v3H.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_12_1_KrJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_130_1_93d.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_131_1_MND.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_132_1_Bku.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_133_1_wvt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_134_1_m2P.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_135_1_Wst.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_136_1_RfL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_137_1_cGx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_138_1_kfJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_139_1_x46.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_13_1_FLZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_140_1_H0m.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_141_1_1kT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_142_1_kkT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_143_2_xEL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_144_1_hYP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_145_1_ikR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_146_2_zDR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_147_1_SZK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_148_1_9KO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_149_1_3GC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_14_1_B8D.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_150_1_bMB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_151_1_rmO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_152_1_brA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_153_2_Xd2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_154_1_qR6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_155_1_wiS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_156_1_lpu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_157_1_sYv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_158_1_Vqi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_159_1_VIv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_15_1_39f.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_160_1_BrI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_161_1_c4e.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_162_1_S0D.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_163_1_ucM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_164_1_KFm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_165_1_Mjx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_166_1_cMc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_167_1_WPA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_168_1_PeV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_169_1_yOK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_16_1_RUh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_170_1_CER.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_171_1_Mwx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_172_1_ykl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_173_1_uSp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_174_2_aTm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_175_1_mjp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_176_1_Egs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_177_1_TF7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_178_1_z1q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_179_1_6ag.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_17_1_ciB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_180_2_CzX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_181_1_6nN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_182_1_JNs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_183_1_Fth.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_184_1_WFh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_185_1_bto.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_186_1_we1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_187_1_WOL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_188_1_rKe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_189_1_Xcn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_18_1_umX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_190_1_l6j.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_191_1_w77.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_192_1_apw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_193_1_Wxd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_194_1_uTk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_195_1_lCs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_196_1_c8C.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_197_1_AM9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_198_2_U94.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_199_1_HUH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_19_2_aTl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_1_1_UVB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_200_2_awJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_201_1_xV2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_202_2_XM8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_203_2_HE9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_204_1_vHx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_205_1_ZoO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_206_1_Dw0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_207_1_1x2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_208_1_jya.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_209_1_P6W.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_20_1_70e.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_210_1_zGX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_211_1_68G.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_212_1_rE3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_213_1_yhr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_214_1_vHv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_215_1_4xK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_216_1_RoM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_217_1_pZg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_218_1_IWZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_219_1_Eg7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_21_2_uu7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_220_1_2hn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_22_1_pfu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_23_2_gMh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_24_1_WuF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_25_1_crY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_26_2_TmD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_27_1_Os7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_28_1_BRX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_29_1_JJu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_2_1_Ccd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_30_1_LNx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_31_1_HL0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_32_1_5yu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_33_1_YR7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_34_3_EpI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_35_2_qyX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_36_1_fxw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_37_1_UWW.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_38_1_I1Y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_39_1_EZR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_3_1_okS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_40_1_nKJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_41_1_BTQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_42_2_q2X.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_43_1_28U.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_44_1_8Xa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_45_1_XiA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_46_1_HE3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_47_1_00Y.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_48_1_rOH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_49_1_5If.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_4_1_5lO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_50_1_6lg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_51_1_YQe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_52_1_Q99.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_53_1_6En.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_54_1_oaU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_55_1_gUh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_56_1_zwe.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_57_1_wUA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_58_1_dBc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_59_2_kyP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_5_1_8yB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_60_2_gMd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_61_2_hUz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_62_1_3fZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_63_1_YEs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_64_2_5bY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_65_1_nD0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_66_2_vW6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_67_1_DxV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_68_1_XRG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_69_1_GLd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_6_1_rWN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_70_1_BYu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_71_1_rFY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_72_1_LuD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_73_1_UX2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_74_1_VkL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_75_1_LAS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_76_2_dMd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_77_2_JcB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_78_3_8ll.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_79_1_jlE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_7_1_J67.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_80_2_TTv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_81_1_FvJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_82_1_kiS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_83_1_vMc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_84_1_UOw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_85_1_Zsr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_86_0_xzq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_87_1_fux.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_88_1_EZm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_89_2_CB3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_8_3_rLd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_90_1_1ax.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_91_1_7Ln.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_92_1_m7k.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_93_1_M6j.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_94_1_v7p.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_95_1_gNn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_96_1_L97.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_97_1_obS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_98_1_6yn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_99_1_oeA.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleElectron/2012Jan22_Gsf/Run2011B-PromptReco-v1/patTuple_skim_9_1_qad.root',
]
        )