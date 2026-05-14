from sqlalchemy.orm import Session
from ..repositories.athl_repo import AthleteRepository
from ..repositories.team_repo import TeamRepository
from ..clients.client import ESPNClient
from ..exceptions import TeamNotFoundError

def get_team_athletes(team_id: int, session: Session):
    athlete = AthleteRepository(session=session)
    team = TeamRepository(session=session).get_team_by_id(team_id=team_id)  # returns a Teams object
    if not team:
        raise TeamNotFoundError

    if not team.athletes:
        client = ESPNClient(base_url=f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/{team.espn_id}/roster")
        
        request = client.get_roster(f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/{team.espn_id}/roster")
        players = request['athletes']

        for player in players:
            athl_id = player.get('id')
            full_name = player.get('fullName')
            position = player['position']['name']
            age = player.get('age')
            weight = player.get('weight')
            height = player.get('height')
            jersey_num = player.get('jersey')
            debut = player.get('debutYear', None)

            athlete.create_athlete(athl_id=athl_id, full_name=full_name, position=position, age=age, weight=weight, 
                                    height=height, jersey_num=jersey_num, debut=debut, team=team)

    return team.athletes