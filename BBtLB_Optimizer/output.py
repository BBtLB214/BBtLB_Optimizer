import csv

def output_lineups(lineups, filename='lineups.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player', 'Position', 'Team', 'Salary', 'Proj (Med/Floor/Ceil)', 'Value', 'Leverage', 'Notes'])
        for lineup in lineups:
            writer.writerow([lineup.get('player', ''), lineup.get('position', ''), lineup.get('team', ''), lineup.get('salary', ''), lineup.get('proj', ''), lineup.get('value', ''), lineup.get('leverage', ''), lineup.get('notes', '')])
