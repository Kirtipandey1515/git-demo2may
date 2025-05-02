from selenium.webdriver.common.by import By


class Saucedemo():
    def __init__(self , driver):
        self.driver = driver

    def sauce(self):
        """
        prices = self.driver.find_elements(By.XPATH, "//*[@class='inventory_item_price']")
        for price in prices:
            if "$" in price.text:
                price_list = price.text.strip().replace("$", "")
            total_sum = sum(float(price) for price in price_list)

            print(f"Total Price: {total_sum}")
"""
        prices = self.driver.find_elements(By.XPATH, "//*[@class='inventory_item_price']")

        price_list = [price.text.strip().replace("$", "") for price in prices if "$" in price.text]

        total_sum = sum(float(price) for price in price_list)

        print(f"Total Price: {total_sum}")


        buttons = self.driver.find_elements(By.XPATH, "//*[@class = 'btn btn_primary btn_small btn_inventory ']")
        for button in buttons:
            button.click()