#!/home/sandip/anaconda3/bin/python3.6

#load the system module
import sys


# reading  watermelon.fsa
my_file1 = open("watermelon.fsa")
my_dna = my_file1.read().rstrip("\n")
dna_length = len(my_dna)


#reading exon
exon1 = my_dna[0:726]
exon2 = my_dna[1693:2551]
exon3 = my_dna[29746:30628]
exon4 = my_dna[32108:32225]
exon5 = my_dna[32635:32914]
exon6 = my_dna[32932:33006]
exon7 = my_dna[34731:36349]
exon8 = my_dna[36320:36731]
exon9 = my_dna[42043:42817]
exon10 = my_dna[43946:44231]
exon11 = my_dna[44456:44528]
exon12 = my_dna[45546:45618]
exon13 = my_dna[50760:50833]
exon14 = my_dna[52679:53747]
exon15 = my_dna[54399:55017]
exon16 = my_dna[67124:67604]
exon17 = my_dna[68217:69015]
exon18 = my_dna[68942:69350]
exon19 = my_dna[70072:70261]
exon20 = my_dna[71738:72310]
exon21 = my_dna[74592:74753]
exon22 = my_dna[75276:75359]
exon23 = my_dna[76360:76432]
exon24 = my_dna[78203:78274]
exon25 = my_dna[86723:87080]
exon26 = my_dna[87128:87500]
exon27 = my_dna[88707:89407]
exon28 = my_dna[91441:91524]
exon29 = my_dna[96686:97073]
exon30 = my_dna[112517:114047]
exon31 = my_dna[121266:121339]
exon32 = my_dna[130200:130272]
exon33 = my_dna[131225:131299]
exon34 = my_dna[148377:151548]
exon35 = my_dna[151917:151991]
exon36 = my_dna[155600:155681]
exon37 = my_dna[174365:174826]
exon38 = my_dna[176229:176744]
exon39 = my_dna[179828:180251]
exon40 = my_dna[182961:183050]
exon41 = my_dna[185934:186193]
exon42 = my_dna[187055:189062]
exon43 = my_dna[189674:189733]
exon44 = my_dna[204423:206157]
exon45 = my_dna[222045:222579]
exon46 = my_dna[227589:227662]
exon47 = my_dna[230172:230793]
exon48 = my_dna[238844:238916]
exon49 = my_dna[239934:240006]
exon50 = my_dna[240231:240516]
exon51 = my_dna[241645:242218]
exon52 = my_dna[242699:242924]
exon53 = my_dna[243220:243450]
exon54 = my_dna[244298:245514]
exon55 = my_dna[265952:266502]
exon56 = my_dna[267463:268230]
exon57 = my_dna[272806:272828]
exon58 = my_dna[274339:274897]
exon59 = my_dna[275819:276992]
exon60 = my_dna[279454:279901]
exon61 = my_dna[286844:286919]
exon62 = my_dna[287215:287289]
exon63 = my_dna[287652:287740]
exon64 = my_dna[306499:306618]
exon65 = my_dna[307209:309067]
exon66 = my_dna[311223:312072]
exon67 = my_dna[330833:331184]
exon68 = my_dna[332074:332155]
exon69 = my_dna[333597:333787]
exon70 = my_dna[335931:336084]
exon71 = my_dna[337300:337692]
exon72 = my_dna[344865:345260]
exon73 = my_dna[346364:346502]
exon74 = my_dna[348454:348716]
exon75 = my_dna[350530:350774]
exon76 = my_dna[351835:352302]
exon77 = my_dna[353940:354009]
exon78 = my_dna[354915:355058]
exon79 = my_dna[358590:358677]
exon80 = my_dna[362963:363662]
exon81 = my_dna[365317:365914]
exon82 = my_dna[366129:366432]
exon83 = my_dna[376484:376763]
exon84 = my_dna[377833:378083]
exon85 = my_dna[378928:379011]
exon = (exon1 + exon2 + exon3 + exon4 + exon5 + exon6 + exon7 + exon8 + exon9 + exon10 + exon11 + exon12 +exon13 + exon14 + exon15 + exon16 + exon17 + exon18 + exon19 + exon20 + exon21 + exon22 + exon23 + exon24 + exon25 + exon26 + exon27 + exon28 + exon29 + exon30 + exon31 + exon32 +exon33 + exon34 + exon35 + exon36 + exon37 + exon38 + exon39 + exon40 + exon41 + exon42 + exon43 + exon44 + exon45 + exon46 + exon47 + exon48 + exon49 + exon50 + exon51 + exon52 +exon53 + exon54 + exon55 + exon56 + exon57 + exon58 + exon59 + exon60 + exon61 + exon62 + exon63 + exon64 + exon65 + exon66 + exon67 + exon68 + exon69 + exon70 + exon71 + exon72 +exon73 + exon74 + exon75 + exon76 + exon77 + exon78 + exon79 + exon80 + exon81 + exon82 + exon83 + exon84 + exon85)
exon_length = len(exon)
g_count1 = exon.upper().count('G')
c_count1 = exon.upper().count('C')
gc_content1 = (g_count1 + c_count1)
gc_content_ratio1 = (gc_content1/exon_length)*100
exon_ratio =(exon_length/dna_length)*100
print("exon" + '           '+ str(exon_length)+ ' ', "%.2f" % exon_ratio, "%.2f" % gc_content_ratio1)



# reading intron
intron1 = my_dna[726:1693]
intron2 = my_dna[30628:32108]
intron3 = my_dna[33006:34731]
intron4 = my_dna[70261:71738]
intron5 = my_dna[72310:74592]
intron6 = my_dna[89407:91441]
intron7 = my_dna[174826:176229]
intron8 = my_dna[176744:179828]
intron9 = my_dna[180251:182961]
intron10= my_dna[186193:189674]
intron11= my_dna[243450:244298]
intron12= my_dna[266502:267463]
intron13= my_dna[332155:333595]
intron14= my_dna[336084:337300]
intron15= my_dna[345260:346364]
intron16= my_dna[348716:350530]
intron17= my_dna[350774:351835]
intron18= my_dna[352302:353940]
intron19= my_dna[354009:354915]
intron20= my_dna[378083:378928]

Intron = (intron1 + intron2 +intron3 +intron4 +intron5 +intron6 +intron7 + intron8 + intron9 + intron10 +intron11 +intron12 + intron13 + intron14 + intron15 + intron16 + intron17 + intron18 + intron19 + intron20)
Intron_length = len(Intron)
g_count2 = Intron.upper().count('G')
c_count2 = Intron.upper().count('C')
gc_content2 = (g_count2 + c_count2)
gc_content_ratio2 = (gc_content2/Intron_length)*100
Intron_ratio =(Intron_length/dna_length)*100
print("Intron" + '         '+ str(Intron_length)+ '  ',"%.2f" % Intron_ratio,"%.2f" % gc_content_ratio2)


# Reading mis_feature
misc_feature1 = my_dna[4257:7876]
misc_feature2 = my_dna[5345:5418]
misc_feature3 = my_dna[11969:12424]
misc_feature4 = my_dna[21731:21962]
misc_feature5 = my_dna[21962:22398]
misc_feature6 = my_dna[56332:56435]
misc_feature7 = my_dna[95665:95778]
misc_feature8 = my_dna[109438:109546]
misc_feature9 = my_dna[110135:110264]
misc_feature10 = my_dna[110905:111090]
misc_feature11 = my_dna[132693:132946]
misc_feature12 = my_dna[139516:139550]
misc_feature13 = my_dna[139715:143326]
misc_feature14 = my_dna[140378:140451]
misc_feature15 = my_dna[152691:154871]
misc_feature16 = my_dna[153987:154060]
misc_feature17 = my_dna[170165:171491]
misc_feature18 = my_dna[170501:170575]
misc_feature19 = my_dna[183915:185776]
misc_feature20 = my_dna[220861:221131]
misc_feature21 = my_dna[223353:223536]
misc_feature22 = my_dna[223761:224140]
misc_feature23 = my_dna[224183:224763]
misc_feature24 = my_dna[224256:224330]
misc_feature25 = my_dna[224475:224550]
misc_feature26 = my_dna[247268:248777]
misc_feature27 = my_dna[274064:274235]
misc_feature28 = my_dna[311009:311217]
misc_feature29 = my_dna[321309:322800]
misc_feature30 = my_dna[322700:322774]
misc_feature31 = my_dna[322810:326632]
misc_feature32 = my_dna[330721:330778]
misc_feature33 = my_dna[335197:335317]
misc_feature34 = my_dna[338629:338776]
misc_feature35 = my_dna[343911:343965]
misc_feature36 = my_dna[362837:362923]
misc_feature37 = my_dna[366674:366719]

misc_feature = (misc_feature1 + misc_feature2 + misc_feature3 + misc_feature4 + misc_feature5 + misc_feature6 + misc_feature7 + misc_feature8 + misc_feature9 +  misc_feature10 + misc_feature11 + misc_feature12 + misc_feature13 + misc_feature14 + misc_feature15 + misc_feature16 + misc_feature17 + misc_feature18 + misc_feature19 + misc_feature20 + misc_feature21 + misc_feature22 + misc_feature23 + misc_feature24 + misc_feature25 + misc_feature26 + misc_feature27 + misc_feature28 + misc_feature29 + misc_feature30 + misc_feature31 + misc_feature32 + misc_feature33 + misc_feature34 + misc_feature35 + misc_feature36 + misc_feature37)
misc_feature_length = len(misc_feature)
g_count3 = misc_feature.upper().count('G')
c_count3 = misc_feature.upper().count('C')
gc_content3 = (g_count3 + c_count3)
gc_content_ratio3 = (gc_content3/misc_feature_length)*100
misc_feature_ratio =(misc_feature_length/dna_length)*100
print("misc_feature" + '   '+ str(misc_feature_length)+ '  ',"%.2f" % misc_feature_ratio,"%.2f" % gc_content_ratio3)


# Reading rRNA
rRNA1 = my_dna[148377:151548]
rRNA2 = my_dna[306499:306618]
rRNA3 = my_dna[307209:309067]
rRNA = (rRNA1 + rRNA2 + rRNA3)
rRNA_length = len(rRNA)
g_count4 = rRNA.upper().count('G')
c_count4 = rRNA.upper().count('C')
gc_content4 = (g_count4 + c_count4)
gc_content_ratio4 = (gc_content4/rRNA_length)*100
rRNA_ratio =(rRNA_length/dna_length)*100
print("rRNA" + '           '+ str(rRNA_length)+ '   ',"%.2f" % rRNA_ratio,"%.2f" % gc_content_ratio4)


# Reading repeat_reagion
rr1 = my_dna[42841:50127]
rr2 = my_dna[234335:241621]
repeat_region = (rr1 + rr2)
repeat_region_length = len(repeat_region)
g_count5 = Intron.upper().count('G')
c_count5 = Intron.upper().count('C')
gc_content5 = (g_count5 + c_count5)
gc_content_ratio5 = (gc_content2/Intron_length)*100
repeat_region_ratio =(repeat_region_length/dna_length)*100
print("repeat_region" + '  '+ str(repeat_region_length)+ '  ',"%.2f" % repeat_region_ratio,"%.2f" % gc_content_ratio5)


# Reading tRNA
tRNA1 = my_dna[44456:44528]
tRNA2 = my_dna[45546:45618]
tRNA3 = my_dna[50760:50833]
tRNA4 = my_dna[75276:75359]
tRNA5 = my_dna[76360:76432]
tRNA6 = my_dna[78203:78274]
tRNA7 = my_dna[121266:121339]
tRNA8 = my_dna[130200:130272]
tRNA9 = my_dna[131225:131299]
tRNA10 = my_dna[151917:151991]
tRNA11 = my_dna[155600:155681]
tRNA12 = my_dna[227589:227662]
tRNA13 = my_dna[238844:238916]
tRNA14 = my_dna[239934:240006]
tRNA15 = my_dna[286844:286919]
tRNA16 = my_dna[287215:287289]
tRNA17 = my_dna[287652:287740]
tRNA18 = my_dna[358590:358677]
tRNA = (tRNA1 + tRNA2 + tRNA3 + tRNA4 + tRNA5 + tRNA6 + tRNA7 + tRNA8 + tRNA9 + tRNA10 + tRNA11 + tRNA12 + tRNA13 + tRNA14 + tRNA15 + tRNA16 + tRNA17 + tRNA18)
tRNA_length = len(tRNA)
g_count6 = tRNA.upper().count('G')
c_count6 = tRNA.upper().count('C')
gc_content6 = (g_count6 + c_count6)
gc_content_ratio6 = (gc_content6/tRNA_length)*100
tRNA_ratio =(tRNA_length/dna_length)*100
print("tRNA" + '           '+ str(tRNA_length)+ '   ',"%.2f" % tRNA_ratio,"%.2f" % gc_content_ratio6)

# reading watermelon.gff
my_file2 = open("watermelon.gff")
file_contents = my_file2.read()




