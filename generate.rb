require 'rltk'

grammar = RLTK::CFG.new
seven = ['arteriosclerosis' , 'artificiality' , 'autobiographical' , 'conceptualization' , 'decriminalization' , 'disproportionality' , 'editorializing' , 'heterogeneity' , 'infinitesimally' , 'intercolonization' , 'irrefutability' , 'irreversibility' , 'manoeuvrability' , 'megalomaniacal' , 'oversimplification' , 'proletarianism' , 'sentimentalization' , 'superficiality']
six = ['antediluvian' , 'circumnavigation' , 'disambiguation' , 'disappriciated' , 'discontinuity' , 'dissimilation' , 'eleemosynary' , 'incomprehensible' , 'indefatigable' , 'prestidigitation' , 'responsibility' , 'sesquicentennial' , 'superannuated' , 'supernumerary' , 'teleportality' , 'verisimilitude']
five = ['assimilation' , 'conscientiousness' , 'creativity' , 'diagnostician' , 'electricity' , 'humiliation' , 'mathematical' , 'opportunity' , 'popularity' , 'similarity' , 'incredulity' , 'paediatrician' , 'perpendicular' , 'unbelievable' , 'university' , 'vocabulary']
four = ['bureaucratic' , 'contradicting' , 'copulation', 'degenerate', 'dictionary' , 'directory' , 'disestablish', 'execution' , 'indecisive', 'insoluble' , 'mandatory', 'obligation' , 'obviously' , 'overwhelming' , 'persecution' , 'population' , 'similitude' , 'supposedly' , 'television' , 'termination' , 'undoubtedly']
three = ['adequate', 'amazement', 'attention', 'attractive', 'average', 'banana', 'bicycle' , 'blindingly', 'buffalo' , 'cabinet', 'certainly', 'companion', 'complement', 'conference', 'conference' , 'connection', 'considered', 'curious' , 'customary' , 'dangerous' , 'difficult', 'dilemma', 'dinosaur' , 'documents', 'easily', 'electric' , 'everything', 'exciting' , 'exercise' , 'exhaustion' , 'Family' , 'Favourite' , 'glacier', 'happenings', 'horizon' , 'illustrate', 'industry' , 'instrument', 'legacy', 'liberal', 'library' , 'numerous' , 'palatial', 'period' , 'persistent' , 'photograph', 'reunion' , 'substitute' , 'terrible' , 'typical' ]
two = ['acquired', 'again' , 'aircrafts', 'alleged', 'ancient', 'auto', 'avoid', 'bacon', 'basket', 'behaved', 'between', 'bible', 'billion', 'birthright', 'brilliant', 'buildings', 'collapsed', 'conscience', 'cycle' , 'danger', 'daring', 'discuss', 'drearier', 'enter', 'evening', 'every', 'evil', 'Forceps', 'hamper', 'hockey', 'hundred', 'inspired', 'involved', 'kitten', 'london', 'lumber', 'mountain', 'photo', 'playful', 'police', 'sheepish']
one = ['a', 'all', 'and', 'are', 'as', 'be', 'by', 'day', 'did', 'each', 'Few', 'For', 'get', 'have', 'he', 'him', 'his', 'i', 'in', 'is', 'it', 'long', 'man', 'me', 'more', 'much', 'my', 'new', 'not', 'now', 'of', 'off', 'old', 'on', 'one', 'or', 'out', 'same', 'she', 'so', 'state', 'than', 'that', 'the', 'they', 'time', 'to', 'up', 'war', 'was']
other_one = ['not', 'blue','good','day','night','hour','old','long','small','time','moon','sun','earth','fire','air','quite','go','years','same','facts','love']

grammar.production(:haiku, 'five seven five')
grammar.production(:seven) do
  clause('one six')
  clause('two five')
  clause('three four')
  clause('four three')
  clause('five two')
  clause('six one')
  seven.each do |s|
    clause(s)
  end
end
grammar.production(:six) do
  clause('one five')
  clause('two four')
  clause('three three')
  clause('four two')
  clause('five one')
  six.each do |s|
    clause(s)
  end
end
grammar.production(:five) do
  clause('one four')
  clause('two three')
  clause('three two')
  clause('four one')
  five.each do |f|
    clause(f)
  end
end

grammar.production(:four) do
  clause('one three')
  clause('two two')
  clause('three one')
  four.each do |f|
    clause(f)
  end
end

grammar.production(:three) do
  clause('one two')
  clause('two one')
  three.each do |t|
    clause(t)
  end
end

grammar.production(:two) do
  clause('one one')
  two.each do |t|
    clause(t)
  end
end

grammar.production(:one) do
  one.each do |o|
    clause(o)
  end
end

grammar.productions.each do |p|
  puts p
end
