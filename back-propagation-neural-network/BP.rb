# coding: utf-8

class BP
  def initialize
    # There are 3 layers (Input, Hidden, Output each)
    @num_input_units = 6
    @num_hidden_units = 2
    @num_output_units = 1

    @w1 = Array.new(@num_hidden_units) { Array.new(@num_input_units) } # connection weight of layer 1-2
    for i in 0..@num_hidden_units-1 do
      for j in 0..@num_input_units-1 do
        @w1[i][j] = (rand -0.3..0.3)
      end
    end

    @w2 = Array.new(@num_output_units) { Array.new(@num_hidden_units) } # connection weight of layer 2-3
    for i in 0..@num_output_units-1 do
      for j in 0..@num_hidden_units-1 do
        @w2[i][j] = (rand -0.3..0.3)
      end
    end

    doLearning
  end

  def doLearning
    puts 'Start Learning...'

    training_data = Array.new
    teacher_data = Array.new

    open('../@data/6bit_symmetry.data').each do |line|
      pattern = line.split(' ')
      training_data << pattern[0]
      teacher_data << [pattern[1].to_i]
    end
    p training_data
    p teacher_data

    # training_data = ['100001', '001010', '110011', '001110', '000011']
    # teacher_data = [[1],[0],[1],[1],[1]]

    epsilon = 0.1 # learning rate
    alpha = 0.9 # momentum

    delta_w1 = Array.new(@num_hidden_units) { Array.new(@num_input_units){0.0} } # w1 error
    delta_w2 = Array.new(@num_output_units) { Array.new(@num_hidden_units){0.0} } # w2 error

    error_tolerance = 0.001
    epoch = 0
    begin
    # for x in 0..60 do
      error = 0.0
      epoch += 1
      for n in 0..training_data.length-1 do
        unit_out = estimateOutput(training_data[n])

        for i in 0..@num_output_units-1 do
          error += 0.5*(unit_out['output'][i] - teacher_data[n][i])*(unit_out['output'][i] - teacher_data[n][i])
        end
        # Calculate error propagation
        ## (11) d of output layer [k=m]
        d2 = Array.new(@num_output_units)
        for i in 0..@num_output_units-1 do
          o = unit_out['output'][i]
          y = teacher_data[n][i]
          d2[i] = (o-y)*o*(1-o)
        end
        # puts "#{training_data[n]} (y = #{teacher_data[n]}): \nd2 = #{d2}" if x==100

        ## (10) d of hidden layer [k!=m]
        d1 = Array.new(@num_hidden_units) {0.0}
        for i in 0..@num_output_units-1 do
          for j in 0..@num_hidden_units-1 do
            o = unit_out['hidden'][j]
            d1[j] += (@w2[i][j]*d2[i] * o*(1-o))
          end
        end
        # puts "d1 = #{d1}" if x==100

        ## (8), (9)
        ### revision of w2
        for i in 0..@num_output_units-1 do
          for j in 0..@num_hidden_units-1 do
            o = unit_out['hidden'][j]
            delta_w2[i][j] = -1*epsilon*d2[i]*o + alpha*delta_w2[i][j]
            @w2[i][j] += delta_w2[i][j]
          end
        end
        # puts "delta_w2 = #{delta_w2}\nw2 = #{@w2}\n\n" if x==100

        ### revision of w1
        for i in 0..@num_hidden_units-1 do
          for j in 0..@num_input_units-1 do
            o = unit_out['input'][j]
            delta_w1[i][j] = -1*epsilon*d1[i]*o + alpha*delta_w1[i][j]
            @w1[i][j] += delta_w1[i][j]
          end
        end
        # puts "delta_w1 = #{delta_w1}\nw2 = #{@w1}\n\n" if x==100
      end
      puts error if epoch%1000 == 0
    end while error > error_tolerance # convergence test

    puts 'Complete Learning!'
    puts "\n***** Connection weight of layer 1-2 *****\n#{@w1}"
    puts "\n***** Connection weight of layer 2-3 *****\n#{@w2}"

    # doTest
    p estimateOutput(training_data[0])['output'][0]
    p estimateOutput(training_data[1])['output'][0]
    p estimateOutput(training_data[2])['output'][0]
    p estimateOutput(training_data[3])['output'][0]
    p estimateOutput(training_data[4])['output'][0]
  end

  def doTest
    puts "\nTest Result"
    for i in 0..63 # from 000000 to 111111
      input = i.to_s(2) # binary form
      input = '0'*(6-input.length) << input # arrange num of digits to 6
      output = estimateOutput(input)['output']
      puts "#{input} => #{output}"
    end
  end

  def estimateOutput(_input)
    unit_in = Hash.new
    unit_out = Hash.new

    # unit bias
    theta = Hash.new
    theta['hidden'] = [1.0, 1.0]
    theta['output'] = [-6.89]

    # (1), (2)
    ## Case: layer 1 as input layer
    unit_in['input'] = Array.new(@num_input_units)
    unit_out['input'] = Array.new(@num_input_units)
    for i in 0..@num_input_units-1 do
      unit_in['input'][i] = _input[i].to_f
      unit_out['input'][i] = unit_in['input'][i]
    end

    # (3), (4)
    ## Case: layer 2 as hidden layer
    unit_in['hidden'] = Array.new(@num_hidden_units){0.0}
    unit_out['hidden'] = Array.new(@num_hidden_units)
    for i in 0..@num_hidden_units-1 do
      for j in 0..@num_input_units-1 do
        unit_in['hidden'][i] += @w1[i][j]*unit_out['input'][j]
      end
      unit_out['hidden'][i] = f(unit_in['hidden'][i], theta['hidden'][i])
    end

    ## Case: layer 3 as output layer
    unit_in['output'] = Array.new(@num_output_units){0.0}
    unit_out['output'] = Array.new(@num_output_units)
    for i in 0..@num_output_units-1 do
      for j in 0..@num_hidden_units-1 do
        unit_in['output'][i] += @w2[i][j]*unit_out['hidden'][j]
      end
      unit_out['output'][i] = f(unit_in['output'][i], theta['output'][i])
    end

    unit_out
  end

  def f(_x, _theta) # sigmoid function
    1/(1+Math.exp(-1*_x+_theta))
  end
end

BP.new
