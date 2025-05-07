from scipy.optimize import linprog

def generate_lineup(players, salary_cap, position_constraints, is_gpp=True):
    objective = [p['ceiling'] if is_gpp else p['floor'] for p in players.values()]
    result = linprog(c=[-x for x in objective], bounds=[(0, 1)] * len(players))
    return result.x
