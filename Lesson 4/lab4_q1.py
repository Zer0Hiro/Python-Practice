def main():
    #BMI = weight (kg) / (height (m))^2
    weight = int(input("Enter Weight (in kg): "))
    height = int(input("Enter Height (in cm): "))
    bmi = float(weight / ((height/100)**2))
    #BMI size check
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25.0:
        print("Normal weight")
    elif bmi < 30.0:
        print("Increased weight")
    elif bmi < 40.0:
        print("Obese")
    else:
        print("Very high obese")
        
main()