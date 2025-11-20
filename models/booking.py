from pydantic import BaseModel
from typing import Optional

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

    def build(self):
        return self.model_dump()

class CreatebookingResponse(BaseModel):
    bookingid: int
    booking: Booking

    def build(self):
        return self.model_dump()
