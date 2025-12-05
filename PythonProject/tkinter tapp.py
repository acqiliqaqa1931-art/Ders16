import tkinter as tk
from tkinter import messagebox


user_data={}

ill_list=[

"axiliya",
"axondroplaziya",
"akropektoral sindromu",
"akustik travma",
"aqalaktiya",
"albinizm",
"alisa mocuzeler olkesinde sindromu",
"alkoqol deliriyasi",
"alkoqol paranoidi",
"alkoqolizm",
"alkoqolsuzluq sindromu",
"allergik rinit",
"allergiya",
"alport sindromu",
"alternariozlar",
"altsheymer xesteliyi",
"alvarez sindromu",
"ambliopia",
"amimiya",
"amneziya",
"amniotik maye",
"ampeloterapiya",
"amputasiya",
"anadangəlme kontraktur araxnodaktiliya",
"anadangəlme yod catismasligi sindromu",
"anaerob infeksiya",
"anafilaktik sok",
"anal fissur",
"anal inkontinensiya",
"anal qasinma",
"anal stenoz",
"anal tromboz",
"andermann sindromu",
"anevrizmatik sumuk kistasi",
"angelman sindromu",
"angiofibroma",
"anizokoriya",
"ankilostomoz",
"ankilozan spondilit",
"ankraofobiya",
"anoreksiya",
"anorektal fistul",
"anti-sintetaza sindromu",
"antifosfolipid sindromu",
"antofobiya",
"anton sindromu",
"antropofobiya",
"aortal catismasliq",
"aortal stenoz",
"apert sindromu",
"apifobiya",
"appendisit",
"apraksiya",
"apsou-sulman sindromu",
"araknofobiya",
"arias sindromu",
"arktik quduzluq virusu",
"argiroz",
"armudvari əzele sindromu",
"arterial hipertenziya",
"artrit",
"aseptik meningit",
"asherson sindromu",
"asperger sindromu",
"aspergilloz",
"assitin",
"asteniya",
"astiqmatizm",
"asagi cenənin cixiqilari",
"asagi etraqlarin varikoz genelmesi",
"at qripi",
"at quyruqu sindromu",
"atopik ekzema",
"atopiya",
"autizm",
"autoimmunitet",
"avellis sindromu",
"ayaq gobeleyi",
"ayaq uzunlugunun ferqliyi",
"baccio-yosinari sindromu",
"baddi-kiari sindromu",
"bagirsak kecmezliyi",
"bakterial xestelikler",
"barakat sindromu",
"bas agrisi",
"basgicellenme",
"behcet xesteliyi",
"behr sindromu",
"bel agrisi",
"bell iflici",
"benedikt sindromu",
"beri-beri",
"beyin xercengi",
"beyin qansizmasi",
"beyker kistasi",
"bedxasseli hipertermiya",
"bipolyar pozuntu",
"birincili skleroz xolangit",
"birkamerali sumuk kistasi",
"blastula",
"blau sindromu",
"blefarospazm",
"bos pencə",
"botulizm",
"boyrek dasi",
"boyrek dasi xesteliyi",
"boyume agrisi",
"bradikardiya",
"bradzot",
"bromizm",
"bronxial astma",
"bronxit",
"bronxospazm",
"bruk sindromu",
"bruksizm",
"brunner sindromu",
"bruton xesteliyi",
"bubon taunu",
"bud sumuyunun siniqlari",
"bulimiya nervoza",
"burun arakesmesinin hematomasi",
"burun qanaxmasi",
"bullur xesteliyi",
"burgər xesteliyi",
"caynaq el",
"cirtdan boy",
"cuzam",
"capiqli alopesiya",
"carpaz sindromlar",
"cay ve tost sindromu",
"cekilme sindromu",
"ciyin sumuyunun siniqlari",
"coxlu sistem atrofiyasi",
"daban mahmizi",
"daginiq skleroz",
"dalaqin yirtilmasi",
"daltonizm",
"dang qizdirmaasi",
"daun sindromu",
"de kervain tenosinoviti",
"de kerven tireoditi",
"degenerativ xestelik",
"deinacrida heteracantha",
"dekompression xestelik",
"dekstrokardiya",
"demensiya",
"dempinq sindromu",
"depersonalizasiya",
"depressiya",
"dermatit",
"dermatomiozit",
"dermatoz",
"demgil",
"demrovabenzər pitiriaz",
"deniz xesteliyi",
"deri xercengi",
"di georq sindromu",
"diabetik koma",
"diabetik neyropatiya",
"diareya",
"diatez",
"diferiya",
"diqqet catismazligi ve hiperaktivlik pozuntusu",
"diogen sindromu",
"dishidroz",
"diskoid lupus",
"disqrafiya",
"disleksiya",
"dismenoreya",
"diz qapaginin siniqlari",
"dizenteriya",
"dogus zamani temperatur",
"donma",
"dovsan sindromu",
"dolun inkisafinin lengimesi",
"drave sindromu",
"dressler sindromu",
"dubin-conson sindromu",
"dueyn sindromu",
"duodenit",
"duyunlu eritema",
"duyunlu zob",
"duz bagirsak polipleri"
"ebola virusu xesteliyi",
"ebstein anomaliyasi",
"ekximoz",
"ekxondroma",
"eklamsiya",
"ekzema",
"elastik psevdoksantoma",
"elejalde sindromu",
"elektrik zedelenmeleri",
"elers-danlos sindromu",
"embrion",
"emfizem",
"emosional qirilma",
"empatiya yorqunlugu",
"endemik zob",
"endokrin xestelikler",
"endokrinologiya",
"endometrioz",
"epilepsiya",
"epispadiya",
"epizotik ulserativ sindrom",
"eritremiya",
"erqoterapiya",
"esitme halusinasiyalari",
"evans sindromu",
"eyzenmenger sindromu",
"eqli gerilik",
"el-ayaq sindromu",
"ellenen purpura",
"eyriboyunluq",
"fallo tetradasi",
"fantom eza",
"faringit",
"fasileli axsama",
"fassial qranulyoma",
"femister ucluyu",
"fibromialgiya",
"fibrosarkoma",
"fil xesteliyi",
"filarioz",
"flammer sindromu",
"flasbek (psixologiya)",
"fobiya",
"fokal nodulyar hiperplaziya",
"foks-fordays xesteliyi",
"foqt-koyanaqi-xarad xesteliyi",
"folkmanin isemik kontrakturasi",
"follikulyar tiroid xercengi",
"fonofobiya",
"forestye xesteliyi",
"freiberq xesteliyi",
"freqoli sindromu",
"furne qanqrensi",
"gece yemek sindromu",
"gecikmis yuxu merhelesi sindromu",
"gelotofobiya",
"germinoma",
"gesvind sindromu",
"gigantizm",
"qigant-huceyreli arteriit",
"ginekomastiya",
"goyoskurek",
"goz daxili tezyiq",
"gozde kimyevi zedelenme",
"gozyasi damcisi elameti",
"gunes yaniglqlari",
"gunter xesteliyi",
"hallux",
"hallux valgus",
"hantinqton xesteliyi",
"harlequin tipli iktiyozis",
"hasimoto uru",
"hava emboliyasi",
"havana sindromu",
"heberden duyunu",
"hellp sindromu",
"hemangioma",
"hemartroz",
"hematoma",
"hemiplegiya",
"hemofiliya",
"hemofiliya a",
"hemofiliya b",
"hemoxromotoz",
"hepatic ensefalopatiya",
"hepatit",
"hepatit a",
"hepatit b",
"hepatit c",
"hepatit d",
"hepatit e",
"hepatoblastoma",
"hepatopulmonar sindrom",
"hepatorenal sindrom",
"hepatosellular adenoma",
"hepatosellular xerceng",
"herpes",
"heterotopik ossifikasiya",
"hicqiriq",
"hidrosefaliya",
"hidrotoraks",
"hiper-igm-immunodefisit sindromu",
"hiperaljeziya",
"hiperemiya",
"hiperhidroz",
"hiperqlikemiya",
"hiperqrafiya",
"hiperlipidemiya",
"hipermobil spektrum pozgunlugu",
"hiperparatiroidizm",
"hipersayiqliq",
"hipertonik kriz",
"hipertrixoz",
"hipertropiya",
"hipokineziya",
"hipopiqmentasiya",
"hipospadiya",
"hipotireoz",
"his destesinin sag ayaqciginin blokadasi",
"his destesinin sol ayaqciginin blokadasi",
"his gobeleyi",
"holt-orama sindromu",
"homosistinuriya",
"horner sindromu",
"hurler sindromu",
"hus",
"xalyazion",
"xarici aksent sindromu",
"xend-suller-kriscen xesteliyi",
"xerceng xesteliyi",
"xx kisi sindromu",
"xolangiokarsinoma",
"xolangit",
"xoledoxolitiaz",
"xolestaz sindromu",
"xosxasseli paroksizmal basgicellenme",
"xroniki bas agrisi",
"xroniki boyrek catismasligi",
"xroniki pankreatit",
"xronofobiya",
"ixtioz",
"insan qripi",
"insan papilloma virusu",
"insomniya",
"insulinomalar",
"insult",
"intervertebral yirtiq",
"intihar",
"ipoxondriya",
"irin",
"irsi hemoxromatoz",
"ispan qripi",
"isteriya xesteliyi",
"isemik insult",
"isialgiya",
"ishtahasizliq",
"itdirseyi",
"izosporoz",
"kabuki sindromu",
"kamurati-enqelmann xesteliyi",
"kandidoz",
"kapqras sindromu",
"kaplan sindromu",
"kardiogen sok",
"kardioskleroz",
"karies",
"karni kompleksi",
"kasin-bek xesteliyi",
"katapleksiya",
"katarakta",
"kavasaki xesteliyi",
"keratit",
"keratodermiya",
"kernikterus",
"kerniq simptomu",
"kerns-seyr sindromu",
"kelle sumuklerinin siniqlari",
"kelle-beyin zedelenmesi",
"kemerleyici demrov",
"kepenek simptomu",
"kesisme sindromu",
"keskin boyrek catismasligi",
"keskin qaraciyer catismasligi",
"keskin qarin",
"keskin nefes yollari pozulmasi sindromu",
"keskin pankreatit",
"keskin respirator infeksiyalar",
"kikuchi-fucimoto xesteliyi",
"kimyevi yaniglar",
"kinbek xesteliyi",
"kinofobiya",
"klaynfelter sindromu",
"kleptomaniya",
"kleyne-levin sindromu",
"kluwer-busi sindromu",
"kohler xesteliyi",
"koksiqodiniya",
"koqnitiv catismasliq",
"kolit",
"kolorektal xerceng"
"koma",
"komplement catismasligi",
"komputer gorme sindromu",
"kontakt dermatit",
"konyunktivit",
"kor helqe sindromu",
"koronar stent",
"koronavirus xesteliyi 2019",
"kostello sindromu",
"korfez muharibesi sindromu",
"korpucuk sumuyunun siniqlari",
"kretinizm",
"kreysfeld-yakob xesteliyi",
"krim-kongo hemorragik qizdir masi",
"kriptokokkoz",
"kron xesteliyi",
"kseroftalmiya",
"kuttner sisi",
"qabi rgalarin siniqlari",
"qalcanin kondensasion osteit sindromu",
"qaleassi sinigi",
"qalxanabenz er vezin adenomas i",
"qalxanabenz er vezin anaplastik xercengi",
"qalxanabenz er vezin xercengi",
"qanadabenz er kureka",
"qanqren",
"qanqrenoz piodermiya",
"qanzer sindromu",
"qaraciyer absesi",
"qaraciyer xercengi",
"qaraciyer travmalari",
"qaraciyer venalari",
"qaraciyer yetmezliyi",
"qaraciyerin alkoqol xesteliyi",
"qarayara",
"qardner sindromu",
"qarin yatalagi",
"gastrit",
"gastro-ezofageal reflyuks xesteliyi",
"gastro sizis",
"qebizlik",
"qerbi nil qizdir masi",
"qiqiqlanmis bagirsak sindromu",
"qirmizi qurdeseneyi",
"qisa anagen sindromu",
"qisa bagirsak sindromu",
"qisda qalma sindromu",
"qizdirma",
"qizil yel xesteliyi",
"qizilca",
"qiqs",
"qida catismazligi",
"qida intoleransi",
"qlomerulonefrit",
"qlukaqonoma",
"qose xesteliyi",
"qotur",
"qreyv xesteliyi",
"qrip",
"qrizel xesteliyi",
"qudpascer xesteliyi",
"quduzluq",
"qulaqciqlar arasi ceperin qusuru",
"qulaqdibi xesteliyi",
"quru goz sindromu",
"langer-giedion sindromu",
"laron sindromu",
"larsen sindromu",
"lata",
"layella sindromu",
"laym xesteliyi",
"legius sindromu",
"leqq-kalve-pertes xesteliyi",
"les-nihan sindromu",
"letterer-sive xesteliyi",
"leykoz",
"lirt deri sindromu",
"lima sindromu",
"limfoma",
"lipoma",
"liposarkoma",
"lizosomal toplanma xestelikleri",
"lofgren sindromu",
"lunatizm",
"lyambliyoz",
"mafucci sindromu",
"magic sindromu",
"magistral damarlarin tranzpozisiyasi",
"mak-ardl xesteliyi",
"makkyun-olbrayt sindromu",
"malyariya",
"manubriosternal sindrom",
"marfan sindromu",
"markus qunn sindromu",
"marsal sindromu",
"martin-bell sindromu",
"mavi korpe sindromu",
"medulyar tiroid xerceng",
"mekkel divertikulu",
"meqasistis (dolde)",
"melanoma",
"men statindaki dik atilan fransiz sindromu",
"meningit",
"menkes xesteliyi",
"mental ceza",
"menyer xesteliyi",
"metabolik xestelikler",
"metastatik qaraciyer sisleri",
"meymunciceyi",
"meymunciceyi virusu",
"mede xercengi",
"mede xorasi",
"medealti vezi travmalari",
"medealti vezin xercengi",
"medecikler arasi ceperin qusuru",
"mexmerek",
"merk ezi agri sindromu",
"merk ezi hipoventil yasiya sindromu",
"merk ezi sekersiz diabet",
"meshurlara perestis sindromu",
"miasteniya",
"mikozlar",
"mikulic xesteliyi",
"migren",
"miller-diker sindromu",
"minamata xesteliyi",
"miopatiya",
"miopiya (yaxindangorme)",
"miotoniya",
"mioz",
"mitoxondrial xestelikler",
"mitral qapaq catismasligi",
"miyazlar",
"mobius sindromu",
"mondor xesteliyi",
"moniezioz",
"monilioz",
"mongol lekesi",
"morgellons",
"morton nevromasi",
"mukopolisaxaridozlar",
"multiorqan disfunksiya sindromu",
"mur-federman sindromu",
"musiqili qulaq sindromu",
"musofobiya",
"mutizm",
"narahat ayaqlar sindromu",
"narkolepsiya",
"narsistik sexsiyyet pozuntusu",
"nazik bagirsagin qaz sistleri",
"nazik bagirsak xercengi",
"nazik bagirsak kecmezliyi sindromu",
"nefrit (xestelik)",
"nefrogenik sekersiz diabet",
"nefroptoz",
"nevroz",
"neyrodegenerativ xestelik",
"neyrodermit",
"neyroendokrin sis",
"neyromiyelit optika",
"nefes darligi",
"nimann-pik xesteliyi",
"nimfomaniya",
"noma (xestelik)",
"norovirus",
"o'donoxun qorxulu ucluyu",
"obsessiv-kompulsiv pozuntu",
"ocaqli dazliq",
"oddi sfinktoru disfunksiyasi",
"ombrofobiya",
"onxoserkoz",
"onixofaqiya",
"onixokriptoz",
"onixomikoz",
"onurga sutununun siniqlari",
"optik nevrit",
"oraq huceyreli anemiya",
"oral allergiya sindromu",
"ormand xesteliyi",
"ornitofobiya",
"ortaqulaq iltihablanmasi",
"osqud-slatter xesteliyi",
"osteoartroz",
"osteodistrofiya",
"osteoxondritler",
"osteoid osteoma",
"osteoma",
"osteomalyasiya",
"osteomielit",
"osteoparoz",
"osteopetroz",
"osteoskleroz",
"otahara sindromu",
"otalgiya",
"otit",
"od dasi xesteliyi",
"od kisesi diskineziyasi",
"od kisesi polipleri",
"od kisesin bed xasseli sisi",
"od kisesinin iltihabi"
"ovre xesteliyi",
"oyrenilmis caresizlik sindromu",
"padalka simptomu",
"paxidermoperiostoz",
"pakman displaziyasi",
"palindrom revmatizm",
"pambiqvari osteoporoz",
"pandas sindromu",
"panik atak",
"pankost sisi",
"pankreatit",
"panner xesteliyi",
"pannikulit",
"papilyar tiroid xercengi",
"pappataci qizdir masi",
"papula",
"paranoid sexsiyyet pozuntusu",
"paranoya",
"paraproktit",
"paratuberkuloz",
"parazitar xestelikler",
"paresteziya",
"parez",
"parkinson xesteliyi",
"paroksizmal hemikraniya",
"partlayan bas sindromu",
"pasterellyoz",
"patau sindromu",
"pedofiliya",
"pellagra",
"pelleg rini-stid xesteliyi",
"pemfiqus",
"periferik arteriyalarin daralmasi",
"perikardit",
"periodontit",
"peritonit",
"piblokto",
"pielonefrit",
"pika xesteliyi",
"pika sindromu",
"pillekanvari ezele sindromu",
"pilonidal xestelik",
"pirson sindromu",
"pis dunya sindromu",
"pisik cigirtisi sindromu",
"pisik goz sindromu",
"pnev motoraks",
"podaqra",
"poliartrit",
"polineyropatiya",
"poliomielit",
"pompe xesteliyi",
"portal hipertenziya",
"portal vena trombozu",
"pospiviroidae",
"postxolesistektomik sindrom",
"pott xesteliyi",
"prader-villi sindromu",
"priapizm",
"primrouz sindromu",
"prionlar",
"progeriya",
"prostat xercengi",
"psevdomembranoz kolit",
"psixoloji pozuntu",
"psixopatiya",
"psoriatik artrit",
"psoriaz",
"ptoz",
"pullu demrov",
"rabdomioliz",
"radiasiya xesteliyi",
"raxit",
"rank",
"rank-l",
"rapunzel sindromu",
"reaktiv artrit",
"refleks simpatik distrofiy a",
"rektal qanaxma",
"rektal prolaps",
"rektosele",
"rektovaginal fistul",
"residivlesen polixondrit",
"retinopatiya",
"retroqrad eyakulyasiya",
"rett sindromu",
"revmatik qizdirma",
"revmatik polimialgiya",
"revmatoid artrit",
"reya sindromu",
"reyno fenomeni",
"rift vadisi qizdir masi",
"rinit",
"risser elameti",
"robinov sindromu",
"rozasea xesteliyi",
"rubinsteyn-teybi sindromu",
"sabl zerbesi simptomu",
"sacroiliitis",
"sag qalanin gunahkarliq hissi sindromu",
"sakralizasiya",
"salmonellyoz",
"sapho sindromu",
"sari dirnaq sindromu",
"sari qizdirma",
"sariliq",
"sarkoidoz",
"sarkoma",
"sarkoma yung",
"sarkopeniya",
"sarkopsilloz",
"seksual fetisizm",
"sekvestr",
"selektiv iga defisiti",
"selen catismasligi",
"sellulit",
"selulit",
"sensenbrenner sindromu",
"sepsis",
"septik artrit",
"septik sok",
"septo-optik displaziya",
"sesamoidit",
"sever xesteliyi",
"seher buxovlanmasi",
"senger ayagi",
"serhed sexsiyyet pozuntusu",
"sfi nqolipidoz",
"siniq qelb sindromu",
"sizanaq xesteliyi",
"sidik qacirma",
"sifilis",
"silloqomaniya",
"simulyasiya",
"sinding-larsen-yoxanson sinigi",
"sinqa",
"sinus taxikardiyasi",
"sippl sindromu",
"sirroz",
"sistik fibroz",
"sistit",
"sistosele",
"skarlatin",
"sklerodermiya",
"skolioz",
"skrofula",
"smit-magenis sindromu",
"solipsizm sindromu",
"somatizasiya pozuntusu",
"sonsuzluq (biologiya)",
"sosial loferlik",
"sosial media asililigi",
"sosiskayabenz er barmaq",
"spondiloz",
"spontan abort",
"sporotrikoz",
"stenokardiya",
"stikler sindromu",
"still xesteliyi",
"stimmler sindromu",
"streff sindromu",
"streptokokk faringit",
"subyektiv ikili sindromu",
"suciceyi",
"superior vena kava sindromu",
"susak sindromu",
"sumuk sisi",
"suz enek",
"svayer-ceyms sindromu",
"svit sindromu",
"seqren sindromu",
"seyerman xesteliyi",
"sebekeli livedo",
"sexsiyyet pozuntulari",
"sekerli diabet",
"sekersiz diabet",
"siqqildayan barmaq",
"sinsilint",
"sis",
"sizofreniya",
"smidt sindromu",
"sok",
"sprengel deformasiyasi",
"steynner t xesteliyi",
"taxipnoe",
"takayasu xesteliyi",
"talassemiya",
"tanatofobiya",
"tanqanika gul us epidemiyasi",
"tarsal tunel sindromu",
"tarui xesteliyi",
"taun",
"taura sindromu",
"testofobiya",
"tetanus",
"tetra-amelia sindromu",
"tebii cicek",
"telebe sindromu",
"tesdiqlenme asililigi",
"tesvis heyecan pozuntusu"
"tetilde urek sindromu",
"tibb telebeleri sindromu",
"tinnitus",
"tireotoksik bohran",
"tit se sindromu",
"toxmaq barmagi",
"toksik sok sindromu",
"toksik yag sindromu",
"toksoplazmoz",
"tomofobiya",
"tonzillit",
"traxoma",
"transient takipniya",
"transkripsiya (genetika)",
"traps sindrom",
"travmatik sok",
"tric er kollins sindromu",
"trixotillomaniya",
"tripanofobiya",
"tromboflebit",
"trombositopeniya",
"trombotik trombositopenik purpura",
"tromboz",
"tropik xestelikler",
"tulyaremiya",
"turet sindromu",
"tukenmislik sindromu",

"uippl xesteliyi",
"uiver sindromu",
"ulisses sindromu",
"ulnar deviasiya",
"uolkott-rallison sindromu",
"usaqliqin atoniyasi",
"usaqliq boynu xercengi",

"uner tan sindromu",
"urek astmasi",
"urek catismamazligi",
"uveit",
"uzukvari pankreas",

"varikoz genelme",
"veber-kriscen xesteliyi",
"vena kava kompression sindrom",
"venereofobiya",
"venustrafobiya",
"vermifobiya",
"verner sindromu",
"vernike xesteliyi",
"veba",
"verem",
"videmana-rautensstrauha sindromu",
"villebrand xesteliyi",
"vilson xesteliyi",
"vilson-torner sindromu",
"vilyams sindromu",
"vincester sindromu",
"viskott-oldric sindromu",
"visler-fankoni sindromu",
"vitiliqo xesteliyi",
"vizual azadliq hallusinasiya lari",
"volf xirshxor sindromu",
"volvulus",
"vudhauz-sakati sindromu",

"yad el sindromu",
"yanan agiz sindromu",
"yanan ayaq sindromu",
"yan iq",
"yapisqan trombosit sindromu",
"yarimkeskin limfositar tireodit",
"yasti pence",
"yayilmis damardaxili laxtalanma",
"yoluxucu xestelik",
"yu-cenq xesteliyi",
"yuxu iflici",
"yumurta dusmesi sindromu",
"yunis-varon sindromu",
"ziyil",
"zollinger-ellison sindromu",
"zoonozlar",
"zokem"
]

def register_page():
    reg=tk.Toplevel(root)
    reg.title("Qeydiyyat")
    reg.geometry("300x350")

    tk.Label(reg,text="Xestenin adi").pack(pady=5)
    ent_user=tk.Entry(reg)
    ent_user.pack()

    tk.Label(reg,text="Xesteliyi").pack(pady=5)
    ent_illness=tk.Entry(reg)
    ent_illness.pack()

    tk.Label(reg,text="Xestenin Soyadi").pack(pady=5)
    ent_nickname=tk.Entry(reg)
    ent_nickname.pack()

    tk.Label(reg,text="Xestenin Yasi").pack(pady=5)
    ent_age=tk.Entry(reg)
    ent_age.pack()

    tk.Label(reg,text="Xestenin Cinsi").pack(pady=5)
    ent_gender=tk.Entry(reg)
    ent_gender.pack()
    def register():
        username=ent_user.get()
        illness=ent_illness.get()
        ad=ent_nickname.get()
        yas=ent_age.get()
        cins=ent_gender.get()

        if not username or not illness:
            messagebox.showerror("Xeta","Login ve ya xestenin xesteliyi bos ola bilmez")
            return

        if username in user_data:
            messagebox.showerror("Xeta","Bu username istifade olunur")
            return

        if cins!="kisi" and cins!="qadin":
            messagebox.showerror("Xeta","Cinsiyyet kisi yada qadin olmalidir!")
            return

        if not yas.isdigit():
            messagebox.showerror("Xeta","Yas sadece reqem olmalidir!")
            return

        if not illness in ill_list:
            messagebox.showerror("Xeta","Bele bir xestelik yoxdur!")
            return













        user_data[username]={
            "xestelik:":illness,
            "ad":username,
            "yas":yas,
            "cins":cins
        }

        messagebox.showinfo("Ugurlu","Qeydiyyatdan kecdiniz!")
        reg.destroy()

    tk.Button(reg,text="Qeyd ol",bg="green",fg="white",command=register).pack(pady=5)

def change_illness_window(username):
    win=tk.Toplevel(root)
    win.title("Xesteliyi deyis")
    win.geometry("300x230")

    tk.Label(win,text="Kohne xestelik").pack(pady=5)
    old_illness=tk.Entry(win)
    old_illness.pack()

    tk.Label(win,text="Yeni xestelik").pack(pady=5)
    new_illness=tk.Entry(win)
    new_illness.pack()

    tk.Label(win,text="Xesteliyi tesdiqle").pack(pady=5)
    new_illness1=tk.Entry(win)
    new_illness1.pack()

    def change_illness():
        if old_illness.get()!=user_data[username]["password"]:
            messagebox.showerror("Xeta","Kohne sifre yanlisdir!")
            return
        if new_illness.get()!=new_illness1.get():
            messagebox.showerror("Xeta","Sifreler uygun gelmir!")
            return

        user_data[username]["xestelik"]=new_illness.get()
        messagebox.showinfo("Ugurlu","Xesteliyinizi deyisdirdiniz!")
        win.destroy()

    tk.Button(win,text="Tesdiqle",bg="pink",fg="white",command=change_illness).pack(pady=5)

def open_profile(username):
    prof=tk.Toplevel(root)
    prof.title("Profil")
    prof.geometry("300x380")

    user=user_data[username]

    tk.Label(prof,text=f"Profil {username}",font=("Arial",14,"bold")).pack(pady=10)

    tk.Label(prof,text="Ad").pack()
    ent_user=tk.Entry(prof)
    ent_user.insert(0,user["ad"])
    ent_user.pack()

    tk.Label(prof,text="Yas").pack()
    ent_age=tk.Entry(prof)
    ent_age.insert(0,user["yas"])
    ent_age.pack()

    tk.Label(prof,text="Cins").pack()
    ent_gender=tk.Entry(prof)
    ent_gender.insert(0,user["cins"])
    ent_gender.pack()

    def update_info():
        user["ad"]=ent_user.get()
        user["yas"]=ent_age.get()
        user["cins"]=ent_gender.get()
        messagebox.showinfo("Ugurlu","Melumat yenilendi!")
        prof.destroy()

    def delete_account():
        if messagebox.askyesno("Tesdiq","Xestenin melumatlarini simek isteyirsiniz?"):
            del user_data[username]
            messagebox.showinfo("Ugurlu","Xestenin melumatlari silindi")
            prof.destroy()


    tk.Button(prof,text="Yenile",bg="blue",fg="white",command=update_info).pack(pady=10)

    tk.Button(prof,text="Sil",bg="red",fg="white",command=delete_account).pack(pady=10)

    tk.Button(prof,text="Sifreni deyis",bg="green",fg="white",command=lambda:change_illness_window(username)).pack(pady=10)


def open_admin_panel():
    admin_win=tk.Toplevel(root)
    admin_win.title("Admin Panel")
    admin_win.geometry("700x700")
    tk.Label(admin_win,text="Admin Paneli").pack(pady=10)

    listbox=tk.Listbox(admin_win,width=30)
    listbox.pack(pady=10)

    for username in user_data:
        listbox.insert(tk.END,username)

    tk.Label(admin_win, text="Ad").pack(pady=5)
    ent_name = tk.Entry(admin_win)
    ent_name.pack()

    tk.Label(admin_win, text="Yas").pack(pady=5)
    ent_age = tk.Entry(admin_win)
    ent_age.pack()

    tk.Label(admin_win, text="Cins").pack(pady=5)
    ent_gender = tk.Entry(admin_win)
    ent_gender.pack()

    tk.Label(admin_win, text="Yeni sifre").pack(pady=5)
    ent_new_illness = tk.Entry(admin_win,show="*")
    ent_new_illness.pack()

    def select_user(event):
        selected=listbox.curselection()
        if selected:
            username=listbox.get(selected[0])
            user=user_data[username]
            ent_name.delete(0,tk.END)
            ent_name.insert(0,user["name"])

            ent_age.delete(0,tk.END)
            ent_age.insert(0,user["age"])

            ent_gender.delete(0,tk.END)
            ent_gender.insert(0,user["gender"])
    listbox.bind("<<ListboxSelect>>",select_user)

    def update_user():
        selected = listbox.curselection()
        if selected:
            username = listbox.get(selected[0])

            user = user_data[username]
            user["ad"]=ent_name.get()
            user["yas"] = ent_age.get()
            user["cins"] = ent_gender.get()
            messagebox.showinfo("OK",f"{username} Melumat yenilendi!")

    def change_user_pass():
        selected = listbox.curselection()
        if selected:
            username = listbox.get(selected[0])
            new_pass=ent_new_illness.get()

            if len(new_pass)<3:
                messagebox.showerror("Xeta","Sifre 3den az ola bilmez!")
                return

            user_data[username]["password"]=new_pass
            messagebox.showinfo("OK", "Sifre yenilendi!")

    def delete():
        selected=listbox.curselection()
        if selected:
            username=listbox.get(selected[0])
            if messagebox.askyesno("Tesdiq", "Hesabi silmek istiyirsiniz?"):
                del user_data[username]
                listbox.delete(selected[0])

                ent_name.delete(0,tk.END)
                ent_age.delete(0,tk.END)
                ent_gender.delete(0,tk.END)
                messagebox.showinfo("OK",f"{username} silindi!")

    tk.Button(admin_win, text="Yenile", bg="grey", fg="pink", command=update_user).pack(pady=5)

    tk.Button(admin_win, text="Hesabi sil", bg="blue", fg="white", command=delete).pack(pady=5)

    tk.Button(admin_win, text="Sifre deyis", bg="green", fg="white", command=change_user_pass).pack(pady=5)










def login():
    username=ent_user.get()
    illness=ent_illness.get()

    if username=="admin" and illness=="admin":
        open_admin_panel()

    if username in user_data and user_data[username]["xestelik:"]==illness:
        open_profile(username)
    else:
        messagebox.showerror("Xeta","Xestenin adi ve ya xesteliyi yanlisdir!")

root=tk.Tk()
root.title("Xestexana login")
root.geometry("500x500")

tk.Label(root,text="Xestenin adi").pack(pady=5)
ent_user=tk.Entry(root)
ent_user.pack()

tk.Label(root,text="Xestenin xesteliyi").pack(pady=5)
ent_illness=tk.Entry(root)
ent_illness.pack()

btn=tk.Button(root,text="Daxil ol",bg="green",fg="white",command=login)
btn.pack(pady=10)

btn1=tk.Button(root,text="Qeydiyyat",bg="#2196F3",fg="white",command=register_page)
btn1.pack(pady=10)


root.mainloop()