from selene import browser, be


class GithubPage:
    
    @staticmethod
    def go_to_sign_in_desktop():
        browser.element('.HeaderMenu-link--sign-up').click()
        browser.element('#email').should(be.visible)
    
    def go_to_sign_in_mobile(self):
        browser.element('.Button--link').click()
        self.go_to_sign_in_desktop()
