# -*- coding: utf-8 -*-
import json
from pathlib import Path
import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from roadmap import DAYS
from illustrations import GALLERY
from ena_charts import ENA_CHARTS


def ena_figure(interval, limit):
    """Tải dữ liệu ENA/USDT từ Binance và vẽ nến + volume."""
    r = requests.get(
        "https://api.binance.com/api/v3/klines",
        params={"symbol": "ENAUSDT", "interval": interval, "limit": limit},
        timeout=10,
    )
    data = r.json()
    df = pd.DataFrame(data, columns=["t", "open", "high", "low", "close", "volume", "ct", "qv", "n", "tb", "tq", "i"])
    df["t"] = pd.to_datetime(df["t"], unit="ms")
    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
    fig = go.Figure(data=[go.Candlestick(x=df["t"], open=df["open"], high=df["high"], low=df["low"], close=df["close"])])
    fig.add_trace(go.Bar(x=df["t"], y=df["volume"], name="Volume", marker_color="orange", opacity=0.5, yaxis="y2"))
    fig.update_layout(title=f"ENA/USDT — {interval}", xaxis_rangeslider_visible=False,
                      yaxis=dict(title="Giá"), yaxis2=dict(title="Volume", overlaying="y", side="right"),
                      height=450)
    return fig

PROGRESS_FILE = Path(__file__).parent / "progress.json"

st.set_page_config(page_title="Wyckoff 30 Ngày — ENA", page_icon="📈", layout="wide")


def load_progress():
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {"done": [], "notes": {}}
    return {"done": [], "notes": {}}


def save_progress(p):
    PROGRESS_FILE.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")


progress = load_progress()
done = set(progress["done"])
notes = progress.get("notes", {})

st.title("📈 Học Wyckoff 30 ngày — 15 phút/ngày")
st.caption("Lộ trình dễ hiểu, ví dụ thực tế, áp dụng cho token ENA")

total = len(DAYS)
st.progress(len(done) / total, text=f"Tiến độ: {len(done)}/{total} ngày hoàn thành")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["📚 Lộ trình", "📝 Bài học hôm nay", "🎯 Case study ENA", "📊 Chart ENA", "❓ Quiz", "⏱ Học 15 phút", "🖼 Minh họa"])

with tab1:
    weeks = {"Tuần 1 (Ngày 1–7)": DAYS[0:7], "Tuần 2 (Ngày 8–14)": DAYS[7:14],
             "Tuần 3 (Ngày 15–21)": DAYS[14:21], "Tuần 4 (Ngày 22–30)": DAYS[21:30]}
    for wname, wdays in weeks.items():
        with st.expander(wname, expanded=True):
            for d in wdays:
                col1, col2 = st.columns([0.08, 0.92])
                with col1:
                    if st.checkbox("", value=d["day"] in done, key=f"cb{d['day']}"):
                        done.add(d["day"])
                    else:
                        done.discard(d["day"])
                with col2:
                    if d["day"] in done:
                        st.markdown(f"~~Ngày {d['day']}: {d['title']}~~")
                    else:
                        st.markdown(f"**Ngày {d['day']}: {d['title']}**")
    progress["done"] = sorted(done)
    save_progress(progress)

with tab2:
    day_options = [f"Ngày {d['day']}: {d['title']}" for d in DAYS]
    choice = st.selectbox("Chọn ngày học:", day_options)
    idx = day_options.index(choice)
    d = DAYS[idx]
    st.subheader(f"Ngày {d['day']}: {d['title']}")
    st.markdown(d["lesson"])
    st.info(f"**Ví dụ ENA:** {d['example']}")
    st.markdown("#### 📊 Chart ENA cho bài học này")
    cfg = ENA_CHARTS.get(d["day"])
    if cfg:
        interval, limit, guide = cfg
        try:
            st.plotly_chart(ena_figure(interval, limit), use_container_width=True)
            st.caption(f"👉 **Hướng dẫn đọc chart:** {guide}")
        except Exception as e:
            st.error(f"Không tải được dữ liệu ENA: {e}")
    note = st.text_area("Ghi chú cá nhân:", value=notes.get(str(d["day"]), ""), key=f"note{d['day']}")
    notes[str(d["day"])] = note
    progress["notes"] = notes
    save_progress(progress)
    if d["day"] in done:
        st.success("✅ Đã hoàn thành ngày này")
    else:
        if st.button("Đánh dấu hoàn thành"):
            done.add(d["day"])
            progress["done"] = sorted(done)
            save_progress(progress)
            st.rerun()

with tab3:
    st.subheader("🎯 Case study: Phân tích ENA theo Wyckoff")
    st.markdown("""
### Bước phân tích thực tế (làm mỗi ngày ~15 phút)
1. **Khung tuần (1W):** ENA đang ở phase Wyckoff nào? (tích lũy / tăng / phân phối / giảm)
2. **Khung ngày (1D):** Xác định các Trading Range (nếu có), biên trên/dưới, các event SC/BC/Spring/Upthrust/SOS/SOW.
3. **Khung 4H:** Volume có xác nhận không? Funding rate đang dương hay âm?
4. **Kịch bản:** Long / Short / Chờ — kèm entry, stoploss, take profit dự kiến.

### Checklist nhanh trước khi trade ENA
- [ ] Phase khung lớn rõ ràng
- [ ] Có TR và các event Wyckoff xác nhận
- [ ] Volume breakout tăng >50% trung bình
- [ ] Funding rate hỗ trợ hướng trade
- [ ] Rủi ro ≤ 2% tài khoản, RR ≥ 1:2

### Kịch bản mẫu (tham khảo)
| Tình huống ENA | Hành động |
|---|---|
| Sideway lâu, volume giảm, spring ở đáy | Chờ LPS → LONG, SL dưới spring |
| Phá đỉnh cũ + volume lớn + retest | LONG tại retest, TP = chiều cao TR |
| Vượt đỉnh rồi xả, volume lớn | Chốt lời / SHORT tại LPSY |
| Thủng support TR + volume lớn | Không long, chờ markdown |

> ⚠️ Đây là nội dung giáo dục, không phải lời khuyên đầu tư.
""")

with tab4:
    st.subheader("📊 Biểu đồ ENA/USDT (dữ liệu Binance)")
    col1, col2 = st.columns(2)
    interval = col1.selectbox("Khung thời gian:", ["1d", "4h", "1h", "15m"], index=0)
    limit = col2.selectbox("Số nến:", [100, 300, 500], index=1)
    try:
        st.plotly_chart(ena_figure(interval, limit), use_container_width=True)
        st.caption("Dùng chart này để luyện gán phase Wyckoff: tích lũy / tăng / phân phối / giảm.")
    except Exception as e:
        st.error(f"Không tải được dữ liệu: {e}")

with tab5:
    st.subheader("❓ Quiz nhanh")
    QUIZ = [
        ("Nguyên lý nào nói 'cause tạo ra effect'?", ["Cung – Cầu", "Nhân – Quả", "Nỗ lực – Kết quả"], 1),
        ("Spring là gì?", ["Bẫy bò ở đỉnh", "Bẫy gấu ở đáy", "Breakout thật"], 1),
        ("Breakout có volume thấp thường là?", ["Breakout mạnh", "False breakout", "Xu hướng khỏe"], 1),
        ("Funding rate âm liên tục cho thấy?", ["Thị trường quá lạc quan", "Phe short chiếm ưu thế, dễ đảo chiều lên", "Giá chắc chắn giảm"], 1),
        ("Sau UTAD (upthrust), nên?", ["Mua thêm", "Chốt lời / không long", "Bỏ qua stoploss"], 1),
    ]
    score = 0
    for i, (q, opts, correct) in enumerate(QUIZ):
        ans = st.radio(q, opts, key=f"q{i}", index=None)
        if ans is not None and opts.index(ans) == correct:
            score += 1
    if st.button("Chấm điểm"):
        st.success(f"Bạn đúng {score}/{len(QUIZ)} câu")

with tab6:
    st.subheader("⏱ Phiên học 15 phút")
    import time
    minutes = st.number_input("Số phút:", min_value=1, max_value=60, value=15)
    if st.button("Bắt đầu"):
        placeholder = st.empty()
        end = time.time() + minutes * 60
        while time.time() < end:
            remaining = int(end - time.time())
            m, s = divmod(remaining, 60)
            placeholder.metric("Thời gian còn lại", f"{m:02d}:{s:02d}")
            time.sleep(1)
        placeholder.success("⏰ Hết giờ! Ghi chú lại 1 điều bạn đã hiểu hôm nay nhé.")
        st.balloons()

with tab7:
    st.subheader("🖼 Thư viện chart minh họa")
    choice = st.selectbox("Chọn hình minh họa:", [g[0] for g in GALLERY])
    for name, make_fig, text in GALLERY:
        if name == choice:
            st.plotly_chart(make_fig(), use_container_width=True)
            st.markdown(text)

st.sidebar.success(f"✅ {len(done)}/{total} ngày hoàn thành")
st.sidebar.markdown("Chạy app: `streamlit run app.py` trong thư mục wyckoff-app")
