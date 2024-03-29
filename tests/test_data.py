example_data = {
    "classify": [
        {"text": "股市呈多頭趨勢，投資人樂觀進場", "label": "positive"},
        {"text": "股市呈空頭趨勢，投資人恐慌撤資", "label": "negative"},
        {"text": "今日股市開盤，大盤為 17,000 點，台積電為 542 元", "label": "neutral"},
    ],
    "extract": [
        {"text": "台積電宣布主管都要會使用 ChatGPT", "entities": {"company": ["台積電"]},},
        {
            "text": "矽谷銀行母公司 SVB Financial Group 因賠本拋債籌錢，股價大暴跌，恐慌性賣壓席捲歐美銀行業",
            "entities": {
                "company": ["矽谷銀行", "SVB Financial Group"],
                "location": ["歐", "美"],
            },
        },
        {
            "text": "貢沃爾集團創辦人托恩奎斯特在休士頓舉行的CERAWeek能源會議上說，這代表更多的海上航程，船運價格一直非常高，而且一直處於高點",
            "entities": {
                "company": ["貢沃爾集團"],
                "person": ["托恩奎斯特"],
                "location": ["休士頓"],
            },
        },
    ],
    "qa": [
        {
            "text": "Mobius 資本合夥公司共同創辦人墨比爾斯接受彭博電視台專訪時透露，晶片製造股是投資組合中名列第一的類別，因為美國和中國都在半導體研發和生產方面投入巨額資金，晶片相關類股將會有不錯的表現。費城半導體指數今年以來上漲 20%，遠優於標準普爾 500 指數的 4% 漲幅，晶片股可望創下 2016 年 7-9 月以來最佳超越美股大盤表現。請問墨比爾斯投資組合中佔比最高的是？",  # noqa E501
            "answer": "晶片製造股",
        }
    ],
}
new_data = {
    "classify": [
        {"text": "就疫情對半導體供應鏈的影響，反映在股市近期的低迷上"},
        {"text": "昨日聯電召開法說會，說明有關第四季財報重點內容"},
        {"text": "受到美股開紅盤影響，台股今日開盤上揚逾5%"},
    ],
    "extract": [
        {"text": "美國國務院主管經濟成長、能源與環境的次卿費南德茲表示，自俄羅斯入侵烏克蘭以來，「我們已看到根本性改變，這種改變不可能短期恢復。」"},
    ],
    "qa": [
        {
            "text": "NASA 航空安全報告系統（ASRS）數據顯示，IEEE Spectrum 分析，年初推行 5G 無線網路後，高度表故障和故障投訴量激增，都與飛行員與飛機無線電（雷達）高度表問題有關。1~5 月共 93 起雷達高度表故障或故障報告，僅 1 月高度表故障投訴就接近前五年總和 2 倍。大多數故障事件，都提到 5G 造成干擾，包括上述田納西州和洛杉磯兩起。請問為什麼高度錶故障次數會增加？"  # noqa E501
        }
    ],
    "summarize": [
        {
            "text": "華爾街分析師週五 (10 日)  認為，矽谷銀行 (Silicon Valley Bank) 倒閉事件提醒投資人，當聯準會 (Fed) 變得激進時，往往會造成破壞，市場轉向押注聯準會 3 月升息 1 碼，年內降息的機率大增。金融服務商 SVB 集團旗下矽谷銀行 (Silicon Valley Bank) 週四被迫賤賣手中債券來籌措現金，虧損 18 億美元，由於籌資失敗，SVB 週五 (10 日) 正準備出售公司，最終遭加州金融保護與創新部 (DFPI) 關閉，這是 2008 年金融危機來最大銀行倒閉案，拖累全球銀行業市值蒸發數十億美元。由於擔心金融體系存在系統性風險，投資人湧向債券避險，2 年期美債殖利率短短兩天內下跌了 46 個基點，與 2008 年 9 月雷曼兄弟倒閉時連續兩天的急劇下跌相當。聯準會 3 月升息 2 碼的預期大幅降低，年內降息的希望重燃。根據 CME 的 FedWatch 工具顯示，交易員押注聯準會 3 月升 1 碼的機率回升至 60% 左右，升息 2 碼機率從先前的高於 70% 降至 40%。交易員亦預期 12 月可能降息。SVB 暴雷是聯準會以 40 年來最激進的升息行動遏制通膨的最新結果，由於新創企業客戶提取存款，維持公司在 IPO 和私募融資的寒冷環境中營運。瑞銀全球財富管理投資長 Mark Haefele ：「聯準會現在有非常明確的證據表明，升息正在對金融體系和經濟產生影響，雖然這還不足以讓聯準會停下腳步，但這是他們將考慮在內。」Oanda 高級市場分析師 Edward Moya 表示：「週五非農就業和薪資成長數據顯示，聯準會先前的升息已產生預期的經濟降溫效果，加上矽谷銀行倒閉，預測 3 月會議上重回 2 碼升息幅度的可能性不大。」Moya 點評道：「就業報告證實聯準會政策是限制性的，他們的緊縮工作已接近完成，如果 SVB 沒有破產和帶來系統性風險，聯準會升息 2 碼的理由就成立了。」Moya 研判：「現在焦點將落在 SVB 的漣漪效應和下週二的通膨報告上，只要不出現一份過熱的通膨報告，聯準會應該會持續 1 碼的升息步伐。」"  # noqa E501
        }
    ],
    "generate": [{"text": "請用中文生成針對期貨與選擇權入門課的課程大綱"}],
}

prompt_template = (
    "{inputs}\n\n以上是許多公司、組織、產業別、產品名或人物名稱，請將每個詞彙中前後重複、不通順的部分"
    "修正為一個合理的名稱。請輸出成一個字典檔，key是原本的錯誤名稱，value是修正後的正確名稱。"
    "請不要加其他文字說明和變數指派。"
)
bad_financial_nouns = [
    "摩根梵市場股    摩根梵市場股",
    "匯豐摩根士丹    匯豐摩根士丹",
    "大通摩根證券    大通摩根證券",
    "摩根大通託管JP摩摩根大通託管",
    "匯豐台摩根士    匯豐台摩根士",
    "美商摩根-013    美商摩根-013",
    "大通託JP摩根(股)大通託JP摩根",
    "摩根大通銀行    摩根大通銀行",
    "摩根梵加德新    摩根梵加德新",
    "摩根大通託管梵加摩根大通託管",
    "摩根銀行台北分行摩根銀行台北",
    "美商摩根大通銀行美商摩根大通",
    "摩根沙烏地      摩根沙烏地",
    "大通JP摩根證    大通JP摩根證",
    "美商摩根-020    美商摩根-020",
    "大通託管JP摩根基大通託管JP摩",
    "大通摩根基金    大通摩根基金",
    "摩根星光基金    摩根星光基金",
    "摩根哥倫比亞    摩根哥倫比亞",
    "匯豐摩根士丹    吳俊佶",
    "大通託管摩根宜安大通託管摩根",
    "摩根JP摩根投    摩根JP摩根投",
    "摩根沙烏地阿    摩根沙烏地阿",
    "匯豐託管摩根    匯豐託管摩根",
    "摩根大通台北分行摩根大通台北",
    "摩根富達VI      摩根富達VI",
    "香港匯豐摩根    香港匯豐摩根",
    "匯豐摩根史丹    匯豐摩根史丹",
    "摩根美國基金    摩根美國基金",
    "摩根保管特寶    摩根保管特寶",
    "摩根保管富蘭    摩根保管富蘭",
    "摩根特寶豐全    摩根特寶豐全",
    "大通摩根士丹    大通摩根士丹",
    "摩根梵市場股    錢國維",
    "美商摩根大通    美商摩根大通",
]

