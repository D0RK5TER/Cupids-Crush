from .db import db, environment, SCHEMA, add_prefix_for_prod


class Image(db.Model):
  __tablename__ = 'images'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  image_url = db.Column(db.String, nullable=False)
  preview = db.Column(db.String, nullable=False, default='true', server_default='true')
  images_key = db.relationship("User", back_populates="images")

  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'image_url': self.image_url,
      'preview': self.preview
    }

  def setitem(self, key, value):
    setattr(self, key, value)

  def getitem(self, key):
    return getattr(self, key)
