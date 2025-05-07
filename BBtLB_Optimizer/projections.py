def get_player_projections(api_data, model_data, opponent_stats):
    player_projections = {}
    for player in api_data['players']:
        base_proj = model_data[player['id']]['base']
        opponent_factor = opponent_stats[player['opponent']]
        player_projections[player['id']] = {
            'median': base_proj['median'] * opponent_factor['multiplier'],
            'floor': base_proj['floor'] * opponent_factor['multiplier'],
            'ceiling': base_proj['ceiling'] * opponent_factor['multiplier'],
        }
    return player_projections
