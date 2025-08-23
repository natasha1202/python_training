class Application:

    def __init__(self, driver):
        self.wd = driver
        # self.wd.implicitly_wait(60)

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        self.wd.open_groups_page()
        # init group creation
        self.wd.find_element_by_name("new").click()
        # fill group form
        self.wd.find_element_by_name("group_name").click()
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        self.wd.find_element_by_name("group_header").click()
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        self.wd.find_element_by_name("group_footer").click()
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element_by_name("submit").click()
        self.wd.return_to_groups_page()

    def create_contact(self, contact):
        # init contact creation
        self.wd.find_element_by_xpath(".//a[contains(@href, 'edit.php')]").click()
        # fill contact form
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.first_name)

        self.wd.find_element_by_name("middlename").click()
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middle_name)

        self.wd.find_element_by_name("lastname").click()
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.last_name)

        self.wd.find_element_by_name("nickname").click()
        self.wd.find_element_by_name("nickname").clear()
        self.wd.find_element_by_name("nickname").send_keys(contact.nickname)

        self.wd.find_element_by_name("title").click()
        self.wd.find_element_by_name("title").clear()
        self.wd.find_element_by_name("title").send_keys(contact.title)

        self.wd.find_element_by_name("company").click()
        self.wd.find_element_by_name("company").clear()
        self.wd.find_element_by_name("company").send_keys(contact.company)

        self.wd.find_element_by_name("address").click()
        self.wd.find_element_by_name("address").clear()
        self.wd.find_element_by_name("address").send_keys(contact.address)

        # self.wd.find_element_by_name("?").click()
        # self.wd.find_element_by_name("?").clear()
        # self.wd.find_element_by_name("?").send_keys(contact.phone)

        self.wd.find_element_by_name("home").click()
        self.wd.find_element_by_name("home").clear()
        self.wd.find_element_by_name("home").send_keys(contact.home)

        self.wd.find_element_by_name("mobile").click()
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.mobile)

        self.wd.find_element_by_name("work").click()
        self.wd.find_element_by_name("work").clear()
        self.wd.find_element_by_name("work").send_keys(contact.work)

        self.wd.find_element_by_name("fax").click()
        self.wd.find_element_by_name("fax").clear()
        self.wd.find_element_by_name("fax").send_keys(contact.fax)

        self.wd.find_element_by_name("email").click()
        self.wd.find_element_by_name("email").clear()
        self.wd.find_element_by_name("email").send_keys(contact.email)

        self.wd.find_element_by_name("email2").click()
        self.wd.find_element_by_name("email2").clear()
        self.wd.find_element_by_name("email2").send_keys(contact.email2)

        self.wd.find_element_by_name("email3").click()
        self.wd.find_element_by_name("email3").clear()
        self.wd.find_element_by_name("email3").send_keys(contact.middle_name)

        self.wd.find_element_by_name("homepage").click()
        self.wd.find_element_by_name("homepage").clear()
        self.wd.find_element_by_name("homepage").send_keys(contact.homepage)

        # submit group creation
        self.wd.find_element_by_name("submit").click()
        self.wd.go_to_homepage()

    def go_to_homepage(self):
        self.wd.find_element_by_xpath(".//a[contains(@href, './')]").click()

    def open_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        self.wd.find_element_by_name("user").send_keys(username)
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()


