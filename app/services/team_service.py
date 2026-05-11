from sqlalchemy.orm import Session
from repositories.team_repo import TeamRepository
from repositories.stdm_repo import StadiumRepository
from schemas.team_schema import TeamUpdate
from clients.client import ESPNClient

def get_team_by_id(team_id: int, session: Session):
    team = TeamRepository(session=session)
    return team.get_team_by_id(team_id=team_id)


def get_all_teams(session: Session):
    tm_repo = TeamRepository(session=session)
    stdm_repo = StadiumRepository(session=session)
    db_teams = tm_repo.get_teams()

    if not db_teams:
        client = ESPNClient(base_url="https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba")
        
        page = 1
        refs = []

        while True:
            request = client.get_teams(params={'page': page})
            refs.extend(request.get('items'))  # appends all the items without excluding

            if page >= request.get('pageCount'):
                break

            page += 1  # changes the page to execute more requests

        for ref in refs:
            team_url = ref['$ref'].partition('nba')[2]
            team_data = client.get_team_by_ref(team_url=team_url)

            tm_name = team_data.get('displayName')
            abbreviation = team_data.get('abbreviation')
            is_active = team_data.get('isActive')
            tm_region = team_data.get('location')

            try:
                stdm_name = team_data['venue']['fullName']
                stdm_location = team_data['venue']['address']['city']
                stdm_location += f',  {team_data['venue']['address']['state']}'
            except KeyError:
                stdm_name = 'Unknown'
                stdm_location = 'Unknown'

            new_team = tm_repo.create_team(name=tm_name, abbreviation=abbreviation, is_active=is_active, 
                                            titles=0, region=tm_region)
            session.commit()

            stdm_repo.create_stadium(name=stdm_name, location=stdm_location, team_id=new_team.id    )
            session.commit()
        
    db_teams = tm_repo.get_teams()
    return db_teams


def create_new_team(name: str, titles: int, region:str, session: Session):
    new_team = TeamRepository(session=session)
    new_team.create_team(name=name, titles=titles, region=region)



def patch_team(team_id: int, team_update: TeamUpdate, session: Session):
    team_to_updt = TeamRepository(session=session)
    return team_to_updt.update_team(team_id=team_id, team_update=team_update)


def remove_item(team_id: int, session: Session):
    team_to_del = TeamRepository(session=session)
    team_to_del.delete_team(team_id=team_id)