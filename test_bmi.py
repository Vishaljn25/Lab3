import Lab2.bmi as bmi


def test_bmi_normal_weight():
  print("You are in normal weight classification")
def test_bmi_over_weight():
  print("You are in overweight classification")
def test_bmi_under_weight():
  print("You are in underweight classification")
 

y = bmi.calculate_bmi()
if (y == -1):
  test_bmi_under_weight()
elif y == 0 :
 test_bmi_normal_weight()
else:
 test_bmi_over_weight()




