# -*- coding: utf-8 -*-
"""Chart minh họa các mẫu Wyckoff bằng dữ liệu mô phỏng + diễn giải đính kèm."""
import plotly.graph_objects as go


def _annotate(fig, points):
    """points: list of (x, y, label)"""
    for x, y, label in points:
        fig.add_annotation(x=x, y=y, text=label, showarrow=True,
                           arrowhead=2, ax=0, ay=-28,
                           bgcolor="#FFF3CD", bordercolor="#856404", font=dict(size=11))


def accumulation_fig():
    x = list(range(40))
    y = [30, 26, 24, 22, 24, 26, 27, 25, 23, 24, 26, 27, 28, 26, 25, 24, 23,
         21, 24, 26, 27, 28, 27, 26, 25, 26, 27, 29, 31, 33, 32, 31, 32, 34,
         36, 38, 40, 42, 44, 46]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines+markers", name="Giá",
                             line=dict(color="#1F77B4", width=2)))
    fig.add_hrect(y0=21, y1=29, fillcolor="lightblue", opacity=0.25,
                  annotation_text="Trading Range", annotation_position="top left")
    _annotate(fig, [
        (7, 25, "SC: bán tháo"), (10, 26, "AR: hồi"),
        (16, 23, "ST: test lại đáy"), (19, 26, "SOS: sức mạnh"),
        (24, 25, "Spring: xuyên đáy rồi bật"),
        (28, 29, "LPS: pullback cuối"), (34, 36, "Breakout"),
    ])
    fig.update_layout(title="Mẫu TÍCH LŨY (Accumulation Schematic)",
                      xaxis_title="Thời gian", yaxis_title="Giá", height=420)
    return fig


ACCUMULATION_TEXT = """
**Diễn giải:** Sau downtrend, giá đi ngang trong Trading Range (vùng xanh).
- **SC → AR → ST:** lực bán kiệt dần sau cú bán tháo.
- **Spring:** cú đâm thủng đáy giả để quét stoploss, rồi bật lại nhanh — đây là tín hiệu gom hàng của tay to.
- **SOS + LPS:** nhịp tăng mạnh xác nhận sức mạnh, pullback nhẹ giữ trên đáy.
- **Breakout:** phá biên trên TR → bắt đầu sóng tăng (markup).

**Áp dụng vào ENA:** khi thấy ENA sideway lâu + volume giảm dần, rồi xuất hiện nến đâm thủng đáy và rút chân nhanh với volume lớn → khả năng là Spring, chờ LPS rồi long, stoploss dưới đáy Spring.
"""


def distribution_fig():
    x = list(range(40))
    y = [20, 24, 28, 32, 30, 28, 29, 31, 33, 35, 33, 31, 30, 32, 34, 33, 31,
         33, 35, 37, 34, 31, 29, 31, 30, 29, 27, 25, 26, 24, 22, 20, 18, 16,
         14, 12, 10, 8, 6, 4]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines+markers", name="Giá",
                             line=dict(color="#D62728", width=2)))
    fig.add_hrect(y0=29, y1=37, fillcolor="mistyrose", opacity=0.3,
                  annotation_text="Trading Range", annotation_position="top left")
    _annotate(fig, [
        (4, 32, "BC: mua đu đỉnh"), (7, 29, "AR: điều chỉnh"),
        (9, 35, "ST: test lại đỉnh"), (14, 34, "SOW: suy yếu"),
        (19, 37, "UTAD: vượt đỉnh giả"), (23, 31, "LPSY: hồi yếu"),
        (30, 24, "Breakdown"),
    ])
    fig.update_layout(title="Mẫu PHÂN PHỐI (Distribution Schematic)",
                      xaxis_title="Thời gian", yaxis_title="Giá", height=420)
    return fig


DISTRIBUTION_TEXT = """
**Diễn giải:** Sau uptrend, giá đi ngang trong Trading Range (vùng hồng).
- **BC → AR → ST:** lực mua đu đỉnh cạn dần sau cú mua cao trào.
- **UTAD:** cú vượt đỉnh giả để dụ mua FOMO, rồi rơi nhanh — tín hiệu tay to đang xả.
- **SOW + LPSY:** nhịp giảm mạnh xác nhận suy yếu, nhịp hồi yếu lên kháng cự.
- **Breakdown:** thủng biên dưới TR → bắt đầu sóng giảm (markdown).

**Áp dụng vào ENA:** sau nhịp pump, nếu ENA đi ngang rồi vượt đỉnh cũ nhưng xả nhanh trong 1–2 nến với volume lớn → khả năng là Upthrust/UTAD, nên chốt lời và không long đu.
"""


def spring_fig():
    x = list(range(20))
    y = [28, 27.8, 28.2, 27.9, 28.1, 28.0, 27.7, 27.5, 27.8, 26.0,
         28.5, 29.0, 29.5, 29.2, 29.8, 30.5, 31.0, 30.8, 31.5, 32.0]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines+markers", name="Giá",
                             line=dict(color="#2CA02C", width=2.5)))
    fig.add_hline(y=27.5, line_dash="dash", line_color="gray",
                  annotation_text="Support", annotation_position="right")
    _annotate(fig, [(9, 26.0, "Spring: quét stoploss"), (10, 28.5, "Bật lại mạnh")])
    fig.update_layout(title="SPRING — bẫy gấu ở đáy",
                      xaxis_title="Thời gian", yaxis_title="Giá", height=400)
    return fig


SPRING_TEXT = """
**Diễn giải:** Giá đâm thủng support giả trong 1–2 nến (kích hoạt stoploss của phe long),
rồi đóng nến bật lại nhanh trong range, thường kèm volume tăng và nến rút chân dài.
Tay to dùng cú này để gom thêm hàng giá rẻ.

**Dấu hiệu nhận biết trên ENA:** thủng đáy vùng tích lũy khung 4H/1D rồi đóng nến xanh dài,
volume cao hơn trung bình. Hành động: chờ pullback (LPS) → long, stoploss ngay dưới đáy Spring.
"""


def upthrust_fig():
    x = list(range(20))
    y = [22, 22.2, 21.8, 22.1, 21.9, 22.0, 22.3, 22.5, 22.2, 24.0,
         21.5, 21.0, 20.5, 20.8, 20.2, 19.5, 19.0, 19.2, 18.5, 18.0]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines+markers", name="Giá",
                             line=dict(color="#D62728", width=2.5)))
    fig.add_hline(y=22.5, line_dash="dash", line_color="gray",
                  annotation_text="Resistance", annotation_position="right")
    _annotate(fig, [(9, 24.0, "Upthrust: dụ FOMO"), (10, 21.5, "Rơi nhanh")])
    fig.update_layout(title="UPTHRUST — bẫy bò ở đỉnh",
                      xaxis_title="Thời gian", yaxis_title="Giá", height=400)
    return fig


UPTHRUST_TEXT = """
**Diễn giải:** Giá vượt kháng cự giả trong 1–2 nến (dụ phe FOMO mua đu),
rồi rơi nhanh trở lại trong range, thường kèm volume lớn và bị đè giá mạnh.
Tay to dùng cú này để xả hàng giá cao.

**Dấu hiệu nhận biết trên ENA:** vượt đỉnh cũ rồi xả nhanh với volume lớn, funding rate chuyển dương.
Hành động: chốt lời / không long đu; có thể short tại nhịp hồi yếu (LPSY), stoploss trên đỉnh Upthrust.
"""


def effort_result_fig():
    x = list(range(15))
    price = [20, 20.1, 19.9, 20.2, 20.0, 20.1, 20.3, 20.2, 20.4, 20.6,
             21.5, 23.0, 24.5, 25.0, 25.5]
    volume = [50, 55, 60, 80, 100, 130, 160, 190, 150, 120, 130, 140, 110, 90, 80]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=price, mode="lines+markers", name="Giá",
                             line=dict(color="#1F77B4", width=2), yaxis="y"))
    fig.add_trace(go.Bar(x=x, y=volume, name="Volume", marker_color="orange",
                         opacity=0.6, yaxis="y2"))
    fig.update_layout(title="EFFORT vs RESULT — hấp thụ rồi bung",
                      xaxis_title="Thời gian",
                      yaxis=dict(title="Giá"), yaxis2=dict(title="Volume", overlaying="y", side="right"),
                      height=400)
    return fig


EFFORT_RESULT_TEXT = """
**Diễn giải:** Đoạn đầu volume tăng mạnh nhưng giá hầu như không dịch chuyển —
đó là **hấp thụ (absorption)**: tay to đang nuốt hết lệnh bán/mua của nhỏ lẻ.
Khi lực đối ứng cạn, giá bung mạnh theo hướng đã tích lũy (đoạn cuối).

**Áp dụng vào ENA:** ENA đi ngang lâu với volume lớn nhưng giá dậm chân tại chỗ →
đừng vội kết luận yếu; hãy xem hướng phá vỡ khỏi range để xác định phe thắng.
"""


GALLERY = [
    ("📦 Mẫu tích lũy", accumulation_fig, ACCUMULATION_TEXT),
    ("📤 Mẫu phân phối", distribution_fig, DISTRIBUTION_TEXT),
    ("🪤 Spring (bẫy gấu)", spring_fig, SPRING_TEXT),
    ("🪤 Upthrust (bẫy bò)", upthrust_fig, UPTHRUST_TEXT),
    ("⚖️ Effort vs Result", effort_result_fig, EFFORT_RESULT_TEXT),
]
