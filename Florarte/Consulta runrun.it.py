import pandas as pd

# Carregar o arquivo Excel
file_path = r'D:\Download\Estúdio_-_Solicitações-2025-02-18-07h-57m-59s.xlsx'
sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')

# Lista de códigos para pesquisar
search_codes = ['69440',
    '88670001',
    '88670002',
    '88671001',
    '88672001',
    '88673001',
    '88674001',
    '82621001',
    '82627001',
    '82641001',
    '95787001',
    '95788001',
    '95789001',
    '95790001',
    '95791001',
    '95792001',
    '87647001',
    '87685001',
    '95793001',
    '95799001',
    '95803001',
    '95804001',
    '95805001',
    '95806001',
    '95807001',
    '95808001',
    '95809001',
    '95810001',
    '95811001',
    '95812001',
    '95813001',
    '95814001',
    '95854001',
    '95855001',
    '95903001',
    '95907001',
    '96067001',
    '96068001',
    '96070001',
    '96071001',
    '96072001',
    '96075001',
    '96076001',
    '96077001',
    '96078001',
    '96079001',
    '96080001',
    '96081001',
    '96082001',
    '96083001',
    '96084001',
    '96085001',
    '96086001',
    '96087001',
    '96098001',
    '96108001',
    '96113001',
    '96116001',
    '96117001',
    '96118001',
    '96119001',
    '96120001',
    '96121001',
    '96122001',
    '96135001',
    '96136001',
    '90450001',
    '96150001',
    '96156001',
    '96156002',
    '96156003',
    '96167001',
    '96168001',
    '96169001',
    '96171001',
    '96172001',
    '96177001',
    '96177002',
    '87688001',
    '88091001',
    '88092001',
    '88093001',
    '88097001',
    '88100001',
    '88101001',
    '90435001',
    '95857001',
    '95861001',
    '95864001',
    '95867001',
    '95868001',
    '95869001',
    '95870001',
    '95871001',
    '95900001',
    '95929001',
    '95934001',
    '96020001',
    '96022001',
    '96133001',
    '96134001',
    '96176001',
    '88185001',
    '87848002',
    '88757001',
    '88769001',
    '89899001',
    '89902001',
    '95668001',
    '95669001',
    '95670001',
    '95671001',
    '95673001',
    '95675001',
    '95856001',
    '95858001',
    '95859001',
    '95860001',
    '95862001',
    '95866001',
    '95873001',
    '95879001',
    '95880001',
    '95881001',
    '95882001',
    '95883001',
    '95886001',
    '95889001',
    '95894001',
    '95895001',
    '95898001',
    '95901001',
    '95904001',
    '95915001',
    '95916001',
    '95917001',
    '95918001',
    '95919001',
    '95922001',
    '95923001',
    '95924001',
    '95925001',
    '95943001',
    '95944001',
    '95971001',
    '95984001',
    '95988001',
    '95990001',
    '95994001',
    '95995001',
    '95996001',
    '95997001',
    '95998001',
    '95999001',
    '96000001',
    '96001001',
    '96008001',
    '96009001',
    '96011001',
    '96012001',
    '96015001',
    '96016001',
    '96019001',
    '96021001',
    '96023001',
    '96027001',
    '96028001',
    '96029001',
    '96033001',
    '96034001',
    '96035001',
    '96036001',
    '96037001',
    '96038001',
    '96039001',
    '96066001',
    '96123001',
    '96126001',
    '96127001',
    '96128001',
    '96138001',
    '96139001',
    '96140001',
    '96141001',
    '95774001',
    '95777001',
    '95779001',
    '95780001',
    '95781001',
    '95782001',
    '95872001',
    '95896001',
    '95897001',
    '96144001',
    '96146001',
    '96147001',
    '95660001',
    '95667001',
    '95850001',
    '95899001',
    '90643001',
    '95940001',
    '95942001',
    '91382001',
    '95884001',
    '95885001',
    '95887001',
    '95888001',
    '95890001',
    '95912001',
    '95974001',
    '95974002',
    '96002001',
    '96003001',
    '96007001',
    '96010001',
    '96013001',
    '96014001',
    '96024001',
    '96026001',
    '96041001',
    '96042001',
    '96043001',
    '96044001',
    '96045001',
    '96046001',
    '96047001',
    '96048001',
    '96049001',
    '96051001',
    '96052001',
    '96055001',
    '96057001',
    '96060001',
    '96062001',
    '83975001',
    '83976001',
    '83977001',
    '84246001',
    '84289001',
    '84290001',
    '88005001',
    '88007001',
    '88008001',
    '88009001',
    '88013001',
    '88018001',
    '88019001',
    '88023001',
    '88114001',
    '88117001',
    '88121001',
    '88123001',
    '88124001',
    '88129001',
    '88132001',
    '88133001',
    '88137001',
    '88141001',
    '88145001',
    '88148001',
    '88154001',
    '88160001',
    '88173001',
    '88180001',
    '88183001',
    '88187001',
    '88191001',
    '89806001',
    '95863001',
    '95865001',
    '95874001',
    '95875001',
    '95876001',
    '95878001',
    '95908001',
    '95909001',
    '95910001',
    '95911001',
    '95913001',
    '95914001',
    '95920001',
    '95921001',
    '95926001',
    '95989001',
    '95991001',
    '96004001',
    '96005001',
    '96006001',
    '96017001',
    '96018001',
    '96030001',
    '96050001',
    '96050002',
    '96054001',
    '96056001',
    '96058001',
    '96058002',
    '96063001',
    '96163001',
    '96164001',
    '96165001',
    '87988001',
    '87991001',
    '87992001',
    '96160001',
    '96161001',
    '96162001',
    '87997001',
    '87999001',
    '88002001',
    '95783001',
    '95784001',
    '95785001',
    '95786001',
    '96059001',
    '96173001',
    '96174001',
    '96175001',
    '96061001',
    '96142001',
    '96143001',
    '96179001',
    '92676001',
    '93206001',
    '94147001',
    '94148001',
    '94149001',
    '95461001',
    '95462001',
    '81946012',
    '81960004',
    '89408004',
    '89410002',
    '89981001',
    '90030001',
    '88617001',
    '90060002',
    '90265001',
    '90266001',
    '90329001',
    '91188001',
    '91192001',
    '91198001',
    '91212001',
    '91214001',
    '91230001',
    '91231001',
    '91237001',
    '91240001',
    '91253001',
    '91253002',
    '91340002',
    '91345002',
    '91351002',
    '91352002',
    '91354002',
    '91356002',
    '91392002',
    '91401002',
    '91403002',
    '91407002',
    '91581001',
    '91590001',
    '91593001',
    '91600001',
    '91605001',
    '91666001',
    '91672001',
    '91694001',
    '91697001',
    '91702001',
    '91749001',
    '91752001',
    '91760001',
    '91841001',
    '92577001',
    '92597001',
    '92617001',
    '92619001',
    '92632001',
    '92635001',
    '92636001',
    '92642001',
    '92707001',
    '92714001',
    '92730001',
    '92733001',
    '92817002',
    '92825002',
    '92871001',
    '92871002',
    '92871003',
    '92899001',
    '92928001',
    '92929001',
    '92955002',
    '92956002',
    '92975001',
    '92982001',
    '93305001',
    '93489001',
    '93511001',
    '93572001',
    '93614001',
    '93643001',
    '93646001',
    '93647001',
    '93648001',
    '93722001',
    '93734001',
    '93744001',
    '93787001',
    '93788001',
    '93790001',
    '93794001',
    '93806001',
    '93807001',
    '93817001',
    '93819001',
    '93834001',
    '93841001',
    '93984001',
    '93985001',
    '93986001',
    '93987001',
    '93989001',
    '94517001',
    '95494001',
    '95495001',
    '95496001',
    '95497001',
    '95498001',
    '95499001',
    '95500001',
    '95503001',
    '95517001',
    '91002001',
    '91005001',
    '91009001',
    '94143001',
    '94575001',
    '95465001',
    '85221008',
    '57945001',
    '57945002',
    '57945003',
    '57946001',
    '57946002',
    '57946003',
    '57947001',
    '57953001',
    '57954001',
    '58405001',
    '72553001',
    '80757004',
    '85712001',
    '88565002',
    '88566002',
    '88568001',
    '88572001',
    '88610001',
    '89599002',
    '90461001',
    '90472001',
    '90472002',
    '90472003',
    '90494002',
    '90501001',
    '90653001',
    '90978001',
    '91167001',
    '91176001',
    '91722001',
    '91730001',
    '91734001',
    '91736001',
    '91923001',
    '91946001',
    '92093001',
    '92098001',
    '92098002',
    '92210001',
    '92444001',
    '92465001',
    '92743001',
    '92761001',
    '92893001',
    '92908001',
    '93136002',
    '93189002',
    '93527001',
    '93555001',
    '93635001',
    '93729001',
    '93747001',
    '93755001',
    '93760001',
    '93766001',
    '93774001',
    '93778001',
    '93781001',
    '93784001',
    '93786001',
    '93791001',
    '93795001',
    '93874001',
    '93897002',
    '93912001',
    '93944001',
    '93950001',
    '93957001',
    '93964001',
    '94050001',
    '94055001',
    '94056001',
    '94108001',
    '94113001',
    '94160001',
    '94162001',
    '94163001',
    '94165001',
    '94166001',
    '94168001',
    '94170001',
    '94172001',
    '94320001',
    '94658002',
    '95559001',
    '95560001',
    '95589001',
    '95954001',
    '95955001',
    '95956001',
    '95957001',
    '95958001',
    '95959001',
    '60572003',
    '60575003',
    '61078001',
    '61097002',
    '62424003',
    '64104001',
    '64145001',
    '64190001',
    '74137003',
    '76992001',
    '87041001',
    '87042001',
    '87043001',
    '87046001',
    '87047001',
    '87048001',
    '87049001',
    '87050001',
    '87051001',
    '87052001',
    '89253001',
    '89298003',
    '89300002',
    '89300003',
    '89300004',
    '89300005',
    '89321002',
    '89329001',
    '89337001',
    '89339001',
    '89340001',
    '89351001',
    '89355001',
    '89358001',
    '89363001',
    '89374001',
    '89422001',
    '89426001',
    '89428001',
    '89429001',
    '89433001',
    '89435001',
    '89438001',
    '89990001',
    '91365001',
    '91389001',
    '91394001',
    '91490005',
    '91496001',
    '91512002',
    '91513001',
    '91525001',
    '91531002',
    '91565001',
    '91567001',
    '91626001',
    '91668001',
    '91675001',
    '91677001',
    '91678001',
    '91700001',
    '91704001',
    '91706001',
    '91714001',
    '91727001',
    '91732001',
    '91769001',
    '91781001',
    '91782001',
    '91790001',
    '91795001',
    '91797001',
    '91804001',
    '91806001',
    '91809001',
    '91857001',
    '91862001',
    '91907002',
    '91911001',
    '91913001',
    '91921003',
    '91964001',
    '91978001',
    '91984001',
    '92095001',
    '92117001',
    '92191001',
    '92219001',
    '92222001',
    '92281001',
    '92362001',
    '92394001',
    '92408001',
    '92410001',
    '92422002',
    '92510001',
    '92640001',
    '92644001',
    '92646001',
    '92651001',
    '92658001',
    '92660001',
    '92664001',
    '92673001',
    '92687001',
    '92696001',
    '92701001',
    '92855001',
    '92909001',
    '92918001',
    '92923001',
    '92927001',
    '92930001',
    '93003001',
    '93005001',
    '93008001',
    '93010001',
    '93014001',
    '93015001',
    '93017001',
    '93018001',
    '93019001',
    '93020001',
    '93021001',
    '93361001',
    '93393001',
    '93542001',
    '93749001',
    '93750001',
    '93983001',
    '93990001',
    '93991001',
    '93992001',
    '93993001',
    '93994001',
    '93995001',
    '93996001',
    '93997001',
    '93998001',
    '93999001',
    '94000001',
    '94001001',
    '94002001',
    '94003001',
    '94004001',
    '94005001',
    '94006001',
    '94007001',
    '94008001',
    '94009001',
    '94010001',
    '94011001',
    '94013001',
    '94020001',
    '94034001',
    '94035001',
    '94077001',
    '94157001',
    '94164001',
    '94169001',
    '94175001',
    '94211001',
    '94235001',
    '94255001',
    '94256001',
    '94263001',
    '94273001',
    '94274001',
    '94275001',
    '94276001',
    '94278001',
    '94279001',
    '94280001',
    '94281001',
    '94282001',
    '94284001',
    '94285001',
    '94286001',
    '94288001',
    '94289001',
    '94412001',
    '94414001',
    '94835002',
    '94889001',
    '94926001',
    '94945001',
    '94948001',
    '95598001',
    '95601001',
    '68194001',
    '68633001',
    '68715001',
    '68816001',
    '68828001',
    '68829001',
    '68851001',
    '68872001',
    '68902001',
    '68907001',
    '45278001',
    '46990005',
    '57783007',
    '57876005',
    '57876008',
    '57897006',
    '68925002',
    '76569002',
    '76982002',
    '77602005',
    '77602006',
    '77602007',
    '77879004',
    '88057005',
    '89587001',
    '89587002',
    '89587003',
    '89587004',
    '89592002',
    '89592003',
    '89592004',
    '89592005',
    '89592006',
    '89605001',
    '89606001',
    '89606002',
    '89608003',
    '89608004',
    '89611001',
    '89622002',
    '89622003',
    '89622004',
    '89622005',
    '89622006',
    '89623001',
    '89625001',
    '89635002',
    '89637002',
    '90191002',
    '90232001',
    '90232002',
    '90235001',
    '90236001',
    '90244001',
    '90262001',
    '90271001',
    '90271002',
    '90274003',
    '90274004',
    '90274005',
    '90281001',
    '90284001',
    '90284002',
    '90296001',
    '90421009',
    '90421013',
    '90536001',
    '91416001',
    '91416002',
    '91432001',
    '91432002',
    '91449001',
    '91451001',
    '91452001',
    '91459001',
    '91460001',
    '91462001',
    '93043002',
    '93043003',
    '93051008',
    '93051012',
    '93093003',
    '93178001',
    '93237006',
    '93237010',
    '93237012',
    '93259002',
    '93259004',
    '93259005',
    '93259006',
    '93259009',
    '93259011',
    '93259012',
    '93259013',
    '93375012',
    '93568003',
    '93575004',
    '93575005',
    '93582004',
    '93582005',
    '93595001',
    '93595002',
    '93595004',
    '93595005',
    '93595006',
    '93595007',
    '93603003',
    '93850010',
    '94912001',
    '94912002',
    '94912003',
    '94912004',
    '94913001',
    '94913002',
    '94913003',
    '94913004',
    '94913005',
    '94913006',
    '95081002',
    '95210001',
    '95210002',
    '95235001',
    '95236001',
    '95280001',
    '95292001',
    '95604001',
    '95648002',
    '95649001',
    '95654001',
    '95654002',
    '95654003',
    '95654004',
    '95654005',
    '95851001',
    '95851002',
    '95851003',
    '95851004',
    '95851005',
    '95852001',
    '95932001',
    '95933001',
    '95936001',
    '95945001',
    '95945002',
    '95945003',
    '95945004',
    '95945005',
    '95947001',
    '95948001',
    '95949001',
    '95951001',
    '95969001',
    '91641001',
    '95714002',
    '73416001',
    '73416002',
    '77522001',
    '77700001',
    '77954001',
    '79106001',
    '79198001',
    '79215001',
    '79222001',
    '79282001',
    '79322001',
    '91153001',
    '91157001',
    '91158001',
    '92413001',
    '93198001',
    '93378001',
    '93433001',
    '93495001',
    '93968001',
    '93973001',
    '94062001',
    '94064001',
    '94112001',
    '94605001',
    '94644001',
    '94645001',
    '94646001',
    '94652001',
    '95391001',
    '95391002',
    '95392002',
    '95439001',
    '95457001',
    '95664001',
    '95664002',
    '95839001',
    '95840001',
    '95841001',
    '95843001',
    '95844001',
    '95845001',
    '95846001',
    '85236001',
    '89864001',
    '89868001',
    '89869001',
    '90535001',
    '90542001',
    '90546001',
    '90548001',
    '91863001',
    '91868001',
    '91870001',
    '91873001',
    '91883001',
    '91884001',
    '91885001',
    '91886001',
    '91887001',
    '91917001',
    '92351001',
    '92385001',
    '93050005',
    '93060001',
    '93060002',
    '93060003',
    '93768001',
    '93869001',
    '93888001',
    '93890001',
    '93894001',
    '93894002',
    '93898001',
    '95477001',
    '75398001',
    '92299001',
    '93100001',
    '93119001',
    '93130001',
    '93197001',
    '93234001',
    '93253001',
    '93336001',
    '93432001',
    '93440001',
    '93444001',
    '93450001',
    '93452001',
    '93454001',
    '93461001',
    '93476001',
    '93481001',
    '93487001',
    '93493001',
    '95684001',
    '95686001',
    '55251001',
    '55253001',
    '55255001',
    '45784004',
    '68730006',
    '55365001',
    '68564',
    '68565',
    '68566',
    '68567',
    '68568',
    '68569',
    '68570',
    '68571',
    '68572',
    '68573',
    '68574',
    '68575',
    '68576',
    '68580',
    '68581',
    '68583',
    '68584',
    '68585',
    '68586',
    '68587',
    '68588',
    '68589',
    '68590',
    '56009006',
    '83670005',
    '83682003',
    '83682006',
    '83695001',
    '83695003',
    '83695004',
    '83695006',
    '83696002',
    '83696003',
    '83696005',
    '88210002',
    '84139002',
    '84143001',
    '83068002',
    '84082001',
    '84082003',
    '87701001',
    '87701002',
    '87701003',
    '83763001',
    '83763002',
    '54031001',
    '54031002',
    '55496001',
    '55497001',
    '55498001',
    '55499001',
    '55500001',
    '55501001',
    '85533001',
    '56008012',
    '52319008',
    '52319009',
    '82997001',
    '82997002',
    '82997003',
    '82997004',
    '82997005',
    '82997006',
    '82997007',
    '86105001',
    '88285002',
    '96148001',
]  # Adicione aqui os códigos que você deseja pesquisar
search_column = 'Escreva abaixo os detalhes de sua solicitação:'  # Nome da coluna onde os valores serão pesquisados

# Função para buscar e retornar os valores
def find_values(search_codes, search_column):
    results = []
    for code in search_codes:
        result = sheet1[sheet1[search_column].str.contains(code, na=False)][['Respondido em', 'Respondido por', 'Email do respondente', 'Link da tarefa']].values
        if len(result) > 0:
            results.append((code, result))
    return results

# Busca os valores
results = find_values(search_codes, search_column)

# Exporta os resultados para um arquivo TXT
with open(r'C:\Users\drdc\Downloads\solicitacoes_runrun.it.txt', 'w') as f:
    f.write('Código Procurado\tRespondido em\tRespondido por\tEmail do respondente\tLink da tarefa\n')
    for code, result in results:
        for r in result:
            result_str = "\t".join(map(str, r))
            f.write(f"{code}\t{result_str}\n")

# Exibe os resultados no console
for code, result in results:
    for r in result:
        result_str = "\t".join(map(str, r))
        print(f'Código: {code} - Resultado: {result_str}')
