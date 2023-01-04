from sqlalchemy.orm import Session
from models.event import EventModel
from sqlalchemy.orm import Session



class EventRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess
        
    def create_event(self, signup: EventModel) -> bool:
        try:
            self.sess.add(signup)
            self.sess.commit()
        except:
            return False
        return True
    
    def get_all_events(self):
        return self.sess.query(EventModel).all()