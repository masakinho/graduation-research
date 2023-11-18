# -*- coding: utf-8 -*-
import json

# JSONデータの例（異なるキーを持つと仮定）
json_data = """
{
    "data": [
{"text": "ドラマのように連続する映画を発明したらいつのまにかテレビドラマそのものになってたって皮肉だよなと思う", "edit_history_tweet_ids": ["1723929265639764097"], "id": "1723929265639764097", "in_reply_to_user_id": "5550932", "conversation_id": "1723929116884255141"}, 
{"text": "@Totto_shion1018 皮肉だよ", "edit_history_tweet_ids": ["1723917472557125939"], "id": "1723917472557125939", "in_reply_to_user_id": "990362420576055297", "conversation_id": "1723914083823710583"}, 
{"text": "自決メガネを支持してるボリュームゾーンは\\n１既婚者中年女性\\n２その夫世\\n３その子供世代(中高生)\\nなんである。\\n長生きする属性なんであるw皮肉だよね。飢えてないのに羅生門を地で行ってるw", "edit_history_tweet_ids": ["1723874084839473299"], "id": "1723874084839473299", "in_reply_to_user_id": "1667423683764436993", "conversation_id": "1723872307007868954"}, 
{"text": "@Suipx_ 元チ ーターだろ？じゃないとブロンズ帯で燻ってる訳ないやん笑 チート辞めても同じレベルで迷惑かけてんだから皮肉だよな笑", "edit_history_tweet_ids": ["1723796981443592214"], "id": "1723796981443592214", "in_reply_to_user_id": "1696458971270520832", "conversation_id": "1723786470555836679"}, 
{"text": "@yuuuuuya2018 皮肉だよw\\n普通に評価最悪ですw", "edit_history_tweet_ids": ["1723765704543858809"], "id": "1723765704543858809", "in_reply_to_user_id": "1426919897032921088", "conversation_id": "1723750182695928113"}, 
{"text": "@gunk3141592654 @6d745 私自身人形に人権はないと思うよ\\nただ単に愛しているなら彼女が結婚したいと言っていないのにするというのは彼女を本当の意味で愛しているのだろうかという皮肉だよ", "edit_history_tweet_ids": ["1723669922692423920"], "id": "1723669922692423920", "in_reply_to_user_id": "4408479689", "conversation_id": "1723502626602647973"}, 
{"text": "@retake272 地上波に来てからのほうが話題になってるの皮肉だよねえ…", "edit_history_tweet_ids": ["1723664075027272107"], "id": "1723664075027272107", "in_reply_to_user_id": "119706493", "conversation_id": "1723663487841530008"}, 
{"text": "皮肉だよな…", "edit_history_tweet_ids": ["1723635260574105801"], "id": "1723635260574105801", "in_reply_to_user_id": "1598629283030659072", "conversation_id": "1723635113278464267"}, 
{"text": "@martytaka777 ＞11月11日は、ポーランド独立記念日。10万人を超えるポーランド人がワルシャワで行進した。\\n\\n方や日本と来た日には・・・\\n\\n8月15日は盛大にお祝い（皮肉だよ）するが、4月28日なんて、ほとんど完全に無視されてるもんな・・・😭\\n情けない", "edit_history_tweet_ids": ["1723555312739975280"], "id": "1723555312739975280", "in_reply_to_user_id": "771195014718251009", "conversation_id": "1723541606274601075"}, 
{"text": "@bunny197202 @gerogeroR 皮肉だよ。", "edit_history_tweet_ids": ["1723523827425308937"], "id": "1723523827425308937", "in_reply_to_user_id": "1463885532874739714", "conversation_id": "1723519319290830922"}, 
{"text": "@toritetuhanzai @ryoutou_ryouda 撮り鉄なんか人の言うこと聞くことないやんて言う皮肉だよ", "edit_history_tweet_ids": ["1723299241769251277"], "id": "1723299241769251277", "in_reply_to_user_id": "1708229041822822400", "conversation_id": "1723290504278991337"}, 
{"text": "@Destiny_Knight4 どういう皮肉だよw", "edit_history_tweet_ids": ["1723288038959403301"], "id": "1723288038959403301", "in_reply_to_user_id": "846024055", "conversation_id": "1723284778215260428"}, 
{"text": "@mami_tanaka 皮肉か？皮肉だよな！", "edit_history_tweet_ids": ["1723215975297028409"], "id": "1723215975297028409", "in_reply_to_user_id": "372678643", "conversation_id": "1723194605812990020"}, 
{"text": "@shikakui_okao ハムスターは元々砂漠に棲息しているので、目の前で見つけた食べ物を全て口に突っ込んで確保しようとするんだよ\\nつまり皮肉だよ", "edit_history_tweet_ids": ["1723191591530344671"], "id": "1723191591530344671", "in_reply_to_user_id": "1543251502734929920", "conversation_id": "1723188104369225749"}, 
{"text": "@gekibnews どゆこと？当てられても真っ直ぐ走れって言ってるの？😂流石に白い車に対する皮肉だよね😅", "edit_history_tweet_ids": ["1722993086702174704"], "id": "1722993086702174704", "in_reply_to_user_id": "1075997635327143936", "conversation_id": "1722918267306832085"}, 
{"text": "@AIfnBwKTZkaetbg @yomayoi_got @takaino_chico @InooJUMP_np いか聞いてる？\\n\\n誤字？\\n\\n聞いても答えてない点、こちらはスルーしてあげてんのに、自分だけ主張してて草〜って皮肉だよ笑笑", "edit_history_tweet_ids": ["1722974091034923368"], "id": "1722974091034923368", "in_reply_to_user_id": "1558765602608906241", "conversation_id": "1721796265254817925"}, 
{"text": "あ、やっぱ言ってなかったのね\\nそういう皮肉だよな", "edit_history_tweet_ids": ["1722959183589573054"], "id": "1722959183589573054", "in_reply_to_user_id": "3057960140", "conversation_id": "1722381286692757811"}, 
{"text": "付き合い方が下手な人だから、向き合い方もよくなかったんだと思う。\\nただ独りでがむしゃらにやったって 続かないし、どこかで息切れする可能性を危惧してたのは事実。あまりに唐突でびっくりしてるけど、予定調和だったってこと？\\n\\n気が楽になった感じがあるのが何とも皮肉だよね。笑", "edit_history_tweet_ids": ["1722930737861874034"], "id": "1722930737861874034", "in_reply_to_user_id": "64309198", "conversation_id": "1722929010890719742"}, 
{"text": "@RonielYamato 皮肉だよね、一番人体に近い職種の人が一番本末転倒してるって\\n\\nまあ、商業に傾い ちゃった結果なんだろうけど", "edit_history_tweet_ids": ["1722918373720567947"], "id": "1722918373720567947", "in_reply_to_user_id": "1363134372094779394", "conversation_id": "1722832113068896643"}, 
{"text": "@ZanEngineer 環境活動家が三週間かけて減らしたCO2より格段に削減してるの皮肉だよな", "edit_history_tweet_ids": ["1722526025941483866"], "id": "1722526025941483866", "in_reply_to_user_id": "1191030472316338176", "conversation_id": "1722482221800685774"}
]

}

"""

# JSONデータをパース
data = json.loads(json_data)


def extract_values_with_key(data, target_key):
    values = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == target_key:
                values.append(v)
            elif isinstance(v, (dict, list)):
                values.extend(extract_values_with_key(v, target_key))
    elif isinstance(data, list):
        for item in data:
            values.extend(extract_values_with_key(item, target_key))
    return values


# 特定のキーを含むデータ全体を集める
target_key = "conversation_id"  # 例として指定したキー
collected_result = extract_values_with_key(data, target_key)
print(json.dumps(collected_result, indent=2))
