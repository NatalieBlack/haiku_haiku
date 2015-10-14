require 'rltk'

grammar = RLTK::CFG.new

grammar.production(:haiku, 'five seven five')
grammar.production(:five) do
  clause('one four')
  clause('four one')
  clause('two three')
  clause('three two')
  clause(five.sample)
  clause(five.sample)
  clause(five.sample)
  clause(five.sample)
  clause(five.sample)
end

grammar.production(:four) do
  clause('two two')
end

grammar.production(:seven) do
end

#grammar.production(:a, 'b')
#grammar.production(:b, 'G')
