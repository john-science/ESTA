
# This is a mapping from EIC to a tuple with three values:
#
#  * column for this value in the DTIM Link files (can take values from 0 to 25
#  * spatial surrogate keyword, so we know which spatial surrogate maps to this EIC
#  * EIC emis adjustment factor: 0.0 would drop the emissions, 1.0 leaves them unchanged,
#                                0.5 cuts the emissions in half, 2.0 doubles them, etc...
#
# NOTE: This mapping is meant for DTIM-like spatial surrogates

{71070111000000: (0, 'trips', 1.0),   # ('LDA', 'NCAT', 'STREX')
 71070611000000: (0, 'vmt', 1.0),     # ('LDA', 'NCAT', 'RUNEX')
 71070811000000: (0, 'vmt', 1.0),     # ('LDA', 'NCAT', 'RUNLOSS')
 71071011000000: (0, 'vmt', 1.0),     # ('LDA', 'NCAT', 'RESTLOSS')
 71071211000000: (0, 'vmt', 1.0),     # ('LDA', 'NCAT', 'HOTSOAK')
 71071411000000: (0, 'vmt', 1.0),     # ('LDA', 'NCAT', 'DIURN')
 71071802480000: (0, 'vmt', 1.0),     # ('LDA', 'NCAT', 'PMTW')
 71072054100000: (0, 'vmt', 1.0),     # ('LDA', 'NCAT', 'PMBW')
 71073111000000: (0, 'trips', 1.0),   # ('LDA', 'CAT', 'STREX')
 71073411000000: (0, 'vmt', 1.0),     # ('LDA', 'CAT', 'RUNEX')
 71073611000000: (0, 'vmt', 1.0),     # ('LDA', 'CAT', 'RUNLOSS')
 71073811000000: (0, 'vmt', 1.0),     # ('LDA', 'CAT', 'RESTLOSS')
 71074011000000: (0, 'vmt', 1.0),     # ('LDA', 'CAT', 'HOTSOAK')
 71074211000000: (0, 'vmt', 1.0),     # ('LDA', 'CAT', 'DIURN')
 71074402480000: (0, 'vmt', 1.0),     # ('LDA', 'CAT', 'PMTW')
 71074654100000: (0, 'vmt', 1.0),     # ('LDA', 'CAT', 'PMBW')
 71076412100000: (13, 'vmt', 1.0),    # ('LDA', 'DSL', 'RUNEX')
 71076602480000: (13, 'vmt', 1.0),    # ('LDA', 'DSL', 'PMTW')
 71076854100000: (13, 'vmt', 1.0),    # ('LDA', 'DSL', 'PMBW')
 72270111000000: (1, 'trips', 1.0),   # ('LDT1', 'NCAT', 'STREX')
 72270611000000: (1, 'vmt', 1.0),     # ('LDT1', 'NCAT', 'RUNEX')
 72270811000000: (1, 'vmt', 1.0),     # ('LDT1', 'NCAT', 'RUNLOSS')
 72271011000000: (1, 'vmt', 1.0),     # ('LDT1', 'NCAT', 'RESTLOSS')
 72271211000000: (1, 'vmt', 1.0),     # ('LDT1', 'NCAT', 'HOTSOAK')
 72271411000000: (1, 'vmt', 1.0),     # ('LDT1', 'NCAT', 'DIURN')
 72271802480000: (1, 'vmt', 1.0),     # ('LDT1', 'NCAT', 'PMTW')
 72272054100000: (1, 'vmt', 1.0),     # ('LDT1', 'NCAT', 'PMBW')
 72273111000000: (1, 'trips', 1.0),   # ('LDT1', 'CAT', 'STREX')
 72273411000000: (1, 'vmt', 1.0),     # ('LDT1', 'CAT', 'RUNEX')
 72273611000000: (1, 'vmt', 1.0),     # ('LDT1', 'CAT', 'RUNLOSS')
 72273811000000: (1, 'vmt', 1.0),     # ('LDT1', 'CAT', 'RESTLOSS')
 72274011000000: (1, 'vmt', 1.0),     # ('LDT1', 'CAT', 'HOTSOAK')
 72274211000000: (1, 'vmt', 1.0),     # ('LDT1', 'CAT', 'DIURN')
 72274402480000: (1, 'vmt', 1.0),     # ('LDT1', 'CAT', 'PMTW')
 72274654100000: (1, 'vmt', 1.0),     # ('LDT1', 'CAT', 'PMBW')
 72276412100000: (14, 'vmt', 1.0),    # ('LDT1', 'DSL', 'RUNEX')
 72276602480000: (14, 'vmt', 1.0),    # ('LDT1', 'DSL', 'PMTW')
 72276854100000: (14, 'vmt', 1.0),    # ('LDT1', 'DSL', 'PMBW')
 72370111000000: (2, 'trips', 1.0),   # ('LDT2', 'NCAT', 'STREX')
 72370611000000: (2, 'vmt', 1.0),     # ('LDT2', 'NCAT', 'RUNEX')
 72370811000000: (2, 'vmt', 1.0),     # ('LDT2', 'NCAT', 'RUNLOSS')
 72371011000000: (2, 'vmt', 1.0),     # ('LDT2', 'NCAT', 'RESTLOSS')
 72371211000000: (2, 'vmt', 1.0),     # ('LDT2', 'NCAT', 'HOTSOAK')
 72371411000000: (2, 'vmt', 1.0),     # ('LDT2', 'NCAT', 'DIURN')
 72371802480000: (2, 'vmt', 1.0),     # ('LDT2', 'NCAT', 'PMTW')
 72372054100000: (2, 'vmt', 1.0),     # ('LDT2', 'NCAT', 'PMBW')
 72373111000000: (2, 'trips', 1.0),   # ('LDT2', 'CAT', 'STREX')
 72373411000000: (2, 'vmt', 1.0),     # ('LDT2', 'CAT', 'RUNEX')
 72373611000000: (2, 'vmt', 1.0),     # ('LDT2', 'CAT', 'RUNLOSS')
 72373811000000: (2, 'vmt', 1.0),     # ('LDT2', 'CAT', 'RESTLOSS')
 72374011000000: (2, 'vmt', 1.0),     # ('LDT2', 'CAT', 'HOTSOAK')
 72374211000000: (2, 'vmt', 1.0),     # ('LDT2', 'CAT', 'DIURN')
 72374402480000: (2, 'vmt', 1.0),     # ('LDT2', 'CAT', 'PMTW')
 72374654100000: (2, 'vmt', 1.0),     # ('LDT2', 'CAT', 'PMBW')
 72376412100000: (15, 'vmt', 1.0),    # ('LDT2', 'DSL', 'RUNEX')
 72376602480000: (15, 'vmt', 1.0),    # ('LDT2', 'DSL', 'PMTW')
 72376854100000: (15, 'vmt', 1.0),    # ('LDT2', 'DSL', 'PMBW')
 72470111000000: (3, 'trips', 1.0),   # ('MDV', 'NCAT', 'STREX')
 72470611000000: (3, 'vmt', 1.0),     # ('MDV', 'NCAT', 'RUNEX')
 72470811000000: (3, 'vmt', 1.0),     # ('MDV', 'NCAT', 'RUNLOSS')
 72471011000000: (3, 'vmt', 1.0),     # ('MDV', 'NCAT', 'RESTLOSS')
 72471211000000: (3, 'vmt', 1.0),     # ('MDV', 'NCAT', 'HOTSOAK')
 72471411000000: (3, 'vmt', 1.0),     # ('MDV', 'NCAT', 'DIURN')
 72471802480000: (3, 'vmt', 1.0),     # ('MDV', 'NCAT', 'PMTW')
 72472054100000: (3, 'vmt', 1.0),     # ('MDV', 'NCAT', 'PMBW')
 72473111000000: (3, 'trips', 1.0),   # ('MDV', 'CAT', 'STREX')
 72473411000000: (3, 'vmt', 1.0),     # ('MDV', 'CAT', 'RUNEX')
 72473611000000: (3, 'vmt', 1.0),     # ('MDV', 'CAT', 'RUNLOSS')
 72473811000000: (3, 'vmt', 1.0),     # ('MDV', 'CAT', 'RESTLOSS')
 72474011000000: (3, 'vmt', 1.0),     # ('MDV', 'CAT', 'HOTSOAK')
 72474211000000: (3, 'vmt', 1.0),     # ('MDV', 'CAT', 'DIURN')
 72474402480000: (3, 'vmt', 1.0),     # ('MDV', 'CAT', 'PMTW')
 72474654100000: (3, 'vmt', 1.0),     # ('MDV', 'CAT', 'PMBW')
 72476412100000: (16, 'vmt', 1.0),    # ('MDV', 'DSL', 'RUNEX')
 72476602480000: (16, 'vmt', 1.0),    # ('MDV', 'DSL', 'PMTW')
 72476854100000: (16, 'vmt', 1.0),    # ('MDV', 'DSL', 'PMBW')
 73270111000000: (4, 'trips', 1.0),   # ('LHD1', 'NCAT', 'STREX')
 73270611000000: (4, 'vmt', 1.0),     # ('LHD1', 'NCAT', 'RUNEX')
 73270711000000: (4, 'trips', 1.0),   # ('LHD1', 'NCAT', 'IDLEX')
 73270811000000: (4, 'vmt', 1.0),     # ('LHD1', 'NCAT', 'RUNLOSS')
 73271011000000: (4, 'vmt', 1.0),     # ('LHD1', 'NCAT', 'RESTLOSS')
 73271211000000: (4, 'vmt', 1.0),     # ('LHD1', 'NCAT', 'HOTSOAK')
 73271411000000: (4, 'vmt', 1.0),     # ('LHD1', 'NCAT', 'DIURN')
 73271802480000: (4, 'vmt', 1.0),     # ('LHD1', 'NCAT', 'PMTW')
 73272054100000: (4, 'vmt', 1.0),     # ('LHD1', 'NCAT', 'PMBW')
 73273111000000: (4, 'trips', 1.0),   # ('LHD1', 'CAT', 'STREX')
 73273411000000: (4, 'vmt', 1.0),     # ('LHD1', 'CAT', 'RUNEX')
 73273511000000: (4, 'trips', 1.0),   # ('LHD1', 'CAT', 'IDLEX')
 73273611000000: (4, 'vmt', 1.0),     # ('LHD1', 'CAT', 'RUNLOSS')
 73273811000000: (4, 'vmt', 1.0),     # ('LHD1', 'CAT', 'RESTLOSS')
 73274011000000: (4, 'vmt', 1.0),     # ('LHD1', 'CAT', 'HOTSOAK')
 73274211000000: (4, 'vmt', 1.0),     # ('LHD1', 'CAT', 'DIURN')
 73274402480000: (4, 'vmt', 1.0),     # ('LHD1', 'CAT', 'PMTW')
 73274654100000: (4, 'vmt', 1.0),     # ('LHD1', 'CAT', 'PMBW')
 73370111000000: (5, 'trips', 1.0),   # ('LHD2', 'NCAT', 'STREX')
 73370611000000: (5, 'vmt', 1.0),     # ('LHD2', 'NCAT', 'RUNEX')
 73370711000000: (5, 'trips', 1.0),   # ('LHD2', 'NCAT', 'IDLEX')
 73370811000000: (5, 'vmt', 1.0),     # ('LHD2', 'NCAT', 'RUNLOSS')
 73371011000000: (5, 'vmt', 1.0),     # ('LHD2', 'NCAT', 'RESTLOSS')
 73371211000000: (5, 'vmt', 1.0),     # ('LHD2', 'NCAT', 'HOTSOAK')
 73371411000000: (5, 'vmt', 1.0),     # ('LHD2', 'NCAT', 'DIURN')
 73371802480000: (5, 'vmt', 1.0),     # ('LHD2', 'NCAT', 'PMTW')
 73372054100000: (5, 'vmt', 1.0),     # ('LHD2', 'NCAT', 'PMBW')
 73373111000000: (5, 'trips', 1.0),   # ('LHD2', 'CAT', 'STREX')
 73373411000000: (5, 'vmt', 1.0),     # ('LHD2', 'CAT', 'RUNEX')
 73373511000000: (5, 'trips', 1.0),   # ('LHD2', 'CAT', 'IDLEX')
 73373611000000: (5, 'vmt', 1.0),     # ('LHD2', 'CAT', 'RUNLOSS')
 73373811000000: (5, 'vmt', 1.0),     # ('LHD2', 'CAT', 'RESTLOSS')
 73374011000000: (5, 'vmt', 1.0),     # ('LHD2', 'CAT', 'HOTSOAK')
 73374211000000: (5, 'vmt', 1.0),     # ('LHD2', 'CAT', 'DIURN')
 73374402480000: (5, 'vmt', 1.0),     # ('LHD2', 'CAT', 'PMTW')
 73374654100000: (5, 'vmt', 1.0),     # ('LHD2', 'CAT', 'PMBW')
 73470111000000: (6, 'trips', 1.0),   # ('T6TS', 'NCAT', 'STREX')
 73470611000000: (6, 'vmt', 1.0),     # ('T6TS', 'NCAT', 'RUNEX')
 73470711000000: (6, 'trips', 1.0),   # ('T6TS', 'NCAT', 'IDLEX')
 73470811000000: (6, 'vmt', 1.0),     # ('T6TS', 'NCAT', 'RUNLOSS')
 73471011000000: (6, 'vmt', 1.0),     # ('T6TS', 'NCAT', 'RESTLOSS')
 73471211000000: (6, 'vmt', 1.0),     # ('T6TS', 'NCAT', 'HOTSOAK')
 73471411000000: (6, 'vmt', 1.0),     # ('T6TS', 'NCAT', 'DIURN')
 73471802480000: (6, 'vmt', 1.0),     # ('T6TS', 'NCAT', 'PMTW')
 73472054100000: (6, 'vmt', 1.0),     # ('T6TS', 'NCAT', 'PMBW')
 73473111000000: (6, 'trips', 1.0),   # ('T6TS', 'CAT', 'STREX')
 73473411000000: (6, 'vmt', 1.0),     # ('T6TS', 'CAT', 'RUNEX')
 73473511000000: (6, 'trips', 1.0),   # ('T6TS', 'CAT', 'IDLEX')
 73473611000000: (6, 'vmt', 1.0),     # ('T6TS', 'CAT', 'RUNLOSS')
 73473811000000: (6, 'vmt', 1.0),     # ('T6TS', 'CAT', 'RESTLOSS')
 73474011000000: (6, 'vmt', 1.0),     # ('T6TS', 'CAT', 'HOTSOAK')
 73474211000000: (6, 'vmt', 1.0),     # ('T6TS', 'CAT', 'DIURN')
 73474402480000: (6, 'vmt', 1.0),     # ('T6TS', 'CAT', 'PMTW')
 73474654100000: (6, 'vmt', 1.0),     # ('T6TS', 'CAT', 'PMBW')
 73670111000000: (7, 'trips', 1.0),   # ('T7IS', 'NCAT', 'STREX')
 73670611000000: (7, 'vmt', 1.0),     # ('T7IS', 'NCAT', 'RUNEX')
 73670811000000: (7, 'vmt', 1.0),     # ('T7IS', 'NCAT', 'RUNLOSS')
 73671011000000: (7, 'vmt', 1.0),     # ('T7IS', 'NCAT', 'RESTLOSS')
 73671211000000: (7, 'vmt', 1.0),     # ('T7IS', 'NCAT', 'HOTSOAK')
 73671411000000: (7, 'vmt', 1.0),     # ('T7IS', 'NCAT', 'DIURN')
 73671802480000: (7, 'vmt', 1.0),     # ('T7IS', 'NCAT', 'PMTW')
 73672054100000: (7, 'vmt', 1.0),     # ('T7IS', 'NCAT', 'PMBW')
 73673111000000: (7, 'trips', 1.0),   # ('T7IS', 'CAT', 'STREX')
 73673411000000: (7, 'vmt', 1.0),     # ('T7IS', 'CAT', 'RUNEX')
 73673611000000: (7, 'vmt', 1.0),     # ('T7IS', 'CAT', 'RUNLOSS')
 73673811000000: (7, 'vmt', 1.0),     # ('T7IS', 'CAT', 'RESTLOSS')
 73674011000000: (7, 'vmt', 1.0),     # ('T7IS', 'CAT', 'HOTSOAK')
 73674211000000: (7, 'vmt', 1.0),     # ('T7IS', 'CAT', 'DIURN')
 73674402480000: (7, 'vmt', 1.0),     # ('T7IS', 'CAT', 'PMTW')
 73674654100000: (7, 'vmt', 1.0),     # ('T7IS', 'CAT', 'PMBW')
 74276412100000: (18, 'vmt', 1.0),    # ('LHD1', 'DSL', 'RUNEX')
 74276512100000: (18, 'trips', 1.0),  # ('LHD1', 'DSL', 'IDLEX')
 74276602480000: (18, 'vmt', 1.0),    # ('LHD1', 'DSL', 'PMTW')
 74276854100000: (18, 'vmt', 1.0),    # ('LHD1', 'DSL', 'PMBW')
 74376412100000: (18, 'vmt', 1.0),    # ('LHD2', 'DSL', 'RUNEX')
 74376512100000: (18, 'trips', 1.0),  # ('LHD2', 'DSL', 'IDLEX')
 74376602480000: (18, 'vmt', 1.0),    # ('LHD2', 'DSL', 'PMTW')
 74376854100000: (18, 'vmt', 1.0),    # ('LHD2', 'DSL', 'PMBW')
 74476112107000: (19, 'trips', 1.0),  # ('T6 Ag', 'DSL', 'STREX')
 74476112107001: (19, 'trips', 1.0),  # ('T6 CAIRP heavy', 'DSL', 'STREX')
 74476112107004: (19, 'trips', 1.0),  # ('T6 CAIRP small', 'DSL', 'STREX')
 74476112107005: (19, 'trips', 1.0),  # ('T6 instate construction heavy', 'DSL', 'STREX')
 74476112107006: (19, 'trips', 1.0),  # ('T6 instate construction small', 'DSL', 'STREX')
 74476112107007: (19, 'trips', 1.0),  # ('T6 instate heavy', 'DSL', 'STREX')
 74476112107008: (19, 'trips', 1.0),  # ('T6 instate small', 'DSL', 'STREX')
 74476112107009: (19, 'trips', 1.0),  # ('T6 OOS heavy', 'DSL', 'STREX')
 74476112107010: (19, 'trips', 1.0),  # ('T6 OOS small', 'DSL', 'STREX')
 74476112107011: (19, 'trips', 1.0),  # ('T6 Public', 'DSL', 'STREX')
 74476112107012: (19, 'trips', 1.0),  # ('T6 utility', 'DSL', 'STREX')
 74476412107000: (19, 'vmt', 1.0),    # ('T6 Ag', 'DSL', 'RUNEX')
 74476412107001: (19, 'vmt', 1.0),    # ('T6 CAIRP heavy', 'DSL', 'RUNEX')
 74476412107004: (19, 'vmt', 1.0),    # ('T6 CAIRP small', 'DSL', 'RUNEX')
 74476412107005: (19, 'vmt', 1.0),    # ('T6 instate construction heavy', 'DSL', 'RUNEX')
 74476412107006: (19, 'vmt', 1.0),    # ('T6 instate construction small', 'DSL', 'RUNEX')
 74476412107007: (19, 'vmt', 1.0),    # ('T6 instate heavy', 'DSL', 'RUNEX')
 74476412107008: (19, 'vmt', 1.0),    # ('T6 instate small', 'DSL', 'RUNEX')
 74476412107009: (19, 'vmt', 1.0),    # ('T6 OOS heavy', 'DSL', 'RUNEX')
 74476412107010: (19, 'vmt', 1.0),    # ('T6 OOS small', 'DSL', 'RUNEX')
 74476412107011: (19, 'vmt', 1.0),    # ('T6 Public', 'DSL', 'RUNEX')
 74476412107012: (19, 'vmt', 1.0),    # ('T6 utility', 'DSL', 'RUNEX')
 74476512107000: (19, 'trips', 1.0),  # ('T6 Ag', 'DSL', 'IDLEX')
 74476512107001: (19, 'trips', 1.0),  # ('T6 CAIRP heavy', 'DSL', 'IDLEX')
 74476512107004: (19, 'trips', 1.0),  # ('T6 CAIRP small', 'DSL', 'IDLEX')
 74476512107005: (19, 'trips', 1.0),  # ('T6 instate construction heavy', 'DSL', 'IDLEX')
 74476512107006: (19, 'trips', 1.0),  # ('T6 instate construction small', 'DSL', 'IDLEX')
 74476512107007: (19, 'trips', 1.0),  # ('T6 instate heavy', 'DSL', 'IDLEX')
 74476512107008: (19, 'trips', 1.0),  # ('T6 instate small', 'DSL', 'IDLEX')
 74476512107009: (19, 'trips', 1.0),  # ('T6 OOS heavy', 'DSL', 'IDLEX')
 74476512107010: (19, 'trips', 1.0),  # ('T6 OOS small', 'DSL', 'IDLEX')
 74476512107011: (19, 'trips', 1.0),  # ('T6 Public', 'DSL', 'IDLEX')
 74476512107012: (19, 'trips', 1.0),  # ('T6 utility', 'DSL', 'IDLEX')
 74476602487000: (19, 'vmt', 1.0),    # ('T6 Ag', 'DSL', 'PMTW')
 74476602487001: (19, 'vmt', 1.0),    # ('T6 CAIRP heavy', 'DSL', 'PMTW')
 74476602487004: (19, 'vmt', 1.0),    # ('T6 CAIRP small', 'DSL', 'PMTW')
 74476602487005: (19, 'vmt', 1.0),    # ('T6 instate construction heavy', 'DSL', 'PMTW')
 74476602487006: (19, 'vmt', 1.0),    # ('T6 instate construction small', 'DSL', 'PMTW')
 74476602487007: (19, 'vmt', 1.0),    # ('T6 instate heavy', 'DSL', 'PMTW')
 74476602487008: (19, 'vmt', 1.0),    # ('T6 instate small', 'DSL', 'PMTW')
 74476602487009: (19, 'vmt', 1.0),    # ('T6 OOS heavy', 'DSL', 'PMTW')
 74476602487010: (19, 'vmt', 1.0),    # ('T6 OOS small', 'DSL', 'PMTW')
 74476602487011: (19, 'vmt', 1.0),    # ('T6 Public', 'DSL', 'PMTW')
 74476602487012: (19, 'vmt', 1.0),    # ('T6 utility', 'DSL', 'PMTW')
 74476854107000: (19, 'vmt', 1.0),    # ('T6 Ag', 'DSL', 'PMBW')
 74476854107001: (19, 'vmt', 1.0),    # ('T6 CAIRP heavy', 'DSL', 'PMBW')
 74476854107004: (19, 'vmt', 1.0),    # ('T6 CAIRP small', 'DSL', 'PMBW')
 74476854107005: (19, 'vmt', 1.0),    # ('T6 instate construction heavy', 'DSL', 'PMBW')
 74476854107006: (19, 'vmt', 1.0),    # ('T6 instate construction small', 'DSL', 'PMBW')
 74476854107007: (19, 'vmt', 1.0),    # ('T6 instate heavy', 'DSL', 'PMBW')
 74476854107008: (19, 'vmt', 1.0),    # ('T6 instate small', 'DSL', 'PMBW')
 74476854107009: (19, 'vmt', 1.0),    # ('T6 OOS heavy', 'DSL', 'PMBW')
 74476854107010: (19, 'vmt', 1.0),    # ('T6 OOS small', 'DSL', 'PMBW')
 74476854107011: (19, 'vmt', 1.0),    # ('T6 Public', 'DSL', 'PMBW')
 74476854107012: (19, 'vmt', 1.0),    # ('T6 utility', 'DSL', 'PMBW')
 74676112107013: (20, 'trips', 1.0),  # ('T7 Ag', 'DSL', 'STREX')
 74676112107016: (20, 'trips', 1.0),  # ('T7 CAIRP', 'DSL', 'STREX')
 74676112107017: (20, 'trips', 1.0),  # ('T7 CAIRP construction', 'DSL', 'STREX')
 74676112107018: (20, 'trips', 1.0),  # ('T7 NNOOS', 'DSL', 'STREX')
 74676112107019: (20, 'trips', 1.0),  # ('T7 NOOS', 'DSL', 'STREX')
 74676112107020: (20, 'trips', 1.0),  # ('T7 other port', 'DSL', 'STREX')
 74676112107021: (20, 'trips', 1.0),  # ('T7 POAK', 'DSL', 'STREX')
 74676112107024: (20, 'trips', 1.0),  # ('T7 POLA', 'DSL', 'STREX')
 74676112107025: (20, 'trips', 1.0),  # ('T7 Public', 'DSL', 'STREX')
 74676112107026: (20, 'trips', 1.0),  # ('T7 Single', 'DSL', 'STREX')
 74676112107027: (20, 'trips', 1.0),  # ('T7 single construction', 'DSL', 'STREX')
 74676112107028: (20, 'trips', 1.0),  # ('T7 SWCV', 'DSL', 'STREX')
 74676112107029: (20, 'trips', 1.0),  # ('T7 tractor', 'DSL', 'STREX')
 74676112107030: (20, 'trips', 1.0),  # ('T7 tractor construction', 'DSL', 'STREX')
 74676112107031: (20, 'trips', 1.0),  # ('T7 utility', 'DSL', 'STREX')
 74676112107032: (20, 'trips', 1.0),  # ('PTO', 'DSL', 'STREX')
 74676412107013: (20, 'vmt', 1.0),    # ('T7 Ag', 'DSL', 'RUNEX')
 74676412107016: (20, 'vmt', 1.0),    # ('T7 CAIRP', 'DSL', 'RUNEX')
 74676412107017: (20, 'vmt', 1.0),    # ('T7 CAIRP construction', 'DSL', 'RUNEX')
 74676412107018: (20, 'vmt', 1.0),    # ('T7 NNOOS', 'DSL', 'RUNEX')
 74676412107019: (20, 'vmt', 1.0),    # ('T7 NOOS', 'DSL', 'RUNEX')
 74676412107020: (20, 'vmt', 1.0),    # ('T7 other port', 'DSL', 'RUNEX')
 74676412107021: (20, 'vmt', 1.0),    # ('T7 POAK', 'DSL', 'RUNEX')
 74676412107024: (20, 'vmt', 1.0),    # ('T7 POLA', 'DSL', 'RUNEX')
 74676412107025: (20, 'vmt', 1.0),    # ('T7 Public', 'DSL', 'RUNEX')
 74676412107026: (20, 'vmt', 1.0),    # ('T7 Single', 'DSL', 'RUNEX')
 74676412107027: (20, 'vmt', 1.0),    # ('T7 single construction', 'DSL', 'RUNEX')
 74676412107028: (20, 'vmt', 1.0),    # ('T7 SWCV', 'DSL', 'RUNEX')
 74676412107029: (20, 'vmt', 1.0),    # ('T7 tractor', 'DSL', 'RUNEX')
 74676412107030: (20, 'vmt', 1.0),    # ('T7 tractor construction', 'DSL', 'RUNEX')
 74676412107031: (20, 'vmt', 1.0),    # ('T7 utility', 'DSL', 'RUNEX')
 74676412107032: (20, 'vmt', 1.0),    # ('PTO', 'DSL', 'RUNEX')
 74676512107013: (20, 'trips', 1.0),  # ('T7 Ag', 'DSL', 'IDLEX')
 74676512107016: (20, 'trips', 1.0),  # ('T7 CAIRP', 'DSL', 'IDLEX')
 74676512107017: (20, 'trips', 1.0),  # ('T7 CAIRP construction', 'DSL', 'IDLEX')
 74676512107018: (20, 'trips', 1.0),  # ('T7 NNOOS', 'DSL', 'IDLEX')
 74676512107019: (20, 'trips', 1.0),  # ('T7 NOOS', 'DSL', 'IDLEX')
 74676512107020: (20, 'trips', 1.0),  # ('T7 other port', 'DSL', 'IDLEX')
 74676512107021: (20, 'trips', 1.0),  # ('T7 POAK', 'DSL', 'IDLEX')
 74676512107024: (20, 'trips', 1.0),  # ('T7 POLA', 'DSL', 'IDLEX')
 74676512107025: (20, 'trips', 1.0),  # ('T7 Public', 'DSL', 'IDLEX')
 74676512107026: (20, 'trips', 1.0),  # ('T7 Single', 'DSL', 'IDLEX')
 74676512107027: (20, 'trips', 1.0),  # ('T7 single construction', 'DSL', 'IDLEX')
 74676512107028: (20, 'trips', 1.0),  # ('T7 SWCV', 'DSL', 'IDLEX')
 74676512107029: (20, 'trips', 1.0),  # ('T7 tractor', 'DSL', 'IDLEX')
 74676512107030: (20, 'trips', 1.0),  # ('T7 tractor construction', 'DSL', 'IDLEX')
 74676512107031: (20, 'trips', 1.0),  # ('T7 utility', 'DSL', 'IDLEX')
 74676512107032: (20, 'trips', 1.0),  # ('PTO', 'DSL', 'IDLEX')
 74676854107032: (20, 'vmt', 1.0),    # ('PTO', 'DSL', 'PMBW')
 74676602487032: (20, 'vmt', 1.0),    # ('PTO', 'DSL', 'PMTW')
 74676602487013: (20, 'vmt', 1.0),    # ('T7 Ag', 'DSL', 'PMTW')
 74676602487016: (20, 'vmt', 1.0),    # ('T7 CAIRP', 'DSL', 'PMTW')
 74676602487017: (20, 'vmt', 1.0),    # ('T7 CAIRP construction', 'DSL', 'PMTW')
 74676602487018: (20, 'vmt', 1.0),    # ('T7 NNOOS', 'DSL', 'PMTW')
 74676602487019: (20, 'vmt', 1.0),    # ('T7 NOOS', 'DSL', 'PMTW')
 74676602487020: (20, 'vmt', 1.0),    # ('T7 other port', 'DSL', 'PMTW')
 74676602487021: (20, 'vmt', 1.0),    # ('T7 POAK', 'DSL', 'PMTW')
 74676602487024: (20, 'vmt', 1.0),    # ('T7 POLA', 'DSL', 'PMTW')
 74676602487025: (20, 'vmt', 1.0),    # ('T7 Public', 'DSL', 'PMTW')
 74676602487026: (20, 'vmt', 1.0),    # ('T7 Single', 'DSL', 'PMTW')
 74676602487027: (20, 'vmt', 1.0),    # ('T7 single construction', 'DSL', 'PMTW')
 74676602487028: (20, 'vmt', 1.0),    # ('T7 SWCV', 'DSL', 'PMTW')
 74676602487029: (20, 'vmt', 1.0),    # ('T7 tractor', 'DSL', 'PMTW')
 74676602487030: (20, 'vmt', 1.0),    # ('T7 tractor construction', 'DSL', 'PMTW')
 74676602487031: (20, 'vmt', 1.0),    # ('T7 utility', 'DSL', 'PMTW')
 74676854107013: (20, 'vmt', 1.0),    # ('T7 Ag', 'DSL', 'PMBW')
 74676854107016: (20, 'vmt', 1.0),    # ('T7 CAIRP', 'DSL', 'PMBW')
 74676854107017: (20, 'vmt', 1.0),    # ('T7 CAIRP construction', 'DSL', 'PMBW')
 74676854107018: (20, 'vmt', 1.0),    # ('T7 NNOOS', 'DSL', 'PMBW')
 74676854107019: (20, 'vmt', 1.0),    # ('T7 NOOS', 'DSL', 'PMBW')
 74676854107020: (20, 'vmt', 1.0),    # ('T7 other port', 'DSL', 'PMBW')
 74676854107021: (20, 'vmt', 1.0),    # ('T7 POAK', 'DSL', 'PMBW')
 74676854107024: (20, 'vmt', 1.0),    # ('T7 POLA', 'DSL', 'PMBW')
 74676854107025: (20, 'vmt', 1.0),    # ('T7 Public', 'DSL', 'PMBW')
 74676854107026: (20, 'vmt', 1.0),    # ('T7 Single', 'DSL', 'PMBW')
 74676854107027: (20, 'vmt', 1.0),    # ('T7 single construction', 'DSL', 'PMBW')
 74676854107028: (20, 'vmt', 1.0),    # ('T7 SWCV', 'DSL', 'PMBW')
 74676854107029: (20, 'vmt', 1.0),    # ('T7 tractor', 'DSL', 'PMBW')
 74676854107030: (20, 'vmt', 1.0),    # ('T7 tractor construction', 'DSL', 'PMBW')
 74676854107031: (20, 'vmt', 1.0),    # ('T7 utility', 'DSL', 'PMBW')
 75070111000000: (10, 'trips', 1.0),  # ('MCY', 'NCAT', 'STREX')
 75070611000000: (10, 'vmt', 1.0),    # ('MCY', 'NCAT', 'RUNEX')
 75070811000000: (10, 'vmt', 1.0),    # ('MCY', 'NCAT', 'RUNLOSS')
 75071011000000: (10, 'vmt', 1.0),    # ('MCY', 'NCAT', 'RESTLOSS')
 75071211000000: (10, 'vmt', 1.0),    # ('MCY', 'NCAT', 'HOTSOAK')
 75071411000000: (10, 'vmt', 1.0),    # ('MCY', 'NCAT', 'DIURN')
 75071802480000: (10, 'vmt', 1.0),    # ('MCY', 'NCAT', 'PMTW')
 75072054100000: (10, 'vmt', 1.0),    # ('MCY', 'NCAT', 'PMBW')
 75073111000000: (10, 'trips', 1.0),  # ('MCY', 'CAT', 'STREX')
 75073411000000: (10, 'vmt', 1.0),    # ('MCY', 'CAT', 'RUNEX')
 75073611000000: (10, 'vmt', 1.0),    # ('MCY', 'CAT', 'RUNLOSS')
 75073811000000: (10, 'vmt', 1.0),    # ('MCY', 'CAT', 'RESTLOSS')
 75074011000000: (10, 'vmt', 1.0),    # ('MCY', 'CAT', 'HOTSOAK')
 75074211000000: (10, 'vmt', 1.0),    # ('MCY', 'CAT', 'DIURN')
 75074402480000: (10, 'vmt', 1.0),    # ('MCY', 'CAT', 'PMTW')
 75074654100000: (10, 'vmt', 1.0),    # ('MCY', 'CAT', 'PMBW')
 76076112100000: (22, 'trips', 1.0),  # ('UBUS', 'DSL', 'STREX')
 76076412100000: (22, 'vmt', 1.0),    # ('UBUS', 'DSL', 'RUNEX')
 76076602480000: (22, 'vmt', 1.0),    # ('UBUS', 'DSL', 'PMTW')
 76076854100000: (22, 'vmt', 1.0),    # ('UBUS', 'DSL', 'PMBW')
 76270111000000: (9, 'trips', 1.0),   # ('UBUS', 'NCAT', 'STREX')
 76270611000000: (9, 'vmt', 1.0),     # ('UBUS', 'NCAT', 'RUNEX')
 76270811000000: (9, 'vmt', 1.0),     # ('UBUS', 'NCAT', 'RUNLOSS')
 76271011000000: (9, 'vmt', 1.0),     # ('UBUS', 'NCAT', 'RESTLOSS')
 76271211000000: (9, 'vmt', 1.0),     # ('UBUS', 'NCAT', 'HOTSOAK')
 76271411000000: (9, 'vmt', 1.0),     # ('UBUS', 'NCAT', 'DIURN')
 76271802480000: (9, 'vmt', 1.0),     # ('UBUS', 'NCAT', 'PMTW')
 76272054100000: (9, 'vmt', 1.0),     # ('UBUS', 'NCAT', 'PMBW')
 76273111000000: (9, 'trips', 1.0),   # ('UBUS', 'CAT', 'STREX')
 76273411000000: (9, 'vmt', 1.0),     # ('UBUS', 'CAT', 'RUNEX')
 76273611000000: (9, 'vmt', 1.0),     # ('UBUS', 'CAT', 'RUNLOSS')
 76273811000000: (9, 'vmt', 1.0),     # ('UBUS', 'CAT', 'RESTLOSS')
 76274011000000: (9, 'vmt', 1.0),     # ('UBUS', 'CAT', 'HOTSOAK')
 76274211000000: (9, 'vmt', 1.0),     # ('UBUS', 'CAT', 'DIURN')
 76274402480000: (9, 'vmt', 1.0),     # ('UBUS', 'CAT', 'PMTW')
 76274654100000: (9, 'vmt', 1.0),     # ('UBUS', 'CAT', 'PMBW')
 77071011000000: (11, 'vmt', 1.0),    # ('SBUS', 'NCAT', 'RESTLOSS')
 77071411000000: (11, 'vmt', 1.0),    # ('SBUS', 'NCAT', 'DIURN')
 77071802480000: (11, 'vmt', 1.0),    # ('SBUS', 'NCAT', 'PMTW')
 77170111000000: (11, 'trips', 1.0),  # ('SBUS', 'NCAT', 'STREX')
 77170611000000: (11, 'vmt', 1.0),    # ('SBUS', 'NCAT', 'RUNEX')
 77170711000000: (11, 'trips', 1.0),  # ('SBUS', 'NCAT', 'IDLEX')
 77170811000000: (11, 'vmt', 1.0),    # ('SBUS', 'NCAT', 'RUNLOSS')
 77171211000000: (11, 'vmt', 1.0),    # ('SBUS', 'NCAT', 'HOTSOAK')
 77172054100000: (11, 'vmt', 1.0),    # ('SBUS', 'NCAT', 'PMBW')
 77173111000000: (11, 'trips', 1.0),  # ('SBUS', 'CAT', 'STREX')
 77173411000000: (11, 'vmt', 1.0),    # ('SBUS', 'CAT', 'RUNEX')
 77173511000000: (11, 'trips', 1.0),  # ('SBUS', 'CAT', 'IDLEX')
 77173611000000: (11, 'vmt', 1.0),    # ('SBUS', 'CAT', 'RUNLOSS')
 77173811000000: (11, 'vmt', 1.0),    # ('SBUS', 'CAT', 'RESTLOSS')
 77174011000000: (11, 'vmt', 1.0),    # ('SBUS', 'CAT', 'HOTSOAK')
 77174211000000: (11, 'vmt', 1.0),    # ('SBUS', 'CAT', 'DIURN')
 77174402480000: (11, 'vmt', 1.0),    # ('SBUS', 'CAT', 'PMTW')
 77174654100000: (11, 'vmt', 1.0),    # ('SBUS', 'CAT', 'PMBW')
 77276112100000: (24, 'trips', 1.0),  # ('SBUS', 'DSL', 'STREX')
 77276412100000: (24, 'vmt', 1.0),    # ('SBUS', 'DSL', 'RUNEX')
 77276512100000: (24, 'trips', 1.0),  # ('SBUS', 'DSL', 'IDLEX')
 77276602480000: (24, 'vmt', 1.0),    # ('SBUS', 'DSL', 'PMTW')
 77276854100000: (24, 'vmt', 1.0),    # ('SBUS', 'DSL', 'PMBW')
 77671411000000: (8, 'vmt', 1.0),     # ('OBUS', 'NCAT', 'DIURN')
 77671802480000: (8, 'vmt', 1.0),     # ('OBUS', 'NCAT', 'PMTW')
 77672054100000: (8, 'vmt', 1.0),     # ('OBUS', 'NCAT', 'PMBW')
 77770111000000: (8, 'trips', 1.0),   # ('OBUS', 'NCAT', 'STREX')
 77770611000000: (8, 'vmt', 1.0),     # ('OBUS', 'NCAT', 'RUNEX')
 77770711000000: (8, 'trips', 1.0),   # ('OBUS', 'NCAT', 'IDLEX')
 77770811000000: (8, 'vmt', 1.0),     # ('OBUS', 'NCAT', 'RUNLOSS')
 77771011000000: (8, 'vmt', 1.0),     # ('OBUS', 'NCAT', 'RESTLOSS')
 77771211000000: (8, 'vmt', 1.0),     # ('OBUS', 'NCAT', 'HOTSOAK')
 77773111000000: (8, 'trips', 1.0),   # ('OBUS', 'CAT', 'STREX')
 77773411000000: (8, 'vmt', 1.0),     # ('OBUS', 'CAT', 'RUNEX')
 77773511000000: (8, 'trips', 1.0),   # ('OBUS', 'CAT', 'IDLEX')
 77773611000000: (8, 'vmt', 1.0),     # ('OBUS', 'CAT', 'RUNLOSS')
 77773811000000: (8, 'vmt', 1.0),     # ('OBUS', 'CAT', 'RESTLOSS')
 77774011000000: (8, 'vmt', 1.0),     # ('OBUS', 'CAT', 'HOTSOAK')
 77774211000000: (8, 'vmt', 1.0),     # ('OBUS', 'CAT', 'DIURN')
 77774402480000: (8, 'vmt', 1.0),     # ('OBUS', 'CAT', 'PMTW')
 77774654100000: (8, 'vmt', 1.0),     # ('OBUS', 'CAT', 'PMBW')
 77876112100000: (20, 'trips', 1.0),  # ('Motor Coach', 'DSL', 'STREX')
 77876412100000: (20, 'vmt', 1.0),    # ('Motor Coach', 'DSL', 'RUNEX')
 77876512100000: (20, 'trips', 1.0),  # ('Motor Coach', 'DSL', 'IDLEX')
 77876602480000: (20, 'vmt', 1.0),    # ('Motor Coach', 'DSL', 'PMTW')
 77876854100000: (20, 'vmt', 1.0),    # ('Motor Coach', 'DSL', 'PMBW')
 77976112100000: (21, 'trips', 1.0),  # ('All Other Buses', 'DSL', 'STREX')
 77976412100000: (21, 'vmt', 1.0),    # ('All Other Buses', 'DSL', 'RUNEX')
 77976512100000: (21, 'trips', 1.0),  # ('All Other Buses', 'DSL', 'IDLEX')
 77976602480000: (21, 'vmt', 1.0),    # ('All Other Buses', 'DSL', 'PMTW')
 77976854100000: (21, 'vmt', 1.0),    # ('All Other Buses', 'DSL', 'PMBW')
 78070111000000: (12, 'trips', 1.0),  # ('MH', 'NCAT', 'STREX')
 78070611000000: (12, 'vmt', 1.0),    # ('MH', 'NCAT', 'RUNEX')
 78070811000000: (12, 'vmt', 1.0),    # ('MH', 'NCAT', 'RUNLOSS')
 78071011000000: (12, 'vmt', 1.0),    # ('MH', 'NCAT', 'RESTLOSS')
 78071211000000: (12, 'vmt', 1.0),    # ('MH', 'NCAT', 'HOTSOAK')
 78071411000000: (12, 'vmt', 1.0),    # ('MH', 'NCAT', 'DIURN')
 78071802480000: (12, 'vmt', 1.0),    # ('MH', 'NCAT', 'PMTW')
 78072054100000: (12, 'vmt', 1.0),    # ('MH', 'NCAT', 'PMBW')
 78073111000000: (12, 'trips', 1.0),  # ('MH', 'CAT', 'STREX')
 78073411000000: (12, 'vmt', 1.0),    # ('MH', 'CAT', 'RUNEX')
 78073611000000: (12, 'vmt', 1.0),    # ('MH', 'CAT', 'RUNLOSS')
 78073811000000: (12, 'vmt', 1.0),    # ('MH', 'CAT', 'RESTLOSS')
 78074011000000: (12, 'vmt', 1.0),    # ('MH', 'CAT', 'HOTSOAK')
 78074211000000: (12, 'vmt', 1.0),    # ('MH', 'CAT', 'DIURN')
 78074402480000: (12, 'vmt', 1.0),    # ('MH', 'CAT', 'PMTW')
 78074654100000: (12, 'vmt', 1.0),    # ('MH', 'CAT', 'PMBW')
 78076412100000: (25, 'vmt', 1.0),    # ('MH', 'DSL', 'RUNEX')
 78076602480000: (25, 'vmt', 1.0),    # ('MH', 'DSL', 'PMTW')
 78076854100000: (25, 'vmt', 1.0)}    # ('MH', 'DSL', 'PMBW')
 
