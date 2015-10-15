from nltk.parse.generate import generate
from nltk import CFG as G
from nltk.grammar import Nonterminal as N
import random as a_random
seven = ['arteriosclerosis' , 'artificiality' , 'autobiographical' , 'conceptualization' , 'decriminalization' , 'disproportionality' , 'editorializing' , 'heterogeneity' , 'infinitesimally' , 'intercolonization' , 'irrefutability' , 'irreversibility' , 'manoeuvrability' , 'megalomaniacal' , 'oversimplification' , 'proletarianism' , 'sentimentalization' , 'superficiality']
six = ['antediluvian' , 'circumnavigation' , 'disambiguation' , 'disappriciated' , 'discontinuity' , 'dissimilation' , 'eleemosynary' , 'incomprehensible' , 'indefatigable' , 'prestidigitation' , 'responsibility' , 'sesquicentennial' , 'superannuated' , 'supernumerary' , 'teleportality' , 'verisimilitude']
five = ['assimilation' , 'conscientiousness' , 'creativity' , 'diagnostician' , 'electricity' , 'humiliation' , 'mathematical' , 'opportunity' , 'popularity' , 'similarity' , 'incredulity' , 'paediatrician' , 'perpendicular' , 'unbelievable' , 'university' , 'vocabulary']
four = ['bureaucratic' , 'contradicting' , 'copulation', 'degenerate', 'dictionary' , 'directory' , 'disestablish', 'execution' , 'indecisive', 'insoluble' , 'mandatory', 'obligation' , 'obviously' , 'overwhelming' , 'persecution' , 'population' , 'similitude' , 'supposedly' , 'television' , 'termination' , 'undoubtedly']
three = ['adequate', 'amazement', 'attention', 'attractive', 'average', 'banana', 'bicycle' , 'blindingly', 'buffalo' , 'cabinet', 'certainly', 'companion', 'complement', 'conference', 'conference' , 'connection', 'considered', 'curious' , 'customary' , 'dangerous' , 'difficult', 'dilemma', 'dinosaur' , 'documents', 'easily', 'electric' , 'everything', 'exciting' , 'exercise' , 'exhaustion' , 'family' , 'favourite' , 'glacier', 'happenings', 'horizon' , 'illustrate', 'industry' , 'instrument', 'legacy', 'liberal', 'library' , 'numerous' , 'palatial', 'period' , 'persistent' , 'photograph', 'reunion' , 'substitute' , 'terrible' , 'typical' ]
two = ['acquired', 'again' , 'aircrafts', 'alleged', 'ancient', 'auto', 'avoid', 'bacon', 'basket', 'behaved', 'between', 'bible', 'billion', 'birthright', 'brilliant', 'buildings', 'collapsed', 'conscience', 'cycle' , 'danger', 'daring', 'discuss', 'drearier', 'enter', 'evening', 'every', 'evil', 'forceps', 'hamper', 'hockey', 'hundred', 'inspired', 'involved', 'kitten', 'london', 'lumber', 'mountain', 'photo', 'playful', 'police', 'sheepish']
one = ['a', 'all', 'and', 'are', 'as', 'be', 'by', 'day', 'did', 'each', 'few', 'for', 'get', 'have', 'he', 'him', 'his', 'i', 'in', 'is', 'it', 'long', 'man', 'me', 'more', 'much', 'my', 'new', 'not', 'now', 'of', 'off', 'old', 'on', 'one', 'or', 'out', 'same', 'she', 'so', 'state', 'than', 'that', 'the', 'they', 'time', 'to', 'up', 'war', 'was']
other_one = ['not', 'blue','good','day','night','hour','old','long','small','time','moon','sun','earth','fire','air','quite','go','years','same','facts','love']
this_is_the_grammar = """haiku -> five sev five 
      sev -> 'arteriosclerosis' | 'artificiality' | 'autobiographical' | 'conceptualization' | 'decriminalization' | 'disproportionality' | 'editorializing' | 'heterogeneity' | 'infinitesimally' | 'intercolonization' | 'irrefutability' | 'irreversibility' | 'manoeuvrability' | 'megalomaniacal' | 'oversimplification' | 'proletarianism' | 'sentimentalization' | 'superficiality'
      sev -> one six
      sev -> two five 
      sev -> three four 
      sev -> four three
      sev -> five two
      sev -> six one
      six -> 'antediluvian' | 'circumnavigation' | 'disambiguation' | 'disappriciated' | 'discontinuity' | 'dissimilation' | 'eleemosynary' | 'incomprehensible' | 'indefatigable' | 'prestidigitation' | 'responsibility' | 'sesquicentennial' | 'superannuated' | 'supernumerary' | 'teleportality' | 'verisimilitude'
      six -> one five
      six -> two four
      six -> three three
      six -> four two
      six -> five one
      five -> 'assimilation' | 'conscientiousness' | 'creativity' | 'diagnostician' | 'electricity' | 'humiliation' | 'mathematical' | 'opportunity' | 'popularity' | 'similarity' | 'incredulity' | 'paediatrician' | 'perpendicular' | 'unbelievable' | 'university' | 'vocabulary'
      five -> two three
      five -> three two
      four -> 'bureaucratic' | 'contradicting' | 'copulation'| 'degenerate'| 'dictionary' | 'directory' | 'disestablish'| 'execution' | 'indecisive'| 'insoluble' | 'mandatory'| 'obligation' | 'obviously' | 'overwhelming' | 'persecution' | 'population' | 'similitude' | 'supposedly' | 'television' | 'termination' | 'undoubtedly'
      four -> two two
      four -> one three 
      four -> three one
      three -> 'adequate'| 'amazement'| 'attention'| 'attractive'| 'average'| 'banana'| 'bicycle' | 'blindingly'| 'buffalo' | 'cabinet'| 'certainly'| 'companion'| 'complement'| 'conference'| 'conference' | 'connection'| 'considered'| 'curious' | 'customary' | 'dangerous' | 'difficult'| 'dilemma'| 'dinosaur' | 'documents'| 'easily'| 'electric' | 'everything'| 'exciting' | 'exercise' | 'exhaustion' | 'family' | 'favourite' | 'glacier'| 'happenings'| 'horizon' | 'illustrate'| 'industry' | 'instrument'| 'legacy'| 'liberal'| 'library' | 'numerous' | 'palatial'| 'period' | 'persistent' | 'photograph'| 'reunion' | 'substitute' | 'terrible' | 'typical' 
      two -> 'acquired'| 'again' | 'aircrafts'| 'alleged'| 'ancient'| 'auto'| 'avoid'| 'basket'| 'behaved'| 'between'| 'bible'| 'billion'| 'birthright'| 'brilliant'| 'buildings'| 'collapsed'| 'conscience'| 'cycle' | 'danger'| 'daring'| 'discuss'| 'drearier'| 'enter'| 'evening'| 'every'| 'evil'| 'forceps'| 'hamper'| 'hockey'| 'hundred'| 'inspired'| 'involved'| 'kitten'| 'london'| 'lumber'| 'mountain'| 'photo'| 'playful'| 'police'| 'sheepish'
      one -> '""" + a_random.choice(other_one) + """'
      one -> '""" + a_random.choice(other_one) + """'
      one -> '""" + a_random.choice(other_one) + """'
      one -> '""" + a_random.choice(other_one) + "'"
pentas = []
sevens = []
with_blank_spaces = ' '


############################################
############################################
############################################
def choose_line(some_lines):#5
    return a_random.choice(#7
                    some_lines).lower() #5

############################################

############################################
choose = choose_line #5

g = G.fromstring(#7
                    this_is_the_grammar) #5
############################################

############################################
while not len(pentas):#5
    for poem in generate(g, #7
                           start=N('five')): #5
############################################

############################################
      pentas.append(#5
                    with_blank_spaces.join(poem))#7

fives = pentas #5
############################################

############################################
third = choose(fives) #5
first = choose(fives) #7

def display_the(poem):#5
############################################
    print '\n'.join(poem)#5

for poem in generate(g,#7
                       start=N('sev')): #5
############################################
  sevens.append(#5
                with_blank_spaces.join(poem))#7


sept = sevens#5
############################################
 


############################################
mid = choose(sept)#5
haiku = [first,mid,third]#7

display_the(haiku)#5

############################################
