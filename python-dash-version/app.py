"""
GÖREN Performans Takip Sistemi - Python Dash Version
T.C. Sağlık Bakanlığı · Ankara İl Sağlık Müdürlüğü

Kurulum:
    pip install dash plotly pandas

Çalıştırma:
    python app.py
    Tarayıcıda http://127.0.0.1:8050 adresine gidin.
"""

import dash
from dash import html, dcc, callback, Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

# ─── RENK PALETİ ───────────────────────────────────────────────
COLORS = {
    "primary": "#DC0D15",
    "primary_dark": "#A30A10",
    "success": "#55BAB7",
    "warning": "#AF3C4E",
    "info": "#0095C6",
    "threat": "#DC0D15",
    "bg": "#F5F7F9",
    "card": "#FFFFFF",
    "text": "#222222",
    "text_secondary": "#555555",
    "border": "#DCE0E5",
    "muted_bg": "#EBEEF2",
}

# ─── VERİ ───────────────────────────────────────────────────────
HOSPITALS = {
    "Genel Hastaneler": ["Ankara Şehir Hastanesi", "Ankara Eğitim ve Araştırma Hastanesi", "Dr. Sami Ulus Hastanesi"],
    "ADSM": ["Altındağ ADSM", "Çankaya ADSM", "Keçiören ADSM"],
    "ADSH": ["Ankara ADSH", "Gölbaşı ADSH"],
}

INDICATORS = [
    "Acil Servis Bekleme Süresi", "Yatak Doluluk Oranı", "Ameliyat İptal Oranı",
    "Hasta Memnuniyeti", "Enfeksiyon Hızı", "Ortalama Yatış Süresi",
]

KPIS = [
    {"label": "Toplam GP", "value": "87.4", "delta": "+2.1", "up": True, "color": COLORS["success"]},
    {"label": "Gösterge Sayısı", "value": "42", "delta": "0", "up": None, "color": COLORS["info"]},
    {"label": "Başarı Oranı", "value": "%78.5", "delta": "+4.2%", "up": True, "color": COLORS["success"]},
    {"label": "GD Ortalaması", "value": "3.28", "delta": "-0.15", "up": False, "color": COLORS["warning"]},
]

PERIOD_COMPARISON = [
    {"label": "Toplam GP", "current": "87.4", "prev": "85.3", "up": True},
    {"label": "Başarı Oranı", "current": "%78.5", "prev": "%74.3", "up": True},
    {"label": "GD Ortalaması", "current": "3.28", "prev": "3.43", "up": False},
    {"label": "Gösterge Sayısı", "current": "42", "prev": "42", "up": None},
]

MONTHLY_CHANGES = [
    {"name": "Hasta Memnuniyeti", "delta": "+5.2", "up": True},
    {"name": "Yatak Doluluk Oranı", "delta": "+3.1", "up": True},
    {"name": "Ameliyat İptal Oranı", "delta": "-2.8", "up": False},
    {"name": "Enfeksiyon Hızı", "delta": "-1.5", "up": False},
]

PRIORITIES = [
    {"name": "Acil Servis Bekleme Süresi", "gpLoss": "4.2 GP", "rank": 1},
    {"name": "Ameliyat İptal Oranı", "gpLoss": "3.1 GP", "rank": 2},
    {"name": "Enfeksiyon Hızı", "gpLoss": "2.7 GP", "rank": 3},
    {"name": "Lab Sonuç Süresi", "gpLoss": "1.9 GP", "rank": 4},
]

TREND_DATA = [
    {"month": "Eki", "value": 72, "target": 80, "achieved": False},
    {"month": "Kas", "value": 75, "target": 80, "achieved": False},
    {"month": "Ara", "value": 81, "target": 80, "achieved": True},
    {"month": "Oca", "value": 78, "target": 80, "achieved": False},
    {"month": "Şub", "value": 83, "target": 80, "achieved": True},
    {"month": "Mar", "value": 85, "target": 80, "achieved": True},
    {"month": "Nis*", "value": 84, "target": 80, "achieved": True},
    {"month": "May*", "value": 86, "target": 80, "achieved": True},
    {"month": "Haz*", "value": 87, "target": 80, "achieved": True},
]

DISTRIBUTION_DATA = [
    {"name": "Ankara Şehir Hst.", "value": 92, "color": COLORS["success"]},
    {"name": "Ankara EAH", "value": 85, "color": COLORS["success"]},
    {"name": "Dr. Sami Ulus", "value": 78, "color": "#F59E0B"},
    {"name": "Keçiören ADSM", "value": 65, "color": COLORS["warning"]},
    {"name": "Altındağ ADSM", "value": 58, "color": COLORS["warning"]},
]

PARAMETER_DATA = [
    {"month": "Eki", "numerator": 1250, "denominator": 1500},
    {"month": "Kas", "numerator": 1300, "denominator": 1520},
    {"month": "Ara", "numerator": 1400, "denominator": 1480},
    {"month": "Oca", "numerator": 1350, "denominator": 1510},
    {"month": "Şub", "numerator": 1420, "denominator": 1490},
    {"month": "Mar", "numerator": 1460, "denominator": 1500},
]

ANOMALIES = [
    {"indicator": "Acil Servis Bekleme Süresi", "zScore": 2.8, "period": "Şubat 2026", "severity": "Yüksek"},
    {"indicator": "Lab Sonuç Süresi", "zScore": 2.3, "period": "Mart 2026", "severity": "Orta"},
]

PREDICTIONS = [
    {"period": "Nisan 2026", "indicator": "Yatak Doluluk", "risk": "Yüksek", "message": "Hedef altında kalma riski %72"},
    {"period": "Mayıs 2026", "indicator": "Ameliyat İptal", "risk": "Orta", "message": "Artış eğilimi devam edebilir"},
    {"period": "Haziran 2026", "indicator": "Enfeksiyon Hızı", "risk": "Düşük", "message": "Stabil seyir bekleniyor"},
]

COMPARISON_DATA = [
    {"name": "Hasta Memnuniyeti", "Ankara Şehir Hst.": 92, "Ankara EAH": 85, "Dr. Sami Ulus": 78},
    {"name": "Yatak Doluluk", "Ankara Şehir Hst.": 88, "Ankara EAH": 91, "Dr. Sami Ulus": 82},
    {"name": "Ameliyat İptal", "Ankara Şehir Hst.": 5, "Ankara EAH": 8, "Dr. Sami Ulus": 12},
    {"name": "Enfeksiyon Hızı", "Ankara Şehir Hst.": 3.2, "Ankara EAH": 4.1, "Dr. Sami Ulus": 5.5},
    {"name": "Bekleme Süresi", "Ankara Şehir Hst.": 15, "Ankara EAH": 22, "Dr. Sami Ulus": 28},
]

ALL_HOSPITALS = [
    "Ankara Şehir Hastanesi", "Ankara EAH", "Dr. Sami Ulus",
    "Keçiören ADSM", "Altındağ ADSM", "Çankaya ADSM",
    "Ankara ADSH", "Gölbaşı ADSH",
]


# ─── STİL YARDIMCILARI ─────────────────────────────────────────
def card_style(extra=None):
    s = {
        "backgroundColor": COLORS["card"],
        "borderRadius": "8px",
        "border": f"1px solid {COLORS['border']}",
        "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
        "padding": "20px",
        "marginBottom": "24px",
    }
    if extra:
        s.update(extra)
    return s


def section_title(text, icon=None):
    children = []
    if icon:
        children.append(html.Span(icon, style={"marginRight": "8px"}))
    children.append(text)
    return html.H3(children, style={
        "fontSize": "18px", "fontWeight": "600", "color": COLORS["text"],
        "marginBottom": "4px", "display": "flex", "alignItems": "center"
    })


def section_desc(text):
    return html.P(text, style={
        "fontSize": "14px", "color": COLORS["text_secondary"], "marginBottom": "16px"
    })


# ─── GRAFİKLER ─────────────────────────────────────────────────
def create_trend_chart():
    months = [d["month"] for d in TREND_DATA]
    values = [d["value"] for d in TREND_DATA]
    colors = [COLORS["success"] if d["achieved"] else COLORS["threat"] for d in TREND_DATA]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=values, mode="lines+markers",
        line=dict(color=COLORS["info"], width=2),
        marker=dict(size=10, color=colors, line=dict(color="white", width=2)),
        name="Gerçekleşme / Tahmin",
    ))
    fig.add_hline(y=80, line_dash="dash", line_color=COLORS["warning"],
                  annotation_text="Hedef", annotation_position="top left")
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white", height=300,
        margin=dict(l=40, r=20, t=20, b=40),
        xaxis=dict(gridcolor=COLORS["border"]),
        yaxis=dict(gridcolor=COLORS["border"]),
        font=dict(family="Segoe UI, Helvetica Neue, Arial, sans-serif", size=13),
    )
    return fig


def create_distribution_chart():
    names = [d["name"] for d in DISTRIBUTION_DATA]
    values = [d["value"] for d in DISTRIBUTION_DATA]
    colors = [d["color"] for d in DISTRIBUTION_DATA]

    fig = go.Figure(go.Bar(
        y=names, x=values, orientation="h",
        marker_color=colors,
        text=values, textposition="auto",
    ))
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white", height=250,
        margin=dict(l=140, r=20, t=10, b=30),
        xaxis=dict(range=[0, 100], gridcolor=COLORS["border"]),
        yaxis=dict(autorange="reversed"),
        font=dict(family="Segoe UI, Helvetica Neue, Arial, sans-serif", size=13),
    )
    return fig


def create_parameter_chart():
    months = [d["month"] for d in PARAMETER_DATA]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=[d["numerator"] for d in PARAMETER_DATA],
        mode="lines+markers", name="Pay",
        line=dict(color=COLORS["success"], width=2), marker=dict(size=6),
    ))
    fig.add_trace(go.Scatter(
        x=months, y=[d["denominator"] for d in PARAMETER_DATA],
        mode="lines+markers", name="Payda",
        line=dict(color=COLORS["info"], width=2), marker=dict(size=6),
    ))
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white", height=280,
        margin=dict(l=40, r=20, t=20, b=40),
        xaxis=dict(gridcolor=COLORS["border"]),
        yaxis=dict(gridcolor=COLORS["border"]),
        font=dict(family="Segoe UI, Helvetica Neue, Arial, sans-serif", size=13),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def create_comparison_chart():
    categories = [d["name"] for d in COMPARISON_DATA]
    fig = go.Figure()
    for hosp, color in [("Ankara Şehir Hst.", COLORS["threat"]), ("Ankara EAH", COLORS["info"]), ("Dr. Sami Ulus", COLORS["success"])]:
        fig.add_trace(go.Bar(
            x=categories, y=[d[hosp] for d in COMPARISON_DATA],
            name=hosp, marker_color=color,
        ))
    fig.update_layout(
        barmode="group",
        plot_bgcolor="white", paper_bgcolor="white", height=320,
        margin=dict(l=40, r=20, t=20, b=60),
        xaxis=dict(gridcolor=COLORS["border"]),
        yaxis=dict(gridcolor=COLORS["border"]),
        font=dict(family="Segoe UI, Helvetica Neue, Arial, sans-serif", size=12),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


# ─── BİLEŞENLER ────────────────────────────────────────────────
def build_header():
    return html.Header(style={"position": "sticky", "top": 0, "zIndex": 50}, children=[
        # Government strip
        html.Div(style={
            "background": f"linear-gradient(135deg, {COLORS['primary']}, {COLORS['primary_dark']})",
            "height": "36px", "display": "flex", "alignItems": "center",
            "justifyContent": "space-between", "padding": "0 16px",
            "color": "white", "fontSize": "12px",
        }, children=[
            html.Span("T.C. Sağlık Bakanlığı · Ankara İl Sağlık Müdürlüğü", style={"fontWeight": "500"}),
            html.Div(style={"display": "flex", "alignItems": "center", "gap": "12px"}, children=[
                html.Span("🔔 3", style={"position": "relative"}),
                html.Span("kullanici@saglik.gov.tr"),
                html.Span("Çıkış", style={"cursor": "pointer"}),
            ]),
        ]),
        # Brand bar
        html.Div(style={
            "backgroundColor": COLORS["card"], "borderBottom": f"1px solid {COLORS['border']}",
            "padding": "8px 16px",
        }, children=[
            html.Div(style={"maxWidth": "1440px", "margin": "0 auto", "display": "flex",
                            "alignItems": "center", "justifyContent": "space-between"}, children=[
                html.Div(style={"display": "flex", "alignItems": "center", "gap": "12px"}, children=[
                    html.Div("🏥", style={"fontSize": "28px", "width": "44px", "height": "44px",
                                          "display": "flex", "alignItems": "center", "justifyContent": "center",
                                          "backgroundColor": COLORS["muted_bg"], "borderRadius": "8px"}),
                    html.Div([
                        html.Div("Ankara İl Sağlık Müdürlüğü",
                                 style={"fontSize": "14px", "color": COLORS["text_secondary"], "fontWeight": "500"}),
                        html.Div([
                            html.Span("GÖREN", style={"color": COLORS["primary"], "fontWeight": "700"}),
                            " Performans Takip Sistemi",
                        ], style={"fontSize": "16px", "fontWeight": "600"}),
                    ]),
                ]),
                html.Div(style={"display": "flex", "gap": "4px", "flexWrap": "wrap"}, children=[
                    html.Button(label, style={
                        "padding": "4px 8px", "fontSize": "12px", "border": "none",
                        "backgroundColor": "transparent", "cursor": "pointer",
                        "borderRadius": "6px", "color": COLORS["text"],
                    }) for label in ["Admin Panel", "Ayarlar", "Veri Yükle", "Yönetici Özeti", "Yenile", "Yazdır", "Şifre Değiştir"]
                ]),
            ]),
        ]),
        # Context bar
        html.Div(style={
            "backgroundColor": COLORS["muted_bg"], "borderBottom": f"1px solid {COLORS['border']}",
            "padding": "6px 16px", "fontSize": "14px",
        }, children=[
            html.Div(style={"maxWidth": "1440px", "margin": "0 auto", "display": "flex",
                            "justifyContent": "space-between"}, children=[
                html.Span("Ankara Şehir Hastanesi", style={"fontWeight": "500"}),
                html.Span("Son güncelleme: 07.03.2026 14:30", style={"color": COLORS["text_secondary"]}),
            ]),
        ]),
    ])


def build_filter_card():
    hospital_options = []
    for group, items in HOSPITALS.items():
        for item in items:
            hospital_options.append({"label": f"[{group}] {item}", "value": item})

    return html.Div(style=card_style(), children=[
        html.Div(style={"display": "flex", "gap": "16px", "flexWrap": "wrap"}, children=[
            html.Div(style={"flex": "1", "minWidth": "250px"}, children=[
                html.Label("Sağlık Tesisi Seçimi", style={"fontSize": "14px", "fontWeight": "500", "display": "block", "marginBottom": "6px"}),
                dcc.Dropdown(
                    id="hospital-select",
                    options=hospital_options,
                    value="Ankara Şehir Hastanesi",
                    clearable=False,
                    style={"fontSize": "14px"},
                ),
            ]),
            html.Div(style={"flex": "1", "minWidth": "250px"}, children=[
                html.Label("Gösterge Seçimi", style={"fontSize": "14px", "fontWeight": "500", "display": "block", "marginBottom": "6px"}),
                html.Div(style={"display": "flex", "gap": "8px", "alignItems": "center"}, children=[
                    html.Div(style={"flex": "1"}, children=[
                        dcc.Dropdown(
                            id="indicator-select",
                            options=[{"label": i, "value": i} for i in INDICATORS],
                            value=INDICATORS[0],
                            clearable=False,
                            style={"fontSize": "14px"},
                        ),
                    ]),
                    html.Div(style={"display": "flex", "gap": "4px"}, children=[
                        html.Button(btn, style={
                            "padding": "6px 8px", "border": "none", "backgroundColor": "transparent",
                            "cursor": "pointer", "fontSize": "14px", "borderRadius": "6px",
                            "color": COLORS["info"] if btn == "AI" else COLORS["text_secondary"],
                        }) for btn in ["★", "?", "XL", "SWOT", "AI"]
                    ]),
                ]),
            ]),
        ]),
    ])


def build_scorecards():
    cards = []
    for kpi in KPIS:
        delta_color = COLORS["success"] if kpi["up"] else COLORS["warning"] if kpi["up"] is False else COLORS["text_secondary"]
        arrow = "▲" if kpi["up"] else "▼" if kpi["up"] is False else ""
        cards.append(html.Div(style={
            "backgroundColor": COLORS["card"], "borderRadius": "8px",
            "borderLeft": f"4px solid {kpi['color']}", "padding": "16px",
            "boxShadow": "0 4px 12px rgba(0,0,0,0.08)", "flex": "1", "minWidth": "180px",
        }, children=[
            html.Div(kpi["label"], style={"fontSize": "14px", "color": COLORS["text_secondary"], "marginBottom": "8px"}),
            html.Div(kpi["value"], style={"fontSize": "24px", "fontWeight": "700", "color": COLORS["text"]}),
            html.Div(f"{arrow} {kpi['delta']} önceki döneme göre" if kpi["up"] is not None else "",
                     style={"fontSize": "12px", "color": delta_color, "marginTop": "4px", "fontWeight": "500"}),
        ]))

    return html.Div([
        section_title("2026 Ocak-Mart Dönemi Performans Özeti"),
        section_desc("Seçili dönem için temel performans göstergeleri"),
        html.Div(style={"display": "flex", "gap": "16px", "flexWrap": "wrap"}, children=cards),
    ])


def build_period_comparison():
    cards = []
    for d in PERIOD_COMPARISON:
        color = COLORS["success"] if d["up"] else COLORS["warning"] if d["up"] is False else COLORS["text_secondary"]
        arrow = "▲" if d["up"] else "▼" if d["up"] is False else "—"
        cards.append(html.Div(style={
            "padding": "12px", "borderRadius": "8px", "backgroundColor": COLORS["bg"],
            "border": f"1px solid {COLORS['border']}", "textAlign": "center", "flex": "1", "minWidth": "140px",
        }, children=[
            html.Div(d["label"], style={"fontSize": "12px", "color": COLORS["text_secondary"], "marginBottom": "4px"}),
            html.Div(d["current"], style={"fontSize": "18px", "fontWeight": "700"}),
            html.Div(f"{arrow} {d['prev']}", style={"fontSize": "12px", "color": color, "marginTop": "2px"}),
        ]))

    return html.Div(style=card_style(), children=[
        section_title("Dönem Karşılaştırması"),
        section_desc("Önceki dönemle değişim analizi"),
        dcc.Dropdown(
            options=["2025 Q4 ile karşılaştır", "2025 Q3 ile karşılaştır", "2024 Q1 ile karşılaştır (YoY)"],
            value="2025 Q4 ile karşılaştır", clearable=False,
            style={"fontSize": "14px", "marginBottom": "16px", "maxWidth": "300px"},
        ),
        html.Div(style={"display": "flex", "gap": "12px", "flexWrap": "wrap"}, children=cards),
    ])


def build_insight_cards():
    # Monthly changes
    change_items = []
    for item in MONTHLY_CHANGES:
        color = COLORS["success"] if item["up"] else COLORS["warning"]
        arrow = "▲" if item["up"] else "▼"
        change_items.append(html.Div(style={
            "display": "flex", "justifyContent": "space-between", "padding": "6px 0",
            "borderBottom": f"1px solid {COLORS['border']}",
        }, children=[
            html.Span(item["name"], style={"fontSize": "14px"}),
            html.Span(f"{arrow} {item['delta']}", style={"fontSize": "14px", "fontWeight": "500", "color": color}),
        ]))

    # Priorities
    priority_items = []
    for item in PRIORITIES:
        priority_items.append(html.Div(style={
            "display": "flex", "justifyContent": "space-between", "alignItems": "center",
            "padding": "6px 0", "borderBottom": f"1px solid {COLORS['border']}",
        }, children=[
            html.Div(style={"display": "flex", "alignItems": "center", "gap": "8px"}, children=[
                html.Span(str(item["rank"]), style={
                    "width": "20px", "height": "20px", "borderRadius": "50%",
                    "backgroundColor": COLORS["threat"], "color": "white",
                    "fontSize": "11px", "fontWeight": "700", "display": "flex",
                    "alignItems": "center", "justifyContent": "center",
                }),
                html.Span(item["name"], style={"fontSize": "14px"}),
            ]),
            html.Span(f"-{item['gpLoss']}", style={"fontSize": "14px", "fontWeight": "500", "color": COLORS["warning"]}),
        ]))

    return html.Div(style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "16px"}, children=[
        html.Div(style=card_style({"borderTop": f"4px solid {COLORS['warning']}"}), children=[
            section_title("Aylık Değişim", "↕"),
            section_desc("Son aya göre iyileşen ve gerileyen göstergeler"),
            html.Div(change_items),
        ]),
        html.Div(style=card_style({"borderTop": f"4px solid {COLORS['threat']}"}), children=[
            section_title("Akıllı Öncelik", "⚠"),
            section_desc("GP kaybına göre sıralanmış düşük performanslı göstergeler"),
            html.Div(priority_items),
        ]),
    ])


def build_period_selector():
    return html.Div(style={"display": "flex", "alignItems": "center", "gap": "16px", "marginBottom": "24px", "flexWrap": "wrap"}, children=[
        html.Div(style={
            "display": "flex", "backgroundColor": COLORS["muted_bg"],
            "borderRadius": "8px", "padding": "4px",
        }, children=[
            html.Button(p, id=f"period-{p}", style={
                "padding": "6px 16px", "fontSize": "14px", "border": "none",
                "borderRadius": "6px", "cursor": "pointer", "fontWeight": "500",
                "backgroundColor": COLORS["card"] if p == "6 Ay" else "transparent",
                "color": COLORS["text"],
                "boxShadow": "0 1px 3px rgba(0,0,0,0.1)" if p == "6 Ay" else "none",
            }) for p in ["6 Ay", "12 Ay", "Tümü"]
        ]),
        dcc.Checklist(
            options=[{"label": " Önceki Yıl (YoY)", "value": "yoy"}],
            value=[], style={"fontSize": "14px"},
        ),
    ])


def build_anomaly_section():
    items = []
    for a in ANOMALIES:
        sev_color = COLORS["threat"] if a["severity"] == "Yüksek" else COLORS["warning"]
        items.append(html.Div(style={
            "display": "flex", "justifyContent": "space-between", "alignItems": "center",
            "padding": "12px", "borderRadius": "8px", "backgroundColor": COLORS["bg"],
            "border": f"1px solid {COLORS['border']}", "marginBottom": "8px",
        }, children=[
            html.Div([
                html.Span(a["indicator"], style={"fontWeight": "500", "fontSize": "14px"}),
                html.Span(f" ({a['period']})", style={"color": COLORS["text_secondary"], "fontSize": "14px"}),
            ]),
            html.Div(style={"display": "flex", "alignItems": "center", "gap": "12px"}, children=[
                html.Span(f"Z: {a['zScore']}", style={"fontSize": "14px", "color": COLORS["text_secondary"]}),
                html.Span(a["severity"], style={
                    "fontSize": "12px", "fontWeight": "500", "padding": "2px 8px",
                    "borderRadius": "4px", "backgroundColor": sev_color, "color": "white",
                }),
            ]),
        ]))

    return html.Div(style=card_style(), children=[
        section_title("Anomali Tespiti", "⚠"),
        section_desc("Z-skoru ile tespit edilen istatistiksel sapmalar"),
        html.Div(items),
    ])


def build_predictions_section():
    items = []
    for p in PREDICTIONS:
        risk_color = COLORS["threat"] if p["risk"] == "Yüksek" else COLORS["warning"] if p["risk"] == "Orta" else COLORS["success"]
        items.append(html.Div(style={
            "display": "flex", "justifyContent": "space-between", "alignItems": "center",
            "padding": "12px", "borderRadius": "8px", "backgroundColor": COLORS["bg"],
            "border": f"1px solid {COLORS['border']}", "marginBottom": "8px",
        }, children=[
            html.Div([
                html.Div(p["period"], style={"fontSize": "12px", "color": COLORS["text_secondary"]}),
                html.Div(p["indicator"], style={"fontWeight": "500", "fontSize": "14px"}),
                html.Div(p["message"], style={"fontSize": "12px", "color": COLORS["text_secondary"]}),
            ]),
            html.Span(p["risk"], style={
                "fontSize": "12px", "fontWeight": "500", "padding": "2px 8px",
                "borderRadius": "4px", "backgroundColor": risk_color, "color": "white",
            }),
        ]))

    return html.Div(style=card_style(), children=[
        section_title("Tahmine Dayalı Uyarılar", "📈"),
        section_desc("Önümüzdeki 3 aylık dönem için öngörülen riskler"),
        html.Div(items),
    ])


def build_hospital_comparison():
    return html.Div(style=card_style(), children=[
        section_title("Hastane Karşılaştırması"),
        section_desc("Birden fazla sağlık tesisini karşılaştırmalı olarak analiz edin"),
        html.Div(style={"display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "24px"}, children=[
            html.Div(style={"flex": "1", "minWidth": "250px"}, children=[
                html.Label("Karşılaştırılacak Hastaneler", style={"fontSize": "14px", "fontWeight": "500", "display": "block", "marginBottom": "6px"}),
                dcc.Dropdown(
                    options=[{"label": h, "value": h} for h in ALL_HOSPITALS],
                    value=["Ankara Şehir Hastanesi", "Ankara EAH", "Dr. Sami Ulus"],
                    multi=True, style={"fontSize": "14px"},
                ),
                html.Span("En az 2 hastane seçiniz", style={"fontSize": "12px", "color": COLORS["text_secondary"]}),
            ]),
            html.Div(style={"flex": "1", "minWidth": "250px"}, children=[
                html.Label("Metrik", style={"fontSize": "14px", "fontWeight": "500", "display": "block", "marginBottom": "6px"}),
                dcc.Dropdown(
                    options=["Puan Kaybı Haritası", "Başarı Oranı", "Gösterge Detay"],
                    value="Puan Kaybı Haritası", clearable=False, style={"fontSize": "14px"},
                ),
            ]),
        ]),
        html.Div(style={
            "display": "flex", "alignItems": "center", "gap": "16px", "padding": "12px",
            "borderRadius": "8px", "backgroundColor": COLORS["bg"],
            "border": f"1px solid {COLORS['border']}", "marginBottom": "24px",
        }, children=[
            html.Span("3 hastane seçili", style={"fontSize": "14px", "fontWeight": "500"}),
            html.Span("·", style={"color": COLORS["text_secondary"]}),
            html.Span("5 gösterge üzerinden karşılaştırma", style={"fontSize": "14px", "color": COLORS["text_secondary"]}),
        ]),
        dcc.Graph(figure=create_comparison_chart(), config={"displayModeBar": False}),
        html.Div(style={"display": "flex", "gap": "24px", "marginTop": "16px", "fontSize": "14px"}, children=[
            html.Div(style={"display": "flex", "alignItems": "center", "gap": "8px"}, children=[
                html.Span(style={"width": "12px", "height": "12px", "borderRadius": "2px", "backgroundColor": COLORS["threat"]}),
                html.Span("Seçili Hastane"),
            ]),
            html.Div(style={"display": "flex", "alignItems": "center", "gap": "8px"}, children=[
                html.Span(style={"width": "12px", "height": "12px", "borderRadius": "2px", "backgroundColor": COLORS["info"]}),
                html.Span("Karşılaştırma Hastaneleri"),
            ]),
        ]),
    ])


def build_footer():
    return html.Footer(style={
        "backgroundColor": COLORS["card"], "borderTop": f"1px solid {COLORS['border']}",
        "marginTop": "32px", "padding": "16px",
    }, children=[
        html.Div(style={
            "maxWidth": "1440px", "margin": "0 auto", "display": "flex",
            "justifyContent": "space-between", "alignItems": "center",
            "fontSize": "14px", "color": COLORS["text_secondary"],
        }, children=[
            html.Div(style={"display": "flex", "gap": "16px"}, children=[
                html.Span("Son veri güncellemesi: 07.03.2026 14:30"),
                html.Span("·"),
                html.Span("2026 Q1 Dönemi · 42 Gösterge"),
            ]),
            html.Div(style={"display": "flex", "gap": "16px", "alignItems": "center"}, children=[
                html.Span("Yardım", style={"cursor": "pointer"}),
                html.Button("↑", style={
                    "width": "32px", "height": "32px", "borderRadius": "6px",
                    "backgroundColor": COLORS["muted_bg"], "border": "none",
                    "cursor": "pointer", "fontSize": "16px",
                }),
            ]),
        ]),
    ])


# ─── UYGULAMA ──────────────────────────────────────────────────
app = dash.Dash(__name__)
app.title = "GÖREN Performans Takip Sistemi"

app.layout = html.Div(style={
    "backgroundColor": COLORS["bg"], "minHeight": "100vh",
    "fontFamily": "Segoe UI, Helvetica Neue, Arial, sans-serif",
    "fontSize": "15px", "lineHeight": "1.6", "color": COLORS["text"],
}, children=[
    build_header(),

    html.Main(style={"maxWidth": "1440px", "margin": "0 auto", "padding": "24px 16px"}, children=[
        build_filter_card(),

        # Tab switcher
        dcc.Tabs(id="main-tabs", value="goren", style={"marginBottom": "24px"}, children=[
            dcc.Tab(label="GÖREN", value="goren", style={"fontWeight": "600", "fontSize": "14px"},
                    selected_style={"fontWeight": "600", "fontSize": "14px", "borderBottom": f"2px solid {COLORS['primary']}", "color": COLORS["primary"]}),
            dcc.Tab(label="Rapor Kartı", value="rapor", style={"fontWeight": "600", "fontSize": "14px"},
                    selected_style={"fontWeight": "600", "fontSize": "14px", "borderBottom": f"2px solid {COLORS['primary']}", "color": COLORS["primary"]}),
        ]),

        html.Div(id="tab-content"),
    ]),

    build_footer(),
])


@callback(Output("tab-content", "children"), Input("main-tabs", "value"))
def render_tab(tab):
    if tab == "rapor":
        return html.Div(style=card_style({"textAlign": "center", "padding": "48px"}), children=[
            section_title("Rapor Kartı"),
            html.P("Rapor kartı içeriği burada gösterilecektir.",
                   style={"color": COLORS["text_secondary"]}),
        ])

    return html.Div([
        build_scorecards(),
        html.Div(style={"marginTop": "24px"}),
        build_period_comparison(),
        build_insight_cards(),
        build_period_selector(),

        # Trend chart
        html.Div(style=card_style(), children=[
            section_title("Gösterge Trend Analizi ve Tahmin"),
            section_desc("Son 6 aylık gerçekleşme ve 3 aylık tahmin (* ile işaretli)"),
            dcc.Graph(figure=create_trend_chart(), config={"displayModeBar": False}),
        ]),

        # Distribution chart
        html.Div(style=card_style(), children=[
            section_title("Gösterge Dağılım Analizi"),
            section_desc("Hastaneler arası karşılaştırmalı performans dağılımı"),
            dcc.Graph(figure=create_distribution_chart(), config={"displayModeBar": False}),
        ]),

        # Parameter chart
        html.Div(style=card_style(), children=[
            section_title("Kritik Parametre Trendi"),
            section_desc("Alt parametrelerin (pay/payda) aylık seyri"),
            dcc.Graph(figure=create_parameter_chart(), config={"displayModeBar": False}),
        ]),

        build_anomaly_section(),
        build_predictions_section(),
        build_hospital_comparison(),
    ])


if __name__ == "__main__":
    app.run(debug=True)
