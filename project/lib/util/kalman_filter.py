#Code written by Scott Lobdell
#http://scottlobdell.me/2014/08/kalman-filtering-python-reading-sensor-input/

import kalman_object as kalman

def filter(noisy_measurement, process_variance = 1e-3):
  #import random
  iteration_count = len(noisy_measurement) #100 #replace with length of stock price list
  #actual_values = [-0.37727 + j * j * 0.00001 for j in xrange(iteration_count)] #list of "actual values", not necessary for our purposes
  #noisy_measurement = [random.random() * 2.0 - 1.0 + actual_val for actual_val in actual_values] #simulated measurements, replace with actual stock price list

  # in practice we would take our sensor, log some readings and get the
  # standard deviation
  import numpy
  #measurement_standard_deviation = numpy.std([random.random() * 2.0 - 1.0 for j in xrange(iteration_count)]) #instead get std dev of noisy_measurement list
  measurement_standard_deviation = numpy.std(noisy_measurement)

  # The smaller this number, the fewer fluctuations, but can also venture off
  # course... (process_variance, moved to arguments with default 1e-3)
  estimated_measurement_variance = measurement_standard_deviation ** 2  # 0.05 ** 2
  avg_1 = numpy.average(noisy_measurement[0:3])
  kalman_filter = kalman.KFObject(process_variance, estimated_measurement_variance, avg_1)
  posteri_estimate_graph = []

  for iteration in range(1, iteration_count):
      kalman_filter.input_latest_noisy_measurement(noisy_measurement[iteration])
      posteri_estimate_graph.append(kalman_filter.get_latest_estimated_measurement())


  '''
  import pylab
  pylab.figure()
  pylab.plot(noisy_measurement, color='r', label='noisy measurements')
  pylab.plot(posteri_estimate_graph, 'b-', label='a posteri estimate')
  #pylab.plot(actual_values, color='g', label='truth value')
  pylab.legend()
  pylab.xlabel('Iteration')
  pylab.ylabel('Output')
  pylab.show()
  '''

  return posteri_estimate_graph
