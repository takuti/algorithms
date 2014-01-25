# coding: utf-8

require 'igo-ruby'

##############################################
# Create hash
# Argument: _document(String)
# Return: hash(key:word, value:frequency)
##############################################
def CreateHash(_document)
	tagger = Igo::Tagger.new('./ipadic')

	hash = Hash.new
	tagger.parse(_document).each do |m|
		# Noun will be index word. Other categories are ignored.
		if m.feature.split(',')[0] == '名詞'
			hash[m.surface] = 0 if !hash[m.surface]
			hash[m.surface] += 1
		end
	end
	hash
end

##############################################
# Calc TF value
# Argument: _hash
# Return: tf(key:word, value:tf value of the word)
##############################################
def TF(_hash)
	total = 0
	_hash.each{|key, value| total += value} # Calc sum of frequency

	tf = Hash.new
	_hash.each do |key, value|
		tf[key] = value / total.to_f
	end
	tf
end

##############################################
# Calc IDF value
# Argument: _hash, _df, _n(num of documents)
# Return: idf(key:word, value:idf value of the word)
##############################################
def IDF(_hash, _df, _n)
	idf = Hash.new
	_hash.each do |key, value|
		idf[key] = (Math.log10(_n/_df[key])+1)
	end
	idf
end



### Create hash from document
doc_hash = Array.new
doc_hash[0] = CreateHash('リンゴとレモンとレモン')
doc_hash[1] = CreateHash('リンゴとミカン')

### How many documents are including each word
df = Hash.new
for i in 0..(doc_hash.size-1) do
	doc_hash[i].each do |key, value|
		df[key] = 0 if !df[key]
		df[key] += 1
	end
end

### Calc tf*idf, and print result sorted by that value
for i in 0..(doc_hash.size-1) do
	puts "Document No.#{i+1}"
	tf = TF(doc_hash[i])
	idf = IDF(doc_hash[i],df,doc_hash.size)
	w = Hash.new
	doc_hash[i].each do |key, value|
		w[key] = tf[key] * idf[key]
	end

	w.sort_by{|key, value| -value}.each do |key, value|
		puts "#{key} (#{value})"
	end
	puts ''
end
