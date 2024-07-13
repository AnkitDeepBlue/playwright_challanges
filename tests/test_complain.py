import allure


@allure.feature('JanSunwai Form Submission')
@allure.story('Check complaints for text "vipin"')
@allure.description("Check a range of complaints for the presence of the text 'vipin'")
def test_check_complaints_for_vipin(JanSunwai_page):

    base_complaint_no = "40019924012505"  # Replace with actual base complaint number
    mobile_no = "8318607723"  # Replace with actual mobile number

    with allure.step("Checking complaints for text 'vipin'"):
        matching_complaints = JanSunwai_page.check_complaints_for_vipin(base_complaint_no, mobile_no)

    # Log the matching complaints
    if matching_complaints:
        for complaint in matching_complaints:
            allure.attach(complaint, "Matching Complaint", allure.attachment_type.TEXT)
        print(f"Complaints containing 'vipin': {matching_complaints}")
    else:
        print("No complaints containing 'vipin' found in the specified range.")