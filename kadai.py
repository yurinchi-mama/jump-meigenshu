import streamlit as st
import random

# 名言データと画像パス
quotes = {
    "挫けそうなとき聞きたい名言": [
        {"quote": "安西光義: “最後まで・・・希望を捨てちゃいかん。あきらめたらそこで試合終了だよ。” - SLAM DUNK", "image": "SLAM_DUNK_anzai.jpg"},
        {"quote": "堂本五郎: “「負けたことがある」というのがいつか大きな財産になる” - SLAM DUNK", "image": "SLAM_DUNK_doumoto.jpg"},
        {"quote": "ジンベイ: “失った物ばかり数えるな!!! 無いものは無い!!! 確認せい!! お前にまだ残っておるものは何じゃ!!!” - ONE PIECE", "image": "ONE_PIECE_jimbei.jpg"}
    ],
    "迷ったとき聞きたい名言": [
        {"quote": "マイト・ガイ: “自分を信じない奴なんかに努力する価値はない!!!”- NARUTO", "image": "NARUTO_maitogai.jpg"},
        {"quote": "たけし: “おまえ１人が100歩進む、みんなが1歩前進する方が大事だろーが！” - 世紀末リーダー伝たけし", "image": "Seikimatsu_takeshi.jpg"},
        {"quote": "麻倉葉: ”どんなことにだって良いふうにも悪いふうにも理由ならつけられる。だから正義か悪かなんて決めつけるのがおかしいって。だから、大切な事は心で決めるって。感情じゃなくて心でね” -シャーマンキング ", "image": "SHAMAN_KING_asakurayou.jpg"},
    ],
    "挑戦するとき聞きたい名言": [
        {"quote": "シルバーズ・レイリー: “今の時代を作れるのは今を生きてる人間だけだよ!!” - ONE PIECE", "image": "ONE_PIECE_reily.jpg"},
        {"quote": "マーシャル・D・ティーチ:“死ぬも生きるも天任せよ 恐れた奴が負けなのさ!! ゼハハハ!! 次の一瞬を生きようじゃねェか!”- ONE PIECE ", "image": "ONE_PIECE_kurohige.jpg"},
        {"quote": "エンポリオ・イワンコフ:“奇跡は諦めない奴の頭上にしか降りて来ない!!!! “奇跡”ナメるんじゃないよォ!!!!”- ONE PIECE ", "image": "ONE_PIECE_iwankofu.jpg"}
    ]
}

# タイトル
st.title("週刊少年ジャンプ 名言アプリ")

# サイドバーにカテゴリ選択ラジオボタンを配置
category = st.sidebar.radio("カテゴリを選択してください", list(quotes.keys()))

# 名言を表示するボタン
if st.button("名言を表示"):
    selected_quotes = quotes[category]
    selected_quote = random.choice(selected_quotes)
    quote = selected_quote["quote"]
    image_path = selected_quote["image"]
    
    st.markdown(f"### {quote}")
    st.image(image_path, use_column_width=True)
