# PromptMesh - Design System & UI Specifications

**Project Name:** PromptMesh (Hyperlocal D2C Mesh)  
**Platform:** Mobile-First Progressive Web App (PWA)  
**Design Philosophy:** Soft UI (Apple OS Style) + White & Solid Blue Theme + Frosted Glassmorphism  
**Target Audience:** ประชาชนในพื้นที่เสี่ยงภัย (Residents), ทีมกู้ภัย (Rescue Teams), ร้านค้าชุมชน (SME Merchants), หน่วยงานภาครัฐและผู้บริจาค (Local Government & Donors)  
**Version:** 2.0 (Engineering-Ready Specification)

---

## 1. Core Theming & Design Philosophy (ปรัชญาและธีมหลัก)

ระบบการออกแบบของ **PromptMesh** พัฒนาขึ้นโดยคำนึงถึง "สภาวะวิกฤต (Crisis Usability)" เป็นหัวใจสำคัญ ผู้ใช้งานต้องเผชิญกับสถานการณ์น้ำท่วม ความตึงเครียด แสงแดดจ้ากลางแจ้ง หรือฝนตกหนัก ดังนั้น UI ต้องส่งมอบความรู้สึก **มั่นคง น่าเชื่อถือ เข้าถึงง่าย และลดภาระการประมวลผลทางสายตา (Cognitive Load)**

*   **Soft UI (Apple OS Style):** โครงสร้างโค้งมน ผิวสัมผัสเนียนตา (Smooth Curvature) ใช้น้ำหนักเงาแบบ Soft Drop Shadows ที่ฟุ้งกระจายอย่างเป็นธรรมชาติ สร้างมิติการซ้อนทับแบบ Physical Depth โดยไม่ใช้สไตล์ Skeuomorphism ยุคเก่า
*   **White + Solid Blue Theme (ความน่าเชื่อถือระดับสถาบัน):** 
    *   ❌ **No AI Gradients:** ไม่อนุญาตให้ใช้สีไล่เฉดนีออน หรือลูกเล่นแสงสะท้อนแนว Sci-Fi/AI Fantasy ซึ่งลดทอนความน่าเชื่อถือในยามฉุกเฉิน
    *   ✅ **Solid Blue (`#2563eb`):** ใช้สีฟ้าเข้มทึบเป็นสี Action หลัก มอบความรู้สึกสงบ ปลอดภัย และมีมาตรฐานเทียบเท่าแอปพลิเคชันธุรกรรมการเงินและบริการภาครัฐ
*   **Glassmorphism (Frosted Glass สำหรับ Map UI):** ชิ้นส่วน UI ที่ลอยอยู่เหนือแผนที่ (Floating Map Elements) ใช้เทคนิคกระจกฝ้าโปร่งแสง (`backdrop-filter: blur(12px)`) เพื่อให้ผู้ใช้ยังคงมองเห็นบริบทเชิงพื้นที่ (Spatial Context) ของแผนที่ด้านหลังตลอดเวลา
*   **Strictly Vector Icons (Zero Emojis):** 
    *   ❌ **ห้ามใช้ Emoji (เช่น 🚗, 🚤, 🌊, 💰, ⚠️) ในส่วนประกอบ UI โดยเด็ดขาด** เนื่องจาก Emoji เรนเดอร์ไม่เหมือนกันในแต่ละ OS/เบราว์เซอร์ และดูไม่เป็นทางการ
    *   ✅ ใช้ชุดไอคอนเวกเตอร์เส้นเรียบมาตรฐาน (SVG) จาก **Lucide Icons** หรือ **Material Symbols Rounded** เท่านั้น
*   **Mobile-First Ergonomics:** ออกแบบโครงสร้างสำหรับหน้าจอสัมผัสขนาดเล็ก ควบคุมได้ด้วยนิ้วโป้งมือเดียว (One-Hand Thumb Zone) พร้อมรองรับ Safe Area Insets ของอุปกรณ์ iOS และ Android

---

## 2. Color Palette & Design Tokens (ชุดสีและตัวแปรระบบ)

ระบบสีถูกออกแบบให้สอดคล้องตามมาตรฐาน **WCAG 2.1 AA (Contrast Ratio ≥ 4.5:1 สำหรับ Normal Text และ ≥ 3.0:1 สำหรับ Graphical Objects & Large Text)**

```
PromptMesh Color Spectrum:
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│  Primary Blue   │  Surface White  │  Neutral Gray   │ Semantic Danger │
│     #2563eb     │     #ffffff     │     #f0f2f5     │     #ef4444     │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

### 2.1 Master Color Tokens

| Token Name | Hex Code | HSL / RGB | Usage Context | WCAG Contrast |
|---|---|---|---|---|
| `--pm-primary` | `#2563eb` | `rgb(37, 99, 235)` | ปุ่มหลัก (CTA), หมุดตำแหน่งผู้ใช้, ขอบสถานะ Active | 4.6:1 บน `#ffffff` |
| `--pm-primary-hover` | `#1d4ed8` | `rgb(29, 78, 216)` | สภาวะ Hover ของ Primary Button | 6.1:1 บน `#ffffff` |
| `--pm-primary-active` | `#1e40af` | `rgb(30, 64, 175)` | สภาวะ Pressed / Active ของปุ่ม | 8.2:1 บน `#ffffff` |
| `--pm-primary-light` | `#eff6ff` | `rgb(239, 246, 255)` | พื้นหลัง Active State, แท็กที่ถูกเลือก, การ์ด Highlight | N/A (Background) |
| `--pm-primary-subtle` | `#dbeafe` | `rgb(219, 234, 254)` | เส้นขอบโฟกัส (Focus Ring), ปุ่มแบบ Secondary | N/A (Border/Surface) |
| `--pm-bg` | `#f0f2f5` | `rgb(240, 242, 245)` | พื้นหลังหลักของแอปพลิเคชัน (Soft Gray แบบ Apple OS) | N/A (Root BG) |
| `--pm-surface` | `#ffffff` | `rgb(255, 255, 255)` | พื้นหลัง Card, Bottom Sheet, Modal, Input Field | N/A (Canvas) |
| `--pm-surface-trans` | `rgba(255, 255, 255, 0.85)` | `blur(12px)` | กระจกฝ้า Glassmorphic สำหรับ Floating Bars บนแผนที่ | N/A (Glass Surface) |
| `--pm-border` | `#e8ecf1` | `rgb(232, 236, 241)` | เส้นขอบการ์ดบาง 1px, เส้นคั่น Divider | 1.2:1 บน `#ffffff` |
| `--pm-border-focus`| `#93c5fd` | `rgb(147, 197, 253)` | เส้นขอบ Input เมื่อถูก Focus | 2.1:1 บน `#ffffff` |
| `--pm-text-primary` | `#0f172a` | `rgb(15, 23, 42)` | ตัวอักษรเนื้อหาหลัก (Slate 900), หัวข้อทั้งหมด | 16.2:1 บน `#ffffff` |
| `--pm-text-secondary`| `#475569` | `rgb(71, 85, 105)` | คำอธิบายรอง, Metadata, Placeholder, Subtitle | 5.8:1 บน `#ffffff` |
| `--pm-text-muted` | `#94a3b8` | `rgb(148, 163, 184)` | ตัวอักษรระบุเวลา (Timestamp), ข้อความช่วยเหลือแบบจาง | 2.7:1 (Icon/Meta only) |

### 2.2 Semantic Status Colors (สีสื่อความหมายเชิงวิกฤต)

| Status | Solid Color | Light Background | Border Color | ความหมายในระบบ D2C Mesh |
|---|---|---|---|---|
| **Danger (วิกฤต/น้ำท่วม)** | `#ef4444` (`--pm-danger`) | `#fef2f2` | `#fecaca` | แจ้งเตือนน้ำท่วมสูง (>40 cm), พื้นที่ถูกตัดขาด, ถนนปิด |
| **Warning (เฝ้าระวัง)** | `#f59e0b` (`--pm-warning`) | `#fffbeb` | `#fde68a` | ระดับน้ำปานกลาง (15–40 cm), จุดเสี่ยงฝนตกหนัก |
| **Success (ปลอดภัย/สำเร็จ)**| `#10b981` (`--pm-success`) | `#ecfdf5` | `#a7f3d0` | เส้นทางปลอดภัย, ร้านค้าเปิดทำการ, การสแกน E-Voucher สำเร็จ |
| **Info (ข้อมูลทั่วไป)** | `#0284c7` (`--pm-info`) | `#f0f9ff` | `#bae6fd` | ข้อมูลอัปเดตระบบ, ตำแหน่งจุดอพยพ, การซิงก์ข้อมูลออฟไลน์ |

---

## 3. Typography Scale & Hierarchy (ระบบตัวอักษร)

ระบบตัวอักษรใช้ฟอนต์ **"Kanit"** (คณิณ) เป็นฟอนต์หลักทั้งระบบ เนื่องจากมีโครงสร้างเรขาคณิตแบบโมเดิร์น ไร้หัว (Loopless) สัดส่วนช่องไฟโปร่ง อ่านภาษาไทยและอังกฤษได้อย่างลื่นไหลบนจอความละเอียดสูง

### 3.1 Font Configuration

```css
@import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');

:root {
  --font-family-base: 'Kanit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  --font-feature-settings: 'cv02', 'cv03', 'cv04', 'cv11';
}
```

### 3.2 Master Type Scale Table

| Level / Token | Size (Mobile / Desktop) | Line Height | Weight | Letter Spacing | Use Cases & Description |
|---|---|---|---|---|---|
| **Display** (`--text-display`) | 32px (2.0rem) / 40px (2.5rem) | 1.20 | 700 (Bold) | -0.02em | ตัวเลขสถิติสรุปยอดเงิน E-Voucher รวม, สรุปผู้ประสบภัย |
| **Heading 1** (`--text-h1`) | 24px (1.5rem) / 28px (1.75rem) | 1.25 | 600 (SemiBold)| -0.015em | หัวข้อหน้าหลัก (Homepage), ชื่อโมดูลหลัก Track 6, 5, 2 |
| **Heading 2** (`--text-h2`) | 20px (1.25rem) / 24px (1.5rem) | 1.30 | 600 (SemiBold)| -0.01em | หัวข้อในการ์ดสรุปสถานการณ์, หัวข้อ Bottom Sheet ขณะเปิดครึ่งจอ |
| **Heading 3** (`--text-h3`) | 18px (1.125rem) / 20px (1.25rem)| 1.35 | 600 (SemiBold)| 0 | ชื่อร้านค้า Micro-Relief Station, ชื่อประเภทพาหนะนำทาง |
| **Heading 4** (`--text-h4`) | 16px (1.0rem) / 18px (1.125rem) | 1.40 | 500 (Medium)  | 0 | หัวข้อย่อยในฟอร์ม, ชื่อชั้นเลเยอร์แผนที่ (Map Layer Item) |
| **Heading 5** (`--text-h5`) | 15px (0.9375rem) / 16px (1.0rem)| 1.40 | 500 (Medium)  | 0 | ป้ายกำกับกลุ่มข้อมูล (Section Label), ชื่อสเต็ปการนำทาง |
| **Heading 6** (`--text-h6`) | 14px (0.875rem) / 14px (0.875rem)| 1.40 | 500 (Medium)  | +0.01em | ตัวกำกับกลุ่มข้อมูลย่อย, หัวข้อตารางสถิติขนาดเล็ก |
| **Body Large** (`--text-body-lg`) | 16px (1.0rem) / 16px (1.0rem) | 1.50 | 400 (Regular) | 0 | ข้อความแจ้งเตือนภัยด่วน (Alert Description), รายละเอียดคูปอง |
| **Body Regular** (`--text-body`) | 14px (0.875rem) / 14px (0.875rem)| 1.50 | 400 (Regular) | 0 | เนื้อหาทั่วไป, ที่อยู่ร้านค้า, รายละเอียดเส้นทาง Turn-by-Turn |
| **Body Small** (`--text-body-sm`)| 13px (0.8125rem) / 13px (0.8125rem)| 1.45 | 400 (Regular) | 0 | ข้อความเสริมประกอบการค้นหา, รายการสินค้าสต็อกย่อย |
| **Button Label** (`--text-btn`) | 15px (0.9375rem) / 15px (0.9375rem)| 1.00 | 500 (Medium)  | +0.01em | ข้อความบนปุ่มกด Primary/Secondary/Action CTA |
| **Caption / Subtext** (`--text-caption`)| 12px (0.75rem) / 12px (0.75rem)| 1.40 | 300 (Light) / 400 | +0.02em | Timestamp วันเวลาอัปเดตข้อมูลเซนเซอร์, หมายเหตุออฟไลน์ |
| **Overline / Badge** (`--text-badge`)| 11px (0.6875rem) / 11px (0.6875rem)| 1.00 | 600 (SemiBold)| +0.05em | ป้ายสถานะร้านค้า (Store Status Tag), ป้ายประเภทยานพาหนะ |

---

## 4. Spacing, Sizing & Grid System (ระยะห่างและระบบกริด)

ระบบโครงสร้างใช้ **8-Point Grid System** โดยมี **4-Point Half-Grid Step** สำหรับส่วนประกอบขนาดเล็ก (Micro-spacing) เพื่อความแม่นยำในสัดส่วนของ Mobile Device

### 4.1 Spacing Scale

| Step Token | Size (px) | Size (rem) | Typical Implementation |
|---|---|---|---|
| `--pm-space-1` | 4px | 0.25rem | ระยะห่างไอคอนกับข้อความใน Badge, Padding ของ Tag ขนาดเล็ก |
| `--pm-space-2` | 8px | 0.5rem | Gap ระหว่างปุ่มแนวนอน, Padding ภายใน Input แบบ Compact |
| `--pm-space-3` | 12px | 0.75rem | ระยะห่างระหว่าง Icon กับ Text ใน List Item, Card Compact Padding |
| `--pm-space-4` | 16px | 1.0rem | **Standard Screen Edge Padding (Mobile)**, Standard Card Padding |
| `--pm-space-5` | 20px | 1.25rem | Padding ภายใน Card หลัก, ช่องไฟระหว่าง Section บนหน้าจอ |
| `--pm-space-6` | 24px | 1.5rem | **Tablet Margin**, Header Bottom Margin, Bottom Sheet Handle Space |
| `--pm-space-8` | 32px | 2.0rem | **Desktop Margin**, ระยะห่างระหว่าง Block สำคัญ |
| `--pm-space-10` | 40px | 2.5rem | พื้นที่เว้นด้านล่างเพื่อหลบ Floating Action Button (FAB Offset) |
| `--pm-space-12` | 48px | 3.0rem | ความสูงมาตรฐานของ Touch Target สำหรับปุ่มกดหลัก |
| `--pm-space-16` | 64px | 4.0rem | ความสูงของ Navigation Bar / Glassmorphic Floating Top Bar |

### 4.2 Layout Grid & Breakpoints

ระบบ Responsive ยึดหลัก **Mobile-First** โดยจัดสรรคอลัมน์และขอบหน้าจอดังนี้:

```
Mobile Layout (360px - 639px):
├── 16px margin ──[ Col 1 ][ Col 2 ][ Col 3 ][ Col 4 ]── 16px margin ──┤

Desktop Layout (≥ 1024px, Max-width 1280px):
├── 32px ──[ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ][ 8 ][ 9 ][ 10 ][ 11 ][ 12 ]── 32px ──┤
```

| Breakpoint | Window Width Range | Columns | Gutter | Page Margin | Layout Behavior |
|---|---|---|---|---|---|
| **Mobile (`sm`)** | `360px` – `639px` | 4 | 12px | 16px | Full-screen Map พร้อม Collapsible Bottom Sheet เลื่อนจากขอบล่าง |
| **Tablet (`md`)** | `640px` – `1023px` | 8 | 16px | 24px | Map เต็มจอ พร้อม Floating Left Drawer ขนาดกว้าง 380px พับเก็บได้ |
| **Desktop (`lg`)** | `≥ 1024px` | 12 | 24px | 32px (Max 1280px) | Split View: แผนที่ 65% + Side Operational Panel 35% ทางขวา |

### 4.3 Emergency Ergonomics & Touch Target Rules

*   **Minimum Touch Target Size:** ทุกปุ่มที่สามารถกดได้ (Interactive Target) ต้องมีขนาดอย่างน้อย **48 x 48 px** (ตามแนวทาง Apple HIG และ Android Accessibility) แม้ไอคอนจะมีขนาดเพียง 24px ก็ต้องมี Hit Area ขยายออกไป
*   **One-Hand Thumb Zone:** วางปุ่ม CTA หลัก เช่น `Find Safe Route`, `Scan QR to Redeem`, และปุ่ม `AI Assistant FAB` ให้อยู่ในระยะ 1/3 ล่างของหน้าจอมือถือเสมอ เพื่อให้กดได้ด้วยมือเดียวขณะถือสัมภาระหรือเดินทาง

---

## 5. Elevation, Radii & Glassmorphism (มิติ ความโค้ง และกระจกฝ้า)

### 5.1 Border Radius Tokens

```css
:root {
  --pm-radius-sm: 8px;     /* Small tags, micro badges, tooltips */
  --pm-radius-md: 12px;    /* Text inputs, select boxes, dropdown menus */
  --pm-radius-lg: 16px;    /* Standard content cards, dialog boxes */
  --pm-radius-xl: 20px;    /* Highlight cards, map action overlays */
  --pm-radius-sheet: 24px; /* Collapsible Bottom Sheet (top corners only: 24px 24px 0 0) */
  --pm-radius-pill: 9999px;/* Pill buttons, search bars, status chips */
}
```

### 5.2 Soft UI Shadow Tokens (Apple OS Style)

เงาในระบบ PromptMesh จะเน้นความนุ่ม ไม่มีความคมชัดของขอบเงา (Diffused Ambient Light) เพื่อให้ความรู้สึกโปร่งเบา:

```css
:root {
  /* Level 1: Flat cards on soft gray background */
  --pm-shadow-1: 0 2px 8px rgba(15, 23, 42, 0.04), 0 1px 2px rgba(15, 23, 42, 0.02);

  /* Level 2: Interactive cards, Hovered elements */
  --pm-shadow-2: 0 4px 16px rgba(15, 23, 42, 0.06), 0 2px 4px rgba(15, 23, 42, 0.03);

  /* Level 3: Floating UI over Google Maps (Search bar, Layer selector) */
  --pm-shadow-3: 0 8px 24px rgba(15, 23, 42, 0.08), 0 2px 6px rgba(15, 23, 42, 0.04);

  /* Level 4: Collapsible Bottom Sheet, Modal popups */
  --pm-shadow-4: 0 12px 32px rgba(15, 23, 42, 0.12), 0 4px 12px rgba(15, 23, 42, 0.06);

  /* AI FAB Glow Shadow (Solid Blue Accent glow) */
  --pm-shadow-fab: 0 6px 20px rgba(37, 99, 235, 0.35), 0 2px 6px rgba(37, 99, 235, 0.20);
}
```

### 5.3 Glassmorphism Specifications (สำหรับ Floating Map UI)

ส่วนควบคุมแผนที่ (เช่น Search Bar, Timeline Slider, Filter Pills) ต้องไม่บดบังแผนที่ทึบ 100%:

```css
.pm-glass-panel {
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: blur(14px) saturate(180%);
  -webkit-backdrop-filter: blur(14px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.65);
  box-shadow: var(--pm-shadow-3);
}

/* Fallback สำหรับเบราว์เซอร์ที่ไม่รองรับ backdrop-filter */
@supports not ((-webkit-backdrop-filter: blur(14px)) or (backdrop-filter: blur(14px))) {
  .pm-glass-panel {
    background: rgba(255, 255, 255, 0.96);
  }
}
```

---

## 6. Iconography System (ระบบไอคอนเวกเตอร์)

PromptMesh กำหนดมาตรฐานชุดไอคอนเวกเตอร์เส้นเรียบ **(Lucide Icons)** โดยมีขนาดและข้อกำหนดทางเทคนิคที่แน่นอน:

*   **Stroke Width:** `1.75px` (สม่ำเสมอทุกขนาด)
*   **Corner Join & Cap:** `round` (ปลายมน เข้ากับ Soft UI)
*   **Icon Bounding Boxes:** `16x16px`, `20x20px`, `24x24px`, `32x32px`
*   ❌ **Strict Anti-Pattern:** ห้ามแทรก Unicode Emoji ปนในข้อความหรือปุ่มโดยเด็ดขาด

### 6.1 Standardized Icon Mapping Matrix

| 功能 / หมวดหมู่ | ไอคอน Lucide | การใช้งานในระบบ PromptMesh |
|---|---|---|
| **AI Assistant (FAB)** | `bot` / `sparkles` | ปุ่ม Floating Action Button สำหรับเรียกผู้ช่วยอัจฉริยะ |
| **Track 6: Hazard Map** | `layers` | สลับเปิด/ปิดเลเยอร์ ระดับน้ำ, ปริมาณฝน, ระดับความสูงถนน |
| **Track 6: Water Level** | `waves` / `droplets` | ระบุสถานะระดับน้ำท่วมขัง |
| **Track 6: Rain Telemetry** | `cloud-rain` | ข้อมูลฝนตกจาก TMD Radar |
| **Track 6: Time Forecast** | `clock` / `history` | ตัวควบคุมสไลเดอร์คาดการณ์ 1h, 3h, 6h |
| **Track 6: Subscribe Alert** | `bell-plus` | ปุ่มติดตามการแจ้งเตือนระดับซอย |
| **Track 6: Isolation Zone** | `shield-alert` | สัญลักษณ์แจ้งเตือนจุดถูกตัดขาดเป็นเกาะ |
| **Track 5: Sedan/Motorcycle** | `car` | ตัวเลือกยานพาหนะ: รถทั่วไป (ลุยน้ำ ≤ 15 ซม.) |
| **Track 5: Lifted Pickup** | `truck` | ตัวเลือกยานพาหนะ: รถยกสูง (ลุยน้ำ ≤ 40 ซม.) |
| **Track 5: Boat / Jet Ski** | `ship` | ตัวเลือกยานพาหนะ: เรือท้องแบน/เจ็ตสกี |
| **Track 5: Safe Routing** | `navigation` / `route` | เริ่มต้นระบบนำทางอัจฉริยะหลบเลี่ยงน้ำ |
| **Track 5: Crowdsource Report**| `camera` / `flag` | ปุ่มรายงานน้ำท่วมและสิ่งกีดขวางเส้นทาง |
| **Track 2: Micro-Relief Store**| `store` | หมุดร้านค้า SME ที่เปิดทำการและน้ำไม่ท่วม |
| **Track 2: E-Voucher Wallet** | `wallet-cards` | กระเป๋าคูปองเยียวยาดิจิทัล |
| **Track 2: QR Scanner** | `scan` / `qr-code` | เปิดกล้องสแกน QR รับของ / ร้านค้าสร้าง QR |
| **Track 2: Stock Restock** | `package-check` | ข้อมูลสต็อกเสบียงและการแนะนำสั่งซื้อ |
| **General: Location** | `map-pin` | หมุดระบุพิกัดปัจจุบันของผู้ใช้ |
| **General: Emergency SOS** | `phone-call` | ปุ่มโทรด่วนสายด่วนฉุกเฉิน (1784 / 1669) |

---

## 7. UI Component States & Behaviors (สภาวะคอมโพเนนต์และการโต้ตอบ)

### 7.1 Buttons (ระบบปุ่มกด)

ทุกปุ่มมีความสูงมาตรฐาน `48px` สำหรับ Mobile (`44px` สำหรับ Secondary Desktop) และโค้งมน `12px`:

```
Button Anatomy & States:
┌──────────────────────────────────────────────┐
│  [Icon]   Button Label Text                  │
└──────────────────────────────────────────────┘
Default     -> Solid Blue (#2563eb), White Text
Hover       -> Darker Blue (#1d4ed8), Light Elevation
Active      -> Deep Blue (#1e40af), Scale 0.98 Transform
Disabled    -> Neutral Gray (#e2e8f0), Slate Text (#94a3b8)
Loading     -> Spinner Icon replacing leading icon, Pointer-events: none
```

```css
/* Master Button System */
.pm-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--pm-space-2);
  height: 48px;
  padding: 0 var(--pm-space-5);
  background-color: var(--pm-primary);
  color: #ffffff;
  font-family: var(--font-family-base);
  font-size: var(--text-btn);
  font-weight: 500;
  border-radius: var(--pm-radius-md);
  border: none;
  cursor: pointer;
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 4px rgba(37, 99, 235, 0.15);
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}

.pm-btn-primary:hover {
  background-color: var(--pm-primary-hover);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
}

.pm-btn-primary:active {
  background-color: var(--pm-primary-active);
  transform: scale(0.98);
}

.pm-btn-primary:focus-visible {
  outline: 2px solid var(--pm-primary);
  outline-offset: 2px;
}

.pm-btn-primary:disabled {
  background-color: #e2e8f0;
  color: var(--pm-text-muted);
  box-shadow: none;
  cursor: not-allowed;
  transform: none;
}

/* Secondary Button (Soft Blue / Surface) */
.pm-btn-secondary {
  height: 48px;
  padding: 0 var(--pm-space-5);
  background-color: var(--pm-primary-light);
  color: var(--pm-primary);
  border: 1px solid var(--pm-primary-subtle);
  border-radius: var(--pm-radius-md);
  font-weight: 500;
}
.pm-btn-secondary:hover {
  background-color: #dbeafe;
}

/* Danger Button (For Emergency Actions) */
.pm-btn-danger {
  height: 48px;
  background-color: var(--pm-danger);
  color: #ffffff;
  border-radius: var(--pm-radius-md);
}
.pm-btn-danger:hover {
  background-color: #dc2626;
}
```

### 7.2 Form Inputs & Controls (ฟอร์มและตัวรับข้อมูล)

*   **Text & Search Inputs:** ความสูง `48px`, Background `#ffffff`, Border `1px solid #e8ecf1`, Border Radius `12px`
    *   **Focus State:** Border เปลี่ยนเป็น `#2563eb`, Box-shadow `0 0 0 3px rgba(37, 99, 235, 0.15)`
    *   **Error State:** Border เปลี่ยนเป็น `#ef4444`, Box-shadow `0 0 0 3px rgba(239, 68, 68, 0.15)`
*   **Timeline Slider Control (AI Forecaster):**
    *   Track: ความสูง `6px`, สี `#e2e8f0`
    *   Active Progress Track: สี `#2563eb`
    *   Thumb: วงกลมขนาด `24x24px`, สี `#ffffff`, Border `3px solid #2563eb`, Shadow `0 2px 8px rgba(0,0,0,0.15)`
    *   Snap Marks: จุดมาร์กตำแหน่ง 1h, 3h, 6h มีตัวเลขกำกับด้านล่าง
*   **Toggle Switch:**
    *   ขนาด `48x28px`, Pill shape (`border-radius: 9999px`)
    *   Off: Background `#cbd5e1`, Knob `#ffffff` (22px) อยู่ทางซ้าย
    *   On: Background `#2563eb`, Knob `#ffffff` เลื่อนไปทางขวาพร้อม Animation `transition: 0.2s cubic-bezier(0.34, 1.56, 0.64, 1)`

---

## 8. Z-Index Hierarchy & Stacking Context (ลำดับชั้นการซ้อนทับ)

เพื่อป้องกันปัญหา Stacking Context ซ้อนทับกันระหว่างแผนที่ Google Maps, หมุดพิกัด, แถบกระจกฝ้า, Bottom Sheet, และ Modal ได้จัดสรรระดับความสูงมาตรฐานดังนี้:

| Layer Level | Z-Index | Component Name / Description |
|---|---|---|
| **Base Map** | `0` | Google Maps Canvas / WebGL Layer |
| **Map Overlays** | `10` | GeoJSON Polygons (แนวเขตน้ำท่วม, Heatmap ฝน, แนวถนนปลอดภัย) |
| **Map Markers** | `20` | หมุดพิกัดผู้ใช้ (Current Location), หมุดร้านค้า SME, หมุดสิ่งกีดขวาง |
| **Floating Controls** | `30` | ปุ่มควบคุมแผนที่, Map Layer Toggles, Compass, Recenter Button |
| **Timeline Slider** | `40` | แถบเลื่อนเวลา AI 3-Hour Forecast Bar ด้านล่างแผนที่ |
| **Top Glass Bar** | `60` | แถบค้นหาสถานที่ (Search Bar), แถบสถานะ GPS/Network Indicator |
| **AI FAB Button** | `70` | Floating Action Button สำหรับเรียก Assistant (ขวาล่าง) |
| **Collapsible Sheet**| `100` | Bottom Sheet (แสดงข้อมูลเส้นทาง, รายละเอียดร้านค้า, รายการเสบียง) |
| **Backdrop Overlays**| `500` | ม่านสีดำโปร่งแสง (`rgba(15, 23, 42, 0.45)`) เมื่อเปิด Modal หรือ Drawer |
| **Modal / Dialogs** | `600` | หน้าต่างสแกน QR Scanner, หน้ายืนยันการอพยพ, Popup เปลี่ยนเส้นทาง |
| **Emergency Alerts** | `900` | Risk Alert Banner, Isolation Warning Bar (แถบเตือนสีแดงด้านบนสุด) |
| **System Toasts** | `1000` | Toast แจ้งเตือนสถานะการเชื่อมต่อ (Offline Banner / Sync Completed) |

---

## 9. Responsive Breakpoints & Adaptive Layouts (การปรับเปลี่ยนตามอุปกรณ์)

```
        Mobile (< 640px)                    Desktop (≥ 1024px)
┌───────────────────────────────┐   ┌───────────────────────┬───────────┐
│ [Top Glass Search Bar]        │   │ [Top Nav Header]      │ [User Profile]│
│                               │   ├───────────────────────┼───────────┤
│                               │   │                       │ Side      │
│         Google Maps           │   │      Google Maps      │ Panel     │
│         Full View             │   │       (65% width)     │ (35% width│
│                               │   │                       │ Detailed  │
│ [AI FAB]                      │   │                       │ Routing & │
├───────────────────────────────┤   │                       │ Vouchers) │
│ ═════ Bottom Sheet Handle ═══ │   │ [Floating Layer Pill] │           │
│ Collapsible Sheet Content     │   │                       │           │
└───────────────────────────────┘   └───────────────────────┴───────────┘
```

### 9.1 Adaptive Logic

*   **Mobile (< 640px):**
    *   แผนที่เปิดเต็มจอ 100vh ตลอดเวลา
    *   เนื้อหาหลัก (รายการคูปอง, ข้อมูลเส้นทาง, ตัวเลือกยานพาหนะ) บรรจุอยู่ใน **Collapsible Bottom Sheet** ซึ่งสามารถปัดพับเก็บเพื่อดูแผนที่ได้สูงสุด
*   **Tablet (640px – 1023px):**
    *   แผนที่แสดงผลเต็มจอเป็นพื้นหลัง
    *   Bottom Sheet ถูกเปลี่ยนเป็น **Floating Left Card / Drawer** กว้างคงที่ `380px` สามารถคลิกยุบเก็บไปชิดขอบซ้ายได้
*   **Desktop (≥ 1024px):**
    *   Split-Screen แบบ Google Maps Desktop: ฝั่งซ้ายคือแผนที่ความละเอียดสูง (65%) ฝั่งขวาคือ Control Center & Management Console (35%)
    *   แสดงข้อมูล Live Feed, ภาพรวม E-Voucher, และรายงานความเสียหายแบบ Dashboard

---

## 10. Key Custom Components Blueprint (พิมพ์เขียวคอมโพเนนต์สำคัญ)

### 10.1 Collapsible Bottom Sheet (หัวใจหลักของ Mobile Navigation)

*   **ลักษณะทางกายภาพ:** ขอบบนโค้งมน `border-radius: 24px 24px 0 0`, พื้นหลัง `#ffffff`, เงา `--pm-shadow-4`
*   **Handle Bar:** แท่งจับตรงกลางขนาดกว้าง `36px` สูง `4px` สี `#cbd5e1` โค้งมนแบบ Pill สำหรับลากสัมผัส
*   **Snap Points (3 ระดับตามท่าทางสัมผัส):**
    1.  **Minimized (สูง 72px):** แสดงเฉพาะ Handle Bar และข้อมูลสำคัญ 1 บรรทัด เช่น *"มวลน้ำกำลังมาใน 2 ชม. [ค้นหาเส้นทางหนีน้ำ]"* คืนพื้นที่ 90% ให้แผนที่
    2.  **Half (สูง 42% vh):** แสดงรายการสรุป เช่น การ์ดตัวเลือกยานพาหนะ หรือข้อมูลร้านค้าที่เลือก
    3.  **Expanded (สูง 88% vh):** แสดงรายละเอียดแบบเต็ม เช่น สเต็ปการนำทาง Turn-by-Turn หรือรายการสินค้าเสบียงทั้งหมด

```css
/* Bottom Sheet CSS Architecture */
.pm-bottom-sheet {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--pm-surface);
  border-radius: var(--pm-radius-sheet);
  box-shadow: var(--pm-shadow-4);
  z-index: 100;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  touch-action: none;
  padding: var(--pm-space-3) var(--pm-space-4) var(--pm-space-6);
  padding-bottom: calc(var(--pm-space-6) + env(safe-area-inset-bottom));
}

.pm-bottom-sheet-handle {
  width: 36px;
  height: 4px;
  background-color: #cbd5e1;
  border-radius: var(--pm-radius-pill);
  margin: 0 auto var(--pm-space-3);
  cursor: grab;
}
```

### 10.2 Dedicated AI Assistant FAB (Floating Action Button)

*   **มิติและรูปทรง:** วงกลมสมบูรณ์แบบขนาดเส้นผ่านศูนย์กลาง `56 x 56 px`
*   **ตำแหน่ง:** ลอยอยู่มุมขวาล่าง ห่างจากขอบขวา `16px` และสูงเหนือ Bottom Sheet `24px` (`z-index: 70`)
*   **สีและเอฟเฟกต์:** สี Solid Blue (`#2563eb`) ตัวไอคอนเวกเตอร์ Lucide `sparkles` หรือ `bot` สีขาวขนาด `24px`
*   **เงา:** ใช้เงาเรืองแสงสีฟ้า `--pm-shadow-fab: 0 6px 20px rgba(37, 99, 235, 0.35)`
*   **สถานะทำงาน:** ขณะ AI กำลังประมวลผลเส้นทางหรือคำนวณระดับน้ำ จะมีวงแหวนกระพริบแบบ Pulse Animation ล้อมรอบปุ่ม

```css
.pm-ai-fab {
  position: fixed;
  right: 16px;
  bottom: calc(88px + env(safe-area-inset-bottom));
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background-color: var(--pm-primary);
  color: #ffffff;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--pm-shadow-fab);
  z-index: 70;
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.pm-ai-fab:active {
  transform: scale(0.92);
}
```

### 10.3 Vehicle Selector Segmented Card (Track 5: Crisis Routing)

การ์ดแนวนอนบรรจุ 3 ตัวเลือกประเภทยานพาหนะ เพื่อคำนวณ Clearance Limit อัตโนมัติ:

```
┌─────────────────┬─────────────────┬─────────────────┐
│   [Car Icon]    │  [Truck Icon]   │   [Ship Icon]   │
│   รถเก๋ง/มอเตอร์ไซค์ │   กระบะยกสูง    │ เรือ/เจ็ตสกี    │
│    (ลุยได้ ≤15ซม.)  │   (ลุยได้ ≤40ซม.)   │  (แนวน้ำท่วมลึก) │
└─────────────────┴─────────────────┴─────────────────┘
```

*   **Active Item:** กรอบสีฟ้า Solid Blue (`#2563eb`), พื้นหลังสีฟ้าอ่อน (`#eff6ff`), ไอคอนและตัวหนังสือสีฟ้าเข้ม
*   **Inactive Item:** พื้นหลังสีเทาอ่อน (`#f8fafc`), กรอบสีเทาจาง (`#e2e8f0`), ตัวหนังสือสีเทาเข้ม (`#475569`)

### 10.4 Store Status Tag & Micro-Relief Badge (Track 2: E-Voucher)

ป้ายระบุสถานะร้านค้าชุมชนที่แสดงบนหมุดแผนที่และหน้าร้าน:

*   **Tag "พร้อมแจกจ่ายเสบียง" (Active Relief Station):**
    *   Background: `#ecfdf5` (Success Light)
    *   Text & Icon: `#059669` (Success Dark)
    *   Border: `1px solid #a7f3d0`
    *   Icon: Lucide `package-check` (ขนาด 14px)
*   **Tag "น้ำไม่ท่วม" (Flood-Free Access):**
    *   Background: `#eff6ff` (Primary Light)
    *   Text & Icon: `#2563eb` (Solid Blue)
    *   Border: `1px solid #bfdbfe`
    *   Icon: Lucide `shield-check` (ขนาด 14px)

---

## 11. Implementation Reference (Tailwind CSS Config)

สำหรับทีมนักพัฒนา Frontend สามารถคัดลอก Configuration ต่อไปนี้ลงใน `tailwind.config.js` ได้ทันที:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,jsx,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        pm: {
          primary: '#2563eb',
          'primary-hover': '#1d4ed8',
          'primary-active': '#1e40af',
          'primary-light': '#eff6ff',
          'primary-subtle': '#dbeafe',
          bg: '#f0f2f5',
          surface: '#ffffff',
          border: '#e8ecf1',
          'text-main': '#0f172a',
          'text-muted': '#475569',
          'text-light': '#94a3b8',
          danger: '#ef4444',
          'danger-bg': '#fef2f2',
          warning: '#f59e0b',
          'warning-bg': '#fffbeb',
          success: '#10b981',
          'success-bg': '#ecfdf5',
        },
      },
      fontFamily: {
        kanit: ['Kanit', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
      borderRadius: {
        'card': '16px',
        'card-lg': '20px',
        'btn': '12px',
        'sheet': '24px',
      },
      boxShadow: {
        'soft-1': '0 2px 8px rgba(15, 23, 42, 0.04), 0 1px 2px rgba(15, 23, 42, 0.02)',
        'soft-2': '0 4px 16px rgba(15, 23, 42, 0.06), 0 2px 4px rgba(15, 23, 42, 0.03)',
        'glass': '0 8px 24px rgba(15, 23, 42, 0.08), 0 2px 6px rgba(15, 23, 42, 0.04)',
        'fab': '0 6px 20px rgba(37, 99, 235, 0.35), 0 2px 6px rgba(37, 99, 235, 0.20)',
        'sheet': '0 12px 32px rgba(15, 23, 42, 0.12), 0 4px 12px rgba(15, 23, 42, 0.06)',
      },
    },
  },
  plugins: [],
};
```
