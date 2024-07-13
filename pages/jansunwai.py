import requests
from functools import cached_property
from playwright.sync_api import Page, TimeoutError
from utils.logger import setup_logger

class JanSunwai:
    def __init__(self, page: Page):
        self.page = page
        self.logger = setup_logger(self.__class__.__name__)


    def get_complaint_details(self, complaint_no, mobile_no):
        api_url = "https://jansunwai.up.nic.in/fullCompDetailsOfUser"
        params = {
            "complanitcode": complaint_no,
            "iemail": "",
            "mob": mobile_no,
            "randomkey": "",  # If needed, extract or determine this value
        }
        response = requests.get(api_url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to get details for complaint no {complaint_no}")
        return response.text

    def check_complaints_for_vipin(self, base_complaint_no, mobile_no, range_size=20000):
        matching_complaints = []
        for offset in range(-range_size, range_size + 1):
            complaint_no = str(int(base_complaint_no) + offset)
            try:
                details = self.get_complaint_details(complaint_no, mobile_no)
                if 'vipin' in details:
                    self.logger.info(f"'vipin' found in complaint no: {complaint_no}")
                    matching_complaints.append(complaint_no)
            except Exception as e:
                self.logger.error(e)
        self.logger.info(matching_complaints)
        return matching_complaints