temperature = int(input("Enter temperature: "))
def tem(temperature):
  if temperature > 28:
    return "Hot"
  elif temperature >=18 and temperature <=28:
    return "Warm"
  else:
    return "Cold"
print(tem(temperature))
                  