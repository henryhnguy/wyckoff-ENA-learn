# -*- coding: utf-8 -*-
"""Nội dung lộ trình 30 ngày Wyckoff — mỗi bài ~15 phút đọc."""

DAYS = [
    {
        "day": 1,
        "title": "Wyckoff là gì? Ba nguyên lý nền tảng",
        "lesson": """
### 1. Wyckoff là gì?
Wyckoff là phương pháp phân tích thị trường do Richard Wyckoff (1873–1934) phát triển,
nhấn mạnh việc đọc **hành động giá + khối lượng** để suy ra ý đồ của "tay to" (smart money).

### 2. Ba nguyên lý nền tảng
1. **Cung – Cầu (Supply & Demand):** Giá tăng khi cầu > cung, giảm khi cung > cầu, đi ngang khi cân bằng.
2. **Nhân – Quả (Cause & Effect):** Mỗi nhịp tích lũy/phân phối (cause) tạo ra nhịp tăng/giảm tương ứng (effect). Vùng tích lũy càng dài, sóng sau càng mạnh.
3. **Nỗ lực – Kết quả (Effort vs Result):** So sánh khối lượng (nỗ lực) với biên độ giá (kết quả). Khối lượng lớn mà giá không dịch chuyển → có sự hấp thụ (absorption).

### Ví dụ dễ hiểu
Một cửa hàng bán áo giá 100k, ai cũng muốn mua, hàng hết nhanh → giá bị kéo lên **cầu > cung**.
Hàng tồn kho cả tháng, giảm giá 50% vẫn ế → **cung > cầu**.
""",
        "example": "ENA: khi ENA sideway tích lũy càng lâu với volume lớn → 'cause' lớn → sóng tăng sau đó có thể càng mạnh.",
    },
    {
        "day": 2,
        "title": "Chu kỳ thị trường 4 giai đoạn",
        "lesson": """
### Chu kỳ Wyckoff gồm 4 pha
1. **Tích lũy (Accumulation):** Sau downtrend, giá đi ngang, tay to âm thầm gom.
2. **Tăng giá (Markup):** Phá vỡ khỏi vùng tích lũy, sóng tăng.
3. **Phân phối (Distribution):** Sau uptrend, giá đi ngang, tay to bán ra.
4. **Giảm giá (Markdown):** Phá vỡ xuống, sóng giảm.

### Mẹo nhận diện
- Đáy dài + volume giảm dần = thường đang tích lũy.
- Đỉnh dài + volume lớn + nến giật mạnh = thường đang phân phối.
""",
        "example": "ENA thường xuất hiện pha tích lũy trước các nhịp pump mạnh (ví dụ các nhịp sideway dài trong 2024).",
    },
    {
        "day": 3,
        "title": "Sơ đồ mẫu tích lũy (Accumulation Schematic)",
        "lesson": """
### Các sự kiện chính (events)
- **PS (Preliminary Support):** Hỗ trợ sơ bộ, nến rút chân xuất hiện.
- **SC (Selling Climax):** Đỉnh điểm bán tháo, volume cực lớn, nến dài râu dưới.
- **AR (Automatic Rally):** Hồi phục tự động sau SC.
- **ST (Secondary Test):** Test lại vùng SC với volume thấp hơn → xác nhận lực bán kiệt.
- **Spring / Shakeout:** Giá đâm thủng đáy SC rồi bật lại nhanh → bẫy gấu, tín hiệu mạnh.
- **SOS (Sign of Strength):** Nến tăng mạnh volume lớn → xác nhận.
- **LPS (Last Point of Support):** Pullback cuối trước khi breakout.
- **Breakout:** Phá vỡ kháng cự vùng tích lũy → bắt đầu markup.
""",
        "example": "Nếu ENA phá đáy cũ rồi bật lại nhanh kèm volume → khả năng là Spring, cơ hội long.",
    },
    {
        "day": 4,
        "title": "Sơ đồ mẫu phân phối (Distribution Schematic)",
        "lesson": """
### Các sự kiện chính
- **PSY (Preliminary Supply):** Kháng cự sơ bộ sau uptrend.
- **BC (Buying Climax):** Mua đu đỉnh, volume lớn, nến dài.
- **AR (Automatic Reaction):** Điều chỉnh sau BC.
- **ST (Secondary Test):** Test lại vùng BC, volume thấp.
- **UT (Upthrust) / UTAD:** Giá vượt đỉnh BC rồi rơi nhanh → bẫy bò.
- **SOW (Sign of Weakness):** Nến giảm mạnh volume lớn.
- **LPSY (Last Point of Supply):** Hồi lên kháng cự rồi bị đè.
- **Breakdown:** Thủng hỗ trợ → markdown.
""",
        "example": "ENA vượt đỉnh cũ rồi xả nhanh trong 1–2 nến với volume lớn → khả năng Upthrust, nên chốt lời.",
    },
    {
        "day": 5,
        "title": "Đọc volume: effort vs result",
        "lesson": """
### Bảng quy ước
| Tình huống | Volume | Giá | Ý nghĩa |
|---|---|---|---|
| Volume tăng, giá tăng mạnh | ↑↑ | ↑↑ | Effort khớp result → xu hướng khỏe |
| Volume tăng, giá giật | ↑↑ | ↔ | Hấp thụ → sắp đổi phase |
| Volume giảm dần trong range | ↓ | ↔ | Lực bán/mua kiệt → chuẩn bị breakout |
| Volume tăng khi breakout | ↑↑ | phá vỡ | Breakout thật |
| Volume thấp khi breakout | ↓ | phá vỡ | Dễ false breakout |
""",
        "example": "ENA breakout khỏi vùng tích lũy mà volume chỉ hơi tăng → coi chừng fakeout.",
    },
    {
        "day": 6,
        "title": "Spring & Upthrust — bẫy giá kinh điển",
        "lesson": """
### Spring (bẫy gấu trong tích lũy)
Giá thủng support giả, đóng nến quay lại trong range → long đu theo.
### Upthrust (bẫy bò trong phân phối)
Giá vượt resistance giả, đóng nến quay lại → short hoặc chốt lời.

### Dấu hiệu nhận biết
- Xuyên qua vùng rồi hồi nhanh (1–2 nến).
- Volume tăng tại cú đâm thủng.
- Nến rút chân dài.
""",
        "example": "ENA đâm thủng đáy vùng tích lũy rồi đóng nến xanh dài khung 4H → Spring cổ điển.",
    },
    {
        "day": 7,
        "title": "Bài tập ngày 7: Vẽ lại sơ đồ trên TradingView",
        "lesson": """
### Thực hành (15 phút)
1. Mở chart ENA/USDT khung ngày (1D).
2. Tìm 1 vùng tích lũy hoặc phân phối trong quá khứ.
3. Đánh dấu PS, SC/BC, AR, ST, SOS/SOW, breakout.
4. Ghi chú: volume có xác nhận không? Spring/Upthrust có xuất hiện không?

### Checklist
- [ ] Tìm được ít nhất 1 vùng sideway rõ ràng
- [ ] Xác định được các event cơ bản
- [ ] Nhận xét được xu hướng sau breakout
""",
        "example": "Nếu vùng sideway của ENA kéo dài 1–2 tháng rồi phá vỡ với sóng mạnh → ví dụ chuẩn cause & effect.",
    },
    {
        "day": 8,
        "title": "Phân biệt tích lũy vs trap giảm",
        "lesson": """
### Vùng sideway chưa chắc là tích lũy!
Dấu hiệu tích lũy THẬT:
- Có SC + ST volume thấp.
- Có Spring hoặc SOS.
- LPS giữ trên đáy.
Dấu hiệu trap (đang xả):
- Không có đáy sau cao hơn.
- Volume lớn tại nhịp giảm.
- Không có nhịp SOS mạnh.
""",
        "example": "ENA sideway nhưng volume giảm dần và thỉnh thoảng nến đỏ volume lớn → cẩn thận đó là phân phối ẩn.",
    },
    {
        "day": 9,
        "title": "Phân biệt phân phối vs nghỉ giữa sóng tăng",
        "lesson": """
### Sideway sau uptrend có 2 khả năng
1. **Re-accumulation:** Tạo nền cho sóng tăng tiếp. Dấu hiệu: giữ trên support, có spring, breakout lên.
2. **Distribution:** Tay to thoát hàng. Dấu hiệu: UTAD, SOW, phá support.

### Mẹo
Xem volume ở nhịp giảm trong range: nếu volume thấp → re-accumulation; nếu volume lớn → distribution.
""",
        "example": "Sau nhịp tăng mạnh, ENA đi ngang nhưng các nhịp chỉnh đều volume thấp → khả năng re-accumulation.",
    },
    {
        "day": 10,
        "title": "Composite Man — nhân vật ẩn sau giá",
        "lesson": """
### Composite Man là gì?
Wyckoff ví nhà tạo lập lớn như một 'Composite Man' thao túng thị trường:
1. Mua khi ai cũng bán (SC, shakeout).
2. Đẩy giá lên qua các nhịp SOS.
3. Bán khi ai cũng mua (BC, upthrust).
4. Ép giá xuống qua các nhịp SOW.

### Ứng dụng
Hãy tự hỏi: 'Composite Man đang gom hay đang xả ở vùng giá này?'
""",
        "example": "Khi ENA rơi mạnh, tin tức xấu, nhưng volume lớn + nến rút chân → Composite Man có thể đang gom.",
    },
    {
        "day": 11,
        "title": "Khung thời gian & top-down analysis",
        "lesson": """
### Phân tích từ lớn đến nhỏ
- **1W/1D:** Xác định phase tổng thể của ENA (tích lũy/tăng/phân phối/giảm).
- **4H:** Tìm vùng range, spring/upthrust.
- **1H/15m:** Tìm điểm vào lệnh, stoploss.

### Quy tắc
Đi theo xu hướng khung lớn. Không long khi khung ngày đang ở markdown rõ ràng.
""",
        "example": "ENA khung tuần đang markup → chỉ tìm long ở khung 4H tại LPS.",
    },
    {
        "day": 12,
        "title": "Vẽ trading range — cách xác định biên",
        "lesson": """
### Trading Range (TR)
Vùng giá đi ngang giữa support và resistance. Cách vẽ:
1. Xác định 2–3 đỉnh gần bằng nhau → resistance.
2. Xác định 2–3 đáy gần bằng nhau → support.
3. TR = khoảng giá giữa 2 biên.

### Lưu ý
- Biên không phải là 1 đường chính xác mà là 1 vùng (zone).
- TR càng lâu → năng lượng tích lũy càng lớn.
""",
        "example": "ENA từng tạo TR quanh vùng $0.20–$0.40 trong thời gian dài — các biên xác định bởi nhiều lần chạm.",
    },
    {
        "day": 13,
        "title": "Wyckoff & nến Nhật (candlestick)",
        "lesson": """
### Các mẫu nến quan trọng trong Wyckoff
- **Pin bar rút chân dài tại hỗ trợ:** dấu hiệu hấp thụ bán.
- **Nến nhấn chìm tại kháng cự sau nhịp tăng:** dấu hiệu phân phối.
- **Nến Marubozu volume lớn:** lực mua/bán mạnh (SOS/SOW).
- **Inside bar sau breakout:** consolidation, có thể tiếp diễn.

### Kết hợp
Nến + volume + vị trí trong TR = tín hiệu có xác suất cao.
""",
        "example": "ENA rút chân dài volume lớn tại đáy TR → mua gom của tay to.",
    },
    {
        "day": 14,
        "title": "Quiz tuần 1 & 2 — tự kiểm tra",
        "lesson": """
### Tự trả lời (không cần app chấm điểm)
1. Ba nguyên lý Wyckoff là gì?
2. Kể tên 4 phase của chu kỳ thị trường.
3. Spring và Upthrust khác nhau thế nào?
4. Khi volume tăng nhưng giá không dịch chuyển, điều gì xảy ra?
5. Breakout cần volume như thế nào để đáng tin?

### Gợi ý
- 1: Cung-cầu, Nhân-quả, Nỗ lực-kết quả.
- 3: Spring = bẫy gấu ở đáy, Upthrust = bẫy bò ở đỉnh.
- 5: Volume phải tăng mạnh so với trung bình.
""",
        "example": "Ôn lại chart ENA và tự gán phase cho từng giai đoạn — nếu gán được rõ ràng bạn đã hiểu phương pháp.",
    },
    {
        "day": 15,
        "title": "Entry, Stoploss, Take Profit theo Wyckoff",
        "lesson": """
### Điểm vào lệnh phổ biến
1. Sau breakout + retest thành công (LPS).
2. Sau Spring bật lại trong TR.
3. Nhảy vào nến SOS đầu tiên.

### Stoploss
- Dưới đáy Spring (long) hoặc trên đỉnh Upthrust (short).
- Tránh đặt quá sát — crypto rất nhiễu.

### Take Profit
- Mục tiêu = chiều cao TR chiếu lên từ điểm breakout (cause & effect).
- Có thể chia 2 phần: TP1 tại biên TR, TP2 theo sóng.
""",
        "example": "ENA phá TR rộng $0.10 → mục tiêu tối thiểu tăng thêm ~$0.10 từ điểm breakout.",
    },
    {
        "day": 16,
        "title": "Quản lý vốn cơ bản",
        "lesson": """
### Quy tắc 2%
Mỗi lệnh chỉ rủi ro tối đa 2% tài khoản (bao gồm cả stoploss).

### Tính position size
Position size = (Tài khoản × 2%) / Khoảng cách từ entry đến stoploss.

### Ví dụ
Tài khoản $1000, rủi ro 2% = $20. Entry $0.50, stoploss $0.45 → khoảng cách $0.05.
Position size = 20 / 0.05 = 400 ENA.
""",
        "example": "Với ENA biến động mạnh, nên rủi ro 1–2% và stoploss rộng đủ để tránh bị quét.",
    },
    {
        "day": 17,
        "title": "Wyckoff trong thị trường crypto vs forex/cổ phiếu",
        "lesson": """
### Điểm khác biệt ở crypto
- Không đóng cửa phiên → chart chạy 24/7.
- Thanh khoản phân mảnh nhiều sàn → volume tham khảo tốt nhất ở Binance/Bybit hợp đồng hoặc spot lớn.
- Funding rate & open interest là chỉ báo thêm rất hữu ích (crypto có 'đòn bẩy').

### Gợi ý
Kết hợp Wyckoff với funding rate: tích lũy + funding âm → tín hiệu đẹp.
""",
        "example": "ENA tích lũy lâu + funding rate âm → nhiều khả năng short squeeze sắp diễn ra.",
    },
    {
        "day": 18,
        "title": "Wyckoff + Funding rate + OI",
        "lesson": """
### Công cụ on-chain/phái sinh bổ trợ
- **Funding rate âm:** phe short trả phí → thị trường bi quan quá đà, dễ đảo chiều lên.
- **Open Interest giảm + giá giảm:** short đang đóng → áp lực bán yếu đi.
- **OI tăng + giá đi ngang trong TR:** tiền vào đặt cược → chuẩn bị breakout.

### Kết hợp
Wyckoff cho cấu trúc giá, funding/OI cho động lực phía sau.
""",
        "example": "ENA sideway, OI tăng dần, funding âm nhẹ → setup long breakout hấp dẫn.",
    },
    {
        "day": 19,
        "title": "Phân tích ENA theo Wyckoff — phần 1: lịch sử",
        "lesson": """
### Bài tập quan sát (mở chart ENA/USDT khung ngày)
1. Tìm các giai đoạn markup mạnh trong lịch sử ENA.
2. Tìm các vùng phân phối sau pump.
3. Xác định xem các cú giảm sâu có tuân theo spring/shakeout không.

### Ghi chú mẫu
- ENA thường có nhịp pump rất mạnh sau giai đoạn nén dài.
- Sau pump, ENA thường tạo vùng phân phối rõ với upthrust.

👉 Hãy ghi lại ít nhất 3 quan sát của riêng bạn vào phần ghi chú cá nhân bên dưới.
""",
        "example": "Mẫu quan sát: 'Tháng X/2024 ENA nén trong TR hẹp 2 tuần rồi bật mạnh +300%, volume breakout rất lớn.'",
    },
    {
        "day": 20,
        "title": "Phân tích ENA theo Wyckoff — phần 2: hiện tại",
        "lesson": """
### Khung thao tác
1. Khung tuần: ENA đang ở phase nào? (accumulation/markup/distribution/markdown)
2. Khung ngày: có TR không? Biên dưới/trên? Có spring/upthrust gần đây không?
3. Khung 4H: volume có dấu hiệu hấp thụ không?

### Checklist nhanh
- [ ] Xác định phase
- [ ] Vẽ TR nếu có
- [ ] Ghi chú spring/upthrust/SOS/SOW
- [ ] Đề xuất kịch bản: long/short/chờ
""",
        "example": "Ví dụ kịch bản: 'ENA giữ trên support TR, spring xuất hiện ngày X → chờ LPS rồi long, stoploss dưới spring.'",
    },
    {
        "day": 21,
        "title": "Xây dựng trading plan cá nhân",
        "lesson": """
### Mẫu Trading Plan
1. **Khung thời gian giao dịch:** 4H + 1D.
2. **Thiết lập vào lệnh:** breakout + retest, hoặc spring + LPS.
3. **Stoploss:** dưới đáy spring/trên đỉnh upthrust.
4. **Take profit:** chiều cao TR hoặc RR 1:2.
5. **Rủi ro/lệnh:** tối đa 2%.
6. **Nhật ký:** ghi lại mọi lệnh + lý do.

### Nguyên tắc vàng
Không có lệnh là một lệnh tốt. Chờ setup đẹp.
""",
        "example": "Plan cho ENA: chỉ long khi ENA có spring hoặc breakout retest khỏi TR khung ngày với volume tăng >50% trung bình.",
    },
    {
        "day": 22,
        "title": "Luyện tập đọc chart 15 phút mỗi ngày",
        "lesson": """
### Bài tập hàng ngày
1. Mở chart ENA 4H và 1D (5 phút).
2. Gán phase Wyckoff cho ENA hiện tại (5 phút).
3. Viết 1 câu nhận định: 'ENA đang... vì...' (5 phút).

### Tiêu chí tiến bộ
Nếu sau 1 tuần bạn tự tin gán phase và giải thích được vì sao → bạn đã nắm phương pháp.
""",
        "example": "Ví dụ câu nhận định: 'ENA đang tích lũy vì volume giảm dần trong TR và có 2 lần test support thành công.'",
    },
    {
        "day": 23,
        "title": "Những sai lầm phổ biến",
        "lesson": """
### Top sai lầm
1. Gán nhãn Wyckoff cho mọi vùng sideway (không phải TR nào cũng là tích lũy).
2. Coi mọi breakout đều thật (thiếu volume xác nhận).
3. Dời stoploss khi giá chạm — vi phạm plan.
4. Trade quá nhiều khung thời gian cùng lúc.
5. Bỏ qua funding/OI ở crypto.

### Khắc phục
Viết nhật ký, backtest thủ công 20 vùng TR cũ trên chart ENA.
""",
        "example": "Backtest: lật lại 6 tháng chart ENA, đánh dấu các TR, xem breakout nào có volume xác nhận → thống kê tỷ lệ thắng.",
    },
    {
        "day": 24,
        "title": "Kết hợp Wyckoff với hỗ trợ/kháng cự",
        "lesson": """
### Vùng hợp lưu (confluence)
Setup Wyckoff mạnh nhất khi trùng với:
- Hỗ trợ/kháng cự nhiều lần chạm.
- EMA 50/200 khung lớn.
- Vùng supply/demand cũ.
- Round number tâm lý ($0.50, $1.00...).

### Cách dùng
Ưu tiên lệnh ở vùng hợp lưu. Tránh trade ở 'vùng trống'.
""",
        "example": "ENA giữ support trùng EMA200 khung ngày + round number → LPS chất lượng cao.",
    },
    {
        "day": 25,
        "title": "Wyckoff cho short — phân phối chi tiết",
        "lesson": """
### Setup short phổ biến
1. UTAD tạo đỉnh giả → short tại LPSY.
2. Breakdown khỏi TR phân phối + retest → short.
3. Chuỗi lower high + SOW liên tiếp → short theo xu hướng.

### Lưu ý
- Crypto short cần cẩn thận short squeeze (funding âm mạnh).
- Nên đặt stoploss trên UTAD.
""",
        "example": "ENA vượt đỉnh cũ rồi xả, volume lớn, funding chuyển dương → setup short LPSY đẹp.",
    },
    {
        "day": 26,
        "title": "Backtesting nhanh trên ENA",
        "lesson": """
### Quy trình (30–60 phút, có thể kéo dài)
1. Cuộn chart ENA về 6 tháng trước.
2. Tìm 5 vùng TR.
3. Với mỗi TR, ghi: có spring/upthrust không? Breakout volume thế nào? Sóng sau đó đạt bao nhiêu %?
4. Tính tỷ lệ setup 'đẹp' có sóng lớn.
""",
        "example": "Kết quả mẫu: 3/5 TR có spring + breakout volume lớn → 3 sóng tăng mạnh; 2/5 breakout đuối → continuation yếu.",
    },
    {
        "day": 27,
        "title": "Xây checklist giao dịch cuối cùng",
        "lesson": """
### Checklist trước khi vào lệnh ENA
- [ ] Khung tuần/ngày đang ở phase nào?
- [ ] Có TR rõ biên không?
- [ ] Có spring/upthrust hoặc SOS/SOW không?
- [ ] Volume breakout có tăng mạnh không?
- [ ] Funding rate ủng hộ chưa?
- [ ] Stoploss rõ ràng, rủi ro ≤2%?
- [ ] RR tối thiểu 1:2?

Nếu thiếu >2 mục → KHÔNG vào lệnh.
""",
        "example": "Checklist này là công cụ bạn sẽ dùng mỗi khi nhìn chart ENA từ nay về sau.",
    },
    {
        "day": 28,
        "title": "Tâm lý giao dịch & kỷ luật",
        "lesson": """
### Những kẻ thù
- FOMO mua đu sau pump.
- Trả thù thị trường sau lệnh lỗ.
- Dời stoploss.
- Overtrade khi chán.

### Quy tắc
- Lỗ 2 lệnh liên tiếp → nghỉ, không vào lệnh thêm hôm đó.
- Mỗi ngày xem chart tối đa 2 lần để tránh nhiễu.
- Tuân thủ checklist kể cả khi 'cảm thấy chắc kèo'.
""",
        "example": "Sau khi ENA pump 50%, FOMO mua đu đỉnh phân phối là lỗi kinh điển — Wyckoff dạy bạn nhận ra BC/UTAD.",
    },
    {
        "day": 29,
        "title": "Kế hoạch hành động 30 ngày tới",
        "lesson": """
### Sau khi hoàn thành 30 ngày
- Tuần 1: Tiếp tục đọc chart ENA 15 phút/ngày, gán phase.
- Tuần 2: Paper trade (giao dịch thử không tiền thật) theo checklist.
- Tuần 3: Mở tài khoản nhỏ, rủi ro ≤1%/lệnh.
- Tuần 4: Review nhật ký, điều chỉnh plan.

### Mục tiêu thực tế
Không phải dự đoán đúng 100%, mà là có hệ thống lặp lại được và quản lý rủi ro tốt.
""",
        "example": "Ghi vào sổ: 'Mục tiêu 3 tháng tới: hoàn thành 10 lệnh paper trade theo checklist Wyckoff trên ENA.'",
    },
    {
        "day": 30,
        "title": "Tổng kết & tài nguyên học thêm",
        "lesson": """
### Bạn đã học được
- 3 nguyên lý Wyckoff, 4 phase thị trường
- Schematic tích lũy/phân phối, spring/upthrust
- Đọc volume, entry/SL/TP, quản lý vốn
- Ứng dụng thực tế cho ENA

### Tài nguyên
- Sách: 'Studies in Tape Reading' (Wyckoff), 'Wyckoff Method' của David Weis
- Cộng đồng: các kênh chia sẻ VSA/Wyckoff tiếng Việt
- Công cụ: TradingView (vẽ TR, xem volume, funding)

### Chúc mừng!
Bạn đã hoàn thành lộ trình 30 ngày. Hãy kiên trì ghi nhật ký và review chart ENA mỗi ngày.
""",
        "example": "Tiếp theo: mỗi sáng mở chart ENA, viết 1 câu nhận định phase Wyckoff — thói quen nhỏ, lợi ích dài hạn.",
    },
]
