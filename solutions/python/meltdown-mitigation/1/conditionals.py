"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = (generated_power/theoretical_max_power)*100
    if percentage_value >= 80:
        return 'green'
    elif percentage_value >= 60 and percentage_value < 80:
        return 'orange'
    elif percentage_value >= 30 and percentage_value < 60:
        return 'red'
    else:
        return 'black'
    


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < (threshold * 0.9):
        return 'LOW'
    elif temperature * neutrons_produced_per_second < (threshold * 1.1):
        return 'NORMAL'
    elif temperature * neutrons_produced_per_second > threshold:
        return 'DANGER'
    else:
        'LOW'
        