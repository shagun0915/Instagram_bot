from selenium import webdriver
from time import sleep
from secrets import pw
from selenium.webdriver.common.keys import Keys
from random import randint

class Bot():

    links=[]

    comments= [
        'Great Post','Amazing work','Incredible!!','Your posts are awesome','Your work fascinates me','You are doing awazing work. Keep it up',
        'Nice job', 'Woahhh!! You got some real talent brother', 'Your posts bring me so much of inspiration'
    ]

    accounts=[
        'google','twitter','googledevs'
    ]

    def __init__(self):
        self.login('your_insta_username')
        self.like_comment_By_hashtag('technology')
        # self.comment_on_account()

    def login(self, username):
        self.driver=webdriver.Chrome(r"C:\Users\Dell\chromedriver")
        self.driver.get('https://www.instagram.com/?hl=en')
        sleep(5)
        username_input=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        password_input=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(pw)
        submit_btn=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        submit_btn.click()
        sleep(5)
        try:
            not_save_info=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
            not_save_info.click()
            sleep(5)
        except:
            pass
        try:
            not_now_btn=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            not_now_btn.click()
        except:
            pass

    def comment_on_account(self):
        for account in self.accounts:
            #go to profile page
            self.driver.get('https://www.instagram.com/{}/'.format(account))
            #go most recent post
            links=self.driver.find_elements_by_tag_name('a')
            def condition(link):
                return '.com/p/' in link.get_attribute('href')
            valid_links=list(filter(condition, links))
            last_post_url=valid_links[0].get_attribute('href')
            self.driver.get(last_post_url)
            #comment on that post
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(self.comments[randint(0,8)])
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
            sleep(2)
            



    def like_comment_By_hashtag(self, hashtag):
        search_box=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys('#' +hashtag)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').send_keys(Keys.ENTER)
        sleep(5)

        links=self.driver.find_elements_by_tag_name('a')
        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links=list(filter(condition, links))

        for i in range(5):
            link=valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            #like
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(3)
            #comment
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(self.comments[randint(0,8)])
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
            sleep(2)
def main():
    my_bot= Bot()

if __name__ =='__main__':
    main()