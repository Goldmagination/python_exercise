from app import db
import uuid

# each model of the app could be created with an according DTO in the same file 

class Message(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    content = db.Column(db.String(255), nullable=False)
    retrieval_count = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('messages', lazy=True))

    def increment_count(self):
        self.retrieval_count += 1
        db.session.commit()

    def to_dto(self):
        return MessageDTO(
            id=self.id,
            content=self.content,
            retrieval_count=self.retrieval_count,
            user_id=self.user_id)


# DTO object for the intersystem communication
class MessageDTO:
    def __init__(self, id, content, retrieval_count, user_id):
        self.id = id
        self.content = content
        self.retrieval_count = retrieval_count
        self.user_id = user_id

    def __iter__(self):
        yield 'id', self.id
        yield 'content', self.content
        yield 'retrieval_count', self.retrieval_count
        yield 'user_id', self.user_id
