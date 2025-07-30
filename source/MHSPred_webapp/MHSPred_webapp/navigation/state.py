import reflex as rx
#import reflex_local_auth
from . import routes


class NavState(rx.State):
    @rx.event
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)

    @rx.event
    def to_about_us(self):
        return rx.redirect(routes.ABOUT_US_ROUTE)
    
    @rx.event
    def to_contact(self):
        return rx.redirect(routes.CONTACT_US_ROUTE)
    
    @rx.event
    def to_assessment(self):
        return rx.redirect(routes.ASSESSMENT_ROUTE)
    