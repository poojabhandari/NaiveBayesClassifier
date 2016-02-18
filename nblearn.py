import os
import re
import math
import sys
import json


stopWordList={'a' : '1' ,'about' : '1' ,'above' : '1' ,'across' : '1' ,'after' : '1' ,'again' : '1' ,'against' : '1' ,'all' : '1' ,'almost' : '1' ,'alone' : '1' ,'along' : '1' ,'already' : '1' ,'also' : '1' ,'although' : '1' ,'always' : '1' ,'among' : '1' ,'an' : '1' ,'and' : '1' ,'another' : '1' ,'any' : '1' ,'anybody' : '1' ,'anyone' : '1' ,'anything' : '1' ,'anywhere' : '1' ,'are' : '1' ,'area' : '1' ,'areas' : '1' ,'around' : '1' ,'as' : '1' ,'ask' : '1' ,'asked' : '1' ,'asking' : '1' ,'asks' : '1' ,'at' : '1' ,'away' : '1' ,'b' : '1' ,'back' : '1' ,'backed' : '1'  ,'backing' : '1' ,'backs' : '1' ,'be' : '1' ,'became' : '1' ,'because' : '1' ,'become' : '1' ,'becomes' : '1' ,'been' : '1' ,'before' : '1' ,'began' : '1' ,'behind' : '1' ,'being' : '1' ,'beings' : '1' ,'best' : '1' ,'better' : '1' ,'between' : '1' ,'big' : '1' ,'both' : '1' ,'but' : '1' ,'by' : '1' ,'c' : '1' ,'came' : '1' ,'can' : '1' ,'cannot' : '1' ,'case' : '1' ,'cases' : '1' ,'certain' : '1' ,'certainly' : '1' ,'clear' : '1' ,'clearly' : '1' ,'come' : '1' ,'could' : '1' ,'d' : '1' ,'did' : '1' ,'differ' : '1' ,'different' : '1' ,'differently' : '1' ,'do' : '1' ,'does' : '1' ,'done' : '1' ,'down' : '1' ,'down' : '1' ,'downed' : '1' ,'downing' : '1' ,'downs' : '1' ,'during' : '1' ,'e' : '1' ,'each' : '1' ,'early' : '1' ,'either' : '1' ,'end' : '1' ,'ended' : '1' ,'ending' : '1' ,'ends' : '1' ,'enough' : '1' ,'even' : '1' ,'evenly' : '1' ,'ever' : '1' ,'every' : '1' ,'everybody' : '1' ,'everyone' : '1' ,'everything' : '1' ,'everywhere' : '1' ,'f' : '1' ,'face' : '1' ,'faces' : '1' ,'fact' : '1' ,'facts' : '1' ,'far' : '1' ,'felt' : '1' ,'few' : '1' ,'find' : '1' ,'finds' : '1' ,'first' : '1' ,'for' : '1' ,'four' : '1' ,'from' : '1' ,'full' : '1' ,'fully' : '1' ,'further' : '1' ,'furthered' : '1' ,'furthering' : '1' ,'furthers' : '1' ,'g' : '1' ,'gave' : '1' ,'general' : '1' ,'generally' : '1' ,'get' : '1' ,'gets' : '1' ,'give' : '1' ,'given' : '1' ,'gives' : '1' ,'go' : '1' ,'going' : '1' ,'good' : '1' ,'goods' : '1' ,'got' : '1' ,'great' : '1' ,'greater' : '1' ,'greatest' : '1' ,'group' : '1' ,'grouped' : '1' ,'grouping' : '1' ,'groups' : '1' ,'h' : '1' ,'had' : '1' ,'has' : '1' ,'have' : '1' ,'having' : '1' ,'he' : '1' ,'her' : '1' ,'here' : '1' ,'herself' : '1' ,'high' : '1' ,'high' : '1' ,'high' : '1' ,'higher' : '1' ,'highest' : '1' ,'him' : '1' ,'himself' : '1' ,'his' : '1' ,'how' : '1' ,'however' : '1' ,'i' : '1' ,'if' : '1' ,'important' : '1' ,'in' : '1' ,'interest' : '1' ,'interested' : '1' ,'interesting' : '1' ,'interests' : '1' ,'into' : '1' ,'is' : '1' ,'it' : '1' ,'its' : '1' ,'itself' : '1' ,'j' : '1' ,'just' : '1' ,'k' : '1' ,'keep' : '1' ,'keeps' : '1' ,'kind' : '1' ,'knew' : '1' ,'know' : '1' ,'known' : '1' ,'knows' : '1' ,'l' : '1' ,'large' : '1' ,'largely' : '1' ,'last' : '1' ,'later' : '1' ,'latest' : '1' ,'least' : '1' ,'less' : '1' ,'let' : '1' ,'lets' : '1' ,'like' : '1' ,'likely' : '1' ,'long' : '1' ,'longer' : '1' ,'longest' : '1' ,'m' : '1' ,'made' : '1' ,'make' : '1' ,'making' : '1' ,'man' : '1' ,'many' : '1' ,'may' : '1' ,'me' : '1' ,'member' : '1' ,'members' : '1' ,'men' : '1' ,'might' : '1' ,'more' : '1' ,'most' : '1' ,'mostly' : '1' ,'mr' : '1' ,'mrs' : '1' ,'much' : '1' ,'must' : '1' ,'my' : '1' ,'myself' : '1' ,'n' : '1' ,'necessary' : '1' ,'need' : '1' ,'needed' : '1' ,'needing' : '1' ,'needs' : '1' ,'never' : '1' ,'new' : '1' ,'new' : '1' ,'newer' : '1' ,'newest' : '1' ,'next' : '1' ,'no' : '1' ,'nobody' : '1' ,'non' : '1' ,'noone' : '1' ,'not' : '1' ,'nothing' : '1' ,'now' : '1' ,'nowhere' : '1' ,'number' : '1' ,'numbers' : '1' ,'o' : '1' ,'of' : '1' ,'off' : '1' ,'often' : '1' ,'old' : '1' ,'older' : '1' ,'oldest' : '1' ,'on' : '1' ,'once' : '1' ,'one' : '1' ,'only' : '1' ,'open' : '1' ,'opened' : '1' ,'opening' : '1' ,'opens' : '1' ,'or' : '1' ,'order' : '1' ,'ordered' : '1' ,'ordering' : '1' ,'orders' : '1' ,'other' : '1' ,'others' : '1' ,'our' : '1' ,'out' : '1' ,'over' : '1' ,'p' : '1' ,'part' : '1' ,'parted' : '1' ,'parting' : '1' ,'parts' : '1' ,'per' : '1' ,'perhaps' : '1' ,'place' : '1' ,'places' : '1' ,'point' : '1' ,'pointed' : '1' ,'pointing' : '1' ,'points' : '1' ,'possible' : '1' ,'present' : '1' ,'presented' : '1' ,'presenting' : '1' ,'presents' : '1' ,'problem' : '1' ,'problems' : '1' ,'put' : '1' ,'puts' : '1' ,'q' : '1' ,'quite' : '1' ,'r' : '1' ,'rather' : '1' ,'really' : '1' ,'right' : '1' ,'right' : '1' ,'room' : '1' ,'rooms' : '1' ,'s' : '1' ,'said' : '1' ,'same' : '1' ,'saw' : '1' ,'say' : '1' ,'says' : '1' ,'second' : '1' ,'seconds' : '1' ,'see' : '1' ,'seem' : '1' ,'seemed' : '1' ,'seeming' : '1' ,'seems' : '1' ,'sees' : '1' ,'several' : '1' ,'shall' : '1' ,'she' : '1' ,'should' : '1' ,'show' : '1' ,'showed' : '1' ,'showing' : '1' ,'shows' : '1' ,'side' : '1' ,'sides' : '1' ,'since' : '1' ,'small' : '1' ,'smaller' : '1' ,'smallest' : '1' ,'so' : '1' ,'some' : '1' ,'somebody' : '1' ,'someone' : '1' ,'something' : '1' ,'somewhere' : '1' ,'state' : '1' ,'states' : '1' ,'still' : '1' ,'still' : '1' ,'such' : '1' ,'sure' : '1' ,'t' : '1' ,'take' : '1' ,'taken' : '1' ,'than' : '1' ,'that' : '1' ,'the' : '1' ,'their' : '1' ,'them' : '1' ,'then' : '1' ,'there' : '1' ,'therefore' : '1' ,'these' : '1' ,'they' : '1' ,'thing' : '1' ,'things' : '1' ,'think' : '1' ,'thinks' : '1' ,'this' : '1' ,'those' : '1' ,'though' : '1' ,'thought' : '1' ,'thoughts' : '1' ,'three' : '1' ,'through' : '1' ,'thus' : '1' ,'to' : '1' ,'today' : '1' ,'together' : '1' ,'too' : '1' ,'took' : '1' ,'toward' : '1' ,'turn' : '1' ,'turned' : '1' ,'turning' : '1' ,'turns' : '1' ,'two' : '1' ,'u' : '1' ,'under' : '1' ,'until' : '1' ,'up' : '1' ,'upon' : '1' ,'us' : '1' ,'use' : '1' ,'used' : '1' ,'uses' : '1' ,'v' : '1' ,'very' : '1' ,'w' : '1' ,'want' : '1' ,'wanted' : '1' ,'wanting' : '1' ,'wants' : '1' ,'was' : '1' ,'way' : '1' ,'ways' : '1' ,'we' : '1' ,'well' : '1' ,'wells' : '1' ,'went' : '1' ,'were' : '1' ,'what' : '1' ,'when' : '1' ,'where' : '1' ,'whether' : '1' ,'which' : '1' ,'while' : '1' ,'who' : '1' ,'whole' : '1' ,'whose' : '1' ,'why' : '1' ,'will' : '1' ,'with' : '1' ,'within' : '1' ,'without' : '1' ,'work' : '1' ,'worked' : '1' ,'working' : '1' ,'works' : '1' ,'would' : '1' ,'x' : '1' ,'y' : '1' ,'year' : '1' ,'years' : '1' ,'yet' : '1' ,'you' : '1' ,'young' : '1' ,'younger' : '1' ,'youngest' : '1' ,'your' : '1' ,'yours' : '1' ,'z' : '1'  }


def getWordCount(path):
    
    wordHash = {}
    for root, dirs, files in os.walk(path):
        if 'fold1' in dirs:
            dirs.remove('fold1')        
        for fil1 in files:            
            if fil1.endswith(".txt") and fil1 != 'README.txt':                
                eachFile = os.path.join(root, fil1)
                with open(eachFile, 'r') as my_file:                    
                    fileContent = my_file.read()                    
                    for line in fileContent.splitlines():
                        line = re.sub('[^A-Za-z0-9\@#\$_]', ' ', line)
                        wordArray = line.split()                        
                        for word in wordArray:                            
                            wordStr = word.lower()
                            if stopWordList.has_key(wordStr) : continue 
                            if wordStr != '':
                                if wordHash.has_key(wordStr):
                                    value = wordHash[wordStr]
                                    value += 1
                                    wordHash[wordStr] = value
                                else:
                                    wordHash[wordStr] = 1
  
    return wordHash
    
def getRemainingWords(inputWordHash,selector):
    wordList = {}
    
    if selector != 'nT':
        for key in negTruWords:
            if not inputWordHash.has_key(key):
                wordList[key] = 0
   
    if selector != 'nD':
        for key in negDecWords:
            if not inputWordHash.has_key(key):
                wordList[key] = 0
      
    if selector != 'pD':
        for key in posDecWords:
            if not inputWordHash.has_key(key):
                wordList[key] = 0  
    if selector != 'pT':
        for key in posTruWords:
            if not inputWordHash.has_key(key):
                wordList[key] = 0          
                
    for word in wordList:
        inputWordHash[word] = 1
        
    for key in inputWordHash:
        if not wordList.has_key(key):
            prevNum = int(inputWordHash[key])
            prevNum += 1
            inputWordHash[key] = prevNum

    return inputWordHash    

def computeProbability(wordHash):
    
    sumOfValues = 0
    sumOfKeys = 0
              
    for key in wordHash.keys():
        sumOfValues+=wordHash[key]
        sumOfKeys+=1
    probTable = {}
    for key in wordHash.keys():    
        probTable[key] = math.log10(float(wordHash[key])) - math.log10(sumOfValues)

    return probTable


mainPath = sys.argv[1]
print mainPath
jsonData = {}

path1 = mainPath + 'negative_polarity/deceptive_from_MTurk' 
path2 = mainPath + 'negative_polarity/truthful_from_Web'
path3 = mainPath + 'positive_polarity/deceptive_from_MTurk' 
path4 = mainPath + 'positive_polarity/truthful_from_TripAdvisor' 


negDecWords = getWordCount(path1)      
negTruWords = getWordCount(path2)      
posDecWords = getWordCount(path3)
posTruWords = getWordCount(path4)

negDecWords = getRemainingWords(negDecWords,'nD') 
negTruWords = getRemainingWords(negTruWords,'nT')
posDecWords = getRemainingWords(posDecWords,'pD')
posTruWords = getRemainingWords(posTruWords,'pT')
   

jsonData['negDec'] = computeProbability(negDecWords)
jsonData['negTru'] = computeProbability(negTruWords)  
jsonData['posDec'] = computeProbability(posDecWords)
jsonData['posTru'] = computeProbability(posTruWords)
 

with open('nbmodel.txt', 'w') as fp:
    json.dump(jsonData, fp)
            


