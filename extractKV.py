# -*- coding: utf-8 -*-
import json

# JSONデータの例（異なるキーを持つと仮定）
json_data = """
{
    "data": [
{"text": "@ophllk 皮肉だよ。馬鹿。", "edit_history_tweet_ids": ["1735334829099794820"], "in_reply_to_user_id": "1703096083772268544", "author_id": "1638902463381274625", "id": "1735334829099794820", "conversation_id": "1734997721428414832"}, 
{"text": "誰かに言ってる皮肉だよ☆☆☆\\nぼくちゃん元気だからね！！\\n(キャラ崩壊まったなし)", "edit_history_tweet_ids": ["1735254263113376063"], "in_reply_to_user_id": "1641703830659424263", "author_id": "1641703830659424263", "id": "1735254263113376063", "conversation_id": "1734960459839930826"}, 
{"text": "@SakezakoTENGA 皮肉だよ🥺？", "edit_history_tweet_ids": ["1735254009248965116"], "in_reply_to_user_id": "1682950188988764160", "author_id": "1504039465765191681", "id": "1735254009248965116", "conversation_id": "1735232258800529548"}, 
{"text": "@kotsubo48 @nishy03 皮肉だよな？", "edit_history_tweet_ids": ["1735243343108644885"], "in_reply_to_user_id": "2912855948", "author_id": "1381219631969394692", "id": "1735243343108644885", "conversation_id": "1735145299927330905"}, 
{"text": "@yuduk1_mofumofu 死にたいけど「後を追うように」とか文字通り死んでも言われたくないから死ねないって皮肉だよね", "edit_history_tweet_ids": ["1735236084030988449"], "in_reply_to_user_id": "1461140067150602241", "author_id": "2237782664", "id": "1735236084030988449", "conversation_id": "1734949095943627092"}, 
{"text": "@kiyokiyoshii2 皮肉だよ。そのうち起きられなくなるから", "edit_history_tweet_ids": ["1735131683144524174"], "in_reply_to_user_id": "1404420750010769410", "author_id": "163505355", "id": "1735131683144524174", "conversation_id": "1734781475026014288"}, 
{"text": "@anis774 皮肉が分からない人にそれ皮肉だよって教えてもそれすら理解出来ないのか\\n残念だね頭", "edit_history_tweet_ids": ["1735115122765672504"], "in_reply_to_user_id": "17615275", "author_id": "1484786292353564672", "id": "1735115122765672504", "conversation_id": "1735113322549465306"}, 
{"text": "@frozen_umbrella 結構クリティカルな皮肉だよなこれ\\n「悪意のあるコラ」で片付けてしまって本当に良いのか", "edit_history_tweet_ids": ["1735060268085031253"], "in_reply_to_user_id": "1686963644402434048", "author_id": "1292901113427980288", "id": "1735060268085031253", "conversation_id": "1734747036233474230"}, 
{"text": "@mitaianime 皮肉だよ", "edit_history_tweet_ids": ["1735041492270637259"], "in_reply_to_user_id": "1403891629560274951", "author_id": "1704445957688135680", "id": "1735041492270637259", "conversation_id": "1734881172067688613"}, 
{"text": "@HowaitSan_ 指が太いのに体重関係なくて草\\n太ってるって話じゃなくて指が太くて汚いって話だよバカW\\n俺がインキャって言ったのはお前がインキャ煽りしてくるくらいインキャコンプあるんだろうからそれに対する皮肉だよ説明させんな頭悪すぎだろお前", "edit_history_tweet_ids": ["1734856430862422021"], "in_reply_to_user_id": "1313500019555618816", "author_id": "1412016587352117254", "id": "1734856430862422021", "conversation_id": "1734367025861103756"}, 
{"text": "@tnksikik 大丈夫皮肉だよ", "edit_history_tweet_ids": ["1734852881009025438"], "in_reply_to_user_id": "1367547709192740864", "author_id": "1346416992761180160", "id": "1734852881009025438", "conversation_id": "1734838626088006050"}, 
{"text": "@momomounk VTuberの配信ってゲーム実況者と違うと思ってるしそのゲーム以外の配信には来ない人の意見っぽいんでぶっちゃけ皮肉だよ🤣🤣🤣\\n一回見逃したくらいで離れるような 人はVTuberのファンではない\\nそのゲームのファンやろ", "edit_history_tweet_ids": ["1734850870628761890"], "in_reply_to_user_id": "926840163950518272", "author_id": "1523542757301956609", "id": "1734850870628761890", "conversation_id": "1734846476831133779"}, 
{"text": "ちなみにこれを主張する人はもちろん「プリンセス」になる訳だが……なんかとんでもない皮肉だよな。", "edit_history_tweet_ids": ["1734838979806343633"], "in_reply_to_user_id": "1290260089362776064", "author_id": "1290260089362776064", "id": "1734838979806343633", "conversation_id": "1734770441028563355"}, 
{"text": "@himuro398 皮肉だよ。クソ鈍感人間です な。", "edit_history_tweet_ids": ["1734838434232185046"], "in_reply_to_user_id": "1432287556129812484", "author_id": "1045290375101829120", "id": "1734838434232185046", "conversation_id": "1734563079801942059"}, 
{"text": "@111meenya 皮肉だよ馬鹿ww\\nメガネの事といいマジでズレてんな。\\nアウトofアウト！\\n総理席からはよ退席しろしマジで。", "edit_history_tweet_ids": ["1734826972856098964"], "in_reply_to_user_id": "1053393903661924352", "author_id": "788027155393318912", "id": "1734826972856098964", "conversation_id": "1734692756143177931"}, 
{"text": "@YahooNewsTopics 自分都合解釈が過ぎる。\\n不平不満皮肉だよ。\\n国語が苦手なの？", "edit_history_tweet_ids": ["1734818029417210123"], "in_reply_to_user_id": "88846085", "author_id": "1574084937317175296", "id": "1734818029417210123", "conversation_id": "1734535567764054103"}, 
{"text": "@MOG912wwwwww @5351Tomo @sabuibonokami 皮肉だよ", "edit_history_tweet_ids": ["1734761290462330964"], "in_reply_to_user_id": "1318474060175585280", "author_id": "1572236948273790977", "id": "1734761290462330964", "conversation_id": "1734497277597880755"}, 
{"text": "@tmg_dayo 珍しくスゴイ皮肉だよね😂", "edit_history_tweet_ids": ["1734723919700201896"], "in_reply_to_user_id": "3101749044", "author_id": "1155153006620377088", "id": "1734723919700201896", "conversation_id": "1734722520249671749"}, 
{"text": "@himuro398 やっぱり感覚がおかしいわ。\\n皮肉だよ。", "edit_history_tweet_ids": ["1734571520801038676"], "in_reply_to_user_id": "1432287556129812484", "author_id": "1532194300833898496", "id": "1734571520801038676", "conversation_id": "1734563079801942059"}, 
{"text": "共産主義国家によるハニトラor献金で日本人の誇りを捨てた、そしてなんちゃって帰化人の国会議員ばかりの日本。そりゃ 警察も検察も動かんわな。\\n\\nとはいえ、そんな輩を増殖させたのは我々日本人。\\n皮肉だよね。", "edit_history_tweet_ids": ["1734554860392235347"], "in_reply_to_user_id": "1433807542845538306", "author_id": "1433807542845538306", "id": "1734554860392235347", "conversation_id": "1734554578325315837"}, 
{"text": "@teff_mini 皮肉だよこれって気づかなそう〜", "edit_history_tweet_ids": ["1734514196560466172"], "in_reply_to_user_id": "699927548663205888", "author_id": "1166133344104435712", "id": "1734514196560466172", "conversation_id": "1734443458876846089"}, 
{"text": "非課税のお坊さんに書かせるのがえらいって事だよ皮肉 だよwww", "edit_history_tweet_ids": ["1734446226555498668"], "in_reply_to_user_id": "3046301947", "author_id": "3046301947", "id": "1734446226555498668", "conversation_id": "1734440919620083768"}, 
{"text": "@Boooonshin @shynq__ これモンストユーザーが猿みたいにバカって皮肉だよ", "edit_history_tweet_ids": ["1734414224410259674"], "in_reply_to_user_id": "906373382123294720", "author_id": "1542817370401800192", "id": "1734414224410259674", "conversation_id": "1734239005380857915"}, 
{"text": "@nekodama28 @A8502291998420 皮肉だよ🤪", "edit_history_tweet_ids": ["1734390332878717151"], "in_reply_to_user_id": "1420394341760045064", "author_id": "1090165058070503424", "id": "1734390332878717151", "conversation_id": "1733726959480537200"}, 
{"text": "@megane641_2 のにサージェント周は乗れるんだから皮肉だよな。", "edit_history_tweet_ids": ["1734198184317190175"], "in_reply_to_user_id": "2874743137", "author_id": "772244109117431810", "id": "1734198184317190175", "conversation_id": "1734192275889311844"}, 
{"text": "シン・エヴァンゲリオンもむっちゃくちゃ皮肉だよなこれ。\\n自分がいつまでも子供かと思ったら自 分の面倒見てくれた先輩の子供が大きくなってしまったのだしさ。\\n周りが大人になってるのにずっと子供のままでいられないでしょ普 通に。\\nそりゃアスカの恋心もそりゃ醒めますわな🙄", "edit_history_tweet_ids": ["1734191753572634757"], "in_reply_to_user_id": "95480925", "author_id": "95480925", "id": "1734191753572634757", "conversation_id": "1734187812566778121"}, 
{"text": "皮肉だよね～これ(´・ω・`)", "edit_history_tweet_ids": ["1734176755328659662"], "in_reply_to_user_id": "745607475571757057", "author_id": "745607475571757057", "id": "1734176755328659662", "conversation_id": "1734176477170860137"}, 
{"text": "@kanikama_keshin 皮肉だよ", "edit_history_tweet_ids": ["1734122665068384257"], "in_reply_to_user_id": "1522203053969055744", "author_id": "1716317104906043392", "id": "1734122665068384257", "conversation_id": "1734111729188237816"}, 
{"text": "@saiyaman1880153 @w_rzg50 @eg_uj4 自分で皮肉だよって言っちゃうのってすげえダサいよな", "edit_history_tweet_ids": ["1734114444719063436"], "in_reply_to_user_id": "1695295610084298752", "author_id": "1417782315246243841", "id": "1734114444719063436", "conversation_id": "1734002430621479294"}, 
{"text": "@w_rzg50 @eg_uj4 皮肉だよ", "edit_history_tweet_ids": ["1734051526765846789"], "in_reply_to_user_id": "1456483077090611200", "author_id": "1695295610084298752", "id": "1734051526765846789", "conversation_id": "1734002430621479294"}, 
{"text": "@IGf0b 主役になりたいngがその願望を叶えたばっかりに逆に🌱に主人公感を喰われてMOMを持っていかれたのもめちゃくちゃ皮肉だよね…ていうか主人公になりたい🌵とこの漫画の主人公の🌱って構図、なんかもう、すごいのでは？今読み返したらまた全然違う読み方できそう\\nまたの機会に読書会するか", "edit_history_tweet_ids": ["1734021448451420258"], "in_reply_to_user_id": "1276410239722549251", "author_id": "1577307613586665473", "id": "1734021448451420258", "conversation_id": "1733905109707608151"}, 
{"text": "発揮する姿を幾度となく見てきた。\\n戦争が無くならない理由を身を持って示してい るというのが、なんとも皮肉だよね。\\n戦争は正義と正義のぶつかり合いなんて言われるけど、ほんとそうだよね。", "edit_history_tweet_ids": ["1733894001772961969"], "in_reply_to_user_id": "440418820", "author_id": "440418820", "id": "1733894001772961969", "conversation_id": "1733893159686721537"}, 
{"text": "@zesuto_987123 はいはい、実名が危ないから銅板職人の名を自分で贈っておいて、それを自ら晒すとはどんな皮肉だよ🤣", "edit_history_tweet_ids": ["1733836205241102562"], "in_reply_to_user_id": "1568933766592368643", "author_id": "1469721867884068864", "id": "1733836205241102562", "conversation_id": "1733833597776511236"}, 
{"text": "@kikuchanusachan コタロー？😆そんなのあるんだ😆\\n私も昔、漢方で一気に治ったことあるよ❣️西洋医学のクスリは長 く続けるのイマイチ怖いんだよね😢\\n\\n5G電磁波の曝露も😱便利になればなるほど健康被害、なんか皮肉だよね😣", "edit_history_tweet_ids": ["1733789614979403832"], "in_reply_to_user_id": "1206244302", "author_id": "2889519068", "id": "1733789614979403832", "conversation_id": "1732309247474692594"}, 
{"text": "@kiraringo428 皮肉だよ…\\nわ〜すごいすごい👏ほんと…", "edit_history_tweet_ids": ["1733727264867819569"], "in_reply_to_user_id": "1668189203006631936", "author_id": "1568427024833970177", "id": "1733727264867819569", "conversation_id": "1733462667065762042"}, 
{"text": "人口を作れない状況を産み出してきた業界が実際に 人口が減って人手不足になった結果、自身が困ることになってるのって皮肉だよなぁ(笑)", "edit_history_tweet_ids": ["1733642610068410678"], "in_reply_to_user_id": "619137505", "author_id": "619137505", "id": "1733642610068410678", "conversation_id": "1733641173607338008"}, 
{"text": "左翼勢力は\\nお互いに憎しみあって\\n分裂して先鋭化する傾向。\\n\\nゆえに泡沫政党が増えて\\nいま みたいになるわけ。\\n\\n小さな小さなパイに固執して\\nなんなら自民党よりも保守。\\n自分たちの領域と権益と儲けのみが\\n大事な人た ちになってしまう。\\n\\n皮肉だよね", "edit_history_tweet_ids": ["1733633394284564830"], "in_reply_to_user_id": "96541769", "author_id": "96541769", "id": "1733633394284564830", "conversation_id": "1733557579173798360"}, 
{"text": "@D9bf0NRDYrL21Ba  ＞オスプレイは「中国産」とか、無茶苦茶\\n\\n皮肉だよねｗ\\n未亡人製造機と揶揄されてるから、品質が悪いのであれば中国製に違いな いと皮肉を言ってるだけだ", "edit_history_tweet_ids": ["1733601692053045490"], "in_reply_to_user_id": "1452879171252670466", "author_id": "1543520280173154304", "id": "1733601692053045490", "conversation_id": "1733395546013122653"},
{"text": "恩人が生きてるうちに与えられた恩を返したいがために守られるばかりの立場で居たくないテメノスの物語上のポジションが「神官(ヒーラー)」「名探偵」なのまあまあ皮肉だよな\\n\\nヒーラーは皆を守る立場のキャラクターなのに 恩人を守れてないし、探偵は死人が出てからじゃないと役に立たないから...", "in_reply_to_user_id": "1627724813086396417", "id": "1733493791422824864", "conversation_id": "1733493789300519041", "author_id": "1627724813086396417", "edit_history_tweet_ids": ["1733493791422824864"]}, 
{"text": "@Y6879876513484 なんでベンチなのにバスケしてたって言えるの笑バスケ応援してたの方がいいよ〜運動神経ゴミの陰キャくん😂ハッキリ言って君凄い皮肉だよ🤣", "in_reply_to_user_id": "1691394515104600064", "id": "1733350668851945721", "conversation_id": "1729079279122801126", "author_id": "1523596247814213635", "edit_history_tweet_ids": ["1733350668851945721"]}, 
{"text": "@kakaka12225 @umihashindayo 皮肉だよ。女さんが理解出来てないだけ", "in_reply_to_user_id": "1388748091721863176", "id": "1733179151883125186", "conversation_id": "1732966192879681578", "author_id": "1672971949923008512", "edit_history_tweet_ids": ["1733179151883125186"]}, 
{"text": "@akairosyuiro686 見事な皮肉だよねー\\nんなもん、存在しねえ笑", "in_reply_to_user_id": "140803137", "id": "1733118279663956043", "conversation_id": "1733112892093006222", "author_id": "2475267312", "edit_history_tweet_ids": ["1733118279663956043"]}, 
{"text": "@nanashinogonpee 皮肉だよ", "in_reply_to_user_id": "1453305132314202114", "id": "1733078371016626409", "conversation_id": "1733077743259250989", "author_id": "833579019127836672", "edit_history_tweet_ids": ["1733078371016626409"]}, 
{"text": "これよく考えたら、自分を絶対者だと誤認したデカグラマトンが最初から相対者として生まれてるの皮肉だよな…後、そうなると彼らの定義ではマルクトでさえ絶対者ではない訳だ。ここに当てはまるのは連邦生徒会長ぐらいで、連邦生徒会長を越える事でマルクトは初めて絶対者を証明出来るのか", "in_reply_to_user_id": "2465457217", "id": "1733064599711469849", "conversation_id": "1733061336345747887", "author_id": "2465457217", "edit_history_tweet_ids": ["1733064599711469849"]}, 
{"text": "@family_lov_life 私は2人子供がいますが大学費用が工面できないので3人目を諦めまし た。本当は3人欲しかった。\\n他にも理由はありますが大きくは大学費です。\\nだから今回のニュースにはどんな皮肉だよって思いますが、とりあえず大学費無償化に乗り出したことは応援したい。\\nそれが順調にいけば対象拡大もあるかも。", "in_reply_to_user_id": "1351518411453472769", "id": "1732981640459383090", "conversation_id": "1732728427491574180", "author_id": "843054125248000000", "edit_history_tweet_ids": ["1732981640459383090"]}, 
{"text": "@yurumazu 皮肉だよな笑\\n円安の時の日銀や財務省は過度な変動は躊躇なくとか言ってたけど、昨日今日のドル円の動きは投機的な動きもあるように見えるし、過度な変動そのものだろ！って感じですね。", "in_reply_to_user_id": "948208460822339584", "id": "1732979468946506120", "conversation_id": "1732931375609856451", "author_id": "1551934264169713671", "edit_history_tweet_ids": ["1732979468946506120"]}
]


}

"""

# JSONデータをパース
data = json.loads(json_data)


# def extract_values_with_key(data, target_key):
#     values = []
#     if isinstance(data, dict):
#         for k, v in data.items():
#             if k == target_key:
#                 values.append(v)
#             elif isinstance(v, (dict, list)):
#                 values.extend(extract_values_with_key(v, target_key))
#     elif isinstance(data, list):
#         for item in data:
#             values.extend(extract_values_with_key(item, target_key))
#     return values


# # 特定のキーを含むデータ全体を集める
# target_key = "conversation_id"  # 例として指定したキー
# collected_result = extract_values_with_key(data, target_key)
# print(json.dumps(collected_result, indent=2))

def extract_values_with_keys(data, target_keys):
    values = []
    if isinstance(data, dict):
        item_values = []
        for k, v in data.items():
            if k in target_keys:
                item_values.append(v)
            elif isinstance(v, (dict, list)):
                item_values.extend(extract_values_with_keys(v, target_keys))
        if item_values:
            values.append(item_values)
    elif isinstance(data, list):
        for item in data:
            values.extend(extract_values_with_keys(item, target_keys))
    return values


# 特定のキーを含むデータ全体を集める
target_keys = ["conversation_id", "id"]  # 例として指定したキー(会話idとツイートid)
collected_result = extract_values_with_keys(data, target_keys)
print(json.dumps(collected_result, indent=2))
