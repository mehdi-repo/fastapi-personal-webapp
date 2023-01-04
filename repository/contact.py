from sqlalchemy.orm import Session
from models.contact import ContactModel
from sqlalchemy.orm import Session



class ContactRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess
        
    def create_Contact(self, signup: ContactModel) -> bool:
        try:
            self.sess.add(signup)
            self.sess.commit()
        except:
            return False
        return True