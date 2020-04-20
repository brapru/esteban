from api import db

class Devices(db.Model):
    __tablename__ = "devices"

    deviceName = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    state = db.Column(db.Integer)

    def serialize(self):
        return {"name": self.deviceName,
                "state": self.state}

    def __repr__(self):
        return f"Devices('{self.deviceName}', '{self.state}')"
