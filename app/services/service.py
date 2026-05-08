from sqlalchemy.orm import Session
from ..repositories.repo import TeamRepository, StadiumRepository
from ..schemas.schemas import TeamUpdate
from ..clients.client import ESPNClient
from ..exceptions import TeamNotFoundError

def get_team_by_id(team_id: int, session: Session):
    team = TeamRepository(session=session)
    return team.get_team_by_id(team_id=team_id)


def get_all_teams(session: Session):
    repo = TeamRepository(session=session)
    db_teams = repo.get_teams()

    if not db_teams:
        client = ESPNClient(base_url="https://sports.core.api.espn.com/v3/sports/basketball/leagues/nba")
        
        page = 1
        refs = []

        while True:
            request = client.get_teams({'pageIndex': page})
            refs.extend(request['items'])  # appends all the items without excluding

            if page == request['pageCount']:
                break

            page += 1  # changes the page to execute more requests

        for ref in refs:
            team_url = ref['$ref'].partition('nba')[2]
            team_data = client.get_team_by_ref(team_url=team_url)

            name = team_data['displayName']
            abbreviation = team_data['abbreviation']
            is_active = team_data['isActive']
            region = team_data['location']

            repo.create_team(name=name, abbreviation=abbreviation, is_active=is_active, 
                             titles=0, region=region)
            session.commit()
        

    db_teams = repo.get_teams()
    return db_teams


def patch_team(team_id: int, team_update: TeamUpdate, session: Session):
    team_to_updt = TeamRepository(session=session)
    return team_to_updt.update_team(team_id=team_id, team_update=team_update)


def create_new_team(name: str, titles: int, region:str, session: Session):
    new_team = TeamRepository(session=session)
    new_team.create_team(name=name, titles=titles, region=region)


def create_new_stadium(name: str, location: str, team_id: int, session: Session):
    team = TeamRepository(session=session).get_team_by_id(teamid=team_id)
    if not team:
        raise TeamNotFoundError

    new_stadium = StadiumRepository(session=session)
    new_stadium.create_stadium(name=name, location=location, team_id=team_id)


def remove_item(team_id: int, session: Session):
    team_to_del = TeamRepository(session=session)
    team_to_del.delete_team(team_id=team_id)