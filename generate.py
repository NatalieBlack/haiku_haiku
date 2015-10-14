from nltk.parse.generate import generate
from nltk import CFG
from nltk.grammar import Nonterminal
import random
import re
seven = ['Arteriosclerosis' , 'Artificiality' , 'Autobiographical' , 'Conceptualization' , 'Decriminalization' , 'Disproportionality' , 'Editorializing' , 'Heterogeneity' , 'Infinitesimally' , 'Intercolonization' , 'Irrefutability' , 'Irreversibility' , 'Manoeuvrability' , 'Megalomaniacal' , 'Oversimplification' , 'Proletarianism' , 'Sentimentalization' , 'Superficiality']
six = ['Antediluvian' , 'Circumnavigation' , 'Disambiguation' , 'Disappriciated' , 'Discontinuity' , 'Dissimilation' , 'Eleemosynary' , 'Incomprehensible' , 'Indefatigable' , 'Prestidigitation' , 'Responsibility' , 'Sesquicentennial' , 'Superannuated' , 'Supernumerary' , 'Teleportality' , 'Verisimilitude']
five = ['Assimilation' , 'Conscientiousness' , 'Creativity' , 'Diagnostician' , 'Electricity' , 'Humiliation' , 'Mathematical' , 'Opportunity' , 'Popularity' , 'Similarity' , 'Incredulity' , 'Paediatrician' , 'Perpendicular' , 'Unbelievable' , 'University' , 'Vocabulary']
four = ['Bureaucratic' , 'Contradicting' , 'Copulation', 'Degenerate', 'Dictionary' , 'Directory' , 'Disestablish', 'Execution' , 'Indecisive', 'Insoluble' , 'Mandatory', 'Obligation' , 'Obviously' , 'Overwhelming' , 'Persecution' , 'Population' , 'Similitude' , 'Supposedly' , 'Television' , 'Termination' , 'Undoubtedly']
three = ['Adequate', 'Amazement', 'Attention', 'Attractive', 'Average', 'Banana', 'Bicycle' , 'Blindingly', 'Buffalo' , 'Cabinet', 'Certainly', 'Companion', 'Complement', 'Conference', 'Conference' , 'Connection', 'Considered', 'Curious' , 'Customary' , 'Dangerous' , 'Difficult', 'Dilemma', 'Dinosaur' , 'Documents', 'Easily', 'Electric' , 'Everything', 'Exciting' , 'Exercise' , 'Exhaustion' , 'Family' , 'Favourite' , 'Glacier', 'Happenings', 'Horizon' , 'Illustrate', 'Industry' , 'Instrument', 'Legacy', 'Liberal', 'Library' , 'Numerous' , 'Palatial', 'Period' , 'Persistent' , 'Photograph', 'Reunion' , 'Substitute' , 'Terrible' , 'Typical' ]
two = ['Acquired', 'Again' , 'Aircrafts', 'Alleged', 'Ancient', 'Auto', 'Avoid', 'Bacon', 'Basket', 'Behaved', 'Between', 'Bible', 'Billion', 'Birthright', 'Brilliant', 'Buildings', 'Collapsed', 'Conscience', 'Cycle' , 'Danger', 'Daring', 'Discuss', 'Drearier', 'Enter', 'Evening', 'Every', 'Evil', 'Forceps', 'Hamper', 'Hockey', 'Hundred', 'Inspired', 'Involved', 'Kitten', 'London', 'Lumber', 'Mountain', 'Photo', 'Playful', 'Police', 'Sheepish']
one = ['A', 'All', 'And', 'Are', 'As', 'Be', 'By', 'Day', 'Did', 'Each', 'Few', 'For', 'Get', 'Have', 'He', 'Him', 'His', 'I', 'In', 'Is', 'It', 'Long', 'Man', 'Me', 'More', 'Much', 'My', 'New', 'Not', 'Now', 'Of', 'Off', 'Old', 'On', 'One', 'Or', 'Out', 'Same', 'She', 'So', 'State', 'Than', 'That', 'The', 'They', 'Time', 'To', 'Up', 'War', 'Was']
grammar = """haiku -> five seven five 
      seven -> '""" + random.choice(seven) + """'
      seven -> '""" + random.choice(seven) + """'
      seven -> '""" + random.choice(seven) + """'
      seven -> '""" + random.choice(seven) + """'
      seven -> one six
      seven -> two five 
      seven -> three four 
      seven -> four three
      seven -> five two
      seven -> six one
      six -> '""" + random.choice(six) + """'
      six -> '""" + random.choice(six) + """'
      six -> '""" + random.choice(six) + """'
      six -> '""" + random.choice(six) + """'
      six -> one five
      six -> two four
      six -> three three
      six -> four two
      six -> five one
      five -> '""" + random.choice(five) + """'
      five -> '""" + random.choice(five) + """'
      five -> '""" + random.choice(five) + """'
      five -> '""" + random.choice(five) + """'
      five -> one four
      five -> two three
      five -> three two
      five -> four one
      four -> '""" + random.choice(four) + """'
      four -> '""" + random.choice(four) + """'
      four -> '""" + random.choice(four) + """'
      four -> '""" + random.choice(four) + """'
      four -> '""" + random.choice(four) + """'
      four -> one three
      four -> two two
      four -> three one
      three -> '""" + random.choice(three) + """'
      three -> '""" + random.choice(three) + """'
      three -> '""" + random.choice(three) + """'
      three -> '""" + random.choice(three) + """'
      three -> '""" + random.choice(three) + """'
      three -> one two
      three -> two one
      two -> '""" + random.choice(two) + """'
      two -> '""" + random.choice(two) + """'
      two -> '""" + random.choice(two) + """'
      two -> '""" + random.choice(two) + """'
      two -> '""" + random.choice(two) + """'
      two -> one one
      one -> '""" + random.choice(one) + """'
      one -> '""" + random.choice(one) + """'
      one -> '""" + random.choice(one) + """'
      one -> '""" + random.choice(one) + "'"

g = CFG.fromstring(grammar)
#for poem in generate(g, n=100):
#    print ' '.join(poem)

fives = []
sevens = []
for poem in generate(g, start=Nonterminal('five'), n=2000000):
  fives.append(' '.join(poem))

for poem in generate(g, start=Nonterminal('seven'), n=2000000):
  sevens.append(' '.join(poem))

line1 = random.choice(fives)
line2 = random.choice(sevens)
line3 = random.choice(fives)

print '\n'.join([line1,line2,line3]).lower()