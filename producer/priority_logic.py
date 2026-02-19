def determining_urgency(warning):
    if (warning['weapons_count'] > 0 or
        warning['distance_from_fence_m'] <= 50 or
        warning['people_count'] >= 8 or
        warning['vehicle_type'] == 'truck' or (warning['distance_from_fence_m'] <= 150 and warning['people_count'] >= 4) or
            (warning['vehicle_type'] == 'jeep' and warning['people_count'] >= 3)):
        warning['priority'] = 'URGENT'
    else:
        warning['priority'] = 'NORMAL'
    return warning
