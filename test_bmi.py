import Lab2.bmi as bmi


def test_bmi_normal_weight():
  y = bmi.calculate_bmi(70,1.74)
  assert y == 0
  print("You are in normal weight classification")
  
def test_bmi_over_weight():
  y = bmi.calculate_bmi(80, 1.74)
  assert y == 1
  print("You are in overweight classification")
def test_bmi_under_weight():
  y = bmi.calculate_bmi(40, 1.74)
  assert y == -1
  print("You are in underweight classification")
 


