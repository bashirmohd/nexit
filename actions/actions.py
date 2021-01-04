# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher

from database_connectivity import DataUpdate

details={}

class ActionDenyBusiness(Action):

    def name(self) -> Text:
        return "action_deny_business"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("any_business","No"),SlotSet("business_venture","No"),SlotSet("need_loan","No"),]

class ActionAcquireSkills(Action):

    def name(self) -> Text:
        return "action_acquire_skills"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if tracker.get_intent_of_latest_message() == "OfCourse":
            # dispatcher.utter_message(template="utter_ask_skill_type")
            return [SlotSet("acquire_skill","Yes")]
        elif tracker.get_intent_of_latest_message() == "NotSure":
            # dispatcher.utter_message("Thanks")
            return [SlotSet("acquire_skill","No")]

class ActionDenyAffirmJob(Action):

    def name(self) -> Text:
        return "action_deny_affirm_job"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_intent_of_latest_message()=="NoJob":
            dispatcher.utter_message(template="utter_ask_acquire_skill")

            return [SlotSet("job_after_exit","No")]
        elif tracker.get_intent_of_latest_message()=="HadJob":
            dispatcher.utter_message(template="utter_ask_job_type")

            return [SlotSet("job_after_exit","Yes")]
        elif tracker.get_intent_of_latest_message()=="job_type":
            dispatcher.utter_message(template="utter_ask_acquire_skill")

            return [SlotSet("job_type",tracker.latest_message["text"])]

class ActionAffirmBusiness(Action):

    def name(self) -> Text:
        return "action_affirm_business"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("any_business","Yes")]

class ValidateJobSkillDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "user_job_skill_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["skill_type"]

        for slot_name in required_slots:


            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]


        return [SlotSet("requested_slot", None)]

class ValidateBusinessLoanForm(FormValidationAction):
    def name(self) -> Text:
        return "user_business_loan_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["business_venture", "need_loan"]
        # "job_after_exit", "job_type", "acquire_skill", "skill_type", "any_business", "business_venture", "need_loan"

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]

class ValidateUserDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["first_name","dob", "phone","email","gender","marital_status","state_origin","lga_origin","state_residence",
                          "lga_residence", "existing_bussiness","sector","participate","job_after_exit"]

        for slot_name in required_slots:

            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]


        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        details.update({
            "FirstName":tracker.get_slot("first_name"),
            "dob":tracker.get_slot('dob'),
            "phone": tracker.get_slot('phone'),
            "email": tracker.get_slot('email'),
            "gender":tracker.get_slot("gender"),
            "marital_status":tracker.get_slot("marital_status"),
            "state_origin":tracker.get_slot("marital_status"),
            "lga_origin":tracker.get_slot("lga_origin"),
            "state_residence":tracker.get_slot("state_residence"),
            "lga_residence":tracker.get_slot("lga_residence"),
            "existing_bussiness":tracker.get_slot("existing_bussiness"),
            "sector":tracker.get_slot("sector"),
            "participate":tracker.get_slot("participate"),
            "job_after_exit":tracker.get_slot("job_after_exit"),
            "job_type":tracker.get_slot("job_type"),
            "acquire_skill":tracker.get_slot("acquire_skill"),
            "skill_type":tracker.get_slot("skill_type"),
            "any_business":tracker.get_slot("any_business"),
            "business_venture":tracker.get_slot("business_venture"),
            "need_loan":tracker.get_slot("need_loan")
        })
        print(details)
        DataUpdate(
        tracker.get_slot("first_name"),
            tracker.get_slot('dob'),tracker.get_slot('phone'),tracker.get_slot('email'),tracker.get_slot("gender"),tracker.get_slot("marital_status"),
            tracker.get_slot("state_origin"),tracker.get_slot("lga_origin"),tracker.get_slot("state_residence"),
            tracker.get_slot("lga_residence"),tracker.get_slot("existing_bussiness"),tracker.get_slot("sector"),
            tracker.get_slot("participate"),
            tracker.get_slot("job_after_exit"),tracker.get_slot("job_type"),
            tracker.get_slot("acquire_skill"),tracker.get_slot("skill_type"),
            tracker.get_slot("any_business"),
            tracker.get_slot("business_venture"),tracker.get_slot("need_loan"))
        dispatcher.utter_message("Thank You! Your details has been successfully sent. We will contact you soon!.")
        return []


