from models import Tag

def get_or_create_tag(session, name):
    tag = session.query(Tag).filter_by(name=name).first()
    if not tag:
        tag = Tag(name=name)
        session.add(tag)
        session.commit()
    return tag
