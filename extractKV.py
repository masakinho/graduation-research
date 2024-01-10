# -*- coding: utf-8 -*-
import json

# JSONデータの例（異なるキーを持つと仮定）
json_data = """
{
    "data": [
{"text": "@shiromaru__57 皮肉です☺️", "in_reply_to_user_id": "1325044272429629440", "conversation_id": "1737254036796215563", "id": "1737331333121339791", "edit_history_tweet_ids": ["1737331333121339791"], "author_id": "1002893179203477504"}, 
{"text": "@primaverayuko @sinoppa1960 言ったもん勝ち🏅との🧠🍐なのかな👀\\n腐ってるんだな、見かけだけで\\n自慢の息子ですねぇ、親にとって‼️\\nえぇ、皮肉ですよ❓🤪\\nそんなこともわからんのか！親の顔が見て見たいわ💢", "in_reply_to_user_id": "1470988163388948480", "conversation_id": "1737264252027843021", "id": "1737331172743819582", "edit_history_tweet_ids": ["1737331172743819582"], "author_id": "92522047"}, 
{"text": "@LokRgTG6uetgC5w @N_rem_sleep 仰るとおりですよ。\\nあくまでワクチンを信じてる周りの人の反応に対する皮肉ですので。", "in_reply_to_user_id": "1228556378748284928", "conversation_id": "1736732030816440412", "id": "1737330086909800475", "edit_history_tweet_ids": ["1737330086909800475"], "author_id": "1380515607058124806"}, 
{"text": "@yottssi @femimatsu 自分の気に入らない物を感情論で排除した結果、自分の理想とはかけ離れた真逆のものになってしまうという皮肉ですな。\\n女だけの国とか・・・", "in_reply_to_user_id": "95057615", "conversation_id": "1737126138600652902", "id": "1737324617403142486", "edit_history_tweet_ids": ["1737324617403142486"], "author_id": "2209196120"}, 
{"text": "@nogusodao2019 @mhbbc_ @hochi_giants 皮肉ですか？笑", "in_reply_to_user_id": "1111835234314551297", "conversation_id": "1737276946038579542", "id": "1737318078890053753", "edit_history_tweet_ids": ["1737318078890053753"], "author_id": "1436967800338206730"}, 
{"text": "@bUi9yUfYEE1bFBo 皮肉ですよ。これ。", "in_reply_to_user_id": "1252535595848495104", "conversation_id": "1737272539720843573", "id": "1737293782008398013", "edit_history_tweet_ids": ["1737293782008398013"], "author_id": "1442722122070036489"}, 
{"text": "@PbZY7lgvHLOLOrL ですからJリーグに対する皮肉ですよ、私の本心で言ってるわけではありません。", "in_reply_to_user_id": "1483698396322213892", "conversation_id": "1737281203429056815", "id": "1737281717596217363", "edit_history_tweet_ids": ["1737281717596217363"], "author_id": "1016619395123064832"}, 
{"text": "@nonmo89 アイドルの顔面の比較対象に一般人とか高見がブスな事に対する皮肉ですか？", "in_reply_to_user_id": "1697254268506656768", "conversation_id": "1736688158497218936", "id": "1737279834131497196", "edit_history_tweet_ids": ["1737279834131497196"], "author_id": "1737278932146413568"}, 
{"text": "あ  あともう一個追加しよう\\n\\n⑤\\n今回も構造規定に関する処分は無かったね\\n(皮肉ですからね)", "in_reply_to_user_id": "1663752347254939649", "conversation_id": "1737074247707840545", "id": "1737279235671392378", "edit_history_tweet_ids": ["1737279235671392378"], "author_id": "1663752347254939649"}, 
{"text": "1限出席ありの授業に対する皮肉です。", "in_reply_to_user_id": "1631897582174875649", "conversation_id": "1737259261372379605", "id": "1737259378854748187", "edit_history_tweet_ids": ["1737259378854748187"], "author_id": "1631897582174875649"}, 
{"text": "@task0115 はい、皮肉です", "in_reply_to_user_id": "1255525024989016064", "conversation_id": "1736741019511898382", "id": "1737239731547820089", "edit_history_tweet_ids": ["1737239731547820089"], "author_id": "1476167187924946947"}, 
{"text": "@masamasamun 皮肉ですよ。", "in_reply_to_user_id": "1476167187924946947", "conversation_id": "1736741019511898382", "id": "1737227699641594051", "edit_history_tweet_ids": ["1737227699641594051"], "author_id": "1255525024989016064"}, 
{"text": "@angechan__ あの涙は本当に何だったんだろう。\\n大変な時ファン一丸となって応援した気持ちがあるからこそ裏切られたとしか思えないですよね。\\nやり場のない気持ちをぶつける所さえこの祝福ムードでないですからね。\\n廉くんに申し訳ないし、皮肉ですが改めて廉くんのプロアイドルを感じさせられました。", "in_reply_to_user_id": "1476965151496880131", "conversation_id": "1737176779100729789", "id": "1737186111720730908", "edit_history_tweet_ids": ["1737186111720730908"], "author_id": "1456736856"}, 
{"text": "@YazawaChihiro ちょっと皮肉です。\\n縁故と恋愛(世襲者独自の当たり前になってる)", "in_reply_to_user_id": "3495240433", "conversation_id": "1736720273729274274", "id": "1737165006150774882", "edit_history_tweet_ids": ["1737165006150774882"], "author_id": "1709534767304314881"}, 
{"text": "正直確信はないのですが……\\n\\n英国王室を離脱した(いわば「住む場所がなくなった」)ヘンリー王子のことではないかと……\\n\\nだとしたら…その、なんていうか、とんでもない皮肉ですよね\\n\\n“Henry”の意味についてはWiki含め多くのサイトで説明されているのでここでは引用元を伏せます", "in_reply_to_user_id": "1667176083702136834", "conversation_id": "1737158718259892704", "id": "1737160272455086249", "edit_history_tweet_ids": ["1737160272455086249"], "author_id": "1667176083702136834"}, 
{"text": "@nvtype01 考えてみたら 飛べない鳥に「ツバサ」という名前はちょっとした皮肉ですよね😓\\n逆に言うと だからこそ 飛びたいという夢を持てたのかもしれませんが", "in_reply_to_user_id": "740513061946040320", "conversation_id": "1736243572767432938", "id": "1737126911942484065", "edit_history_tweet_ids": ["1737126911942484065"], "author_id": "4771497620"}, 
{"text": "@fire_2040 一応あるっぽいですよ！\\nボーっとするのを勝負するってなんか皮肉ですね🤣🤣", "in_reply_to_user_id": "1356459973035745283", "conversation_id": "1736330865465262417", "id": "1737110963042849138", "edit_history_tweet_ids": ["1737110963042849138"], "author_id": "1708305843245170688"}, 
{"text": "@sparobobaka ガイの死を一番引きずってたのが、殺した当人のムネタケってのがすごい皮肉ですよね……（アキトですらもう乗り越えてたのに）。あっちのエピソードのやるせなさも凄まじい", "in_reply_to_user_id": "1061196001443082240", "conversation_id": "1737105400472989783", "id": "1737107646107500833", "edit_history_tweet_ids": ["1737107646107500833"], "author_id": "88497616"}, 
{"text": "@nina_nirvalen えぇ皮肉 ですとも()", "in_reply_to_user_id": "1216736864305958914", "conversation_id": "1737086716677443963", "id": "1737094167833223647", "edit_history_tweet_ids": ["1737094167833223647"], "author_id": "1121112748396466176"}, 
{"text": "@029dai そういう設定になってるので、そこも含めての、例に出された親子さんへのちょっとした冗談と皮肉です。", "in_reply_to_user_id": "1510261396420055042", "conversation_id": "1737082236254683543", "id": "1737093994059116870", "edit_history_tweet_ids": ["1737093994059116870"], "author_id": "1697273054366437376"}, 
{"text": "@akitanmandai そういうファンを茶化すコントとか、一番やりそうな二人ですけど。\\nなんか皮肉ですね 笑", "in_reply_to_user_id": "609321153", "conversation_id": "1736812704919433310", "id": "1737082873646309508", "edit_history_tweet_ids": ["1737082873646309508"], "author_id": "1231920608969015297"}, 
{"text": "揶揄と皮肉ですよ？", "in_reply_to_user_id": "1183015291854315521", "conversation_id": "1736024493246799895", "id": "1737069948705603808", "edit_history_tweet_ids": ["1737069948705603808"], "author_id": "1183015291854315521"}, 
{"text": "@nocco6 皮肉です。。。", "in_reply_to_user_id": "634454085", "conversation_id": "1736923695426458044", "id": "1737061134765883820", "edit_history_tweet_ids": ["1737061134765883820"], "author_id": "1724767069747761152"}, 
{"text": "@s_kikutake #無所属 に騙される。\\nそれはオミノ氏に言えますよね。\\n\\nオミノ氏はなんで自民党として出馬しないんでしょうね？\\n\\nブーメランって怖い。\\nそもそもオミノ家ってオヤジも自民党じゃん。\\n自民党会派の議員が選挙の時は無所属って、自民党ってそんなやましい組織なんですかね？\\n\\n皮肉ですけど。", "in_reply_to_user_id": "306240661", "conversation_id": "1736710674573820164", "id": "1737059087370850418", "edit_history_tweet_ids": ["1737059087370850418"], "author_id": "786563538462453760"}, 
{"text": "@hinekure07301 皮肉ですね…😭", "in_reply_to_user_id": "440803802", "conversation_id": "1736953427308237090", "id": "1737046373638558034", "edit_history_tweet_ids": ["1737046373638558034"], "author_id": "1109657657764282370"}, 
{"text": "@beljelac 「映る場合もある」と言っています。\\n皮肉です。\\n\\n自民が公明を評価することなど私の関心事ではあ りませんが、自民党に褒められて嬉しいのですか？", "in_reply_to_user_id": "1569213496709238784", "conversation_id": "1736012659584278760", "id": "1737045693699879258", "edit_history_tweet_ids": ["1737045693699879258"], "author_id": "1574399925852737536"}, 
{"text": "@ko4ko4ko4 @kyn15_abc @kibori_2nd もちろん皮肉ですよ。\\n世界一マスクして世界一ワクチン打って世界一手指消毒した日本で世界一の感染者数と世界一の死者数出したんですから。\\n\\nやっぱりワクチン打てば打つほどコロナにもかかるし、他の病気にもかかるんじゃね？", "in_reply_to_user_id": "1284820502012260352", "conversation_id": "1736682131693490471", "id": "1737039956261077461", "edit_history_tweet_ids": ["1737039956261077461"], "author_id": "989802226259447808"}, 
{"text": "@kokoseeee24 @ad7d2935094a4f2 @tasogare58682 @yahweh2424 @NomoreWar2023 あ、それ、SNSで五毛退治しているという🐰に対する皮肉ですね(*^^*)", "in_reply_to_user_id": "1734789157434834944", "conversation_id": "1736179628962943237", "id": "1737036671307399234", "edit_history_tweet_ids": ["1737036671307399234"], "author_id": "1596617577912238080"}, 
{"text": "@HakoniwaTrain @Xha95NSJ5N87eQy 賛同。\\nすっごい皮肉ですね。\\nでもそう評されて当然だと思います。腹もたたないし。\\n一応の良識あるつもりの国民としても、開催（予定）地、地元府民としても。\\n#万博はただの利権\\n#利権万博\\n#カジノ万博\\n#万博いらんねん\\n#万博中止 一択。\\n\\n※あくまで個人的感想。\\n※あくまで独言。", "in_reply_to_user_id": "1093328824090079232", "conversation_id": "1736983019679097205", "id": "1737022683681005673", "edit_history_tweet_ids": ["1737022683681005673"], "author_id": "1597979568555425792"}, 
{"text": "@mmrock_easy 皮肉ですよね‥自分の中では価値観がひっくり返ったような出来事だったのですが、世の中がいつも通りすぎて歯痒いです💦\\n\\nいえいえ〜私の力なんて微々たるもので、見て実行に移してる方々が一番素晴らしいです🙏✨何か掲載すべき情報があればお待ちしてます！", "in_reply_to_user_id": "158446175", "conversation_id": "1736901953219965130", "id": "1737015084042600955", "edit_history_tweet_ids": ["1737015084042600955"], "author_id": "1721340337694892032"}, 
{"text": "@yunishio @ok_sen2208 @owo_yagi3bokujo そのような諸外国は知る限り存在しないのですが、何 処かの独裁国の林でもされていますか？\\n\\nという皮肉です。\\n理解できませんでしたか？", "in_reply_to_user_id": "112901232", "conversation_id": "1736651009043378476", "id": "1737007644244947175", "edit_history_tweet_ids": ["1737007644244947175"], "author_id": "1361245225"}, 
{"text": "@G_st_tw で隣の市に無印できちゃったのが超皮肉ですよねー😂", "in_reply_to_user_id": "1088403172240982016", "conversation_id": "1736699775167422900", "id": "1736985606746669477", "edit_history_tweet_ids": ["1736985606746669477"], "author_id": "1211101875463839744"}, 
{"text": "@readoffman 皮肉です", "in_reply_to_user_id": "1487319889895313409", "conversation_id": "1736795041858039991", "id": "1736980705459273795", "edit_history_tweet_ids": ["1736980705459273795"], "author_id": "1443022593297055744"}, 
{"text": "@RRrP3iuRoOdrzpk @DDD93833956 @JOJOkirst 皮肉ですよ。タクシー代出して 貰えるほど魅力のある顔はしてないから、それに気付くため鏡を見ろってことです。", "in_reply_to_user_id": "1708698241070735360", "conversation_id": "1736699686021722142", "id": "1736960448799633462", "edit_history_tweet_ids": ["1736960448799633462"], "author_id": "1015805921027473408"}, 
{"text": "@sttknm しかも草加さんが戦死した時、1番惜しんだのが巧さんだったと言うのが草加さんにとって皮肉ですよね…。そもそもあの2人の仲があんなに悪い のは、草加さんがよろしくって言った時、巧さんが失礼な態度をとったこともあると思うので、あんな態度とらなければまだマシな仲で済んだ気もします。", "in_reply_to_user_id": "183499286", "conversation_id": "1736893036087689388", "id": "1736956819824923113", "edit_history_tweet_ids": ["1736956819824923113"], "author_id": "1477522064089436163"}, 
{"text": "@sanjou2020 皮肉です", "in_reply_to_user_id": "1254049308401217540", "conversation_id": "1735798394038428149", "id": "1736946764824145978", "edit_history_tweet_ids": ["1736946764824145978"], "author_id": "1332254570618122241"}, 
{"text": "@Tanthencha 知恵袋でとか皮肉ですね", "in_reply_to_user_id": "1540749972572086272", "conversation_id": "1736788638065897845", "id": "1736937386704265464", "edit_history_tweet_ids": ["1736937386704265464"], "author_id": "1274491651604398081"}, 
{"text": "@pakira334y9 @hasegawa24  いや、皮肉ですよね。慇懃無礼ともいう。", "in_reply_to_user_id": "2878154928", "conversation_id": "1736662003325055164", "id": "1736926455131697220", "edit_history_tweet_ids": ["1736926455131697220"], "author_id": "1179140783749787648"}, 
{"text": "@last_alterego 克服してしまうと出来ない子の気持ちがわからないから、出来ないままでいていいと思ってそう。（もちろん皮肉です）", "in_reply_to_user_id": "157387411", "conversation_id": "1736355605173129361", "id": "1736923034840346664", "edit_history_tweet_ids": ["1736923034840346664"], "author_id": "113821487"}, 
{"text": "@Oz4lzi6Ro 同意！\\n横浜赤レンガ倉庫も明治期に建てられボロボロでしたが、商業施設 として再生。横浜の観光名所に。\\n\\n技術的な問題でなく、お金の問題だったのでしょう。\\n\\n観光振興を掲げる下関市が、貴重な観光資源をぶっ壊すなんて皮肉ですね。\\n\\n都市の記憶を消していくと本当につまらない街になるのにね。", "in_reply_to_user_id": "1513782977632694272", "conversation_id": "1736879939990044977", "id": "1736902624782471596", "edit_history_tweet_ids": ["1736902624782471596"], "author_id": "1437722635291422720"}, 
{"text": "@KonomitihitoriT 皮肉ですね。", "in_reply_to_user_id": "1481202863682760706", "conversation_id": "1736897730818236486", "id": "1736898245551595566", "edit_history_tweet_ids": ["1736898245551595566"], "author_id": "1172025252110450688"}, 
{"text": "@GACHIKOI_MOMOHA 皮肉ですので、ご安心ください😂🙇♂️", "in_reply_to_user_id": "1239543477022502913", "conversation_id": "1729373518293606703", "id": "1736887673951015177", "edit_hiistory_tweet_ids": ["1736887673951015177"], "author_id": "801573871249813504"}, 
{"text": "@8XwOZXVF1i1120 私もどちらかといえばエンジンよりの人間ですが、決してEVが嫌いとかでも無く、むしろ好きですよ♪\\n\\nちなみにブロックはどうでもよくて、そういう他者を認めない姿勢が君達が好きなEVの普及を妨げてるんじゃないの？的な皮肉です🤣🤣", "in_reply_to_user_id": "1655544938950709248", "conversation_id": "1736730177252839576", "id": "1736878773533073914", "edit_history_tweet_ids": ["1736878773533073914"], "author_id": "1952314304"}, 
{"text": "@narita_yusuke 皮肉ですか", "in_reply_to_user_id": "1218695211754250240", "conversation_id": "1736726279586722189", "id": "1736744855370633348", "edit_history_tweet_ids": ["1736744855370633348"], "author_id": "1642064331318910976"}, 
{"text": "@81_480 @swan_0619 メモリー消させた時は、奴の本気を見た気がしましたよ😭✨任務遂行のためだ けにいる一見冷たそうなロボと思わせて誰よりも優しかったですね😭人はみんなサムを騙して利用してたのに。皮肉です🥲\\n\\nお二人「ジ.ョ.ジ.ョ.ラ.ビ.ッ.ト」は見ましたか？寒口久上ル素敵なんですよ☺️", "in_reply_to_user_id": "13 360175340887285760", "conversation_id": "1733053769716547596", "id": "1736731983932473380", "edit_history_tweet_ids": ["1736731983932473380"], "author_id": "1587746199011880960"}, 
{"text": "NHKを批判する文脈でリツイートされましたが、これ原子力専門家に対する皮肉ですからね。当時は爆破弁ではなく、水素爆発によって原子炉建屋の外壁が崩落していました。関村教授は原子力工学の第一人者です。", "in_reply_to_user_id": "105424189", "conversation_id": "702899917413416960", "id": "1736723500583563671", "edit_history_tweet_ids": ["1736723500583563671"], "author_id": "105424189"}, 
{"text": "@YH09rameeCQ2bLl 最大限の愛と込めた皮肉ですｗ", "in_reply_to_user_id": "1542124594022166529", "conversation_id": "1736513634648690790", "id": "1736717443329085854", "edit_history_tweet_ids": ["1736717443329085854"], "author_id": "990425524483715072"}, 
{"text": "@lovejpkr39 犯罪を犯し た外国人だけ批判すればいい。\\nその国の人間だからと言う理由で批判すればヘイト。\\nそのようにしたのがネトウヨの支持する自民党というのは本当に皮肉ですね。\\n肉屋を支持する豚ですわ。", "in_reply_to_user_id": "1347783763036569603", "conversation_id": "1736606178036359641", "id": "1736710363046191110", "edit_history_tweet_ids": ["1736710363046191110"], "author_id": "1151793874555117568"}, 
{"text": "@moon991499 ナイス皮肉です。", "in_reply_to_user_id": "1705169081459175424", "conversation_id": "1736664578338255321", "id": "1736698922939347297", "edit_history_tweet_ids": ["1736698922939347297"], "author_id": "1557207568602505216"}, 
{"text": "@Bonjour4145 あれ？数日前までは維新と競り合ってたのに10%も急に伸びてるのなんでだろ🙄❓(皮肉です)", "in_reply_to_user_id": "1155322878776107008", "conversation_id": "1736637641830109222", "id": "1736697804423409674", "edit_history_tweet_ids": ["1736697804423409674"], "author_id": "797169695065604097"}, 
{"text": "@PontaKawagoe @palm_tree_gogo 皮肉です", "in_reply_to_user_id": "1472758352187129862", "conversation_id": "1736189105841811543", "id": "1736679901741326677", "edit_history_tweet_ids": ["1736679901741326677"], "author_id": "1538098235511689216"}, 
{"text": "@Wyrm50 べくれてるんでしょ・・・\\n\\nああ、皮肉です", "in_reply_to_user_id": "365854300", "conversation_id": "1736631233684340877", "id": "1736665918376493157", "edit_history_tweet_ids": ["1736665918376493157"], "author_id": "86226474"}, 
{"text": "@1129suragi 天国への扉ですか。なかなか上手い皮肉ですわね", "in_reply_to_user_id": "874985011144818691", "conversation_id": "1736662574601744630", "id": "1736663405875122376", "edit_history_tweet_ids": ["1736663405875122376"], "author_id": "1681280391557296129"}, 
{"text": "@snufkin976 その火が自分に・・・とは火肉…もとい皮肉ですねぇ。。。", "in_reply_to_user_id": "497532953", "conversation_id": "1735248168437367065", "id": "1736661432970940799", "edit_history_tweet_ids": ["1736661432970940799"], "author_id": "229811791"}, 
{"text": "@mukashihakodomo @chuunen_tsukasa 失敗小僧さんが述べている『立花氏の勝ちパターン』とは、立花氏が3月8日に大津氏に党首の地位を譲ったことが心裡留保であったと自ら認め、その結果、有印私文書偽造の罪で収監されるというシナリオを指します。このシナリオが実現すれば、斎藤氏が党首になる可能性がわずかに存在するという皮肉です。", "in_reply_to_user_id": "201733641", "conversation_id": "1736532884910190938", "id": "1736660533863198756", "edit_history_tweet_ids": ["1736660533863198756"], "author_id": "1678269357514985480"}, 
{"text": "@8i9FEaaOrV18702 @sakuratsukisima フェミに対する皮肉ですw", "in_reply_to_user_id": "1684658477447405572", "conversation_id": "1736624603781640445", "id": "1736636055842099653", "edit_history_tweet_ids": ["1736636055842099653"], "author_id": "1465814507159441408"}, 
{"text": "@blog_randy @bad_texter マジレスすると、これは誤謬ではなく間違い(認知の歪み/偏向)を指摘する“皮肉”です。\\n※知能で食べる食べないを判断するのがそもそも“間違い”なので、あなたの例は例えになっていない(犬&amp;人間=哺乳類は“正解”)", "in_reply_to_user_id": "1081521170334117889", "conversation_id": "1734793577325346822", "id": "1736635809581994037", "edit_history_tweet_ids": ["1736635809581994037"], "author_id": "1032631352695255041"}, 
{"text": "@iwate2megumi 一年半政治やってきて、\\n名前が知れたのがパリ旅行って皮肉ですか？笑\\n\\nご陽気な方ですなぁ〜笑", "in_reply_to_user_id": "1458289025610305536", "conversation_id": "1736369663490318339", "id": "1736621737612316741", "edit_history_tweet_ids": ["1736621737612316741"], "author_id": "1067826272435265536"}, 
{"text": "@vegakoto うちも毒親(特に母)だったので、我慢して我慢して40代になりついに鬱病を発症しました。母から言われた言葉のお陰で(皮肉です)自己肯定感は地べたに落ちるどころか地下深くまで落ちてます。", "in_reply_to_user_id": "1464236249502613505", "conversation_id": "1736582628793524426", "id": "1736617846426501395", "edit_history_tweet_ids": ["1736617846426501395"], "author_id": "1716252775884165120"}, 
{"text": "@111meenya 人気商品だから、明日には転売ヤーが買い漁って、メルカリで高値で取引されちゃうんで、見かけたら早く買っておかないと！！！笑\\n\\nあ、皮肉ですよ", "in_reply_to_user_id": "1053393903661924352", "conversation_id": "1736353564853969339", "id": "1736605950939967552", "edit_history_tweet_ids": ["1736605950939967552"], "author_id": "1067826272435265536"}, 
{"text": "@zyklon37 元記載はそもそもで、日本語訳された表記を確認してればあら？ってなりそうですけどね。\\nそういうことをせず、重要なことをいつもつぶやかないので大元以外はどうでもいい事担当なんだなという皮肉です。", "in_reply_to_user_id": "1480229624915587072", "conversation_id": "1736591312797991231", "id": "1736597906541666809", "edit_history_tweet_ids": ["1736597906541666809"], "author_id": "1541958278804312064"}, 
{"text": "@MMondeSelection 防空システムが超低空というのに対応していないのはなんとも皮肉ですね。一台数十万くらいのドローンが数十機、数百機で飛来すると全然防空は機能しないと。", "in_reply_to_user_id": "1454396477782982657", "conversation_id": "1736513550238257378", "id": "1736528728300343531", "edit_history_tweet_ids": ["1736528728300343531"], "author_id": "1520789214371418114"}, 
{"text": "@Waratas 僕もTHE Wは、数あるお笑い賞レースの中でも1番に好きです\\nおそらく最大の理由は、僕にとって出場者が全員“異性”だからだと思います\\n本大会は世間から[女性蔑視]という今の時代にそぐわない声が多数出ているので、それを僕が1番好きになってしまうのは何とも皮肉ですが…", "in_reply_to_user_id": "93874208", "conversation_id": "1736164349478404111", "id": "1736412072152592397", "edit_history_tweet_ids": ["1736412072152592397"], "author_id": "2921311880"}, 
{"text": "@Chanco_Mattun 昨日まっつんさんと もうこの後に誰も続いてほしくないですねって話してたのにあの頃に旅立たれてたなんて皮肉ですね😢", "in_reply_to_user_id": "963727563968229376", "conversation_id": "1736366060646129728", "id": "1736404521394532384", "edit_history_tweet_ids": ["1736404521394532384"], "author_id": "794403534"}, 
{"text": "@mikarin_baby それを語る彼女の一族がメディアにも度々登場するし活躍する有名新聞記者や学者などインテリのみで構成されてるのがこれまた皮 肉です。", "in_reply_to_user_id": "1371402169207771140", "conversation_id": "1736368824696569880", "id": "1736387858003599835", "edit_history_tweet_ids": ["1736387858003599835"], "author_id": "1521825923544530945"}, 
{"text": "@y_toutou 茂助、個人的にはあの映画の準主人公だったなと思います…秀吉の「首なんてどうでもいいんだよ」というラストの言葉と対比してるの本当に皮肉ですね〜", "in_reply_to_user_id": "3010064071", "conversation_id": "1736363867696242885", "id": "1736365389234557315", "edit_history_tweet_ids": ["1736365389234557315"], "author_id": "1157969703639252998"}, 
{"text": "@yuhikakunnnn @samami_sasami 多分本省の残業時間を公開せよってい う皮肉ですよ()", "in_reply_to_user_id": "2555975094", "conversation_id": "1736215618964406582", "id": "1736364394844664142", "edit_history_tweet_ids": ["1736364394844664142"], "author_id": "1660296277589118978"}, 
{"text": "@mainichi この指揮者みたいな服も税金で買ったのですかね？皮肉です。指揮者に失礼です。", "in_reply_to_user_id": "49540955", "conversation_id": "1736274990054695294", "id": "1736363241364967814", "edit_history_tweet_ids": ["1736363241364967814"], "author_id": "1455308103679766536"}, 
{"text": "@IXT62961634 小学校で道徳をならわなかったのでしょうか？受験に必要な科目ばかりやって政治家になったのでしょうか？全部皮肉です。", "in_reply_to_user_id": "1016436803161579520", "conversation_id": "1736218956430823570", "id": "1736362924531384749", "edit_history_tweet_ids": ["1736362924531384749"], "author_id": "1455308103679766536"}, 
{"text": "海外手当が無くなるので、相当収入は下がるが、これはしょうがない。\\nまずは妻を目覚めさせる事が優先だと考えた。\\n（目覚めるって皮肉です。）\\n\\n実際日本に戻り収入は下がった。\\nまた、慣れない仕事で評価も下がり、2023年は更に収入が下がった。", "in_reply_to_user_id": "1651578861732384769", "conversation_id": "1736361078328840441", "id": "1736362159813321101", "edit_history_tweet_ids": ["1736362159813321101"], "author_id": "1651578861732384769"}, 
{"text": "@cheriefraise4 皮肉です笑笑", "in_reply_to_user_id": "3103114908", "conversation_id": "1736328474456096974", "id": "1736341845335212370", "edit_history_tweet_ids": ["1736341845335212370"], "author_id": "1262058432690937856"}, 
{"text": "@aheaheeeeeeeee 年内から年始にかけて？\\nこのタイミングで情報出して年始以降だったらDMCコラボの二の舞ぞ（当時はパズドラーじゃなかったしDMCコラボと今回が違うことはわかってます。あくまで皮肉です。）", "in_reply_to_user_id": "1091232723526512640", "conversation_id": "1736200305061380482", "id": "1736276106280567227", "edit_history_tweet_ids": ["1736276106280567227"], "author_id": "1693529038890156032"}
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
    conversation_id_values = []  # "conversation_id"の値を格納する配列を初期化
    if isinstance(data, dict):
        item_values = []
        for key in target_keys:
            if key in data:
                item_values.append(data[key])
                if key == "conversation_id":
                    try:
                        conversation_id_values.append(int(data[key]))
                    except ValueError:
                        pass  # intに変換できない場合はスキップ
        if item_values:
            values.append(item_values)
        for v in data.values():
            if isinstance(v, (dict, list)):
                sub_values, sub_conversation_id_values = extract_values_with_keys(v, target_keys)
                values.extend(sub_values)
                conversation_id_values.extend(sub_conversation_id_values)
    elif isinstance(data, list):
        for item in data:
            sub_values, sub_conversation_id_values = extract_values_with_keys(item, target_keys)
            values.extend(sub_values)
            conversation_id_values.extend(sub_conversation_id_values)
    return values, conversation_id_values  # conversation_id_valuesも返すように変更



# 特定のキーを含むデータ全体を集める
target_keys = ["conversation_id", "id"]  # 例として指定したキー(会話idとツイートid)
collected_result = extract_values_with_keys(data, target_keys)
print(json.dumps(collected_result, indent=2))
