import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
#    fileNames = cms.untracked.vstring(
#        'file:../prod/RD/patTuple_muon.root'
#         'rfio:///castor/cern.ch/user/t/tjkim/SDMUONFILTER/July19th_v4/Run2010A-PromptReco-v4/patTuple_muon_22_0_Qie.root'
#    )
#)

#process.load("KoPFA.DiMuonAnalyzer.RD.patTuple_muon_cff")

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
muonId = muonSelectorPSet.clone()
muonId.dxy = 0.02
muonId.eta = 2.4
muonId.pt = 5 #20
from PFAnalyses.CommonTools.Selectors.muonIsoSelectorPSet_cff import muonIsoSelectorPSet
muonIso = muonIsoSelectorPSet.clone()

process.Muons1 = cms.EDProducer(
    "KoMuonSelector",
    cut = cms.vstring("pt","dxy","eta"),
    isocut = cms.vstring(),
    muonLabel  = cms.InputTag("selectedPatMuonsPFlow"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    muonIdSelector = muonId,
    muonIsoSelector = muonIso,

)

process.Muons2 = cms.EDProducer(
    "KoMuonSelector",
    cut = cms.vstring("pt","dxy","eta"),
    isocut = cms.vstring(),
    muonLabel  = cms.InputTag("selectedPatMuonsPFlow"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    muonIdSelector = muonId,
    muonIsoSelector = muonIso,

)

#process.patMuonFilter = cms.EDFilter("CandViewCountFilter",
#  src = cms.InputTag('Muons'),
#  minNumber = cms.uint32(1)
#)

from PFAnalyses.CommonTools.Selectors.looseJetIdPSet_cff import looseJetIdPSet
myJetId = looseJetIdPSet.clone()
myJetId.verbose = False 

process.DiMuon = cms.EDAnalyzer('DiMuonAnalyzer',
  muonLabel1 =  cms.InputTag('Muons1'),
  muonLabel2 =  cms.InputTag('Muons2'),
  metLabel =  cms.InputTag('patMETsPFlow'),
  jetLabel =  cms.InputTag('selectedPatJetsPFlow'),
  useEventCounter = cms.bool( False ),
  filters = cms.untracked.vstring(
                              'initialEvents',
                              'finalEvents'
                              ),
  looseJetId = myJetId, 
)

#process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
#process.hltHighLevel.HLTPaths = cms.vstring('HLT_Mu9')
#process.load("KoPFA.IsoAnalyzer.Isolation_cfi")
#process.MuonIso.collectionLabel = "Muons"
#process.MuonAna = cms.EDAnalyzer('MuonIsoAna',
#    collectionLabel =  cms.InputTag('Muons'),
#)

process.p = cms.Path(
#                     process.loadHistosFromRunInfo*
#                     process.hltHighLevel*
                     process.Muons1*
                     process.Muons2*
#                     process.patMuonFilter*
                     process.VertexFilter*
#                     process.MuonIso*
#                     process.MuonAna*
                     process.DiMuon
                    )

