from models import Project

def create_project(session, name, user_id):
    project = Project(name=name, user_id=user_id)
    session.add(project)
    session.commit()
    return project

def list_projects(session, user_id):
    return session.query(Project).filter_by(user_id=user_id).all()
