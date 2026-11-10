import time

# Input: Patient's temperature
temp = float(input('Enter patient temperature (in degrees Celsius): '))

# 1. Extreme Unreal Lower Bound Check First
if temp < 13.3:
    print('>>>>ERROR>>>TEMPERATURE>>>UNREALISTIC')

# 2. Dangerously below average
elif temp <= 32.2:
    print('Patient has risk of myxedema coma, cardiac arrhythmias and end stage organ failure')
    time.sleep(7)
    print("\nDEFINITION")
    print("Myxedema Coma: The most severe, life-threatening form of hypothyroidism.")
    print("Cardiac Arrhythmias: Cold temperature irritates the heart muscle, causing irregular rhythms.")
    print("End-Stage Organ Failure: As vital organs shut down, the body loses all ability to regulate heat.")
    print("\nATTENTION: THESE NOTES ARE FOR EDUCATIONAL PURPOSES ONLY, NOT FOR REAL LIFE SITUATIONS")

# 3. Extremely below average
elif temp <= 34.9:
    print('Patient has risk of severe septic shock, adrenal insufficiency and hypoglycemia')
    time.sleep(4)
    print("\nDEFINITION")
    print("Severe septic shock: Blood pressure drops dangerously low, decreasing core temperature.")
    print("Adrenal insufficiency: A life-threatening shortage of hormones critical for metabolism.")
    print("Hypoglycemia: Critically low blood glucose. Cells lack the energy to produce heat.")
    print("\nATTENTION: THESE NOTES ARE FOR EDUCATIONAL PURPOSES ONLY, NOT FOR REAL LIFE SITUATIONS")

# 4. Slightly below average
elif temp <= 35.9:
    print('Patient has risk of hypothermia, early sepsis and malnutrition anorexia nervosa or hypothyroidism')
    time.sleep(7)
    print("\nDEFINITION")
    print("Early Sepsis: Severe infection. Vulnerable populations often develop a low temperature.")
    print("Hypothermia: Core body temperature drops below 35°C because the body loses heat too fast.")
    print("Anorexia nervosa: Restrictive eating disorder causing severe restriction of food intake.")
    print("\nATTENTION: THIS IS FOR EDUCATIONAL PURPOSE, NOT REAL LIFE SITUATION")

# 5. Average temperature
elif temp <= 36.9:
    print('Patient has regular temperature')

# 6. Slightly above average
elif temp <= 37.5:
    print('Patient has low grade baseline or normal variation')

# 7. Above average
elif temp <= 38.0:
    print('Patient has low grade fever')

# 8. Extremely above average
elif temp < 40.0:
    print('Patient has pyrexia')
    time.sleep(7)
    print("\nDEFINITION")
    print("Pyrexia is the medical term for a fever—an elevation in core body temperature.")
    print("\nTHIS IS FOR EDUCATIONAL PURPOSES ONLY, NOT FOR REAL LIFE SITUATIONS")

# 9. Dangerously above average
elif temp <= 46.6:
    print('Patient has environmental heatstroke')
    time.sleep(7)
    print("\nDEFINITION")
    print("Environmental heat stroke: Core temperature rises dangerously high due to external heat.")
    print("\nATTENTION: THIS IS FOR EDUCATIONAL PURPOSE, NOT REAL LIFE SITUATION")

# 10. Extreme Unreal Upper Bound Check
else:
    print('>>>>ERROR>>>TEMPERATURE>>>UNREALISTIC')
