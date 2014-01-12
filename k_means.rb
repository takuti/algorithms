# coding: utf-8

class Kmeans
	def initialize
		@num_dimension = 4	# Feature Vector is 4-dimension
		@num_cluster = 3

		@feature_vector = Array.new

		open('data/iris.data').each do |p|
			point_array = p.split(',')
			@feature_vector << {'point' => [point_array[0].to_f, point_array[1].to_f, point_array[2].to_f, point_array[3].to_f], 'cluster' => (rand 0..(@num_cluster-1))}
		end

		@center = Array.new(@num_cluster)
		doClustering
	end

	def doClustering
		change_flg = true

		while change_flg do
			change_flg = false
			calcCenter
			for i in 0..@feature_vector.length-1 do
				c = getCluster(@feature_vector[i]['point'])
				if c != @feature_vector[i]['cluster']
					@feature_vector[i]['cluster'] = c
					change_flg = true
				end
			end
		end

		printResult
	end

	def calcCenter
		for i in 0..@num_cluster-1 do
			@center[i] = {'point' => Array.new(@num_dimension, 0), 'cnt' => 0}
		end

		# calculate sum of each cluster's feature vector
		for i in 0..@feature_vector.length-1 do
			cluster = @feature_vector[i]['cluster']
			@center[cluster]['cnt'] += 1
			for j in 0..@num_dimension-1 do
				@center[cluster]['point'][j] += @feature_vector[i]['point'][j]
			end
		end

		# calculate average
		for i in 0..@num_cluster-1 do
			for j in 0..@num_dimension-1 do
				@center[i]['point'][j] /= @center[i]['cnt'] if @center[i]['cnt'] != 0
			end
		end
	end

	def getCluster(_point)
		min = Float::INFINITY
		for i in 0..@num_cluster-1 do
			d = calcDistance(_point, @center[i]['point'])
			if min > d
				min = d
				new_cluster = i
			end
		end
		new_cluster
	end

	def calcDistance(_p1, _p2)
		square_sum = 0
		for i in 0..@num_dimension-1
			square_sum += (_p1[i]-_p2[i])*(_p1[i]-_p2[i])
		end
		Math.sqrt(square_sum)
	end

	def printResult
		for i in 0..@feature_vector.length-1 do
			p = @feature_vector[i]['point']
			puts "#{p[0]},#{p[1]},#{p[2]},#{p[3]},#{@feature_vector[i]['cluster']}"
		end
	end
end

Kmeans.new