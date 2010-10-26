import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

#process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
#    fileNames = cms.untracked.vstring(
#        'file:../prod/RD/patTuple_muon.root'
#         'rfio:///castor/cern.ch/user/t/tjkim/SDMUONFILTER/July19th_v4/Run2010A-PromptReco-v4/patTuple_muon_22_0_Qie.root'
#    )
#)

#process.load("PFAnalyses.TTbarDIL.Sources.MU.RD.patTuple_Run2010B_PromptReco_cff")
#process.load("PFAnalyses.TTbarDIL.Sources.MU.MC.Spring10.patTuple_WJets_cff")
#process.load("PFAnalyses.TTbarDIL.Sources.MU.MC.Spring10.patTuple_Zmumu_cff")
process.load("PFAnalyses.TTbarDIL.Sources.MU.MC.Spring10.patTuple_ZJets_cff")
#process.load("PFAnalyses.TTbarDIL.Sources.MU.MC.Spring10.patTuple_InclusiveMu15_cff")

# register TFileService
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('vallot.root')
)

process.VertexFilter = cms.EDFilter('VertexFilter',
    vertexLabel =  cms.InputTag('offlinePrimaryVertices'),
    min = cms.untracked.int32(1),
    max = cms.untracked.int32(999),
)

process.load("PFAnalyses.CommonTools.countingSequences_cfi")

from PFAnalyses.CommonTools.Selectors.muonSelectorPSet_cff import muonSelectorPSet
from PFAnalyses.CommonTools.Selectors.muonIsoSelectorPSet_cff import muonIsoSelectorPSet
muonId = muonSelectorPSet.clone()
muonId.dxy = 0.02
muonId.eta = 2.5
muonId.pt = 20 

process.Muons = cms.EDProducer(
    "KoMuonSelector",
    #version = cms.untracked.int32( -1 ),#TOP
    cut = cms.vstring(),
    isocut = cms.vstring(),
    muonLabel  = cms.InputTag("selectedPatMuonsPFlow"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    muonIdSelector = muonId,
    muonIsoSelector = muonIsoSelectorPSet,
)

process.patMuonFilter = cms.EDFilter("CandViewCountFilter",
  src = cms.InputTag('Muons'),
  minNumber = cms.uint32(1)
)

from PFAnalyses.CommonTools.Selectors.looseJetIdPSet_cff import looseJetIdPSet
myJetId = looseJetIdPSet.clone()
myJetId.verbose = False 

process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
process.hltHighLevel.HLTPaths = cms.vstring('HLT_Mu9')
process.MuonAna = cms.EDAnalyzer('MuonIsoAna',
    collectionLabel =  cms.InputTag('Muons'),
)

process.load("KoPFA.IsoAnalyzer.WFilter_cff")
process.WmunuMtCut.muonLabel = "Muons"
process.WmunuMtCut.minMt = 0 #70 
process.WmunuMtCut.maxdphi = 999 # 1.5 #999 #1.5

process.GenZmassFilter = cms.EDFilter('GenZmassFilter',
    genParticlesLabel = cms.InputTag('genParticles'),
    applyFilter = cms.untracked.bool( True ),
    decayMode = cms.untracked.vint32(13),
    min = cms.untracked.int32(0),
    max = cms.untracked.int32(999),
)

process.p = cms.Path(
#                     process.loadHistosFromRunInfo*
                     process.hltHighLevel*
                     process.GenZmassFilter*
                     process.Muons*
                     process.patMuonFilter*
                     process.WmunuMtCut*
                     process.VertexFilter*
                     process.MuonAna
                    )
