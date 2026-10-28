# System Requirements & Feature Specifications

**Project Name:** PromptMesh (Hyperlocal D2C Mesh)  
**Core Mission:** เชื่อมต่อวงจรบรรเทาสาธารณภัยสู่เศรษฐกิจชุมชน  
*"เตือนภัยตรงจุด (Track 6) → เดินทางปลอดภัย (Track 5) → เสบียงหมุนเวียนด้วยเงินท้องถิ่น (Track 2)"*  
**Architecture Principle:** Integration-over-Invention (ผสานระบบโครงสร้างพื้นฐานเดิมของรัฐและธนาคาร ไม่สร้างระบบขึ้นมาใหม่ซ้ำซ้อน)  
**Target Pilot Region:** จังหวัดนครปฐม และพื้นที่รอยต่อลุ่มน้ำท่าจีน กรุงเทพฯ และปริมณฑล  
**Document Version:** 2.0 (Master Engineering Specification)  
**Synchronized with:** [DESIGN.md](file:///D:/hackaton/ai-for-hackathon/docs/DESIGN.md)

---

## 1. System Overview & User Role Matrix

ระบบถูกออกแบบเป็น **Mobile-First Progressive Web App (PWA)** รองรับการทำงานในสภาวะวิกฤตน้ำท่วมและการใช้งานต่อเนื่องตลอด 365 วัน (Disaster-to-Commerce Continuum) ผ่าน 4 บทบาทผู้ใช้หลัก:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PromptMesh Ecosystem                            │
│                                                                        │
│   [ Resident ] ──────► Track 6: Hyperlocal Early Warning               │
│                            │ (แจ้งเตือนล่วงหน้า 3-6 ชม. ระดับซอย)        │
│                            ▼                                           │
│   [ Rescue Team ] ───► Track 5: Vehicle-Aware Crisis Routing           │
│                            │ (นำทางตาม Clearance รถ เก๋ง/กระบะ/เรือ)    │
│                            ▼                                           │
│   [ SME Merchant ] ──► Track 2: Decentralized E-Voucher Relief         │
│   [ Donor / อปท. ]     (แปลงร้านโชห่วยเป็นคลังเสบียง หมุนเวียนเงินท้องถิ่น) │
└────────────────────────────────────────────────────────────────────────┘
```

### 1.1 User Roles & Interface Modes

| Role | Primary Objectives | UI Layout & Access Control |
|---|---|---|
| **Resident (ประชาชน)** | รับการแจ้งเตือนระดับซอย, วางแผนอพยพ, ใช้ E-Voucher สแกนรับถุงยังชีพ/เสบียงที่ร้านค้าใกล้บ้าน | **Citizen View:** หน้าแรกสรุปยอดคูปองและสถานะความเสี่ยงในซอยตนเอง พร้อมปุ่ม CTA เปิดแผนที่นำทาง |
| **Rescue Team (ทีมกู้ภัย)** | ค้นหาเส้นทางเข้าพื้นที่ที่ปลอดภัยตามประเภทยานพาหนะ, รายงานจุดเสี่ยงน้ำท่วมลึก, ปักหมุดผู้ต้องการความช่วยเหลือ | **Operations View:** แผนที่เปิดเต็มจอทันที พร้อมเครื่องมือ Dispatch, Filter กรองความลึกของน้ำ, และปุ่มรายงานสิ่งกีดขวาง |
| **SME Merchant (ร้านค้าชุมชน)** | เปลี่ยนร้านเป็น "Micro-Relief Station", สร้าง QR รับชำระจากคูปองเยียวยา, บริหารสต็อกสินค้าจำเป็น | **Merchant View:** แดชบอร์ดสรุปยอดสแกนรับเงิน, ตัวปรับสถานะร้าน (น้ำไม่ท่วม/มีเสบียง), และ AI แนะนำการสั่งของ |
| **Donor & Gov (ผู้บริจาค/อปท.)** | อัดฉีดงบประมาณเยียวยาเจาะจงระดับซอย, กระจายงบสวัสดิการชุมชนตลอดทั้งปี, ตรวจสอบความโปร่งใสแบบ Real-time | **Gov/Donor Dashboard:** แผนที่ความร้อน (Heatmap) แสดงความต้องการเสบียง, สถิติ Impact เม็ดเงินหมุนเวียนใน SME ท้องถิ่น |

---

## 2. Track 6: Resilient Communities (Hyperlocal Early Warning)

**เป้าหมายหลัก:** ตรวจจับและคาดการณ์สถานการณ์น้ำท่วมระดับซอยย่อย (Hyperlocal) ล่วงหน้า 3–6 ชั่วโมง โดยผสานข้อมูลโทรมาตรภาครัฐ เข้ากับแบบจำลองความสูงภูมิประเทศ (DEM) และรายงานภาคประชาชน

```
Track 6 Data Flow Pipeline:
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ TMD Radar API   │     │ HII Canal Level │     │ RID Dam Status  │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         └───────────────────┐   │   ┌───────────────────┘
                             ▼   ▼   ▼
               ┌──────────────────────────────────┐
               │ Data Harmonization & Ingestion   │
               │ (AWS Lambda / EventBridge 15min) │
               └────────────────┬─────────────────┘
                                │
                                ▼
               ┌──────────────────────────────────┐
               │ AI Hyperlocal Hydrology Model    │
               │ (Runoff Simulation + GISTDA DEM) │
               └────────────────┬─────────────────┘
                                │
                                ▼
               ┌──────────────────────────────────┐
               │ PWA Hazard Map + Push/SMS Alert  │
               └──────────────────────────────────┘
```

### 2.1 Hyperlocal Hazard Map (หน้าแผนที่จำลองความเสี่ยง)
*   **Tracking ID:** `P0-01`
*   **Description:** แสดงแผนที่ความละเอียดสูงแบบเรียลไทม์ ซ้อนทับระดับน้ำท่วมขัง ความสูงถนน และตำแหน่งเซนเซอร์โทรมาตร
*   **UI Components (ตาม [DESIGN.md](file:///D:/hackaton/ai-for-hackathon/docs/DESIGN.md)):**
    *   `Map Canvas`: Base map โดย Google Maps API ปิด POI ที่ไม่เกี่ยวข้อง (`z-index: 0`)
    *   `Glassmorphic Floating Map Control`: แถบเครื่องมือกระจกฝ้าด้านบน (`z-index: 60`, `.pm-glass-panel`)
    *   `Map Layer Toggle`: ปุ่มสลับชั้นข้อมูล (ระดับน้ำท่วม, ปริมาณฝนสะสม, ระดับความสูงถนน Elevation Contour)
    *   `Location Pin`: หมุดตำแหน่งผู้ใช้พร้อมวงรัศมีความแม่นยำ พร้อม Badge แสดงสถานะความเสี่ยง (Safe = เขียว, Warning = ส้ม, Danger = แดง)
*   **Input Data:** พิกัด GPS ผู้ใช้, เลเยอร์ระดับน้ำปัจจุบัน (GeoJSON Polygons), ข้อมูลฝนจากเรดาร์
*   **Output Data:** แผนที่แสดงระดับน้ำท่วมขังในแต่ละถนน โดยแบ่งเฉดสีตามความลึก (0-15 cm, 16-40 cm, >40 cm)
*   **Acceptance Criteria:**
    *   โหลดชั้นข้อมูลและแสดงผลภายในไม่เกิน 1.5 วินาทีบนเครือข่าย 4G/3G
    *   หมุดตำแหน่งผู้ใช้ต้องอัปเดตสถานะความเสี่ยงตาม Polygon ที่พิกัดตกอยู่แบบเรียลไทม์

### 2.2 AI 3-Hour Forecaster (ระบบคาดการณ์ระดับน้ำล่วงหน้า)
*   **Tracking ID:** `P0-02`
*   **Description:** แบบจำลอง AI Hydrology Model คำนวณการไหลบ่าของน้ำ (Rainfall-Runoff) ประเมินระดับน้ำในอีก 1, 3, และ 6 ชั่วโมงข้างหน้า
*   **UI Components:**
    *   `Timeline Slider`: แถบเลื่อนเวลา Glassmorphism ลอยอยู่เหนือขอบล่าง (`z-index: 40`), มีจุด Snap ที่ +1h, +3h, +6h
    *   `Risk Alert Banner`: แถบแจ้งเตือนสีแดงกระพริบ (`--pm-danger`) ติดขอบบนหน้าจอ (`z-index: 900`) เมื่อซอยของผู้ใช้มีแนวโน้มน้ำท่วมเกิน 15 ซม. ใน 3 ชม.
    *   `Subscribe Alert Button`: ปุ่ม Primary Blue (`--pm-primary`) ข้อความ *"ติดตามแจ้งเตือนซอยนี้"* สำหรับให้ญาติหรือผู้ดูแลติดตามสถานการณ์ทาง SMS/Push
*   **System Logic:**
    *   เมื่อผู้ใช้เลื่อน Slider ไปที่ +3h: Canvas ของแผนที่จะทำการ Morph เปลี่ยนสีของ Polygon ตามระดับน้ำที่คาดการณ์ล่วงหน้า
    *   หากระดับน้ำเกิน 30 ซม.: ปรากฏข้อความเตือนให้ย้ายรถยนต์และเตรียมยกของขึ้นที่สูง
*   **Acceptance Criteria:**
    *   แจ้งเตือนผู้ใช้ล่วงหน้าอย่างน้อย 2 ชั่วโมงก่อนที่ระดับน้ำจริงจะแตะระดับวิกฤต (อ้างอิง Success Criterion `SC-02`)

### 2.3 Isolation Alert & Encirclement Detector (ระบบตรวจจับพื้นที่ถูกตัดขาดเป็นเกาะ)
*   **Tracking ID:** `P0-03`
*   **Description:** วิเคราะห์โครงข่ายถนน (Road Graph Network) เพื่อตรวจสอบว่ามีบริเวณชุมชนใดที่ทางเข้าออกทุกเส้นทางมีน้ำท่วมสูงเกินกว่าที่รถทั่วไปจะผ่านได้
*   **UI Components:**
    *   `Highlight Zone`: พื้นที่เสี่ยงถูกตัดขาดเป็นเกาะ จะแสดงเป็น Polygon สีแดงกึ่งโปร่งใส พร้อมเส้นขอบกระพริบ Pulse Animation
    *   `Evacuation Route Button`: ปุ่ม Danger Button (`.pm-btn-danger`) บน Collapsible Bottom Sheet ข้อความ *"ค้นหาเส้นทางอพยพด่วน"* เพื่อคำนวณทางออกที่ยังแห้งอยู่ก่อนเส้นทางจะถูกตัดขาดโดยสมบูรณ์
*   **Acceptance Criteria:**
    *   ระบบต้องตรวจพบสถานะ Isolation ล่วงหน้าไม่น้อยกว่า 90 นาที ก่อนเส้นทางสุดท้ายจะถูกน้ำท่วมมิด

### 2.4 Multi-Channel Alert Gateway (เกตเวย์แจ้งเตือนหลายช่องทาง)
*   **Tracking ID:** `P0-10`
*   **Description:** ส่งคำเตือนภัยไปยังผู้ประสบภัยผ่าน Push Notification สำหรับผู้ใช้ PWA และส่ง SMS / Cell Broadcast สำหรับผู้ที่ไม่มีอินเทอร์เน็ต
*   **Integration:** AWS SNS (Simple Notification Service) + กสทช. Cell Broadcast Service (CBS)
*   **Payload Format (SMS):** `[PromptMesh] เตือนภัยน้ำท่วม! ซอยไร่ขิง 26 มวลน้ำจะสูง 35 ซม. ภายในเวลา 17:30 น. โปรดย้ายรถไปยังวัดไร่ขิง นำทางโทร 1784`

### 2.5 API Integration Points (Track 6)

| องค์กร / ผู้ให้บริการ | ข้อมูลที่ดึง (Endpoint / Protocol) | ความถี่ในการดึง (Polling/Webhook) | รูปแบบข้อมูล |
|---|---|---|---|
| **กรมอุตุนิยมวิทยา (TMD)** | Radar Rain Ingestion API, QPE (Quantitative Precipitation Estimation) | ทุก 15 นาที | JSON / NetCDF Grid |
| **สถาบันสารสนเทศทรัพยากรน้ำ (HII)** | Telemetry Canal Stations API (ระดับน้ำในคลอง, ประตูระบายน้ำ) | ทุก 10 นาที | REST API (JSON) |
| **กรมชลประทาน (RID)** | Upstream Dam Discharge API (อัตราการระบายน้ำเขื่อนเจ้าพระยา/แม่กลอง) | ทุก 1 ชั่วโมง | REST API (JSON) |
| **GISTDA** | Sentinel-1 SAR Flood Extent Service, High-Res Digital Elevation Model (DEM) | ราย 12 ชั่วโมง (หรือเมื่อมีภาพถ่ายดาวเทียมใหม่) | GeoJSON / Cloud-Optimized GeoTIFF |
| **Traffy Fondue Open API**| Citizen Flood Incident Reports (ภาพถ่ายและระดับน้ำจากประชาชน) | Real-time Webhook | REST API (GeoJSON) |

### 2.6 Edge Cases & Error Handling (Track 6)

```
┌───────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Scenario / Edge Case                  │ System Mitigation & Fallback Strategy                  │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ เซนเซอร์วัดระดับน้ำ HII ในพื้นที่หยุดส่ง │ สลับไปใช้การประมาณค่าเชิงพื้นที่ (Spatial Kriging     │
│ สัญญาณ (Sensor Offline/Destroyed)     │ Interpolation) ร่วมกับสถานีข้างเคียง และปรับลดคะแนน       │
│                                       │ ความมั่นใจ (Confidence Score) ของโมเดลเหลือ 65%        │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ประตูระบายน้ำเปิดฉุกเฉิน มวลน้ำพุ่งสูง  │ Trigger กฎ Spike Anomaly Detection: หากระดับน้ำใน     │
│ รวดเร็วกว่าที่ AI พยากรณ์               │ คลองสูงขึ้น >20 ซม. ใน 15 นาที ให้ยกระดับคำเตือนเป็น   │
│                                       │ Emergency Danger ทันทีโดยไม่ต้องรอรอบคำนวณของ AI        │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ฝนตกหนัก บดบังสัญญาณ GPS ในสมาร์ทโฟน   │ ขยายรัศมีตำแหน่งความคลาดเคลื่อน (Accuracy Circle) บน   │
│ (GPS Drift > 100 เมตร)                │ หน้าจอ พร้อมแสดงปุ่มให้ผู้ใช้เลือก "ระบุชื่อซอยด้วยตนเอง" │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ การแจ้งเตือนซ้ำซ้อนสร้างความรำคาญ       │ ตั้งค่า Hysteresis Cooldown: หากระดับน้ำยังแกว่งอยู่ใน  │
│ (False Positive Alert Fatigue)        │ เกณฑ์เดิม จะไม่มีการส่ง Push ซ้ำภายใน 2 ชั่วโมง         │
└───────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 2.7 Offline-First Capabilities (Track 6)
*   **Service Worker Pre-caching:** เมื่อติดตั้ง PWA ระบบจะทำการดาวน์โหลดแผนผังโครงข่ายน้ำท่วมของตำบลที่ลงทะเบียน (Pre-computed Flood Scenarios) ขนาด ~15 MB จัดเก็บลงใน CacheStorage
*   **Stale Data Visualization:** หากอุปกรณ์ขาดการเชื่อมต่ออินเทอร์เน็ต แผนที่จะแสดงชั้นข้อมูลล่าสุดที่มี พร้อมแสดงแบนเนอร์สีเทาอ่อนด้านบน: *"โหมดออฟไลน์: กำลังแสดงข้อมูลระดับน้ำล่าสุดเมื่อ 14:20 น. (35 นาทีที่แล้ว)"*
*   **SMS Sync Parser:** หากได้รับ SMS เตือนภัยจากระบบ PromptMesh แอปพลิเคชันในเครื่องจะตรวจจับและดึงค่าพิกัดจาก SMS มาอัปเดตหมุดเตือนภัยบนแผนที่แบบออฟไลน์ได้

---

## 3. Track 5: Smart Mobility (Crisis Routing)

**เป้าหมายหลัก:** ระบบนำทางเฉพาะกิจยามภัยพิบัติ ที่คำนวณขีดจำกัดความสามารถในการลุยน้ำของยานพาหนะแต่ละประเภท (Vehicle-Specific Clearance) และตัดเส้นทางที่น้ำท่วมลึกออกอัตโนมัติ

```
Dynamic Clearance Routing Engine:
┌───────────────────────────────┐
│ User Selected Vehicle:        │
│ • Sedan/Bike: Max 15 cm       │
│ • Lifted Pickup: Max 40 cm    │
│ • Boat/Jet Ski: > 30 cm       │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐     ┌───────────────────────────────┐
│ Road Graph (OSM / Google)     │ ──► │ Route Optimization Algorithm  │
│ + Real-time Water Depth Layer │     │ (Penalty = Water Depth / Clear│
└───────────────────────────────┘     └──────────────┬────────────────┘
                                                     │
                                                     ▼
                                      ┌───────────────────────────────┐
                                      │ Safe Turn-by-Turn Navigation  │
                                      │ With Dynamic Mid-Route Reroute│
                                      └───────────────────────────────┘
```

### 3.1 Vehicle-Specific Dispatch (ระบบเลือกขีดจำกัดยานพาหนะ)
*   **Tracking ID:** `P0-04`
*   **Description:** อนุญาตให้ผู้ขับขี่เลือกประเภทพาหนะ เพื่อให้ Routing Engine กรองเส้นทางที่ระดับน้ำเกินขีดจำกัดความปลอดภัยของพาหนะนั้นออกจากการคำนวณ
*   **UI Components:**
    *   `Vehicle Selector Card`: Segmented Control 3 ช่องตาม [DESIGN.md](file:///D:/hackaton/ai-for-hackathon/docs/DESIGN.md) ติดตั้งอยู่ใน Collapsible Bottom Sheet:
        *   `Option 1 (Car/Motorcycle)`: Lucide `car`, ข้อความ *"รถเก๋ง/มอเตอร์ไซค์"*, Subtext *"ลุยน้ำได้ ≤ 15 ซม."*
        *   `Option 2 (Lifted Pickup)`: Lucide `truck`, ข้อความ *"กระบะยกสูง"*, Subtext *"ลุยน้ำได้ ≤ 40 ซม."*
        *   `Option 3 (Boat/Jet Ski)`: Lucide `ship`, ข้อความ *"เรือ/เจ็ตสกี"*, Subtext *"วิ่งทางคลอง/ถนนน้ำท่วมมิด"*
    *   `Find Safe Route Button`: Primary Button ขนาดใหญ่ 48px (`.pm-btn-primary`) พร้อม Lucide `navigation` ข้อความ *"นำทางปลอดภัย"*
*   **Clearance Threshold Matrix:**

| ประเภทยานพาหนะ | เกณฑ์ความลึกปลอดภัยสูงสุด | พฤติกรรมของ Routing Engine |
|---|---|---|
| **รถเก๋ง / มอเตอร์ไซค์** | `15 cm` | สั่งปิดเส้นทาง (Penalty = Infinity) ทันทีที่ส่วนใดของถนนมีน้ำท่วมขัง > 15 cm |
| **รถกระบะยกสูง / 4WD** | `40 cm` | อนุญาตให้ผ่านถนนที่น้ำท่วม 15–40 cm ได้ แต่จะปรับลดความเร็วเฉลี่ยในการคำนวณ ETA เหลือ 15 กม./ชม. |
| **เรือท้องแบน / เจ็ตสกี**| `> 30 cm` | สลับไปใช้โครงข่ายแนวลำคลองและถนนสายหลักที่มีน้ำท่วมลึก (>40 cm) โดยหลีกเลี่ยงถนนที่น้ำแห้งหรือมีสายไฟหย่อน |

### 3.2 Dynamic Clearance Routing & Mid-Route Reroute (ระบบเปลี่ยนเส้นทางเรียลไทม์)
*   **Tracking ID:** `P0-05`
*   **Description:** คำนวณเส้นทางใหม่ทันทีระหว่างที่ผู้ใช้กำลังขับรถ หากมีรายงานน้ำท่วมทะลักเข้ามาข้างหน้า
*   **UI Components:**
    *   `Dynamic Reroute Alert`: Modal Pop-up ซ้อนทับกึ่งกลางจอ (`z-index: 600`, `.pm-glass-panel`) พื้นหลังโปร่งแสง ขอบสีส้มเตือนภัย:
        *   ข้อความ: *"พบน้ำท่วมสูง 28 ซม. ข้างหน้าในอีก 400 ม. (เกินขีดจำกัดรถของคุณ)"*
        *   ปุ่มกด: ปุ่มฟ้า *"เปลี่ยนเส้นทางเดี๋ยวนี้ (เลี่ยงเพิ่ม 1.2 กม.)"* และปุ่มโปร่งใส *"เพิกเฉย"*
    *   `Turn-by-Turn Panel`: แถบระบุทิศทางบน Bottom Sheet (Expanded Mode) พื้นหลังสีขาว สะอาดตา ไร้สิ่งรบกวน

### 3.3 Crowdsourced Road Obstruction & Flood Depth Reporter (ระบบรายงานอุปสรรค)
*   **Tracking ID:** `P0-05 Sub-module`
*   **Description:** ฟังก์ชันให้กู้ภัยหรือประชาชนถ่ายภาพและปักหมุดจุดที่น้ำท่วมสูงเกินคาดการณ์ ขยะอุดตัน หรือสะพานชำรุด
*   **UI Components:**
    *   `Report Flooded Road Button`: Floating Button ด้านซ้ายล่างเหนือแผนที่ มี Lucide `camera`
    *   `Report Sheet`: แผ่นปัดขึ้นมาระบุ:
        *   ระดับน้ำจริงโดยประมาณ (ปุ่มตัวเลือก: ข้อเท้า, หัวเข่า, เอว, มิดหลังคารถ)
        *   ปุ่มอัปโหลดรูปภาพหลักฐาน
        *   ระบบจับพิกัด GPS อัตโนมัติ

### 3.4 API Integration Points (Track 5)

| API Service | หน้าที่และการทำงานในระบบ PromptMesh |
|---|---|
| **Google Maps Directions API** | คำนวณโครงข่ายถนนพื้นฐาน (Base Road Graph) และระยะทาง |
| **Google Maps Elevation API** | ดึงค่าความสูงพื้นผิวถนน (Elevation Profiling) เพื่อหาจุดลุ่มต่ำตามแนวซอย |
| **Custom Dynamic Routing Engine (OSRM / GraphHopper)** | นำโครงข่ายถนนจาก OpenStreetMap มาผสานกับชั้นข้อมูลน้ำท่วมแบบ Real-time เพื่อตัด Edge ที่มีน้ำท่วมเกิน Clearance ทิ้ง |
| **Google Roads API** | Snap-to-Road ปรับแต่งพิกัด GPS ผู้ใช้ให้แนบชิดกับเส้นทางที่ถูกต้องขณะฝนตกหนัก |

### 3.5 Edge Cases & Error Handling (Track 5)

```
┌───────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Scenario / Edge Case                  │ System Mitigation & Fallback Strategy                  │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ สูญเสียสัญญาณ GPS ขณะขับรถใต้ทางด่วน    │ ระบบเปลี่ยนไปใช้ Dead Reckoning Mode: คำนวณตำแหน่งจาก    │
│ หรือฝนตกหนักจัด                        │ ความเร็วล่าสุดและเข็มทิศในเครื่อง พร้อมมีเสียงเตือนให้    │
│                                       │ ชะลอความเร็วและระวังระดับน้ำด้านหน้า                   │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ผู้ใช้รายงานข้อมูลขัดแย้งกัน (คนหนึ่งบอกว่า │ ใช้อัลกอริทึม Weighted Consensus: ให้น้ำหนักรายงานจาก    │
│ ผ่านได้ อีกคนบอกว่าน้ำท่วมลึก)         │ ทีมกู้ภัย (Verified Rescue) 3 เท่าของประชาชนทั่วไป      │
│                                       │ หากยังไม่ชัวร์ ให้ขึ้นสถานะสีส้ม (Warning) เป็นค่าเริ่มต้น │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ทางออกทุกทางถูกน้ำท่วมมิด ไม่มีเส้นทาง    │ เข้าสู่โหมด "No Safe Exit - Evacuation Overwrite":     │
│ ที่ปลอดภัยเหลืออยู่                     │ ระบบจะนำทางผู้ใช้ไปยัง "จุดปลอดภัยยกสูงใกล้ที่สุด" (เช่น  │
│                                       │ วัด, โรงเรียนสองชั้น, ลานจอดรถห้าง) แทนการฝืนขับออกนอกโซน │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ผู้ใช้พยายามฝืนขับรถเก๋งเข้าไปในเส้นทางที่ │ แสดง Full-screen Warning Modal สีแดง พร้อมให้กดยืนยัน    │
│ ระบบแจ้งว่าน้ำท่วมเกิน 15 ซม.          │ "ฉันเข้าใจความเสี่ยง" เพื่อบันทึก Timestamp และตัดความ     │
│                                       │ รับผิดชอบทางกฎหมาย (Liability Disclaimer)              │
└───────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 3.6 Offline-First Capabilities (Track 5)
*   **Offline Routing Graph Cache:** ดาวน์โหลดตารางโครงข่ายถนนความละเอียดสูงของจังหวัดนครปฐมในรูปแบบ GeoJSON Topology (~25 MB) ลงใน IndexedDB
*   **Client-Side Dijkstra / A\* Pathfinding:** เมื่อเครือข่ายมือถือขาดหาย แอปสามารถรันอัลกอริทึม A* เพื่อหาเส้นทางที่ปลอดภัยได้บน JavaScript Client โดยใช้ข้อมูลระดับน้ำล่าสุดก่อนสัญญาณดับ
*   **Audio Chime Guidance:** ไฟล์เสียงแนะนำทิศทาง (เช่น *"อีก 200 เมตรเลี้ยวซ้ายเข้าซอยปลอดภัย"*) ถูก Pre-cache ในเครื่อง เพื่อให้อ่านออกเสียงได้แม้ไม่มีอินเทอร์เน็ต

---

## 4. Track 2: SME & Local Economy (Decentralized E-Voucher Relief)

**เป้าหมายหลัก:** เปลี่ยนร้านค้าโชห่วยและตลาดชุมชนให้กลายเป็น "สถานีเสบียงย่อย (Micro-Relief Stations)" และกระจายเม็ดเงินช่วยเหลือตรงสู่ประชาชนด้วยระบบ E-Voucher ผ่านโครงสร้างพร้อมเพย์ (PromptPay) หมุนเวียนเม็ดเงินในท้องถิ่นแทนการแจกถุงยังชีพส่วนกลางที่ล่าช้า

```
Track 2 Voucher Injection & Redemption Flow:
┌───────────────────────────┐
│ Donor / Gov (อปท.)        │ ──► [ Krungthai Open API Gateway ]
│ Injects Relief Budget     │
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Citizen E-Voucher Wallet  │ ──► Generates Single-Use Dynamic QR Token
│ (PWA Client Storage)      │
└───────────────────────────┘
              │
              ▼
┌───────────────────────────┐
│ Local SME Merchant        │ ──► Scans Citizen QR Code via PromptPay Rail
│ (Micro-Relief Station)    │     Funds Instantly Deposited / Claims Logged
└───────────────────────────┘
```

### 4.1 Micro-Relief Station Locator (แผนที่สถานีเสบียงชุมชน)
*   **Tracking ID:** `P0-06`
*   **Description:** แสดงหมุดร้านค้า SME ที่เข้าร่วมโครงการ โดยมีตัวกรองสถานะความพร้อมเปิดให้บริการและสต็อกสินค้า
*   **UI Components:**
    *   `Find Supplies Button`: ปุ่ม Filter บน Glassmorphic Map Control แสดงเฉพาะร้านค้าที่มีเสบียงพร้อม
    *   `Store Status Tag`: ป้ายสถานะแบบโค้งมน 8px (`--pm-radius-sm`) แสดงข้อมูล:
        *   ป้ายสีเขียว: Lucide `package-check` *"พร้อมแจกเสบียง"*
        *   ป้ายสีฟ้า: Lucide `shield-check` *"น้ำไม่ท่วมทางเข้าร้าน"*
        *   ตัวนับสต็อก: *"น้ำดื่มเหลือ 45 แพ็ค / ข้าวสารเหลือ 20 ถุง"*
    *   `Merchant Detail Sheet`: Bottom Sheet แสดงรายการสินค้าที่รับแลกด้วยคูปองเยียวยา พร้อมปุ่ม *"นำทางไปร้านนี้"*

### 4.2 Decentralized E-Voucher Wallet (กระเป๋าเงินเยียวยาดิจิทัล)
*   **Tracking ID:** `P0-07`, `P0-12`
*   **Description:** ระบบบริหารจัดการคูปองช่วยเหลือฉุกเฉินและคูปองสวัสดิการชุมชน รองรับการยืนยันตัวตนและการสแกนชำระเงินผ่านโครงสร้าง PromptPay / เป๋าตัง
*   **Resident & Rescue View (ฝั่งประชาชน):**
    *   `My Vouchers Card`: การ์ดแสดงยอดเงินคงเหลือ (เช่น ฿1,500) และรายการคูปองแบ่งตามประเภท (เสบียงยังชีพ, ยารักษาโรค, วัสดุก่อสร้างซ่อมแซม)
    *   `Scan QR to Redeem Button`: ปุ่ม Primary Blue ขนาดใหญ่พิเศษ เรียกเปิดกล้องสมาร์ทโฟนสำหรับสแกน QR ร้านค้า หรือสร้าง Dynamic QR ให้ร้านค้าสแกน
*   **SME Merchant View (ฝั่งร้านค้า):**
    *   `Generate Receive QR Button`: ปุ่มสร้าง QR โค้ดรับเงินตามมูลค่าชุดเสบียง (เช่น ชุดยังชีพมาตรฐาน ฿300)
    *   `Transaction History`: ตารางสรุปรายการสแกนรับของ พร้อมยอดเงินสุทธิที่เตรียมรับโอนจากธนาคารกรุงไทย
*   **Security & Encryption:** คูปองดิจิทัลทุกใบใช้มาตรฐาน Single-Use HMAC-SHA256 Token หมดอายุภายใน 60 วินาที เพื่อป้องกันการถ่ายภาพหน้าจอไปใช้ซ้ำ (Anti-Replay Attack)

### 4.3 อปท. Welfare Voucher & Year-Round Commerce Mode (สวัสดิการชุมชน 365 วัน)
*   **Tracking ID:** `P1-05`
*   **Description:** สลับโหมดการทำงานของแพลตฟอร์มในช่วงที่ไม่มีน้ำท่วม ให้กลายเป็นระบบกระจายสวัสดิการของเทศบาล/อบต. (เช่น คูปองอาหารกลางวันนักเรียน, เบี้ยยังชีพผู้สูงอายุ, คูปองกระตุ้นตลาดนัดท้องถิ่น)
*   **Benefits:** แก้ปัญหา "Built and Abandoned" ทำให้ประชาชนและร้านค้าเปิดใช้งานแอปสม่ำเสมอตลอดทั้งปี

### 4.4 SME Economic Recovery & Restock Dashboard (แดชบอร์ดฟื้นฟูร้านค้า)
*   **Tracking ID:** `P1-02`, `P2-07`
*   **Description:** ระบบ AI วิเคราะห์ความต้องการสินค้าหลังน้ำลดในแต่ละชุมชน เพื่อแนะนำสินค้าที่ร้านค้าควรสั่งเข้ามาสต็อก
*   **UI Components:**
    *   `Restock Recommendation Card`: การ์ดข้อความแนะนำ เช่น *"AI วิเคราะห์: ซอย 1-4 มีบ้านเรือนเสียหายจากโคลน แนะนำสต็อก อุปกรณ์ทำความสะอาดเพิ่ม 50% และปูนซีเมนต์เพิ่ม 30%"*
    *   `Order from Supplier Button`: ปุ่มเชื่อมโยงคำสั่งซื้อไปยังผู้ค้าส่งท้องถิ่นหรือแพลตฟอร์ม Wholesale

### 4.5 Donor & Gov Fund Injection Portal (พอร์ทัลอัดฉีดงบประมาณ)
*   **Tracking ID:** `P1-01`
*   **Description:** หน้าต่างสำหรับหน่วยงาน อปท., ปภ., หรือมูลนิธิผู้บริจาค เพื่อโอนเงินตรงเข้าสู่งบ E-Voucher ประจำตำบล
*   **UI Components:**
    *   `Inject Funds Button`: ฟอร์มเลือกพื้นที่เป้าหมาย (ระดับอำเภอ/ตำบล/ซอย) และระบุวัตถุประสงค์ของคูปอง
    *   `Live Impact Dashboard`: แผนภูมิแสดงจำนวนร้านค้า SME ที่ได้รับการกระตุ้นยอดขาย และจำนวนครัวเรือนที่ได้รับเสบียงแล้วแบบ Real-time

### 4.6 API Integration Points (Track 2)

| ผู้ให้บริการ API | ฟังก์ชันการเชื่อมต่อและจุดประสงค์ |
|---|---|
| **Krungthai Open API (เป๋าตัง / ถุงเงิน)** | เชื่อมต่อ App-to-App สำหรับการยืนยันสิทธิ์ E-Voucher และกระบวนการเบิกจ่ายเงิน (Settlement) เข้าบัญชีร้านค้า |
| **National ITMX PromptPay QR API** | สร้างและตรวจสอบ QR Code มาตรฐาน EMVCo สำหรับการชำระเงินของร้านค้าชุมชน |
| **กรมการปกครอง (DOPA Citizen Auth API)** | ตรวจสอบสถานะบัตรประชาชนและภูมิลำเนา (เชื่อมผ่าน Krungthai KYC Rail) |
| **อปท. Smart Local Welfare DB API** | ดึงรายชื่อผู้มีสิทธิ์รับสวัสดิการเบี้ยผู้สูงอายุและงบอุดหนุนภัยพิบัติของเทศบาล |

### 4.7 Edge Cases & Error Handling (Track 2)

```
┌───────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Scenario / Edge Case                  │ System Mitigation & Fallback Strategy                  │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ PromptPay Gateway หรือธนาคารกรุงไทย   │ ใช้ Idempotency Key ร่วมกับ Cryptographic Voucher      │
│ เกิด Timeout ระหว่างการสแกน            │ Queue: ระบบใน PWA บันทึกสิทธิ์ไว้ชั่วคราวและขึ้นสถานะ    │
│                                       │ "กำลังรออนุมัติ (Pending)" ป้องกันการตัดยอดเงินซ้ำซ้อน    │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ สมาร์ทโฟนของร้านค้าแบตเตอรี่หมดหรือดับ    │ ผู้นำชุมชนหรือ อสม. ประจำสถานีเสบียง สามารถใช้เครื่องกลาง │
│                                       │ (Backup Tablet) ล็อกอินโหมดผู้ช่วยเพื่อสแกนแทนร้านค้าได้   │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ ผู้รับเสบียงเดินทางมาถึง แต่ร้านค้าของหมด  │ ระบบแจ้งเตือน Real-time Stock Discrepancy: ปรับหมุดร้าน │
│ พอดี (Out of Stock)                   │ เป็นสีส้มทันที พร้อมแนะนำและนำทางไปยังร้าน Micro-Relief │
│                                       │ ลำดับถัดไปที่อยู่ห่างออกไปไม่เกิน 800 เมตร              │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ น้ำท่วมยาวนาน คูปองเยียวยาหมดอายุการใช้  │ มีกลไก Disaster Grace Extension อัตโนมัติ: หากพื้นที่   │
│ งานก่อนที่ประชาชนจะเดินทางออกมาได้      │ ยังคงมีประกาศเขตภัยพิบัติ อายุคูปองจะต่อเวลาให้อัตโนมัติ  │
│                                       │ ครั้งละ 7 วัน จนกว่าสถานการณ์จะคลี่คลาย                 │
└───────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 4.8 Offline-First Capabilities (Track 2)
*   **Cryptographic Offline Vouchers:** คูปองช่วยเหลือฉุกเฉินจะถูกออกเป็นดิจิทัลโทเคนที่เข้ารหัสด้วยคีย์สาธารณะ (Asymmetric ECDSA Key) เก็บไว้ใน IndexedDB ของประชาชนตั้งแต่ก่อนสัญญาณดับ
*   **Store-and-Forward Merchant Ledger:** เครื่องของร้านค้าสามารถสแกนรับรองโทเคนแบบออฟไลน์ได้ โดยเครื่องจะตรวจสอบลายเซ็นดิจิทัลในเครื่องโดยไม่ต้องพึ่งเซิร์ฟเวอร์ และจัดเก็บประวัติธุรกรรมไว้ในฐานข้อมูลเข้ารหัส เมื่อสัญญาณอินเทอร์เน็ตกลับมา แอปจะซิงก์ข้อมูลขึ้นระบบ Krungthai Settlement API อัตโนมัติ
*   **USSD Fallback Redemption:** ในกรณีที่ไม่มีสมาร์ทโฟนหรือไม่มีสัญญาณ 4G ผู้สูงอายุสามารถกดรหัส USSD เช่น `*484*VOUCHER_CODE*STORE_ID#` เพื่อรับข้อความยืนยันการแลกเสบียงทาง SMS

---

## 5. Comprehensive Multi-Layer Resilience Architecture

เมื่อเกิดอุทกภัยรุนแรง เสาสัญญาณโทรศัพท์และกระแสไฟฟ้าอาจหยุดทำงานบางส่วน PromptMesh จึงถูกออกแบบตามสถาปัตยกรรมความต่อเนื่อง 3 ระดับ (3-Layer Resilience Architecture):

```
┌────────────────────────────────────────────────────────────────────────┐
│ Layer 1: PWA Edge Runtime (CacheStorage + IndexedDB)                    │
│ • ทำงานในเครื่อง 100% แม้ไม่มีอินเทอร์เน็ต (ขนาดแคชรวม ≤ 50 MB)         │
│ • เก็บแผนที่ความเสี่ยง, โครงข่ายถนน, และคูปองออฟไลน์                     │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Layer 2: Telecom & SMS / Cell Broadcast Fallback                       │
│ • ส่งข้อความเตือนภัยผ่านคลื่นสัญญาณวิทยุโทรศัพท์พื้นฐาน (ไม่ต้องพึ่ง Data)│
│ • รองรับ Cell Broadcast ประสานงาน กสทช. และค่ายมือถือ                  │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Layer 3: Human & Mesh Community Relay                                  │
│ • เครือข่ายจิตอาสา อสม. และผู้ใหญ่บ้าน ณ จุด Micro-Relief Stations      │
│ • บอร์ดประชาสัมพันธ์ข้อมูลน้ำท่วม และเสียงตามสายประจำหมู่บ้าน (หอกระจายข่าว)│
└────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Storage Quota & Lifecycle Management

| ประเภทข้อมูล | เทคโนโลยีจัดเก็บ | ขนาดข้อมูลสูงสุด | นโยบายการอัปเดต (Invalidation Strategy) |
|---|---|---|---|
| **App Shell & Assets** | Service Worker CacheStorage | ~8 MB | Cache-First, อัปเดตในพื้นหลังเมื่อมี Release ใหม่ |
| **Local Map Vector Tiles**| CacheStorage | ~20 MB | ดาวน์โหลดเฉพาะรัศมี 15 กม. รอบพิกัดประจำตัวผู้ใช้ |
| **Offline Road Graph** | IndexedDB | ~12 MB | Stale-While-Revalidate ทุก 24 ชั่วโมง |
| **Offline Voucher Tokens** | Encrypted IndexedDB (Web Crypto API) | ~2 MB | Network-First, เก็บเฉพาะสิทธิ์ของบัตรประชาชนผู้ถือ |
| **Cached Sensor Feeds** | LocalStorage | ~1 MB | ล้างทิ้งอัตโนมัติหากข้อมูลมีอายุเกิน 6 ชั่วโมง |
| **รวมขนาดทั้งหมด** | — | **~43 MB** | **อยู่ภายใต้กรอบเพดาน 50 MB ตามข้อกำหนด P1-04** |

### 5.2 Conflict Resolution & Data Synchronization
*   **CRDTs (Conflict-Free Replicated Data Types):** ใช้ State-based CRDTs สำหรับข้อมูลการรายงานระดับน้ำจากฝูงชน (Crowdsourcing) เพื่อป้องกันข้อมูลทับซ้อนเมื่ออุปกรณ์หลายเครื่องอัปโหลดข้อมูลหลังสัญญาณติด
*   **Background Sync API:** ลงทะเบียนแท็ก `promptmesh-sync-vouchers` และ `promptmesh-sync-reports` เพื่อให้ Service Worker ส่งข้อมูลทันทีที่เครื่องกลับมาตรวจพบสัญญาณอินเทอร์เน็ต แม้ผู้ใช้จะปิดแอปไปแล้ว

---

## 6. UI Terminology & DESIGN.md Synchronization Matrix

เพื่อให้การสื่อสารระหว่าง Product Management, UX/UI Designers และ Frontend Developers มีความสอดคล้องกันอย่างสมบูรณ์ ตารางต่อไปนี้สรุปการจับคู่ระหว่างฟีเจอร์ในสเปกนี้ กับคอมโพเนนต์และโทเค็นใน [DESIGN.md](file:///D:/hackaton/ai-for-hackathon/docs/DESIGN.md):

| Feature Name | Tracking ID | UI Component Name (DESIGN.md) | Design Tokens / Classes | Z-Index Layer |
|---|---|---|---|---|
| **Base Hazard Map** | `P0-01` | Google Maps Base Canvas | Canvas Style: Clean Light, POI Hidden | `0` |
| **Water Level Overlays** | `P0-01` | GeoJSON Hazard Polygons | `--pm-danger` (High), `--pm-warning` (Med) | `10` |
| **User Risk Marker** | `P0-01` | Location Pin with Pulse Ring | `--pm-primary` circle, Solid Blue fill | `20` |
| **Map Layers & Filters** | `P0-01` | Floating Glass Layer Pills | `.pm-glass-panel`, `--pm-shadow-3` | `30` |
| **Forecast Timeline** | `P0-02` | Glassmorphic Timeline Slider | Snap Marks: 1h, 3h, 6h, Thumb: 24px Solid Blue | `40` |
| **Imminent Flood Warning**| `P0-02` | Risk Alert Banner | Background: `--pm-danger`, Text: `#ffffff` | `900` |
| **Vehicle Selection** | `P0-04` | Vehicle Selector Segmented Card | Lucide: `car`, `truck`, `ship`, Active: `--pm-primary-light` | `100` (in Sheet) |
| **Turn-by-Turn Nav** | `P0-04` | Collapsible Bottom Sheet (Expanded)| `.pm-bottom-sheet`, Top Radius: `24px` | `100` |
| **Mid-Drive Reroute** | `P0-05` | Dynamic Reroute Alert Modal | Backdrop: `500`, Modal Box: `600`, `.pm-glass-panel`| `600` |
| **Road Hazard Report** | `P0-05` | Road Obstruction FAB / Action | Lucide: `camera`, Border Radius: `12px` | `70` |
| **Relief Shop Locator** | `P0-06` | Micro-Relief Station Pins & Tags | Lucide: `store`, Tag: `.pm-badge-success` | `20` & `100` |
| **E-Voucher Balance** | `P0-07` | My Vouchers Card | `.pm-card`, Font: `--text-display` (Kanit Bold 32px) | Standard UI |
| **Redeem Voucher Scan**| `P0-07` | QR Scanner Sheet & Dynamic Code | Lucide: `scan`, Button: `.pm-btn-primary` (48px) | `600` |
| **Contextual AI Help** | `P1-03` | Floating Action Button (AI FAB) | `.pm-ai-fab`, Size: `56x56px`, Lucide: `sparkles` | `70` |
| **Offline Sync Status** | `P1-04` | Offline Toast Indicator | Background: `--pm-text-muted`, Lucide: `wifi-off` | `1000` |

---

## 7. Pilot Execution & Success Validation (KPIs)

การประเมินความพร้อมและตรวจรับระบบซอฟต์แวร์ จะดำเนินการตามเกณฑ์ชี้วัดความสำเร็จ (Success Criteria) ที่ระบุไว้ใน Scope Definition:

*   **SC-01 (ความแม่นยำของการเตือนภัย):** โมเดล AI ระดับน้ำท่วมระดับตำบลมีความแม่นยำไม่น้อยกว่า 70% เมื่อเทียบกับข้อมูลน้ำท่วมย้อนหลังปี 2564–2568 ในลุ่มน้ำท่าจีน
*   **SC-02 (ระยะเวลาเตือนภัยล่วงหน้า):** ส่งการแจ้งเตือนระดับซอยล่วงหน้าเฉลี่ยไม่น้อยกว่า 2 ชั่วโมง ก่อนมวลน้ำเข้าท่วมจริง
*   **SC-03 (ความปลอดภัยในการนำทาง):** ไม่มีรายงานยานพาหนะติดค้างในจุดที่น้ำท่วมลึกเกินสเปกรถแม้แต่กรณีเดียวตลอดช่วงทดสอบ
*   **SC-06 (ความสำเร็จของ E-Voucher):** อัตราความสำเร็จของการสแกนและยืนยันสิทธิ์แลกเสบียง (Redemption Success Rate) ไม่น้อยกว่า 95%
*   **SC-07 (ความเร็วในการหมุนเวียนงบประมาณ):** ใช้เวลาไม่เกิน 30 นาที นับตั้งแต่วินาทีที่ อปท. หรือผู้บริจาคกดปุ่ม `Inject Funds` จนถึงวินาทีที่ประชาชนนำคูปองไปสแกนรับสินค้าชิ้นแรกที่ร้าน SME
*   **SC-12 (ความพร้อมใช้งานของระบบ):** ระบบ PWA และ API มีระดับความพร้อมใช้งาน (Uptime) ไม่ต่ำกว่า 99.5% ตลอดช่วงวิกฤตภัยพิบัติ
