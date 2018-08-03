from sigopt import examples


class TestExamples(object):
  # independently verified:
  x1, x2, expected_y = (0.0, 1.0, 0.2703371615911343)
  y = examples.franke_function(x1, x2)
  assert abs(y - expected_y) < 1.0e-6
