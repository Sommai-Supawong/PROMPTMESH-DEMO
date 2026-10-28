"""
PromptMesh Master Project Document Generator
Author: Solution Architect & Technical Writer
Output: PromptMesh_Master_Document.docx
Description: Complete boardroom-grade Word document synthesizing all project documentation
             for the PromptMesh (Hyperlocal D2C Mesh) initiative.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def build_master_document():
    doc = docx.Document()

    # =========================================================================
    # PAGE SETUP & MARGINS
    # =========================================================================
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

    # =========================================================================
    # GLOBAL TYPOGRAPHY & COLOR PALETTE
    # =========================================================================
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Kanit'
    font.size = Pt(10.5)
    font.color.rgb = RGBColor(15, 23, 42) # Slate 900
    style_normal.paragraph_format.line_spacing = 1.2
    style_normal.paragraph_format.space_after = Pt(4)

    # Corporate Executive Palette
    NAVY = RGBColor(30, 58, 138)        # #1E3A8A (Display/Title)
    DEEP_BLUE = RGBColor(30, 64, 175)    # #1E40AF (Heading 1)
    PRIMARY_BLUE = RGBColor(37, 99, 235) # #2563EB (Heading 2 / Primary Action)
    DARK_SLATE = RGBColor(30, 41, 59)    # #1E293B (Heading 3 / Body Emphasized)
    TEXT_MUTED = RGBColor(71, 85, 105)   # #475569 (Secondary Text / Captions)
    DANGER_RED = RGBColor(239, 68, 68)   # #EF4444 (Risk / Alert)
    SUCCESS_GREEN = RGBColor(16, 185, 129)# #10B981 (Success / Safe)
    WARNING_AMBER = RGBColor(245, 158, 11)# #F59E0B (Warning)

    # =========================================================================
    # XML FORMATTING HELPERS
    # =========================================================================
    def set_cell_background(cell, hex_color):
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/>'
            f'<w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/>'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)

    def format_table(table, col_widths, hdr_bg="1E40AF", alt_bg="F8FAFC", border_color="CBD5E1"):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="1E40AF"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

        for i, row in enumerate(table.rows):
            is_header = (i == 0)
            bg = hdr_bg if is_header else (alt_bg if i % 2 == 1 else "FFFFFF")
            for j, cell in enumerate(row.cells):
                cell.width = col_widths[j]
                set_cell_background(cell, bg)
                set_cell_margins(cell, top=130, bottom=130, left=150, right=150)
                for p in cell.paragraphs:
                    p.paragraph_format.line_spacing = 1.15
                    p.paragraph_format.space_after = Pt(2)
                    p.paragraph_format.space_before = Pt(2)
                    for run in p.runs:
                        run.font.name = 'Kanit'
                        if is_header:
                            run.font.bold = True
                            run.font.color.rgb = RGBColor(255, 255, 255)
                            run.font.size = Pt(9.5)
                        else:
                            run.font.size = Pt(9.0)

    def add_callout(text, title=None, alert_type="info"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        
        bg_color = "EFF6FF" if alert_type == "info" else ("FEF2F2" if alert_type == "danger" else "FFFBEB")
        border_c = "2563EB" if alert_type == "info" else ("EF4444" if alert_type == "danger" else "F59E0B")
        
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=160)
        
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="none"/>'
            f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_c}"/>'
            f'<w:bottom w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.18
        p.paragraph_format.space_after = Pt(2)
        if title:
            r_title = p.add_run(f"[{title}] ")
            r_title.bold = True
            r_title.font.name = 'Kanit'
            r_title.font.size = Pt(10)
            r_title.font.color.rgb = PRIMARY_BLUE if alert_type == "info" else (DANGER_RED if alert_type == "danger" else WARNING_AMBER)
        
        r_text = p.add_run(text)
        r_text.font.name = 'Kanit'
        r_text.font.size = Pt(9.5)
        r_text.font.italic = True
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_h1(text):
        h = doc.add_heading(text, level=1)
        h.paragraph_format.space_before = Pt(20)
        h.paragraph_format.space_after = Pt(6)
        h.paragraph_format.keep_with_next = True
        for r in h.runs:
            r.font.name = 'Kanit'
            r.font.size = Pt(17.5)
            r.font.bold = True
            r.font.color.rgb = DEEP_BLUE
        return h

    def add_h2(text):
        h = doc.add_heading(text, level=2)
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        for r in h.runs:
            r.font.name = 'Kanit'
            r.font.size = Pt(13.5)
            r.font.bold = True
            r.font.color.rgb = PRIMARY_BLUE
        return h

    def add_h3(text):
        h = doc.add_heading(text, level=3)
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(3)
        h.paragraph_format.keep_with_next = True
        for r in h.runs:
            r.font.name = 'Kanit'
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = DARK_SLATE
        return h

    def add_bullet(lead, body):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        r_lead = p.add_run(lead)
        r_lead.bold = True
        r_lead.font.name = 'Kanit'
        r_lead.font.color.rgb = DARK_SLATE
        r_body = p.add_run(body)
        r_body.font.name = 'Kanit'

    # =========================================================================
    # DOCUMENT COVER / METADATA HEADER
    # =========================================================================
    p_badge = doc.add_paragraph()
    p_badge.paragraph_format.space_after = Pt(2)
    r_badge = p_badge.add_run("AI FOR ALL THAILAND INNOVATION SPRINT — PILLAR: RESILIENCE COMMUNITIES")
    r_badge.font.size = Pt(8.5)
    r_badge.font.bold = True
    r_badge.font.color.rgb = PRIMARY_BLUE

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(2)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("PROMPTMESH: HYPERLOCAL DISASTER-TO-COMMERCE (D2C) MESH")
    r_title.font.size = Pt(23)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(10)
    r_sub = p_sub.add_run(
        "Master Project Architecture, Feature Specifications, Design System, & Operational Roadmap\n"
        "เอกสารข้อกำหนดเชิงเทคนิคและสถาปัตยกรรมระบบฉบับสมบูรณ์ (Boardroom Master Document)"
    )
    r_sub.font.size = Pt(11.5)
    r_sub.font.color.rgb = TEXT_MUTED

    meta_tbl = doc.add_table(rows=5, cols=2)
    meta_widths = [Inches(2.2), Inches(4.3)]
    meta_data = [
        ("Platform Architecture", "Mobile-First Progressive Web App (PWA) with 4-Layer Offline-First Resilience"),
        ("Strategic Core Formula", "เตือนภัยตรงจุด (Track 6) → เดินทางปลอดภัย (Track 5) → เสบียงหมุนเวียนด้วยเงินท้องถิ่น (Track 2)"),
        ("Target Pilot Region", "Nakhon Pathom & Bangkok Perimeter (ลุ่มน้ำท่าจีน / พื้นที่รอยต่อนครปฐมและกรุงเทพฯ)"),
        ("Ecosystem Integration", "PromptPay (National ITMX), Krungthai Open API (เป๋าตัง/ถุงเงิน), TMD, HII, RID, GISTDA"),
        ("Project Status & Budget", "Conditional Go (70% Confidence) | 12-Month Pilot Budget: ฿4,900,000 – ฿9,500,000 (~$140k–$270k USD)")
    ]
    for row_idx, (k, v) in enumerate(meta_data):
        row = meta_tbl.rows[row_idx]
        row.cells[0].paragraphs[0].add_run(k).bold = True
        row.cells[1].paragraphs[0].add_run(v)
    format_table(meta_tbl, meta_widths, hdr_bg="1E3A8A", alt_bg="F1F5F9")
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =========================================================================
    # SECTION 1: EXECUTIVE SUMMARY & STRATEGIC VISION
    # =========================================================================
    add_h1("1. Executive Summary & Vision (บทสรุปผู้บริหารและวิสัยทัศน์เชิงยุทธศาสตร์)")
    
    doc.add_paragraph(
        "PromptMesh (Hyperlocal Disaster-to-Commerce Mesh) คือ แพลตฟอร์มรับมือภัยพิบัติอัจฉริยะแบบบูรณาการระดับชุมชนย่อย "
        "ซึ่งได้รับการพัฒนาขึ้นเพื่อปฏิวัติวงจรการจัดการอุทกภัยของประเทศไทย จากเดิมที่พึ่งพาการสงเคราะห์แบบรวมศูนย์ (Centralized Relief) "
        "ที่ล่าช้า สิ้นเปลือง และตัดขาดระบบเศรษฐกิจฐานราก ไปสู่โมเดลกระจายศูนย์ที่กระตุ้นเศรษฐกิจชุมชนอย่างยั่งยืน "
        "แพลตฟอร์มทำหน้าที่เป็น 'สะพานเชื่อมต่อวงจรบรรเทาสาธารณภัยสู่เศรษฐกิจชุมชน' โดยหลอมรวม 3 แทร็กเทคโนโลยีหลักเข้าเป็นหนึ่งเดียว:"
    )

    add_bullet("1. เตือนภัยตรงจุด (Track 6 - Resilient Communities): ", 
               "ระบบพยากรณ์และเตือนภัยล่วงหน้า 3–6 ชั่วโมงในระดับซอยย่อย (Hyperlocal Nowcasting) โดยผสานข้อมูลเรดาร์ฝนเชิงปริมาณ (QPE) "
               "จากกรมอุตุนิยมวิทยา ข้อมูลระดับน้ำโทรมาตรจาก สสน. (HII) และข้อมูลภูมิประเทศความละเอียดสูง (DEM) จาก GISTDA เข้าสู่แบบจำลอง AI Hydrology Engine "
               "เพื่อขจัดปัญหาคำเตือนเหวี่ยงแหรายจังหวัดที่ทำให้ประชาชนเกิดภาวะชาชิน (Cry-Wolf Fatigue)")
    
    add_bullet("2. เดินทางปลอดภัย (Track 5 - Smart Mobility): ", 
               "ระบบนำทางอัจฉริยะแบบปรับเปลี่ยนตามขีดจำกัดยานพาหนะ (Vehicle-Aware Dynamic Clearance Routing) "
               "คำนวณระดับน้ำท่วมผิวทางแบบเรียลไทม์ และตัดเส้นทางที่น้ำท่วมเกินความปลอดภัยของยานพาหนะแต่ละประเภทโดยอัตโนมัติ: "
               "รถเก๋ง/มอเตอร์ไซค์ (Clearance ≤15 ซม.), รถกระบะยกสูง (Clearance ≤40 ซม.), และเรือท้องแบน/เจ็ตสกี (>30 ซม. ในแนวคลอง/ถนนน้ำท่วมมิด) "
               "ป้องกันปัญหารถจมน้ำและการกีดขวางภารกิจกู้ภัย")
    
    add_bullet("3. เสบียงหมุนเวียนด้วยเงินท้องถิ่น (Track 2 - SME & Local Economy): ", 
               "ระบบคูปองเยียวยาดิจิทัลแบบกระจายศูนย์ (Decentralized E-Voucher) ที่เปลี่ยนร้านโชห่วยและตลาดสดในพื้นที่ปลอดภัยให้กลายเป็น 'สถานีเสบียงย่อย (Micro-Relief Stations)' "
               "โดยเงินบริจาคและงบภาครัฐจะถูกโอนตรงสู่กระเป๋าเงินดิจิทัลของผู้ประสบภัย เพื่อนำไปสแกนรับสินค้าจำเป็นผ่านระบบพร้อมเพย์ (PromptPay) "
               "ช่วยให้ผู้ประสบภัยได้รับของที่ต้องการทันที และร้านค้าท้องถิ่นมีรายได้หมุนเวียนพยุงกิจการในช่วงวิกฤต")

    add_callout(
        "Architectural Principle: 'Integration-over-Invention' — PromptMesh ไม่สร้างโครงสร้างพื้นฐานคู่ขนานที่สิ้นเปลืองงบประมาณ "
        "แต่เชื่อมต่อโครงสร้างดิจิทัลที่แข็งแกร่งที่สุดของประเทศไทยเข้าด้วยกัน ได้แก่ โครงข่าย PromptPay (74 ล้านธุรกรรม/วัน), "
        "ระบบ Krungthai Open API (ผู้ใช้งานเป๋าตัง 40 ล้านคน), สถานีโทรมาตร สสน. (4,000+ จุด), และภาพถ่ายดาวเทียม Sentinel-1/GISTDA",
        title="Integration-over-Invention Principle"
    )

    add_h2("การแก้ปัญหา 'สร้างแล้วทิ้ง' ด้วย 365-Day Disaster-to-Commerce Continuum")
    doc.add_paragraph(
        "บทเรียนสำคัญจากแอปพลิเคชันภัยพิบัติในอดีตคือ 'ภาวะสร้างแล้วทิ้ง (Built and Abandoned Syndrome)' "
        "เมื่อระดับน้ำลดลง ประชาชนและร้านค้าจะลบแอปทิ้ง ส่งผลให้ฐานข้อมูลกระจัดกระจายและขาดความต่อเนื่อง "
        "PromptMesh แก้ไขจุดอ่อนนี้ด้วยการออกแบบให้เป็น 'Disaster-to-Commerce Continuum': "
        "ในช่วงที่ไม่มีน้ำท่วม (Non-Disaster Period) แพลตฟอร์มจะสลับโหมดสู่ 'อปท. Welfare & Community Commerce Hub' "
        "เพื่อทำหน้าที่เป็นโครงสร้างพื้นฐานในการกระจายสวัสดิการขององค์กรปกครองส่วนท้องถิ่น (เทศบาล และ อบต. กว่า 7,800 แห่งทั่วประเทศ) "
        "เช่น คูปองอาหารกลางวันนักเรียน, เบี้ยยังชีพผู้สูงอายุ, และคูปองกระตุ้นเศรษฐกิจตลาดนัดชุมชน "
        "ทำให้ประชาชนและร้านค้ามีการใช้งานอย่างต่อเนื่องสม่ำเสมอตลอดทั้ง 365 วัน และพร้อมรับมือทันทีเมื่อเกิดภัยรอบถัดไป"
    )

    # =========================================================================
    # SECTION 2: PROBLEM STATEMENT & MARKET CONTEXT
    # =========================================================================
    add_h1("2. Problem Statement & Market Context (ปัญหาเชิงระบบและบริบทตลาด)")
    
    doc.add_paragraph(
        "แม้ประเทศไทยจะมีการลงทุนมหาศาลในระบบตรวจวัดอุทกวิทยา แต่ข้อมูลเหล่านั้นยังคง 'ติดค้างอยู่ที่ส่วนกลาง' "
        "และไม่สามารถแปลงเป็นการปฏิบัติการในระดับชุมชนได้อย่างทันท่วงที งานวิจัยและรายงานการตรวจสอบข้อเท็จจริงชี้ชัดถึงความล้มเหลวเชิงโครงสร้าง:"
    )

    stat_tbl = doc.add_table(rows=5, cols=3)
    stat_widths = [Inches(1.4), Inches(2.3), Inches(2.8)]
    stat_data = [
        ("Stat / Metric", "Finding Source & Verification", "Systemic Impact on Disaster Response"),
        ("72.31%", "สำนักงานการตรวจเงินแผ่นดิน (สตง.) ตรวจสอบเหตุการณ์น้ำท่วม 195 ครั้ง (2564–2567)", "ชุมชนกว่า 72.31% เผชิญกับน้ำท่วมโดยไม่มีการแจ้งเตือนภัยล่วงหน้า คำเตือนกระจุกตัวที่ระดับจังหวัด ไม่ระบุซอยหรือเวลาที่มวลน้ำจะเข้าท่วม"),
        ("60.66%", "รายงานผลการตรวจสอบสถานีเตือนภัยของ สตง. (ปี 2567)", "สถานีโทรมาตรเตือนภัยกว่า 60.66% ติดตั้งอยู่นอกพื้นที่เสี่ยงภัยจริง ทำให้ข้อมูลเซนเซอร์ตัดขาดจากสภาพน้ำท่วมขังบนถนนในเขตชุมชน"),
        ("41.90%", "รายงานพฤติกรรมการรับข่าวสารภัยพิบัติ (สำนักงานสถิติแห่งชาติ)", "ประชาชน 41.90% ในพื้นที่กึ่งเมืองกึ่งชนบทพึ่งพาการสื่อสารจากผู้นำชุมชนและหอกระจายข่าวมากกว่าสมาร์ทโฟน สะท้อนว่าแอปทั่วไปเข้าไม่ถึงผู้ใช้"),
        ("฿1.44 Trillion", "ความเสียหายสะสมจากอุทกภัย (ธนาคารโลก & สภาพัฒน์)", "ความเสียหายมหาศาลซ้ำซากทำลายเงินทุนหมุนเวียนของร้านค้า SME ท้องถิ่น ร้านค้าถูกตัดขาดและขาดสภาพคล่องจนต้องปิดกิจการถาวร")
    ]
    for row_idx, row_values in enumerate(stat_data):
        row = stat_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(stat_tbl, stat_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("ความล้มเหลวของโมเดลสงเคราะห์แบบรวมศูนย์ (The Centralized Relief Bottleneck)")
    doc.add_paragraph(
        "ระบบบรรเทาทุกข์ในปัจจุบันสร้างความสูญเสียทางเศรษฐกิจซ้ำซ้อนผ่านคอขวด 3 ประการหลัก: "
        "(1) ความล่าช้าในการจัดส่ง: ถุงยังชีพส่วนกลางต้องใช้เวลาจัดซื้อ ขนส่ง และคัดแยก 24–72 ชั่วโมง ซึ่งช้าเกินไปในสภาวะวิกฤต "
        "(2) ของแจกไม่ตรงความต้องการ: ถุงยังชีพสำเร็จรูปมักบรรจุเฉพาะบะหมี่กึ่งสำเร็จรูปและปลากระป๋อง แต่ขาดแคลนผ้าอ้อมเด็ก ยารักษาโรคประจำตัว นมผง หรือแผ่นรองซับ "
        "และ (3) ทำลายระบบการค้าท้องถิ่น: เม็ดเงินจัดซื้อไหลเข้าสู่ซัพพลายเออร์รายใหญ่ส่วนกลาง ในขณะที่ร้านค้าโชห่วยและตลาดสดในพื้นที่ต้องปิดตัว สินค้าเน่าเสีย และขาดรายได้โดยสิ้นเชิง"
    )

    add_h2("การวิเคราะห์ช่องว่างเชิงเปรียบเทียบ (Competitive Landscape Analysis)")
    doc.add_paragraph(
        "ตารางเปรียบเทียบขีดความสามารถระหว่างระบบเตือนภัยและแพลตฟอร์มที่มีอยู่ในปัจจุบัน กับ PromptMesh:"
    )

    comp_tbl = doc.add_table(rows=9, cols=6)
    comp_widths = [Inches(1.8), Inches(0.9), Inches(0.9), Inches(1.0), Inches(1.0), Inches(0.9)]
    comp_data = [
        ("Platform", "Hyperlocal Warning", "Vehicle Clearance", "E-Voucher Relief", "Offline Mode", "365-Day Utility"),
        ("One Map Water (รัฐบาล)", "ระดับลุ่มน้ำ", "ไม่มี", "ไม่มี", "ไม่มี", "เฝ้าระวังน้ำ"),
        ("ThaiWater (สสน./HII)", "ระดับสถานี", "ไม่มี", "ไม่มี", "ไม่มี", "ดูข้อมูลน้ำ"),
        ("DPM Reporter (ปภ.)", "ระดับอำเภอ", "ไม่มี", "ไม่มี", "ไม่มี", "แจ้งเหตุภัย"),
        ("TMD Smart Life (อุตุนิยมฯ)", "ระดับจังหวัด", "ไม่มี", "ไม่มี", "ไม่มี", "พยากรณ์อากาศ"),
        ("Traffy Fondue", "ระดับจุดเกิดเหตุ", "ไม่มี", "ไม่มี", "ไม่มี", "ร้องเรียนทั่วไป"),
        ("Google Maps / Waze", "ไม่มีระดับน้ำ", "ไม่แยกประเภท", "ไม่มี", "แคชจำกัด", "นำทางปกติ"),
        ("Grab / LINE MAN", "ไม่มี", "งดส่งช่วงท่วม", "คูปองส่วนลด", "ไม่มี", "เดลิเวอรี"),
        ("PromptMesh (D2C Mesh)", "ระดับซอย (3-6 ชม.)", "เก๋ง/กระบะ/เรือ", "PromptPay SME", "4-Layer Stack", "อปท. สวัสดิการ")
    ]
    for row_idx, row_values in enumerate(comp_data):
        row = comp_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(comp_tbl, comp_widths, hdr_bg="1E40AF", alt_bg="F1F5F9")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("กรณีศึกษาต้นแบบระดับสากลและความพร้อมด้านฟินเทคของไทย")
    doc.add_paragraph(
        "PromptMesh พัฒนาขึ้นโดยต่อยอดจากบทเรียนความสำเร็จระดับสากล: "
        "(1) FloodMapp + Waze (Norfolk, Virginia) พิสูจน์ว่าการซ้อนทับแบบจำลองน้ำท่วมแบบไดนามิกลงบนแผนที่นำทางสามารถลดอุบัติเหตุรถจมน้ำได้อย่างมีประสิทธิภาพ "
        "(2) UN World Food Programme (WFP) Building Blocks และ Oxfam UnBlocked Cash พิสูจน์ว่าการแจกคูปองดิจิทัลช่วยให้ผู้ประสบภัยฟื้นตัวได้เร็วกว่าการแจกสิ่งของถึง 3 เท่า "
        "ทั้งนี้ ประเทศไทยมีความได้เปรียบทางโครงสร้างฟินเทคเหนือกว่าต่างประเทศอย่างเด่นชัด: "
        "ระบบ PromptPay มีบัญชีลงทะเบียนกว่า 83 ล้านเลขหมาย มีธุรกรรม 74 ล้านรายการต่อวัน และประชาชนกว่า 40 ล้านคนคุ้นเคยกับการใช้แอปเป๋าตัง/ถุงเงิน "
        "ในโครงการ 'คนละครึ่ง' ทำให้ PromptMesh สามารถเชื่อมต่อกระเป๋าเงินเยียวยาเข้ากับพฤติกรรมเดิมของประชาชนได้ทันที"
    )

    # =========================================================================
    # SECTION 3: SOLUTION ARCHITECTURE & USER ROLES
    # =========================================================================
    add_h1("3. Solution Architecture & User Roles (สถาปัตยกรรมระบบและบทบาทผู้ใช้งาน)")
    
    doc.add_paragraph(
        "PromptMesh ออกแบบภายใต้สถาปัตยกรรมคลาวด์แบบ Serverless Microservices ควบคู่กับ Mobile-First Progressive Web App (PWA) "
        "รองรับการใช้งานผ่าน 4 บทบาทหลักอย่างเป็นเอกภาพ:"
    )

    role_tbl = doc.add_table(rows=5, cols=3)
    role_widths = [Inches(1.8), Inches(2.2), Inches(2.5)]
    role_data = [
        ("User Role", "Core Responsibilities & Capabilities", "Tailored UI/UX Presentation"),
        ("1. Resident\n(ประชาชนในพื้นที่เสี่ยง)", 
         "รับการแจ้งเตือนภัยระดับซอยล่วงหน้า 3–6 ชม., วางแผนอพยพตามขีดจำกัดรถ, สแกน E-Voucher รับเสบียงจำเป็นที่ร้านค้าใกล้บ้าน", 
         "Citizen View: หน้าหลักสรุปยอดเงินคูปอง, การ์ดระดับน้ำในซอยตนเอง, และปุ่ม CTA นำทางปลอดภัย"),
        ("2. Rescue Team\n(ทีมกู้ภัย / อาสาสมัคร)", 
         "ค้นหาเส้นทางปลอดภัยตามประเภทพาหนะ, กรองระดับน้ำลึก, รายงานสิ่งกีดขวาง/ถนนขาด, ปักหมุดผู้ป่วยติดเตียงที่ต้องการความช่วยเหลือ", 
         "Operations View: แผนที่ยุทธการเต็มจอทันที, เครื่องมือ Dispatcher, ตัวกรองระดับน้ำ, และปุ่มถ่ายภาพรายงานเหตุ"),
        ("3. SME Merchant\n(ร้านค้าชุมชน / โชห่วย)", 
         "เปลี่ยนร้านเป็น 'Micro-Relief Station', สร้าง QR รับเงินจากคูปองเยียวยา, สลับสถานะความพร้อมของร้าน, รับคำแนะนำสต็อกสินค้าหลังน้ำลด", 
         "Merchant View: แดชบอร์ดสรุปยอดสแกนรับเงิน, ปุ่มสลับสถานะ ('พร้อมแจกเสบียง' / 'น้ำไม่ท่วม'), และระบบจัดการสต็อก"),
        ("4. Donor & Gov / อปท.\n(ผู้บริจาค / เทศบาล / อบต.)", 
         "อัดฉีดงบประมาณเยียวยาเจาะจงระดับซอย (Geo-targeted Injection), บริหารงบสวัสดิการชุมชน 365 วัน, ตรวจสอบความโปร่งใสแบบ Real-time", 
         "Governance Portal: Heatmap ความต้องการเสบียง, ฟอร์มอัดฉีดเงินเข้าสู่ซอยเป้าหมาย, และแดชบอร์ดวัดผลความโปร่งใสแบบเรียลไทม์")
    ]
    for row_idx, row_values in enumerate(role_data):
        row = role_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(role_tbl, role_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("วงจรการทำงานตลอดช่วงเวลาภัยพิบัติ (5-Phase Disaster Continuum)")
    doc.add_paragraph("การทำงานของแพลตฟอร์มจะปรับเปลี่ยนไปตาม 5 ช่วงเวลาของภัยพิบัติอย่างสอดคล้อง:")
    add_bullet("Phase 1: Normal Season (ช่วงเวลาปกติ 365 วัน): ", 
               "แพลตฟอร์มทำงานในโหมด 'อปท. Welfare & Community Commerce' เชื่อมโยงงบสวัสดิการท้องถิ่น เช่น อาหารกลางวันและเบี้ยผู้สูงอายุ "
               "สร้างความคุ้นเคยในการสแกนใช้งาน และ AI ทำการรวบรวมข้อมูลอุทกวิทยาพื้นฐานอย่างต่อเนื่อง")
    add_bullet("Phase 2: Warning Phase (ช่วงเตือนภัย 3–6 ชม. ก่อนท่วม): ", 
               "AI Hydrology Engine ตรวจพบมวลน้ำหลากและฝนตกหนัก แจ้งเตือนแบบเฉพาะเจาะจงระดับซอยผ่าน Push Notification และ SMS "
               "ประชาชนเปิดแอปดูการจำลองระดับน้ำท่วมผ่าน Timeline Slider")
    add_bullet("Phase 3: Evacuation & Mobility Phase (ช่วงอพยพและสัญจร): ", 
               "ผู้ใช้ระบุประเภทยานพาหนะ (เก๋ง/กระบะ/เรือ) ระบบ Dynamic Clearance Routing นำทางหลีกเลี่ยงถนนน้ำท่วมลึก "
               "หรือนำทางไปยังจุดปลอดภัยยกสูงใกล้เคียงทันทีหากชุมชนเสี่ยงถูกตัดขาดเป็นเกาะ")
    add_bullet("Phase 4: Sustenance & Grassroots Relief Phase (ช่วงน้ำท่วมขัง): ", 
               "อปท. และผู้บริจาคอัดฉีดงบตรงเข้า E-Voucher Wallet ประชาชนเดินหรือใช้เรือไปรับเสบียงที่ร้าน Micro-Relief Station ที่ใกล้และปลอดภัย "
               "ร้านค้าได้รับเงินโอนเข้าบัญชีผ่านระบบธนาคารกรุงไทยทันที")
    add_bullet("Phase 5: Recovery & Restocking Phase (ช่วงน้ำลดและฟื้นฟู): ", 
               "AI ทำการประเมินความเสียหายเชิงพื้นที่และออก Restock Recommendation Card ให้ร้านค้าสั่งซื้อวัสดุซ่อมแซมและน้ำยาทำความสะอาดเข้าสต็อกอย่างแม่นยำ")

    # =========================================================================
    # SECTION 4: DETAILED FEATURE SPECIFICATIONS
    # =========================================================================
    add_h1("4. Detailed Feature Specifications (ข้อกำหนดฟีเจอร์เชิงลึก)")
    
    doc.add_paragraph(
        "รายละเอียดข้อกำหนดการทำงานทั้งหมดแบ่งตามโครงสร้าง MoSCoW Prioritization "
        "โดยผสานความต้องการระหว่างคู่มือฟีเจอร์และระบบการออกแบบอย่างสมบูรณ์:"
    )

    add_h2("Track 6: Hyperlocal Early Warning (เตือนภัยตรงจุด)")
    add_bullet("P0-01: Hyperlocal Hazard Map (แผนที่จำลองความเสี่ยงเชิงพื้นที่): ",
               "แผนที่ความละเอียดสูงบน Google Maps Base Canvas ที่ผสาน GeoJSON Polygons แสดงระดับน้ำท่วมขัง (0–15 ซม., 16–40 ซม., >40 ซม.), "
               "ข้อมูลเรดาร์ฝน TMD (QPE) อัปเดตทุก 15 นาที, และเส้นชั้นความสูงถนน (DEM) "
               "มีแถบเครื่องมือ Map Layer Toggle สำหรับสลับชั้นข้อมูล และ Location Pin พร้อมสถานะความเสี่ยง (Safe=เขียว, Warning=ส้ม, Danger=แดง)")
    
    add_bullet("P0-02: AI 3-Hour Forecaster (ระบบคาดการณ์ระดับน้ำล่วงหน้า): ",
               "แบบจำลอง AI Hydrology Nowcasting จำลองการไหลบ่าของน้ำล่วงหน้า 1, 3, และ 6 ชั่วโมง ควบคุมผ่าน Glassmorphic Timeline Slider "
               "หากระดับน้ำในซอยมีแนวโน้มท่วมเกิน 15 ซม. ใน 3 ชม. แถบ Risk Alert Banner สีแดงกระพริบจะแสดงขึ้นทันที "
               "พร้อมปุ่ม Subscribe Alert ('ติดตามแจ้งเตือนซอยนี้') เพื่อให้ญาติที่อยู่ต่างจังหวัดติดตามสถานะทาง SMS ได้")
    
    add_bullet("P0-03: Isolation Alert & Encirclement Detector (ระบบตรวจจับพื้นที่ถูกตัดขาดเป็นเกาะ): ",
               "วิเคราะห์โครงข่ายถนน (Road Graph Network) เพื่อตรวจสอบพื้นที่ที่ทางเข้าออกทั้งหมดถูกน้ำท่วมมิด "
               "แสดง Highlight Zone สีแดงกระพริบ และเปิดปุ่ม Evacuation Route ('ค้นหาเส้นทางอพยพด่วน') "
               "เพื่อนำทางประชาชนออกจากพื้นที่ก่อนเส้นทางสุดท้ายจะถูกตัดขาดล่วงหน้าไม่น้อยกว่า 90 นาที")
    
    add_bullet("P0-10: Multi-Channel Alert Gateway (เกตเวย์แจ้งเตือนหลายช่องทาง): ",
               "ระบบส่งการแจ้งเตือนภัยผ่าน Push Notification สำหรับผู้ใช้ PWA, SMS Gateway ผ่าน AWS SNS, "
               "และรองรับการประสานงานระบบ Cell Broadcast ของ กสทช. สำหรับส่งข้อความฉุกเฉินระดับเสาสัญญาณโดยไม่ต้องใช้อินเทอร์เน็ต")

    add_h2("Track 5: Smart Mobility / Crisis Routing (เดินทางปลอดภัย)")
    add_bullet("P0-04: Vehicle-Specific Dispatch (ระบบนำทางตามขีดจำกัดยานพาหนะ): ",
               "การ์ด Vehicle Selector Segmented Card ให้ผู้ใช้เลือกประเภทพาหนะ 3 ระดับ: "
               "(1) รถเก๋ง/มอเตอร์ไซค์ (Clearance ≤15 ซม.) — อัลกอริทึมตัดถนนที่มีน้ำท่วมเกิน 15 ซม. ทิ้งทันที (Penalty = Infinity); "
               "(2) รถกระบะยกสูง/4WD (Clearance ≤40 ซม.) — อนุญาตให้ผ่านน้ำ 15–40 ซม. ได้ แต่ปรับลดความเร็วเฉลี่ยเหลือ 15 กม./ชม.; "
               "(3) เรือท้องแบน/เจ็ตสกี (Clearance >30 ซม.) — เปลี่ยนเส้นทางไปใช้แนวคลองและถนนสายหลักที่น้ำท่วมมิด")
    
    add_bullet("P0-05: Dynamic Clearance Routing & Mid-Route Reroute (ระบบเปลี่ยนเส้นทางเรียลไทม์): ",
               "ระหว่างนำทาง หากมีมวลน้ำทะลักเข้าสู่ถนนข้างหน้า ระบบจะแสดง Dynamic Reroute Alert Modal: "
               "'พบน้ำท่วมสูง 28 ซม. ข้างหน้าในอีก 400 ม. (เกินขีดจำกัดรถของคุณ) — เปลี่ยนเส้นทางเดี๋ยวนี้? (เลี่ยงเพิ่ม 1.2 กม.)' "
               "หากทางออกทั้งหมดถูกตัดขาด ระบบจะเข้าสู่โหมด 'No Safe Exit' และนำทางไปยังจุดปลอดภัยยกสูงใกล้เคียง (วัด, โรงเรียนสองชั้น)")
    
    add_bullet("P0-05 Sub-module: Crowdsourced Road Obstruction Reporter: ",
               "ฟังก์ชันให้กู้ภัยและประชาชนถ่ายภาพและปักหมุดจุดน้ำท่วมลึกหรือสิ่งกีดขวาง มีตัวเลือกระดับน้ำแบบเข้าใจง่าย (ข้อเท้า, หัวเข่า, เอว, มิดหลังคารถ) "
               "พร้อมระบบ Weighted Consensus ให้น้ำหนักรายงานจากกู้ภัยที่ยืนยันตัวตนแล้ว (Verified Rescue) สูงกว่าประชาชนทั่วไป 3 เท่า")

    add_h2("Track 2: SME & Local Economy / Decentralized Relief (เสบียงหมุนเวียนด้วยเงินท้องถิ่น)")
    add_bullet("P0-06: Micro-Relief Station Locator (แผนที่สถานีเสบียงชุมชน): ",
               "หมุดแสดงร้านค้า SME ในพื้นที่ปลอดภัยที่เข้าร่วมโครงการ พร้อมป้าย Store Status Tag: "
               "ป้ายสีเขียว ('พร้อมแจกเสบียง'), ป้ายสีฟ้า ('น้ำไม่ท่วมทางเข้าร้าน'), และตัวนับสต็อกสินค้าเรียลไทม์ (เช่น 'น้ำดื่มเหลือ 45 แพ็ค')")
    
    add_bullet("P0-07 & P0-12: Decentralized E-Voucher Wallet & Krungthai/PromptPay Integration: ",
               "กระเป๋าเงินเยียวยาดิจิทัลที่เชื่อมต่อกับ Krungthai Open API และ PromptPay QR: "
               "ฝั่งประชาชน: แสดงยอดเงินเยียวยาและปุ่ม 'สแกนเพื่อรับเสบียง' สร้าง Dynamic Single-Use HMAC-SHA256 Token หมดอายุใน 60 วินาที ป้องกันการทุจริต; "
               "ฝั่งร้านค้า: ปุ่ม 'สร้าง QR รับเงิน' และแสดงประวัติการรับเสบียงเพื่อรอการเคลมเงินโอนเข้าบัญชีจากธนาคารกรุงไทย")
    
    add_bullet("P1-05: อปท. Welfare Voucher & Year-Round Commerce Mode: ",
               "ฟังก์ชันสลับโหมดสู่การกระจายสวัสดิการชุมชน 365 วัน สำหรับแจกคูปองอาหารกลางวัน เบี้ยคนชรา และคูปองกระตุ้นตลาดสดท้องถิ่น")
    
    add_bullet("P1-02: SME Economic Recovery & Restock Dashboard: ",
               "ระบบ AI แนะนำรายการสั่งสินค้าฟื้นฟูหลังน้ำลด เช่น 'AI วิเคราะห์: ซอย 1-4 มีดินโคลนสะสม แนะนำสั่งอุปกรณ์ทำความสะอาดเพิ่ม 50% และปูนซีเมนต์เพิ่ม 30%'")
    
    add_bullet("P1-01: Donor & Gov Fund Injection Portal: ",
               "หน้าต่างสำหรับ ปภ. อปท. หรือมูลนิธิ เพื่อเลือกพื้นที่เป้าหมายระดับตำบล/ซอย และกดปุ่ม 'Inject Funds' เพื่อโอนเงินเยียวยาตรงสู่ประชาชน พร้อมแดชบอร์ดวัดผลความโปร่งใส")

    add_h2("รายการที่อยู่นอกขอบเขตของโครงการนำร่อง (Explicit Out-of-Scope - WON'T HAVE)")
    doc.add_paragraph("เพื่อควบคุมความเสี่ยงและกรอบเวลาในการส่งมอบโครงการนำร่อง 12 เดือน รายการต่อไปนี้ถูกกำหนดให้อยู่นอกขอบเขตอย่างชัดเจน:")
    w_tbl = doc.add_table(rows=5, cols=3)
    w_widths = [Inches(1.0), Inches(2.3), Inches(3.2)]
    w_data = [
        ("ID", "Excluded Capability", "Architectural Rationale for Exclusion"),
        ("W-01 & W-03", "การสร้าง Payment Gateway หรือขอใบอนุญาต E-Money เอง", "หลีกเลี่ยงข้อจำกัด พ.ร.บ.ระบบการชำระเงิน พ.ศ. 2560 โดยใช้การเชื่อมต่อผ่าน Krungthai Open API และ PromptPay ที่มีใบอนุญาตถูกต้องอยู่แล้ว"),
        ("W-02", "การติดตั้งโครงข่ายฮาร์ดแวร์เซนเซอร์วัดน้ำของตนเอง", "ยึดหลัก Software-First ดึงข้อมูลจากสถานีโทรมาตร สสน. (HII), กรมชลฯ, และเรดาร์ฝน TMD ที่มีอยู่แล้ว 4,000+ จุด"),
        ("W-04", "ระบบบล็อกเชน (Blockchain Transaction Ledger)", "ระบบ PromptPay และโครงข่าย ITMX ของไทยมีความเร็วและความน่าเชื่อถือสูงเพียงพอ การใช้บล็อกเชนจะเพิ่มความหน่วงและค่าใช้จ่ายโดยไม่จำเป็น"),
        ("W-07 & W-08", "การพัฒนา Native App (iOS/Android) และการใช้ AI Gradients", "เลือกใช้ PWA เพื่อการอัปเดตฉุกเฉินโดยไม่ต้องรอ App Store Review และใช้ดีไซน์ Clean White + Solid Blue เพื่อความน่าเชื่อถือระดับสถาบัน")
    ]
    for row_idx, row_values in enumerate(w_data):
        row = w_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(w_tbl, w_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =========================================================================
    # SECTION 5: UI/UX DESIGN SYSTEM
    # =========================================================================
    add_h1("5. UI/UX Design System (ระบบการออกแบบและสเปกส่วนต่อประสาน)")
    
    doc.add_paragraph(
        "ระบบการออกแบบของ PromptMesh พัฒนาขึ้นโดยคำนึงถึง 'สภาวะวิกฤต (Crisis Usability)' เป็นหัวใจสำคัญ "
        "ผู้ใช้งานต้องเผชิญกับสถานการณ์น้ำท่วม ความตึงเครียด แสงแดดจ้า หรือฝนตกหนัก ดังนั้น UI ต้องส่งมอบความรู้สึก "
        "มั่นคง น่าเชื่อถือ เข้าถึงง่าย และลดภาระการประมวลผลทางสายตา (Cognitive Load) สูงสุด:"
    )

    add_bullet("Soft UI (Apple OS Style): ", "โครงสร้างโค้งมน ผิวสัมผัสเนียนตา (Smooth Curvature) ใช้น้ำหนักเงาแบบ Soft Drop Shadows ที่ฟุ้งกระจายอย่างเป็นธรรมชาติ สร้างมิติการซ้อนทับแบบ Physical Depth โดยไม่ใช้สไตล์ Skeuomorphism ยุคเก่า")
    add_bullet("White & Solid Blue Theme: ", "ใช้สีฟ้าเข้มทึบ Solid Blue (#2563EB) เป็นสี Action หลักบนพื้นหลังสะอาดตา (Clean White / Soft Gray #F0F2F5) มอบความรู้สึกสงบ ปลอดภัย และน่าเชื่อถือระดับสถาบันการเงิน ไม่อนุญาตให้ใช้สีไล่เฉดนีออน (No AI Gradients)")
    add_bullet("Frosted Glassmorphism: ", "ชิ้นส่วน UI ที่ลอยอยู่เหนือแผนที่ (Floating Map Elements) ใช้เทคนิคกระจกฝ้าโปร่งแสง (backdrop-filter: blur(14px)) เพื่อให้ผู้ใช้ยังคงมองเห็นบริบทเชิงพื้นที่ (Spatial Context) ของแผนที่ด้านหลังตลอดเวลา")
    add_bullet("Strictly Vector Icons (Zero Emojis): ", "ห้ามใช้ Emoji ในส่วนประกอบ UI โดยเด็ดขาด เนื่องจากเรนเดอร์ไม่สม่ำเสมอในแต่ละอุปกรณ์ ให้ใช้ชุดไอคอนเวกเตอร์เส้นเรียบ Lucide Icons (ความหนาเส้น 1.75px ปลายมน) เท่านั้น")
    add_bullet("Kanit Typography System: ", "กำหนดใช้ฟอนต์ 'Kanit' (คณิณ) เป็นมาตรฐานทั้งภาษาไทยและอังกฤษ เนื่องจากมีโครงสร้างเรขาคณิตไร้หัว สัดส่วนโปร่ง อ่านง่าย ชัดเจนบนจอภาพความละเอียดสูงทุกระดับ")

    add_h2("ตารางตัวแปรระบบสีหลักและสถานะความปลอดภัย (Color Tokens)")
    color_tbl = doc.add_table(rows=7, cols=4)
    color_widths = [Inches(1.5), Inches(1.2), Inches(1.8), Inches(2.0)]
    color_data = [
        ("Token Name", "Hex / RGB", "Usage Context in PromptMesh", "WCAG 2.1 Contrast Ratio"),
        ("--pm-primary", "#2563EB", "Primary CTA Buttons, Current Location Marker, Active Focus", "4.6:1 (Pass AA บน #FFFFFF)"),
        ("--pm-primary-hover", "#1D4ED8", "Hover State ของปุ่มกดหลัก", "6.1:1 (Pass AAA บน #FFFFFF)"),
        ("--pm-surface-trans", "rgba(255,255,255,0.88)", "Frosted Glass Floating Panels (backdrop-filter: blur(14px))", "Glassmorphic Map Control Overlays"),
        ("--pm-danger", "#EF4444", "แจ้งเตือนน้ำท่วมสูง (>40 cm), พื้นที่ถูกตัดขาด, ปุ่มอพยพด่วน", "4.5:1 (Semantic Danger Status)"),
        ("--pm-warning", "#F59E0B", "แจ้งเตือนระดับน้ำปานกลาง (15–40 cm), จุดเสี่ยงฝนตกหนัก", "3.8:1 (Semantic Warning Status)"),
        ("--pm-success", "#10B981", "เส้นทางปลอดภัย, ร้านค้าเปิดทำการ, สแกนคูปองสำเร็จ", "4.5:1 (Semantic Success Status)")
    ]
    for row_idx, row_values in enumerate(color_data):
        row = color_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(color_tbl, color_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("ระบบลำดับชั้น Z-Index และการซ้อนทับ (Stacking Context)")
    doc.add_paragraph("เพื่อป้องกันปัญหา UI ทับซ้อนกันระหว่างแผนที่ Google Maps, แถบกระจกฝ้า, Bottom Sheet, และ Modal แจ้งเตือน ระบบจัดสรร Z-Index ดังนี้:")
    z_tbl = doc.add_table(rows=6, cols=3)
    z_widths = [Inches(1.2), Inches(1.8), Inches(3.5)]
    z_data = [
        ("Z-Index", "Component Name", "Role & Interaction Behavior"),
        ("0 – 10", "Base Map & Overlays", "Google Maps Canvas (0) ซ้อนทับด้วย GeoJSON Hazard Polygons ระดับน้ำท่วม (10)"),
        ("20 – 30", "Markers & Controls", "หมุด Location Pin ผู้ใช้, หมุดร้านค้า SME (20) และ Floating Map Controls (30)"),
        ("40 – 60", "Timeline & Search", "แถบเลื่อนเวลา AI Forecast Slider (40) และ Glassmorphic Search Bar ด้านบน (60)"),
        ("70 – 100", "AI FAB & Bottom Sheet", "Dedicated AI Assistant FAB (70) และ Collapsible Bottom Sheet (100)"),
        ("500 – 1000", "Modals & Emergency Alerts", "Backdrop Overlay (500), QR Scanner Modal (600), Risk Alert Banner (900), Toast (1000)")
    ]
    for row_idx, row_values in enumerate(z_data):
        row = z_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(z_tbl, z_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("พิมพ์เขียวคอมโพเนนต์สำคัญ (Key Custom UI Components)")
    add_bullet("Collapsible Bottom Sheet (หัวใจหลักของ Mobile Navigation): ", 
               "โครงสร้างขอบบนโค้งมน 24px พร้อม Handle Bar ขนาด 36x4px สามารถปัดสลับ Snap Points ได้ 3 ระดับ: "
               "(1) Minimized (72px) — แสดงเฉพาะข้อความสรุป 1 บรรทัด เพื่อคืนพื้นที่ 90% ให้แผนที่; "
               "(2) Half (42% vh) — แสดงการ์ดตัวเลือกยานพาหนะหรือร้านค้า; "
               "(3) Expanded (88% vh) — แสดงรายละเอียดการนำทาง Turn-by-Turn หรือรายการเสบียงทั้งหมด")
    
    add_bullet("Dedicated AI Assistant FAB (Floating Action Button): ", 
               "ปุ่มวงกลมสีฟ้า Solid Blue ขนาด 56x56px ลอยอยู่ขวาล่างเหนือ Bottom Sheet พร้อมไอคอน Lucide 'sparkles' สีขาว "
               "มีวงแหวน Pulse Animation ล้อมรอบขณะประมวลผล ให้คำแนะนำเชิงบริบทอัตโนมัติตามหน้าที่เปิดอยู่")
    
    add_bullet("Vehicle Selector Segmented Card: ", 
               "การ์ดเลือกพาหนะ 3 ช่องแนวนอน: รถเก๋ง/มอเตอร์ไซค์ (≤15 ซม.), กระบะยกสูง (≤40 ซม.), และเรือท้องแบน (>30 ซม.) มีขอบเน้นสีฟ้า Solid Blue เมื่อถูกเลือก")

    add_bullet("Store Status Tags & Relief Badges: ", 
               "ป้ายสถานะร้านค้าโค้งมน 8px ประกอบด้วยป้ายเขียว 'พร้อมแจกเสบียง' (Lucide 'package-check') และป้ายฟ้า 'น้ำไม่ท่วมทางเข้าร้าน' (Lucide 'shield-check')")

    # =========================================================================
    # SECTION 6: TECHNICAL STACK & OFFLINE-FIRST STRATEGY
    # =========================================================================
    add_h1("6. Technical Stack & Offline-First Strategy (สถาปัตยกรรมทางเทคนิคและกลยุทธ์ออฟไลน์)")
    
    doc.add_paragraph(
        "เมื่อเกิดอุทกภัยรุนแรง เสาสัญญาณโทรศัพท์และกระแสไฟฟ้ามักหยุดทำงานบางส่วน PromptMesh จึงใช้สถาปัตยกรรมความคงทน 4 ระดับ "
        "(4-Layer Graceful Degradation Architecture) เพื่อรับประกันความต่อเนื่องในการทำงาน 100%:"
    )

    res_tbl = doc.add_table(rows=5, cols=3)
    res_widths = [Inches(1.8), Inches(2.2), Inches(2.5)]
    res_data = [
        ("Resilience Tier", "Technologies & Implementation", "Operational Capability Under Severe Disruption"),
        ("Layer 1: PWA Edge Runtime\n(Local Storage)", 
         "Service Worker CacheStorage + IndexedDB (Web Crypto API) ควบคุมขนาดรวมไม่เกิน 50 MB", 
         "ทำงานในสมาร์ทโฟนได้ 100% แม้ไม่มีสัญญาณอินเทอร์เน็ต: แสดงแผนที่แคชรัศมี 15 กม., นำทางแบบ A* ออฟไลน์, และถือโทเคนคูปองเยียวยา"),
        ("Layer 2: Telecom Fallback\n(SMS & Broadcast)", 
         "NBTC Cell Broadcast Service (CBS) + AWS SNS SMS Gateway + รหัส USSD *484*...", 
         "ส่งข้อความเตือนภัยผ่านคลื่นวิทยุโทรศัพท์พื้นฐานโดยไม่ต้องพึ่งพาโมบายล์ดาต้า และรองรับการกดรหัส USSD รับเสบียงสำหรับผู้สูงอายุ"),
        ("Layer 3: Edge Computing\n(Local Station Hardware)", 
         "AWS IoT Greengrass รันบนมินิพีซีประจำสถานีเสบียง + โครงข่ายเซนเซอร์ LoRaWAN (5–15 กม.)", 
         "ประมวลผลโมเดลระดับน้ำในพื้นที่ได้ต่อเนื่องแม้คลาวด์จะขาดการติดต่อ และส่งข้อมูลซิงก์ขึ้นคลาวด์อัตโนมัติเมื่อสัญญาณฟื้นตัว"),
        ("Layer 4: Human & Mesh Relay\n(Community Mesh)", 
         "Wi-Fi Direct / Bluetooth Mesh ระหว่างสมาร์ทโฟน + หอกระจายข่าวประจำหมู่บ้าน", 
         "อาสาสมัคร อสม. และผู้นำชุมชนทำหน้าที่เป็นโหนดสื่อสาร กระจายข่าวเตือนภัยผ่านเสียงตามสาย และนำคูปองไปช่วยเหลือกลุ่มเปราะบาง")
    ]
    for row_idx, row_values in enumerate(res_data):
        row = res_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(res_tbl, res_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("การจัดสรรโควตาหน่วยความจำออฟไลน์ (Storage Quota Breakdown ≤ 50 MB)")
    doc.add_paragraph(
        "เพื่อให้สอดคล้องตามข้อกำหนด P1-04 และไม่สิ้นเปลืองพื้นที่จัดเก็บในโทรศัพท์ของประชาชน ข้อมูลทั้งหมดถูกจำกัดขนาดดังนี้: "
        "(1) App Shell & Assets: 8 MB (CacheStorage); "
        "(2) Local Map Vector Tiles (รัศมี 15 กม. รอบบ้าน): 20 MB (CacheStorage); "
        "(3) Offline Road Graph Topology: 12 MB (IndexedDB); "
        "(4) Encrypted Offline Voucher Tokens: 2 MB (Web Crypto API); "
        "(5) Cached Sensor Feeds: 1 MB (LocalStorage) — รวมทั้งสิ้นเพียง 43 MB (ต่ำกว่าเพดาน 50 MB)"
    )

    add_h2("ตารางการเชื่อมต่อ API ภายนอก (External API Integration Matrix)")
    api_tbl = doc.add_table(rows=8, cols=4)
    api_widths = [Inches(1.8), Inches(1.5), Inches(1.2), Inches(2.0)]
    api_data = [
        ("Agency / Provider", "Data Ingestion Endpoint", "Frequency", "Technical Protocol & Payload"),
        ("กรมอุตุนิยมวิทยา (TMD)", "Radar Rain Ingestion API (QPE)", "ทุก 15 นาที", "REST API (JSON / NetCDF Grid)"),
        ("สถาบันสารสนเทศทรัพยากรน้ำ (HII)", "Telemetry Canal Stations API", "ทุก 10 นาที", "REST API (JSON) ระดับน้ำและประตูระบาย"),
        ("กรมชลประทาน (RID)", "Upstream Dam Discharge API", "ทุก 1 ชั่วโมง", "REST API อัตราการระบายน้ำเขื่อนเจ้าพระยา"),
        ("GISTDA", "Sentinel-1 Flood Extent & DEM", "ทุก 12 ชั่วโมง", "Cloud-Optimized GeoTIFF & GeoJSON"),
        ("Traffy Fondue (NECTEC)", "Citizen Flood Incident Reports", "Real-time", "Webhook Push (GeoJSON + รูปภาพ)"),
        ("ธนาคารกรุงไทย (Krungthai)", "Open API (เป๋าตัง / ถุงเงิน)", "ตามธุรกรรม", "App-to-App OAuth2, HMAC-SHA256"),
        ("National ITMX", "PromptPay QR Settlement Rail", "ตามธุรกรรม", "EMVCo Standard QR Code API")
    ]
    for row_idx, row_values in enumerate(api_data):
        row = api_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(api_tbl, api_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("ความมั่นคงปลอดภัยและการซิงก์ข้อมูล (Security & Data Synchronization)")
    doc.add_paragraph(
        "ระบบรักษาความปลอดภัยของ E-Voucher ใช้มาตรฐาน Single-Use HMAC-SHA256 Token ซึ่งสร้างขึ้นแบบไดนามิกและหมดอายุภายใน 60 วินาที "
        "เพื่อป้องกันการแคปเจอร์หน้าจอไปใช้ซ้ำ (Anti-Replay Attack) พร้อมระบบ Idempotency Key ในการส่งคำขอตัดเงิน "
        "หากเกิดปัญหาเครือข่ายหลุด ข้อมูลรายงานน้ำท่วมจากประชาชนจะถูกจัดการด้วย State-based CRDTs (Conflict-Free Replicated Data Types) "
        "และส่งขึ้นคลาวด์อัตโนมัติผ่าน Background Sync API ทันทีที่เครื่องกลับมาตรวจพบสัญญาณ"
    )

    # =========================================================================
    # SECTION 7: FEASIBILITY, CONSTRAINTS & ROADMAP
    # =========================================================================
    add_h1("7. Feasibility, Constraints & Go-to-Market Timeline (ความเป็นไปได้ ข้อจำกัด และแผนงาน)")
    
    doc.add_paragraph(
        "การประเมินความเป็นไปได้รอบด้าน (4-Dimensional Feasibility Assessment) สรุปผลการพิจารณาเป็น CONDITIONAL GO (ความเชื่อมั่น 70%) "
        "โดยมีรายละเอียดการวิเคราะห์และมาตรการปลดล็อกข้อจำกัดทางกฎหมายและโครงสร้างพื้นฐานดังนี้:"
    )

    feas_tbl = doc.add_table(rows=5, cols=3)
    feas_widths = [Inches(1.8), Inches(1.5), Inches(3.2)]
    feas_data = [
        ("Dimension", "Evaluation Rating", "Key Findings & Mitigation Rationale"),
        ("Technical Feasibility", "CONDITIONAL GO ⚠️", "เทคโนโลยีทุกแทร็กมีระบบต้นแบบรองรับ (Mott MacDonald AI, FloodMapp, Khon La Khrueng) แต่การหลอมรวม 3 แทร็กเป็นเรื่องใหม่"),
        ("Resource & Capability", "CONDITIONAL GO ⚠️", "ทักษะวิศวกรรมซอฟต์แวร์มีพร้อมเต็มที่; ช่องว่างคือความเชี่ยวชาญด้านอุทกวิทยา (Hydrology) แก้ไขโดยจ้างที่ปรึกษาจากมหาวิทยาลัยเกษตรศาสตร์/AIT"),
        ("Timeline Feasibility", "CONDITIONAL GO ⚠️", "กรอบเวลา 12 เดือนสอดคล้องกับฤดูกาลมรสุม (พ.ค.–ต.ค.) สำหรับการทดสอบจริง; ข้อตกลง MOU กับหน่วยงานรัฐคือ Critical Path"),
        ("Budget Feasibility", "CONDITIONAL GO ⚠️", "กรอบงบประมาณ ฿4.9M–฿9.5M สอดคล้องกับทุนสนับสนุนนวัตกรรมจาก DEPA หรือ NIA และมีรายได้จาก อปท. รองรับหลังจบ Pilot")
    ]
    for row_idx, row_values in enumerate(feas_data):
        row = feas_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(feas_tbl, feas_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("การปลดล็อกข้อจำกัดทางกฎหมายและเทคนิค (Constraint Resolution Strategy)")
    doc.add_paragraph("แนวทางการจัดการข้อจำกัดหลัก 3 ประการที่เป็นหัวใจสำคัญในการขับเคลื่อนโครงการ:")
    add_bullet("1. ข้อจำกัดใบอนุญาต E-Money (ธปท. / พ.ร.บ.ระบบการชำระเงิน พ.ศ. 2560): ", 
               "โครงการเลือกใช้กลยุทธ์ 'Banking Partnership Route' ร่วมกับธนาคารกรุงไทย ซึ่งถือใบอนุญาตประกอบธุรกิจเงินอิเล็กทรอนิกส์และบริการชำระเงินถูกต้องครบถ้วนอยู่แล้ว "
               "ทำให้ PromptMesh ทำหน้าที่เป็นเพียงแพลตฟอร์มเทคโนโลยี (Technology Layer) จึงไม่ต้องขอใบอนุญาตด้วยตนเอง ซึ่งช่วยประหยัดเวลาดำเนินการได้ 6–12 เดือน")
    add_bullet("2. ข้อจำกัดความล่าช้าของข้อมูลรัฐ (TMD / HII / RID): ", 
               "ประสานงานผ่านสำนักงานส่งเสริมเศรษฐกิจดิจิทัล (DEPA) หรือ NECTEC เป็นคนกลางในการทำ MOU และหากรอบการดึงข้อมูลลดลงเหลือ 1-2 ชั่วโมง "
               "ระบบ AI Forecaster จะใช้ Time-Series Interpolation เพื่อชดเชยข้อมูลได้อย่างแม่นยำ")
    add_bullet("3. ความชอบด้วยกฎหมายในการกระจายงบสวัสดิการของ อปท.: ", 
               "จัดวางตำแหน่งโครงการนำร่องภายใต้กรอบ 'Smart City Sandbox' เพื่อให้เทศบาลและ อบต. ในจังหวัดนครปฐมสามารถทดสอบการเบิกจ่ายสวัสดิการผ่านดิจิทัลได้อย่างถูกต้องตามระเบียบราชการ")

    add_h2("แผนการดำเนินงาน 12 เดือน (12-Month Go-to-Market Roadmap)")
    road_tbl = doc.add_table(rows=5, cols=3)
    road_widths = [Inches(1.8), Inches(1.4), Inches(3.3)]
    road_data = [
        ("Project Phase", "Timeline Window", "Key Strategic Milestones & Deliverables"),
        ("Phase 0: Foundation\n(การวางรากฐาน)", "เดือนที่ 1 – 3", 
         "• ลงนามข้อตกลง MOU ข้อมูลรัฐ (TMD/HII/RID)\n• เข้าถึง Krungthai Open API Sandbox\n• จัดหาข้อมูล DEM ความละเอียดสูงผ่านเครือข่ายมหาวิทยาลัย\n• สรรหาทีมวิศวกรแกนนำ (11 FTE) ครบถ้วน"),
        ("Phase 1: MVP Build\n(พัฒนาแกนหลัก)", "เดือนที่ 4 – 8", 
         "• พัฒนาโมเดล AI พยากรณ์น้ำท่วมล่วงหน้า 3–6 ชม. จากข้อมูลประวัติศาสตร์\n• สร้างระบบ Vehicle-Specific Clearance Routing และทดสอบอัลกอริทึม A*\n• พัฒนา E-Voucher Wallet บน PWA และเชื่อมต่อระบบพร้อมเพย์"),
        ("Phase 2: Pilot Launch\n(การทดสอบภาคสนาม)", "เดือนที่ 9 – 10", 
         "• เปิดตัวโครงการนำร่องในจังหวัดนครปฐม (ลุ่มน้ำท่าจีน)\n• ลงทะเบียน 500+ ครัวเรือน และ 50+ ร้านค้า Micro-Relief Stations\n• ทดสอบรับมือสถานการณ์จริงช่วงฤดูน้ำหลาก (พ.ค.–ต.ค.)"),
        ("Phase 3: Welfare & Scale\n(ขยายผลสู่ 365 วัน)", "เดือนที่ 11 – 12", 
         "• เปิดโหมด อปท. Community Welfare เชื่อมงบสวัสดิการเทศบาล\n• ปล่อยระบบ AI Restock Dashboard แนะนำการฟื้นฟูสต็อกร้านค้า\n• ขยายผลสู่จังหวัดข้างเคียง (พระนครศรีอยุธยา, อุบลราชธานี)")
    ]
    for row_idx, row_values in enumerate(road_data):
        row = road_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(road_tbl, road_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("โครงสร้างทีมงานและตารางความรับผิดชอบ (Team Structure & RACI)")
    doc.add_paragraph("โครงสร้างทีมงานขนาด 15 อัตรา ประกอบด้วย ทีมงานประจำเต็มเวลา (Core Team 11 FTE) และผู้เชี่ยวชาญเฉพาะด้าน (Extended Team 4 PT):")
    add_bullet("Core Team (11 อัตรา): ", "Product Lead (1), AI/ML Engineer (2 - พยากรณ์น้ำและ AI Restock), GIS Engineer (1 - Google Maps & DEM), Full-Stack Developer (2 - PWA & Soft UI), Backend/API Engineer (1), Fintech Engineer (1 - Krungthai/PromptPay API), UI/UX Designer (1), DevOps Engineer (1), QA Engineer (1)")
    add_bullet("Extended Team (4 อัตรา): ", "Field Operations Lead (1 - ออนบอร์ดร้านค้าและประชาชน), Legal & Compliance Advisor (1 - กฎหมาย ธปท./PDPA), Hydrology Domain Expert (1 - ผู้เชี่ยวชาญอุทกวิทยาจาก ม.เกษตรศาสตร์/AIT), Community Engagement Coordinator (1 - ประสาน อปท. และ อสม.)")

    add_h2("เกณฑ์ชี้วัดความสำเร็จของโครงการนำร่อง (Pilot Success Criteria & KPIs)")
    kpi_tbl = doc.add_table(rows=7, cols=4)
    kpi_widths = [Inches(1.0), Inches(2.2), Inches(1.5), Inches(1.8)]
    kpi_data = [
        ("KPI ID", "Success Metric Description", "Target Benchmark", "Validation & Measurement Method"),
        ("SC-01", "ความแม่นยำพยากรณ์น้ำท่วมระดับตำบล", "≥ 70% Accuracy", "เทียบผลพยากรณ์ AI กับข้อมูลน้ำท่วมจริง 2564–2568"),
        ("SC-02", "ระยะเวลาแจ้งเตือนล่วงหน้าก่อนน้ำถึงซอย", "≥ 2 ชั่วโมงเฉลี่ย", "บันทึก Timestamp: เวลาที่ส่ง Alert vs. เวลาน้ำท่วมจริง"),
        ("SC-03", "ความปลอดภัยในการนำทาง (Safety Rate)", "0 อุบัติเหตุรถจมน้ำ", "ไม่มีรายงานรถที่ใช้ระบบนำทางจมน้ำตลอดช่วงนำร่อง"),
        ("SC-05", "จำนวนร้านค้า Micro-Relief Stations", "≥ 50 ร้านค้า SME", "ฐานข้อมูลร้านค้าที่มีการเปิดใช้งาน Store Status Tag"),
        ("SC-06", "ความสำเร็จธุรกรรม E-Voucher", "≥ 95% Success", "อัตราส่วนการสแกนและยืนยันสิทธิ์สำเร็จบนระบบธนาคาร"),
        ("SC-07", "ความเร็วการกระจายงบเยียวยาสู่ร้านค้า", "≤ 30 นาที", "เวลาจากกดปุ่ม 'Inject Funds' ถึงการสแกนรับของชิ้นแรก")
    ]
    for row_idx, row_values in enumerate(kpi_data):
        row = kpi_tbl.rows[row_idx]
        for col_idx, text in enumerate(row_values):
            row.cells[col_idx].paragraphs[0].add_run(text)
    format_table(kpi_tbl, kpi_widths, hdr_bg="1E40AF", alt_bg="F8FAFC")
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("ข้อเสนอแนะเชิงบริหาร (Boardroom Go / No-Go Recommendation)")
    add_callout(
        "RECOMMENDATION: CONDITIONAL GO (ระดับความเชื่อมั่น 70%)\n\n"
        "โครงการ PromptMesh มีคุณค่าทางยุทธศาสตร์สูงมากในการอุดช่องว่างระดับชาติ และมีโครงสร้างพื้นฐานดิจิทัลรองรับครบถ้วน "
        "คณะกรรมการมีมติอนุมัติให้เดินหน้าโครงการนำร่อง (Phase 0) โดยมีเงื่อนไขผูกพัน 3 ข้อ (Gate Conditions) ที่ต้องผ่านการตรวจรับ:\n"
        "1. บรรลุข้อตกลงความร่วมมือกับธนาคารกรุงไทย (หรือธนาคารออมสิน/ธ.ก.ส.) ภายในเดือนที่ 3 เพื่อปลดล็อกใบอนุญาต E-Money\n"
        "2. บรรลุข้อตกลง MOU ข้อมูลกับ TMD หรือ HII อย่างน้อย 1 หน่วยงาน ภายในเดือนที่ 4 เพื่อป้อนข้อมูลสู่ AI Model\n"
        "3. ยืนยันการเข้าถึงข้อมูลความสูงพื้นผิว (High-Res DEM) ของจังหวัดนครปฐม ภายในเดือนที่ 2\n"
        "หากผ่านเงื่อนไขทั้ง 3 ข้อ ให้เดินหน้าสู่การสร้างระบบ Phase 1 ทันที",
        title="Executive Board Resolution",
        alert_type="info"
    )

    # =========================================================================
    # SAVE FILE
    # =========================================================================
    filename = "PromptMesh_Master_Document.docx"
    doc.save(filename)
    print(f"Master Document successfully created and saved as '{filename}'!")

if __name__ == "__main__":
    build_master_document()
