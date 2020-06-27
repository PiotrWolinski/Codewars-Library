def who_is_next(names, r):
    turn = 0
    cola_drunk_in_round = len(names)
    total_cola_drunk = 0
    while total_cola_drunk < r:
        turn += 1
        total_cola_drunk += cola_drunk_in_round 
        cola_drunk_in_round *= 2

    drinker_id = r - int(total_cola_drunk - cola_drunk_in_round / 2) - 1

    duplicates_in_queue = int(cola_drunk_in_round / 2 / len(names))
    
    drinker_id = drinker_id // duplicates_in_queue
    
    return names[drinker_id]