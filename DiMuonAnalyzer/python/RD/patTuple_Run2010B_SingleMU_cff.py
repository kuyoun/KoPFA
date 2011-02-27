
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_10_1_Gr9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_11_1_pPJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_12_1_fOO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_13_1_paT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_14_1_oaa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_15_1_AIs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_16_1_EyZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_17_1_eUb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_18_1_fUH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_19_1_2oo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_1_1_VdD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_20_1_ELq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_21_1_4CS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_22_1_HzK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_23_1_kpx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_24_1_Ood.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_25_1_ybS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_26_1_ZT7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_27_1_xr7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_28_1_auC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_29_1_tUu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_2_1_OD5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_30_1_11I.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_31_1_j61.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_32_1_OM1.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_33_1_2HE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_34_1_inq.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_35_1_QDo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_36_1_LZb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_37_1_DRy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_38_1_bH9.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_39_1_I5H.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_3_1_PIa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_40_1_NY2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_41_1_ifO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_42_1_047.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_43_1_w8X.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_44_1_SS4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_45_1_6ju.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_46_1_ZpE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_47_1_xA4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_48_1_bXx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_49_1_Y3u.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_4_1_lPM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_50_1_u2h.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_5_1_TT5.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_6_1_aXO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_7_1_GNO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_8_1_raO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Nov22_jetfixed/Run2010B-Nov4ReReco_v1_V2/patTuple_skim_9_1_9hi.root',
]
        )
