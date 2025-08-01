from typing import List
import asyncio
import reflex as rx
from .. import navigation
from ..ui.base import base_page

from sqlmodel import select

from .. import db_model

class ContactState(rx.State):
    from_data : dict = {}
    entries: List['db_model.ContactEntryModel'] = []
    did_submit: bool = False

    @rx.var
    def thank_you(self) -> str:
        first_name = self.from_data.get("first_name") or ""
        return f"Submitted. Thank you for your message {first_name}".strip() + "!"

    @rx.event
    async def handle_submit(self, form_data: dict):
        '''Handle the form submitted'''
        #print(form_data)
        self.from_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        with rx.session() as session:
            db_entry = db_model.ContactEntryModel(**data)
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield
        
        #Set timeout
        await asyncio.sleep(2)
        self.did_submit = False
        yield

def list_entries(sef):
    "allow storing the entries from the contact page in a variable"
    with rx.session() as session:
        entries = session.exec( select(db_model.ContactEntryModel)).all()
        self.entries = entries


@rx.page(route=navigation.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    #contact page
    my_form = rx.form(
                rx.vstack(
                    rx.hstack(
                        rx.input(
                            name="first_name",
                            placeholder="First Name",
                            required=True,
                            type='text',
                            width='100%',
                        ),
                        rx.input(
                            name="last_name",
                            placeholder="Last Name",
                            type='text',
                            width='100%',
                        ),
                    width='100%'
                    ),
                    rx.input(
                        name='email',
                        placeholder='Your email',
                        type='email',
                        width='100%',
                    ),
                    rx.text_area(
                        name='message',
                        placeholder="Your message",
                        required=True,
                        width='100%',
                    ),
                    rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        ),
    
    my_child = rx.vstack(
                    rx.heading("Contact Us", size = "9"),
                    rx.cond(ContactState.did_submit, ContactState.thank_you, ""),
                    rx.desktop_only(
                        rx.box(my_form,
                               width = "50vw"
                               )
                    ),
                    rx.mobile_and_tablet(
                        rx.box(
                            my_form,
                            width =" 50vw"
                            ),
                    ),

                    spacing = "5",
                    justify="center",
                    align="center",
                    min_height="85vh",
                    id ="my-chlid",
                )
    return base_page(my_child)