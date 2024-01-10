def get_column_as_int(matrix, column_index):
 
    column_values = [int(row[column_index]) for row in matrix]
    return column_values

example_matrix = [
   [
    "1737254036796215563",
    "1737331333121339791"
  ],
  [
    "1736732030816440412",
    "1737330086909800475"
  ],
  [
    "1737126138600652902",
    "1737324617403142486"
  ],
  [
    "1737276946038579542",
    "1737318078890053753"
  ],
  [
    "1737272539720843573",
    "1737293782008398013"
  ],
  [
    "1736688158497218936",
    "1737279834131497196"
  ],
  [
    "1737074247707840545",
    "1737279235671392378"
  ],
  [
    "1736741019511898382",
    "1737239731547820089"
  ],
  [
    "1736741019511898382",
    "1737227699641594051"
  ],
  [
    "1737176779100729789",
    "1737186111720730908"
  ],
  [
    "1736720273729274274",
    "1737165006150774882"
  ],
  [
    "1736243572767432938",
    "1737126911942484065"
  ],
  [
    "1737105400472989783",
    "1737107646107500833"
  ],
  [
    "1737086716677443963",
    "1737094167833223647"
  ],
  [
    "1737082236254683543",
    "1737093994059116870"
  ],
  [
    "1736812704919433310",
    "1737082873646309508"
  ],
  [
    "1736710674573820164",
    "1737059087370850418"
  ],
  [
    "1736953427308237090",
    "1737046373638558034"
  ],
  [
    "1736012659584278760",
    "1737045693699879258"
  ],
  [
    "1736682131693490471",
    "1737039956261077461"
  ],
  [
    "1736179628962943237",
    "1737036671307399234"
  ],
  [
    "1736901953219965130",
    "1737015084042600955"
  ],
  [
    "1736651009043378476",
    "1737007644244947175"
  ],
  [
    "1736699775167422900",
    "1736985606746669477"
  ],
  [
    "1736795041858039991",
    "1736980705459273795"
  ],
  [
    "1736699686021722142",
    "1736960448799633462"
  ],
  [
    "1736893036087689388",
    "1736956819824923113"
  ],
  [
    "1735798394038428149",
    "1736946764824145978"
  ],
  [
    "1736788638065897845",
    "1736937386704265464"
  ],
  [
    "1736662003325055164",
    "1736926455131697220"
  ],
  [
    "1736355605173129361",
    "1736923034840346664"
  ],
  [
    "1736879939990044977",
    "1736902624782471596"
  ],
  [
    "1736730177252839576",
    "1736878773533073914"
  ],
  [
    "1736726279586722189",
    "1736744855370633348"
  ],
  [
    "1733053769716547596",
    "1736731983932473380"
  ],
  [
    "1736513634648690790",
    "1736717443329085854"
  ],
  [
    "1736606178036359641",
    "1736710363046191110"
  ],
  [
    "1736664578338255321",
    "1736698922939347297"
  ],
  [
    "1736637641830109222",
    "1736697804423409674"
  ],
  [
    "1736189105841811543",
    "1736679901741326677"
  ],
  [
    "1736631233684340877",
    "1736665918376493157"
  ],
  [
    "1736662574601744630",
    "1736663405875122376"
  ],
  [
    "1735248168437367065",
    "1736661432970940799"
  ],
  [
    "1736532884910190938",
    "1736660533863198756"
  ],
  [
    "1736624603781640445",
    "1736636055842099653"
  ],
  [
    "1734793577325346822",
    "1736635809581994037"
  ],
  [
    "1736369663490318339",
    "1736621737612316741"
  ],
  [
    "1736582628793524426",
    "1736617846426501395"
  ],
  [
    "1736353564853969339",
    "1736605950939967552"
  ],
  [
    "1736591312797991231",
    "1736597906541666809"
  ],
  [
    "1736513550238257378",
    "1736528728300343531"
  ],
  [
    "1736366060646129728",
    "1736404521394532384"
  ],
  [
    "1736368824696569880",
    "1736387858003599835"
  ],
  [
    "1736215618964406582",
    "1736364394844664142"
  ],
  [
    "1736274990054695294",
    "1736363241364967814"
  ],
  [
    "1736218956430823570",
    "1736362924531384749"
  ],
  [
    "1736361078328840441",
    "1736362159813321101"
  ],
  [
    "1736200305061380482",
    "1736276106280567227"
  ]

]

# 例として、列のインデックスを1に指定してみます（0-indexedなので1は2列目を指します）
selected_column_index = 0

# 関数を呼び出して指定した列の中身をint型で取得します
result = get_column_as_int(example_matrix, selected_column_index)

# 結果を出力します
print(result)