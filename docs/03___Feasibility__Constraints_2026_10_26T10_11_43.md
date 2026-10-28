
# 03 — Feasibility & Constraints

**Project:** Hyperlocal Disaster-to-Commerce (D2C) Mesh Platform
**Pillar:** 🌪️ Resilience Communities
**Pilot Area:** Nakhon Pathom & Bangkok Perimeter
**Date:** 2026-10-26
**Stage Owner:** sommai

---

## 1. Feasibility Assessment

### 1.1 Technical Feasibility — CONDITIONAL GO ⚠️

The D2C Mesh integrates three technically distinct tracks — hyperlocal flood prediction, vehicle-aware routing, and e-voucher disbursement — each with different maturity profiles.

**Track A — Hyperlocal Flood Early Warning (AI Layer)**

- **Data availability:** TMD weather radar, HII's 4,000+ telemetry stations, GISTDA THEOS-2 satellite imagery (50 cm resolution), RID canal-level data, and Traffy Fondue crowdsourced reports all exist as operational systems [source: Stage 2 market research]. However, **none offers a standardized open API** — each agency uses proprietary formats and access protocols [source: Stage 2 market research]. The newly launched One Map Water dashboard (Sep 2026) consolidates visualization but does not expose a developer-facing API [source: Stage 2 market research].
- **AI model feasibility:** The Mott MacDonald/UK FCDO Bangkok pilot proved real-time stormwater flood forecasting is technically achievable using rain radar + IoT sensors + ML nowcasting [source: Stage 2 market research]. KMITL's AIoT system demonstrated YOLOv10 + LSTM integration for flash-flood detection [source: Stage 2 market research]. Both remain localized prototypes, confirming the technical approach is sound but unproven at the scale required for Nakhon Pathom province.
- **Elevation data gap:** Centimeter-resolution street-level flood depth estimation requires a high-resolution Digital Elevation Model (DEM). Thailand's publicly available DEMs are typically 30m SRTM resolution. LiDAR-derived DEMs for Nakhon Pathom would need to be sourced from GISTDA or surveyed — a significant data acquisition dependency [source: assumption].

**Track B — Vehicle-Aware Dynamic Routing**

- **Current state:** No existing Thai platform — including Google Maps and Longdo Map — integrates real-time flood data into routing algorithms [source: Stage 2 market research]. FloodMapp + Waze integration (Norfolk, Virginia) proves the concept is implementable using GIS layering of flood models onto road networks [source: Stage 2 market research].
- **Technical approach:** Fuse flood depth predictions from Track A with OpenStreetMap road graph data and vehicle-type clearance thresholds (sedan: ~15 cm, motorcycle: ~20 cm, pickup/SUV: ~40 cm). Standard graph routing algorithms (Dijkstra/A*) with dynamic edge weight modification are well-established [source: web research].
- **Key constraint:** Real-time routing requires sub-second API response times, demanding pre-computed flood scenarios cached at the edge rather than on-the-fly model inference [source: assumption].

**Track C — E-Voucher System**

- **PromptPay integration:** Thailand's PromptPay infrastructure processes 74 million transactions daily with 83 million registered users and near-universal merchant QR acceptance [source: Stage 2 market research]. This eliminates the merchant-onboarding barrier.
- **Krungthai Open API:** Krungthai Bank's developer portal offers App-to-App authentication enabling third-party integration with Paotang accounts [source: Stage 2 market research]. This is the primary technical integration pathway.
- **Voucher logic:** Geo-targeted voucher activation triggered by flood alerts, with redemption restricted to pre-registered Micro-Relief Station merchants within the affected area. The Khon La Khrueng co-payment model (60% subsidy, 200 baht/day cap, 1,000 baht/month) provides a proven architectural template [source: Stage 2 market research].

**Overall Technical Verdict:** CONDITIONAL GO — Each track has proven precedents and available infrastructure, but the integration of all three into a single pipeline is unprecedented. The primary technical risks are API access negotiation with government agencies and offline resilience during floods.

---

### 1.2 Resource & Capability Feasibility — CONDITIONAL GO ⚠️

| Capability Required | Availability | Gap Assessment |
|---|---|---|
| AI/ML engineering (flood prediction models) | Available via hackathon team + cloud ML services | Need domain expertise in hydrology/meteorology [source: assumption] |
| Mobile app development (React Native / Flutter) | Standard skill set, widely available | Offline-first architecture requires specialized expertise [source: assumption] |
| PromptPay/Krungthai API integration | Krungthai Open API portal publicly available [source: Stage 2 market research] | Requires developer registration and sandbox testing; partnership negotiation timeline unknown [source: assumption] |
| GIS/mapping expertise | OpenStreetMap + QGIS ecosystem available | LiDAR DEM processing is specialized [source: assumption] |
| Government API access (TMD, HII, RID, GISTDA) | APIs exist but not standardized [source: Stage 2 market research] | Requires individual MOU/data-sharing agreements with each agency [source: Stage 2 market research] |
| Community coordinator network | อสม. (Village Health Volunteers) network exists nationally [source: web research] | Must be recruited and trained for Micro-Relief Station roles [source: assumption] |
| Regulatory/compliance advisory | Required for BOT e-money licensing navigation | External legal counsel needed [source: assumption] |

**Resource Verdict:** CONDITIONAL GO — Core technical skills are available; the critical gaps are domain expertise (hydrology), regulatory navigation, and government relationship management.

---

### 1.3 Timeline Feasibility — CONDITIONAL GO ⚠️

| Phase | Duration | Key Milestones |
|---|---|---|
| **Phase 0: Foundation** | Months 1–3 | API access agreements with TMD/HII; Krungthai sandbox access; DEM data acquisition; core team formation |
| **Phase 1: MVP — Warning Track** | Months 3–6 | Flood prediction model for Nakhon Pathom trained on historical data; basic alert system (push notification + SMS) |
| **Phase 2: MVP — Routing + E-Voucher** | Months 6–9 | Vehicle-aware routing prototype; e-voucher prototype on Krungthai sandbox; Micro-Relief Station merchant onboarding |
| **Phase 3: Integrated Pilot** | Months 9–12 | End-to-end warning-to-action pipeline tested; pilot with 500–1,000 households in Nakhon Pathom |
| **Phase 4: Year-Round Mode** | Months 12–18 | อปท. welfare voucher integration for non-flood season sustainability |

**Timeline Risks:**
- Government API access agreements may take 3–6 months to formalize — this is the critical path item [source: assumption]
- Thailand's monsoon season (May–October) constrains live flood-testing windows [source: web research]
- BOT regulatory pathway (direct license vs. banking partner route) adds 3–12 months depending on approach [source: web research]

**Timeline Verdict:** CONDITIONAL GO — 12-month pilot is achievable if API access agreements begin immediately and the banking partnership route is pursued (avoiding direct e-money licensing). The monsoon seasonality means the integrated pilot should target the May–October 2028 wet season for live testing [source: assumption].

---

### 1.4 Budget/Cost Feasibility — CONDITIONAL GO ⚠️

| Cost Category | Estimated Range (12 months) | Notes |
|---|---|---|
| Cloud infrastructure (AWS) | ฿600,000 – ฿1,200,000 | ML training, API hosting, edge caching, database [source: assumption] |
| Development team (5–7 FTE) | ฿3,000,000 – ฿5,000,000 | Full-stack, ML, GIS, mobile [source: assumption] |
| LiDAR DEM data acquisition | ฿500,000 – ฿1,500,000 | If not available from GISTDA; could be ฿0 via government partnership [source: assumption] |
| Legal/regulatory advisory | ฿300,000 – ฿600,000 | BOT compliance, data-sharing agreements [source: assumption] |
| Community coordinator training | ฿200,000 – ฿400,000 | อสม. training, Micro-Relief Station setup [source: assumption] |
| IoT sensors (supplementary) | ฿300,000 – ฿800,000 | Optional: low-cost water-level sensors to fill coverage gaps [source: assumption] |
| **Total estimated range** | **฿4,900,000 – ฿9,500,000** | (~$140,000 – $270,000 USD) |

**Funding pathways:**
- DEPA (Digital Economy Promotion Agency) innovation grants [source: web research]
- NSTDA/NECTEC disaster-tech funding programs [source: assumption]
- International: UNDP, World Bank Digital Development grants, UK FCDO (already funding Bangkok flood pilots) [source: Stage 2 market research]
- Hackathon prize + accelerator funding as seed [source: assumption]

**Budget Verdict:** CONDITIONAL GO — Budget is realistic for a government-backed pilot. The อปท. welfare integration creates a revenue pathway (per-transaction or SaaS fee to municipalities) for post-pilot sustainability [source: assumption].

---

## 2. Constraint Register (Hard Constraints)

| # | Constraint | Type | Source | Impact |
|---|---|---|---|---|
| C1 | **BOT e-money licensing** — Any entity operating e-voucher/payment services must be licensed under Payment Systems Act B.E. 2560 or partner with a licensed entity | Regulatory | BOT Payment Systems Act [source: web research] | Blocks e-voucher track entirely if unresolved |
| C2 | **KYC requirements** — BOT mandates Know Your Customer verification for e-Money service activation, including identity verification and true identity confirmation | Regulatory | BOT Circular SorNorChor. 1/2563 [source: web research] | All voucher recipients must be identity-verified |
| C3 | **Government data access** — TMD, HII, RID, and GISTDA data are not available through standardized open APIs; require individual agency agreements | Institutional | Stage 2 market research [source: Stage 2 market research] | Blocks flood prediction track until resolved |
| C4 | **Monsoon seasonality** — Live flood testing limited to May–October wet season | Environmental | Thailand climate patterns [source: web research] | Constrains validation timeline |
| C5 | **Network degradation during floods** — Mobile networks experience disruption in flooded areas precisely when warnings are most needed | Infrastructure | True Corp flood response reports [source: web research]; Hurricane Katrina studies showing 26% subnet unreachability [source: web research] | Core functionality must work offline |
| C6 | **Digital literacy variance** — 41.90% of public receives disaster info via community leaders rather than apps | Behavioral | Thailand State Audit Office [source: Stage 2 market research] | Cannot rely solely on smartphone delivery |
| C7 | **PromptPay dependency** — All voucher transactions route through PromptPay, creating single-point-of-failure on National ITMX infrastructure | Technical | Architecture design [source: assumption] | System unusable if PromptPay is down during disaster |

---

## 3. Supporting Agent Input

### 3.1 aidlc-compliance-agent: BOT E-Money Licensing Navigation

**Regulatory Assessment:**

The Payment Systems Act B.E. 2560 (2017) grants the Bank of Thailand supervisory authority over all designated payment services. Under this framework, operating an e-voucher system constitutes a "payment facilitating service" requiring either [source: web research]:

1. **Direct licensing** — Applying for an e-money license from the Minister of Finance via BOT. This requires demonstrating capital adequacy, operational readiness, KYC/AML compliance systems, and consumer protection measures. Timeline: 6–12 months minimum. BOT requires operations to begin within one year of license issuance.
2. **Banking partnership route (RECOMMENDED)** — Partnering with a licensed financial institution that already holds the required licenses. The D2C Mesh operates as a technology platform layer while the licensed partner handles the regulated payment/e-money functions.

**Recommended Compliance Strategy:**

**Partner with Krungthai Bank** as the regulated financial services provider. Rationale:
- Krungthai already operates the Paotang app serving 40 million users under government welfare programs [source: Stage 2 market research]
- Krungthai's Open API portal explicitly enables third-party App-to-App integration [source: Stage 2 market research]
- Krungthai already holds the BOT licenses required for payment facilitating and e-money services [source: web research]
- The Khon La Khrueng co-payment model (welfare funds → Paotang wallet → merchant QR redemption) is architecturally identical to the D2C Mesh e-voucher flow [source: Stage 2 market research]
- Government consolidation toward PromptPay as the universal welfare rail (new welfare card holders must link PromptPay accounts as of Sep 2026) [source: Stage 2 market research] — aligning with this trend strengthens regulatory positioning

**KYC Compliance:**
- Leverage Thailand's existing citizen ID infrastructure linked to PromptPay (registration uses citizen ID or phone number) [source: web research]
- For disaster situations requiring rapid enrollment, BOT regulations permit simplified KYC for lower-value e-money accounts [source: web research]
- Pre-registration during non-flood season (via อปท. welfare enrollment) builds the verified user base before emergencies occur [source: assumption]

**Compliance Verdict:** CONDITIONAL GO — The banking partnership route with Krungthai Bank eliminates the need for independent e-money licensing and provides an architecturally proven integration pathway. The primary residual risk is Krungthai's willingness and commercial terms for the partnership [source: assumption].

---

### 3.2 aidlc-aws-platform-agent: Offline-First Architecture for Flood Resilience

**Problem Statement:**
Thailand's mobile internet penetration reached 76% at end of 2025 [source: web research], but flood conditions degrade connectivity precisely when the D2C Mesh is most critical. True Corporation documented emergency network mobilization during the August 2026 Nan/Phayao floods [source: web research], confirming that base station flooding, power outages, and fiber cuts create connectivity dead zones. Research confirms this is a global pattern — during Hurricane Katrina, 26% of subnets became unreachable [source: web research].

**Recommended Offline-First Architecture:**

**Layer 1 — Progressive Web App (PWA) with Local-First Data**
- Service workers cache the last-known flood map, routing data, and Micro-Relief Station locations for offline access
- AWS Amplify DataStore provides local-first data with automatic cloud sync when connectivity resumes
- Pre-download flood scenario data for the user's registered location during normal conditions
- Estimated offline cache size: ~50 MB per user (map tiles + flood scenarios + merchant directory) [source: assumption]

**Layer 2 — SMS/USSD Fallback Gateway**
- Thailand's Cell Broadcast system (operated by NBTC) can push alerts to all devices in a geographic area without requiring internet, data plans, or app installation [source: web research]
- Integrate with AIS, True, and DTAC SMS gateways for individual notifications
- USSD-based voucher activation (dial code → receive voucher code → redeem at merchant via USSD or verbal relay)
- AWS SNS (Simple Notification Service) as the SMS orchestration layer [source: assumption]

**Layer 3 — Edge Computing for Continued Prediction**
- Deploy AWS IoT Greengrass on edge devices at Micro-Relief Stations to run lightweight flood prediction models locally
- Edge devices continue processing nearby sensor data and generating alerts even when cloud connectivity is lost
- Sync predictions to the cloud when connectivity resumes
- Supplementary low-cost LoRaWAN water-level sensors (range: 5–15 km) can transmit to edge devices independent of cellular networks [source: web research]

**Layer 4 — Mesh Communication Network**
- Wi-Fi Direct / Bluetooth mesh between smartphones at Micro-Relief Stations as a local communication relay
- Community coordinators' devices act as mesh nodes, relaying alerts to nearby residents
- Consider integration with existing Village Public Address (หอกระจายข่าว) loudspeaker systems for mass alerts without any digital device required [source: assumption]

**Architecture Verdict:** The offline-first stack is technically achievable using proven AWS services (Amplify DataStore, IoT Greengrass, SNS, Lambda@Edge) combined with Thailand's existing telco infrastructure (Cell Broadcast, SMS). The key design principle is **graceful degradation**: full experience online → cached map + SMS alerts on poor connectivity → Cell Broadcast + loudspeaker + community relay with no connectivity [source: assumption].

---

## 4. RAID Log

### 4.1 Risks

| ID | Risk | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | Government agencies refuse or delay API access to flood data (TMD, HII, RID, GISTDA) | High | Critical | Begin engagement via DEPA or NSTDA as intermediary; use publicly scraped data from ThaiWater portal as interim fallback [source: assumption] | Project Lead |
| R2 | Krungthai Bank declines partnership or imposes prohibitive commercial terms | Medium | Critical | Prepare alternative banking partner pipeline (Government Savings Bank, Bank for Agriculture — both government banks with welfare mandates) [source: assumption] | Business Lead |
| R3 | Flood prediction model accuracy insufficient for street-level warnings | Medium | High | Start with neighborhood-level (tambon) warnings rather than street-level; iterate toward higher resolution with more data [source: assumption] | ML Lead |
| R4 | Network infrastructure fails during major flood event, rendering digital channels unusable | High | High | Offline-first architecture (Layer 1–4 above); community relay mechanisms; pre-positioned printed QR voucher cards at Micro-Relief Stations [source: assumption] | Platform Lead |
| R5 | Low user adoption due to digital literacy barriers (41.90% rely on community leaders) [source: Stage 2 market research] | Medium | High | Dual-channel strategy: digital app for tech-savvy users + community coordinator relay for non-digital users; year-round อปท. welfare usage builds familiarity before flood season [source: assumption] | Community Lead |
| R6 | Regulatory environment changes — BOT tightens e-money or payment facilitating regulations | Low | Critical | Banking partnership route insulates platform from direct regulatory exposure; maintain compliance monitoring [source: assumption] | Compliance Lead |
| R7 | Seasonal engagement drop — users and merchants disengage between flood seasons | Medium | Medium | Year-round อปท. welfare voucher distribution maintains continuous platform usage [source: Stage 2 market research] | Product Lead |

### 4.2 Assumptions

| ID | Assumption | Criticality | Validation Method | Status |
|---|---|---|---|---|
| A1 | Krungthai Bank's Open API can support the voucher activation/redemption workflow required by D2C Mesh | High | Sandbox testing via developers.krungthai.com [source: Stage 2 market research] | [status: unconfirmed] |
| A2 | TMD/HII/RID data can be accessed at sufficient frequency (≤15 min intervals) for real-time flood prediction | High | Formal API capability assessment with each agency | [status: unconfirmed] |
| A3 | A high-resolution DEM for Nakhon Pathom is available from GISTDA or can be acquired within budget | Medium | Direct inquiry to GISTDA | [status: unconfirmed] |
| A4 | Local SMEs in Nakhon Pathom will register as Micro-Relief Stations given the year-round welfare commerce incentive | Medium | Field survey during Phase 0 | [status: unconfirmed] |
| A5 | อปท. municipalities are willing and legally able to route welfare budgets through a third-party digital platform | High | Legal review of Decentralization Act 1999 + pilot engagement with Nakhon Pathom อปท. | [status: unconfirmed] |
| A6 | The อสม. (Village Health Volunteer) network can be leveraged as community coordinators for the relay mechanism | Medium | Engagement with Nakhon Pathom Provincial Health Office | [status: unconfirmed] |
| A7 | Pre-computed flood scenarios can adequately substitute for real-time model inference for routing purposes | Medium | Technical benchmarking during Phase 1 | [status: unconfirmed] |
| A8 | Cloud infrastructure costs remain within ฿600K–฿1.2M/year range at pilot scale | Low | AWS cost estimation using pilot workload profile | [status: unconfirmed] |

### 4.3 Issues (Current)

| ID | Issue | Severity | Resolution Path |
|---|---|---|---|
| I1 | No standardized open API exists across Thai flood monitoring agencies — One Map Water consolidates display only, not developer access | High | Escalate through DEPA/NSTDA; propose standardized API specification as a policy recommendation from the hackathon [source: Stage 2 market research] |
| I2 | 60.66% of existing warning stations are located outside officially designated risk zones [source: Stage 2 market research] — sensor placement may not align with platform needs | Medium | Supplement with low-cost IoT sensors at Micro-Relief Stations; use AI to interpolate from available stations |
| I3 | Traffy Fondue crowdsourced data suffers from label categorization inaccuracies [source: Stage 2 market research] | Low | Apply NLP/classification layer to clean Traffy Fondue inputs before feeding into prediction model |

### 4.4 Dependencies

| ID | Dependency | Type | Lead Time | Status |
|---|---|---|---|---|
| D1 | MOU with TMD for radar and forecast data access | External/Government | 3–6 months [source: assumption] | Not started |
| D2 | MOU with HII for telemetry station data access | External/Government | 3–6 months [source: assumption] | Not started |
| D3 | MOU with RID for canal and reservoir data access | External/Government | 3–6 months [source: assumption] | Not started |
| D4 | Krungthai Bank partnership agreement + sandbox access | External/Banking | 2–4 months [source: assumption] | Not started |
| D5 | High-resolution DEM data for Nakhon Pathom province | External/GISTDA | 1–3 months [source: assumption] | Not started |
| D6 | AWS credits or cloud funding for pilot infrastructure | External/Funding | 1–2 months [source: assumption] | Not started |
| D7 | อปท. Nakhon Pathom engagement for welfare voucher pilot | External/Government | 3–6 months [source: assumption] | Not started |
| D8 | อสม. network engagement for community relay mechanism | External/Health Ministry | 2–4 months [source: assumption] | Not started |

---

## 5. Overall Feasibility Verdict

**CONDITIONAL GO** 🟡

**Confidence Level:** 70%

**Rationale:**

The D2C Mesh platform is technically feasible and strategically well-positioned — every individual component has proven precedents (AI flood prediction, PromptPay payment rails, Paotang welfare distribution model, offline-first mobile architecture). Thailand's mature digital payment infrastructure uniquely enables the e-voucher track in ways that would be impossible in most disaster-prone countries [source: Stage 2 market research].

**The conditions for GO are:**

1. **Secure Krungthai Bank partnership** (or alternative government bank) within 3 months — this resolves the BOT e-money licensing constraint (C1) and provides the payment integration pathway. This is the single most critical dependency.
2. **Obtain at least one government data MOU** (TMD or HII) within 4 months — without flood data access, Track A cannot function. Begin immediately through DEPA/NSTDA facilitation.
3. **Validate high-resolution DEM availability** for Nakhon Pathom within 2 months — if unavailable, the platform degrades to neighborhood-level rather than street-level prediction accuracy.

**If any condition is not met within the stated timeframe**, the project should pivot:
- If Krungthai declines → approach GSB or BAAC as alternatives
- If no government data MOU → pivot to a crowdsource-only data model (Traffy Fondue + community-reported flood levels) with significantly reduced prediction accuracy
- If DEM unavailable → reduce scope to tambon (sub-district) level warnings; still valuable but less differentiated

The strongest de-risking factor is the **year-round อปท. welfare voucher model** — even if the flood prediction track faces delays, the e-voucher commerce platform can begin generating value for municipalities and merchants immediately, building the user base and merchant network ahead of the flood prediction integration [source: Stage 2 market research].
