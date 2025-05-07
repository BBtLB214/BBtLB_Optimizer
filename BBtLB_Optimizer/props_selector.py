def generate_prop_combos(players, props_data, min_corr=0.7):
    combos = []
    for player in players:
        for prop in props_data.get(player, []):
            if prop['correlation'] >= min_corr:
                combos.append((player, prop['stat'], prop['line']))
    return combos
